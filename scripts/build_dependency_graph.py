#!/usr/bin/env python3
"""Build the inventory and proof maps from docs/dependency_inventory.json.

This is a documentation renderer. It does not run a proof assistant or verify
mathematical statements. Python 3 and Graphviz's `dot` executable are required.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, deque
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "docs" / "dependency_inventory.json"
RESULT_KINDS = {"theorem", "corollary", "lemma", "proposition", "remark"}
REPO_URL = "https://github.com/nicolasrobles/modular_inverses_ii"


def quote(text: str) -> str:
    return json.dumps(str(text), ensure_ascii=False)


def anchor(node_id: str) -> str:
    return node_id.replace(":", "-").replace("_", "-")


def validate(data: dict) -> None:
    nodes = data["nodes"]
    by_id = {n["id"]: n for n in nodes}
    if len(by_id) != len(nodes):
        raise ValueError("Duplicate node id")
    edges = data["edges"]
    edge_keys = [(e["from"], e["to"], e.get("relation", "proof")) for e in edges]
    if len(set(edge_keys)) != len(edge_keys):
        raise ValueError("Duplicate edge")
    adjacency = {key: set() for key in by_id}
    degree = dict.fromkeys(by_id, 0)
    for edge in edges:
        u, v = edge["from"], edge["to"]
        if u not in by_id or v not in by_id:
            raise ValueError(f"Unknown endpoint: {u} -> {v}")
        if u == v:
            raise ValueError(f"Self dependency: {u}")
        if not edge.get("reason"):
            raise ValueError(f"Missing edge explanation: {u} -> {v}")
        if v not in adjacency[u]:
            adjacency[u].add(v)
            degree[v] += 1
    queue = deque(k for k, value in degree.items() if value == 0)
    visited = 0
    while queue:
        u = queue.popleft()
        visited += 1
        for v in adjacency[u]:
            degree[v] -= 1
            if degree[v] == 0:
                queue.append(v)
    if visited != len(nodes):
        raise ValueError("The dependency record contains a directed cycle")
    numbered = [n for n in nodes if n["kind"] in RESULT_KINDS]
    if Counter(n["kind"] for n in numbered) != data["metadata"]["counts"]:
        raise ValueError("The numbered statement counts differ from the metadata")
    for node in numbered:
        if not node.get("number") or not node.get("source", {}).get("statement_lines"):
            raise ValueError(f"Missing statement locator: {node['id']}")
    overview = data["overview"]
    overview_ids = {n["id"] for n in overview["nodes"]}
    if len(overview_ids) != len(overview["nodes"]):
        raise ValueError("Duplicate overview node")
    members = []
    for node in overview["nodes"]:
        members.extend(node["members"])
    if set(members) - set(by_id):
        raise ValueError("Unknown overview member")
    if not {n["id"] for n in numbered}.issubset(members):
        raise ValueError("The overview omits a numbered statement")
    for e in overview["edges"]:
        if e["from"] not in overview_ids or e["to"] not in overview_ids:
            raise ValueError("Unknown overview edge endpoint")


def display_name(node: dict) -> str:
    if node["kind"] in RESULT_KINDS:
        return node["kind"].capitalize() + " " + node["number"]
    return node["title"]


def cell(text: str) -> str:
    return str(text).replace("|", "&#124;").replace("\n", " ")


def locator(value) -> str:
    if not value:
        return ""
    if isinstance(value[0], list):
        return "; ".join(locator(v) for v in value)
    if len(value) == 2:
        return str(value[0]) if value[0] == value[1] else f"{value[0]}-{value[1]}"
    return ", ".join(map(str, value))


def link(node: dict) -> str:
    return f"[{display_name(node)}](#{anchor(node['id'])})"


def inputs(data: dict, node_id: str) -> str:
    by_id = {n["id"]: n for n in data["nodes"]}
    items = []
    for edge in data["edges"]:
        if edge["to"] == node_id:
            suffix = " (proof method)" if edge.get("relation") == "method" else ""
            items.append(link(by_id[edge["from"]]) + suffix)
    return "; ".join(items) or "Direct in-text argument; see the source locator."


def write_inventory(data: dict) -> None:
    metadata = data["metadata"]
    numbered = [n for n in data["nodes"] if n["kind"] in RESULT_KINDS]
    auxiliary = [n for n in data["nodes"] if n["kind"] == "auxiliary"]
    external = [n for n in data["nodes"] if n["kind"] == "external"]
    result_count = sum(n["kind"] != "remark" for n in numbered)
    remark_count = sum(n["kind"] == "remark" for n in numbered)
    lines = [
        "# Statement and proof-dependency inventory", "",
        f"**{metadata['title']} - {metadata['source_version']}.**", "",
        f"This inventory records **{result_count} numbered results and {remark_count} numbered remarks**. "
        "Results stated in the introduction are counted once, even when their proofs occur later. "
        "Equation numbers and statement numbers are separate numbering systems.", "",
        f"The complete map also records **{len(auxiliary)} supporting steps** and "
        f"**{len(external)} literature inputs**. These are documentation entries, not additional numbered results.", "",
        "[README](README.md) · [Dependency guide](DEPENDENCIES.md) · "
        "[Numbered graph (PDF)](docs/dependency_graph.pdf) · "
        "[Complete graph (PDF)](docs/dependency_complete.pdf) · "
        "[Machine-readable record](docs/dependency_inventory.json)", "",
        "## Source and status", "",
        f"- Baseline: `{metadata['source_filename']}`.",
        f"- SHA-256: `{metadata['source_sha256']}`.",
        "- Locations are one-based lines in that source; statement pages refer to its compiled PDF.",
        "- The manuscript is not distributed in this repository.",
        "- Formalization has not started. There are no Lean declarations or kernel-checked results here.", "",
        "The **basis** column describes how v17 presents the item: a cited input, an in-text proof, "
        "or a transfer of an earlier argument. It does not certify the proof. "
        "Summaries abbreviate the statements; their full hypotheses remain in the identified manuscript.", "",
        "| Kind | Count |", "| --- | ---: |",
    ]
    for kind in ["theorem", "corollary", "lemma", "proposition", "remark"]:
        lines.append(f"| {kind.capitalize()} | {metadata['counts'][kind]} |")
    lines += ["", "## Numbered statements", ""]
    sections = {
        "1": "Introduction", "2": "Preliminary lemmas",
        "3": "Second moments averaged over the height", "4": "Differences of modular inverses",
        "5": "Moments of the distance to the point set", "6": "Long ranges of the frequency",
    }
    for section, title in sections.items():
        lines += [f"### Section {section}: {title}", "",
                  "| Item | Summary | Basis and source |", "| --- | --- | --- |"]
        for n in numbered:
            if n["section"] != section:
                continue
            source = n["source"]
            loc = f"Statement {locator(source['statement_lines'])}; PDF p. {source['statement_page']}"
            if source.get("proof_lines"):
                loc += f"; proof {locator(source['proof_lines'])}"
            first = (f'<a id="{anchor(n["id"])}"></a>**{display_name(n)}**<br>'
                     f'`{n["id"]}`<br>{n["title"]}')
            lines.append(f"| {first} | {cell(n['summary'])} | {cell(n['origin'])}. {loc}. |")
        lines.append("")
    lines += [
        "## Direct dependencies of numbered statements", "",
        "These are the predecessors in the complete documented graph. "
        "Where the proof is split into supporting calculations, follow the linked calculation to its inputs. "
        "The numbered-only graph suppresses those calculations and removes transitively redundant solid edges.", "",
        "| Statement | Direct recorded inputs |", "| --- | --- |",
    ]
    for n in numbered:
        lines.append(f"| {link(n)} | {inputs(data,n['id'])} |")
    lines += ["", "## Supporting steps", "",
              "Identifiers beginning `step:`, `geom:` or `support:` are repository identifiers. "
              "They identify calculations already in v17; they do not rename or add manuscript results. "
              "Identifiers beginning `eq:` retain actual TeX labels.", ""]
    branch_names = {
        "height": "Spectral and height arguments", "discrepancy": "Pair-difference discrepancy",
        "distance": "Elementary distance argument", "long_range": "Long-frequency argument",
        "shared": "Shared elementary facts",
    }
    for branch, heading in branch_names.items():
        lines += [f"### {heading}", "",
                  "| Step and source | Content | Direct recorded inputs |", "| --- | --- | --- |"]
        for n in auxiliary:
            if n["branch"] != branch:
                continue
            eqs = ", ".join("(" + e["number"] + ")" for e in n.get("equations", []))
            first = (f'<a id="{anchor(n["id"])}"></a>**{n["title"]}**<br>'
                     f'`{n["id"]}`<br>Lines {locator(n["source"]["lines"])}')
            if eqs:
                first += f"; equations {eqs}"
            lines.append(f"| {first} | {cell(n['summary'])} | {inputs(data,n['id'])} |")
        lines.append("")
    lines += ["## Literature inputs", "",
              "The entries below are inputs to the written proofs. Locators follow the citations in v17. "
              "Different uses of the same work remain separate nodes so the graph identifies the particular result being used.", "",
              "| Input | Reference and locator | Used in |", "| --- | --- | --- |"]
    by_id = {n["id"]: n for n in data["nodes"]}
    for n in external:
        references = "; ".join(f"[{r['bibkey']}](#ref-{r['bibkey'].lower()}), {r['locator']}" for r in n["references"])
        outputs = "; ".join(link(by_id[e["to"]]) for e in data["edges"] if e["from"] == n["id"])
        lines.append(f'| <a id="{anchor(n["id"])}"></a>**{n["title"]}**<br>`{n["id"]}` | {references} | {outputs} |')
    lines += ["", "### Bibliographic key", ""]
    for ref in data["bibliography"]:
        entry = f'<a id="ref-{ref["bibkey"].lower()}"></a>**{ref["bibkey"]}.** '
        if ref.get("authors"):
            entry += ref["authors"] + ". "
        entry += f'*{ref["title"]}*. {ref["as_cited"]}.'
        lines += [entry, ""]
    lines += [
        "### Attribution and comparison references", "",
        "BRS Lemma 4.4 and Corollary 4.5 are credited for the duality argument that v17 derives locally; "
        "BRS Section 4.4 is credited for the twisted spectral method. These attributions do not add "
        "a second independent input to the displayed proof. Selberg's 1938 paper and Kuznetsov are "
        "historical references for Selberg's identity; Xi (1.1) is the explicit modern locator used here.", "",
        "The companion paper, the earlier mean estimates of Proskurin, Kueh and Vinogradov, "
        "the conjectural comparison of Sarnak and Tsimerman, the Farey-distribution work of Dress "
        "and Niederreiter, the distance comparisons of Kargaev-Zhigljavsky and Marklof, and "
        "the correlation and large-sieve-matrix work of Boca-Zaharescu and Boca-Radziwill provide "
        "context in the introduction or conclusion. They are not prerequisites of the new proofs "
        "merely because they are cited nearby. The graph starts from the spectral inputs as packaged "
        "in BRS; it does not expand the full literature ancestry of those inputs.", "",
        "## Section 7: unnumbered discussion", "",
        "Section 7 has no numbered theorem, lemma, proposition, corollary, or remark. "
        "Its proved consequences and open directions are recorded separately below.", "",
        "| Subsection | Source lines | Content |", "| --- | --- | --- |",
    ]
    for item in data["discussion"]:
        lines.append(f"| {item['section']}: {item['title']} | {locator(item['source_lines'])} | {cell(item['summary'])} |")
    lines += ["", "## Maintenance", "",
              "This file is generated from `docs/dependency_inventory.json` by "
              "`python3 scripts/build_dependency_graph.py`. Update the record and source fingerprint "
              "when changing the manuscript baseline, then regenerate the inventory and graphs together.", ""]
    (ROOT / "INVENTORY.md").write_text("\n".join(lines), encoding="utf-8")


def project_numbered(data: dict) -> tuple[list[dict], list[dict]]:
    """Suppress auxiliary steps, retain paths, then reduce solid proof edges.

    External sources are omitted from this view. A dashed method-reuse edge
    remains distinct from an edge which uses a proved numerical assertion.
    """
    by_id = {n["id"]: n for n in data["nodes"]}
    numbered = {n["id"] for n in data["nodes"] if n["kind"] in RESULT_KINDS}
    adj = {key: set() for key in by_id}
    method = []
    for edge in data["edges"]:
        if edge.get("relation", "proof") == "method":
            if edge["from"] in numbered and edge["to"] in numbered:
                method.append(edge)
            continue
        if by_id[edge["from"]]["kind"] != "external":
            adj[edge["from"]].add(edge["to"])
    projected = {key: set() for key in numbered}
    for u in numbered:
        stack = list(adj[u])
        seen = set()
        while stack:
            v = stack.pop()
            if v in seen:
                continue
            seen.add(v)
            if v in numbered:
                projected[u].add(v)
            else:
                stack.extend(adj[v])
    # An edge is redundant precisely when another first step reaches its target.
    reduced = {u: set(vs) for u, vs in projected.items()}
    for u, targets in projected.items():
        for v in targets:
            stack = list(targets - {v})
            seen = set()
            while stack:
                w = stack.pop()
                if w == v:
                    reduced[u].discard(v)
                    break
                if w not in seen:
                    seen.add(w)
                    stack.extend(projected[w])
    edges = [
        {"from": u, "to": v, "relation": "proof"}
        for u in sorted(reduced) for v in sorted(reduced[u])
    ]
    edges.extend(method)
    return [n for n in data["nodes"] if n["id"] in numbered], edges


def node_attributes(node: dict, overview: bool = False) -> dict:
    kind = node["kind"]
    if overview:
        label = node["title"] + "\n" + node["short_title"]
    elif kind in RESULT_KINDS:
        label = kind.capitalize() + " " + node["number"] + "\n" + node["short_title"]
    else:
        label = node["short_title"]
    attrs = {
        "label": label,
        "tooltip": node.get("summary", node["title"]),
        "shape": "box",
        "style": "rounded,filled",
        "fillcolor": "#FFFFFF",
        "color": "#64748B",
        "fontcolor": "#172554",
        "fontname": "DejaVu Sans",
        "fontsize": "11",
        "margin": "0.14,0.10",
        "penwidth": "1.1",
    }
    if kind == "theorem" or overview:
        attrs.update(fillcolor="#DBEAFE", color="#2563EB", penwidth="1.4")
    elif kind == "corollary":
        attrs.update(fillcolor="#EFF6FF", color="#3B82F6")
    elif kind == "proposition":
        attrs.update(fillcolor="#E0F2FE", color="#0284C7")
    elif kind == "remark":
        attrs.update(fillcolor="#F1F5F9", color="#64748B", style="rounded,dashed,filled")
    elif kind == "auxiliary":
        attrs.update(shape="ellipse", fillcolor="#F8FAFC", color="#94A3B8", fontsize="10")
    elif kind == "external":
        attrs.update(shape="hexagon", fillcolor="#FFF7ED", color="#C2410C", fontsize="10")
    if not overview:
        attrs["URL"] = f"{REPO_URL}/blob/main/INVENTORY.md#{anchor(node['id'])}"
        attrs["target"] = "_top"
    return attrs


def write_dot(path: Path, nodes: list[dict], edges: list[dict], title: str,
              overview: bool = False, ranks: list[dict] | None = None) -> None:
    lines = ["digraph dependencies {", "  graph ["]
    options = {
        "rankdir": "TB", "bgcolor": "white", "pad": "0.3",
        "nodesep": "0.25" if not overview else "0.45", "ranksep": "0.62",
        "splines": "spline", "outputorder": "edgesfirst", "fontname": "DejaVu Sans",
        "fontsize": "17", "fontcolor": "#0F172A", "labelloc": "t", "label": title,
    }
    lines.extend(f"    {k}={quote(v)}," for k, v in options.items())
    lines.extend([
        "  ];",
        '  edge [color="#64748B", arrowsize="0.65", penwidth="1.0", fontname="DejaVu Sans", fontsize="9"];',
    ])
    for node in nodes:
        attrs = node_attributes(node, overview)
        rendered = ", ".join(f"{k}={quote(v)}" for k, v in attrs.items())
        lines.append(f"  {quote(node['id'])} [{rendered}];")
    for group in ranks or []:
        members = "; ".join(quote(x) for x in group["nodes"])
        lines.append(f"  {{ rank={quote(group['rank'])}; {members}; }}")
    for edge in edges:
        attrs = {}
        if edge.get("reason"):
            attrs["tooltip"] = edge["reason"]
        if edge.get("relation") == "method":
            attrs.update(style="dashed", color="#7C3AED", label="proof method")
        elif edge.get("relation") == "literature":
            attrs.update(color="#C2410C")
        rendered = ", ".join(f"{k}={quote(v)}" for k, v in attrs.items())
        suffix = f" [{rendered}]" if attrs else ""
        lines.append(f"  {quote(edge['from'])} -> {quote(edge['to'])}{suffix};")
    lines.append("}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def render(dot_path: Path, formats: list[str]) -> None:
    for fmt in formats:
        command = ["dot", "-T" + fmt]
        if fmt == "png":
            command += ["-Gdpi=135"]
        command += [str(dot_path), "-o", str(dot_path.with_suffix("." + fmt))]
        subprocess.run(command, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate the record without rendering")
    args = parser.parse_args()
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    validate(data)
    numbered, projected = project_numbered(data)
    print(f"Validated {len(numbered)} numbered entries, {len(data['nodes'])} total nodes, "
          f"and {len(data['edges'])} recorded edges; no directed cycle.")
    if args.check:
        return
    write_inventory(data)
    docs = ROOT / "docs"
    overview = data["overview"]
    version = data["metadata"]["source_version"]
    result_count = sum(n["kind"] != "remark" for n in numbered)
    remark_count = sum(n["kind"] == "remark" for n in numbered)
    write_dot(docs / "dependency_overview.dot", overview["nodes"], overview["edges"],
              data["metadata"]["title"] + "\n" + f"Main proof branches · {version}",
              overview=True, ranks=overview.get("rank_groups"))
    write_dot(docs / "dependency_graph.dot", numbered, projected,
              f"Numbered statements · {version}\n{result_count} results and {remark_count} remarks; "
              "arrows point from prerequisites to consequences")
    write_dot(docs / "dependency_complete.dot", data["nodes"], data["edges"],
              f"Complete documented dependencies · {version}\nNumbered statements, supporting steps, and literature inputs")
    for name in ["dependency_overview", "dependency_graph"]:
        render(docs / (name + ".dot"), ["svg", "pdf", "png"])
    render(docs / "dependency_complete.dot", ["svg", "pdf"])
    print("Wrote INVENTORY.md and rendered overview, numbered-statement, and complete proof maps.")


if __name__ == "__main__":
    main()
