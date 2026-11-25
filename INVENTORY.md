# Statement and proof-dependency inventory

**Height averages of Kloosterman sums and modular inverses - v17.**

This inventory records **31 numbered results and 2 numbered remarks**. Results stated in the introduction are counted once, even when their proofs occur later. Equation numbers and statement numbers are separate numbering systems.

The complete map also records **46 supporting steps** and **13 literature inputs**. These are documentation entries, not additional numbered results.

[README](README.md) · [Dependency guide](DEPENDENCIES.md) · [Numbered graph (PDF)](docs/dependency_graph.pdf) · [Complete graph (PDF)](docs/dependency_complete.pdf) · [Machine-readable record](docs/dependency_inventory.json)

## Source and status

- Baseline: `second_moment_int_v17.tex`.
- SHA-256: `a13de91bb0a5d8c1c3b0ef8ec0054932b48eea5878202ae4414bd7f4e8315a1f`.
- Locations are one-based lines in that source; statement pages refer to its compiled PDF.
- The manuscript is not distributed in this repository.
- Formalization has not started. There are no Lean declarations or kernel-checked results here.

The **basis** column describes how v17 presents the item: a cited input, an in-text proof, or a transfer of an earlier argument. It does not certify the proof. Summaries abbreviate the statements; their full hypotheses remain in the identified manuscript.

| Kind | Count |
| --- | ---: |
| Theorem | 5 |
| Corollary | 4 |
| Lemma | 20 |
| Proposition | 2 |
| Remark | 2 |

## Numbered statements

### Section 1: Introduction

| Item | Summary | Basis and source |
| --- | --- | --- |
| <a id="thm-height"></a>**Theorem 1.1**<br>`thm:height`<br>Height-averaged cumulative second moment | For real $N,X\ge1$, the height average of the second moment over $N\le\lvert n\rvert<2N$ is $\ll_\varepsilon (NX)^\varepsilon NX^2$. Both frequency signs are included. | Proved in v17. Statement 199-204; PDF p. 3; proof 788-806. |
| <a id="thm-short"></a>**Theorem 1.2**<br>`thm:short`<br>Height mean for moving intervals of moduli | For $N,X\ge1$ and $0<\delta\le1$, restricting the moduli to $(Y,(1+\delta)Y]$ gives the height-mean bound $\ll_\varepsilon (NX)^\varepsilon X^2\{N\delta+\min(1,N\delta^2X)\}$. | Reformulation of Lemma 3.2. Statement 216-221; PDF p. 3; proof 780-782. |
| <a id="cor-most"></a>**Corollary 1.3**<br>`cor:most`<br>Exceptional heights for all real frequency cutoffs | For $a,\kappa,\eta>0$ and $X\ge2$, outside a set of Lebesgue measure $O_{a,\kappa,\eta}(X^{1-\kappa+\eta})$, the bound $\mathcal K_2(N;Y)\le3NX^{2+\kappa}$ holds simultaneously for every real $1\le N\le X^a$. | Proved in v17. Statement 225-231; PDF p. 4; proof 808-823. |
| <a id="thm-pair-height"></a>**Theorem 1.4**<br>`thm:pair-height`<br>Height-averaged discrepancy of pair differences | For $X\ge2$, the height average of $\mathcal D_Y+\mathcal D_Y^*$ is $\ll_\varepsilon X^{-2+\varepsilon}$. Each discrepancy is at least $\lfloor Y\rfloor^{-2}$ for every $Y\ge2$. The supremum over rectangles is inside the average. | Proved in v17. Statement 245-254; PDF p. 4; proof 927-943. |
| <a id="cor-pair-height-most"></a>**Corollary 1.5**<br>`cor:pair-height-most`<br>Exceptional heights for pair discrepancy | For $\kappa,\eta>0$ and $X\ge2$, both discrepancies are at most $X^{-2+\kappa}$ outside a set of Lebesgue measure $O_{\kappa,\eta}(X^{1-\kappa+\eta})$. | Proved in v17. Statement 258-260; PDF p. 4; proof 945-951. |
| <a id="thm-distance"></a>**Theorem 1.6**<br>`thm:distance`<br>Distance moments and covering radius | For $X\ge2$, the positive distance moments have orders $X^{-s}$ for $0<s<2$, $X^{-2}(\log X)^2$ for $s=2$, and $X^{-1-s/2}$ for $s>2$. The covering radius lies between $\tfrac12X^{-1/2}$ and $4X^{-1/2}$. | Proved in v17. Statement 264-278; PDF p. 4; proof 977-979; 1048-1068; 1098-1125; 1127-1141. |
| <a id="thm-correction"></a>**Theorem 1.7**<br>`thm:correction`<br>Exact weighted Farey correction and its asymptotic | For integer $Q\ge2$, $1/2\le\tau<1$ and $L=\tau Q^2$, an exact sinc-squared weighted second moment isolates determinant-one Farey pairs. Its asymptotic is $LN_Q+(12\tau/\pi^2)I(\tau)Q^4+O(Q^3\log(2Q))$, uniformly in $\tau$, with $I(\tau)>0$. | Proved in v17. Statement 293-306; PDF p. 5; proof 1269-1285. |
| <a id="cor-obstruction"></a>**Corollary 1.8**<br>`cor:obstruction`<br>Sharpness of the long-interval remainder | For every sufficiently large integer $Q$, some symmetric interval with radius $T\asymp Q^2$ has a second-moment remainder whose absolute value is $\gg Q^4$. The constants are absolute; this is an existence statement for the interval. | Proved in v17. Statement 310-315; PDF p. 5; proof 1298-1314. |

### Section 2: Preliminary lemmas

| Item | Summary | Basis and source |
| --- | --- | --- |
| <a id="lem-kuznetsov"></a>**Lemma 2.1**<br>`lem:kuznetsov`<br>Kuznetsov formula and local spectral large sieve | Records the inverse Kuznetsov formula for both signs and the local spectral large sieve on a window of width $G$, for $N,T\ge1$ and $1\le G\le T$. The formula uses the signed measure $dm=\chi\,dm_0$; the large sieve uses positive $dm_0$. | Cited input. Statement 396-412; PDF p. 8. |
| <a id="lem-window"></a>**Lemma 2.2**<br>`lem:window`<br>Dual spectral-window second moment | Deduces a dual second-moment estimate $\ll_\eta F^2TG(TG+N)^{1+\eta}$ for a spectral-window integral with a multiplier bounded by $F$, for either sign. | Proved in v17. Statement 416-421; PDF p. 8; proof 423-433. |
| <a id="lem-transforms"></a>**Lemma 2.3**<br>`lem:transforms`<br>Twisted transforms away from the low spectrum | Records the uniform-in-$r$ twisted Bessel estimates in the imaginary range $\lvert t\rvert\ge1$ and the holomorphic range $k\ge1$. The low imaginary spectrum is treated separately in Lemma 2.4. | Cited input. Statement 441-450; PDF p. 9. |
| <a id="lem-low"></a>**Lemma 2.4**<br>`lem:low`<br>Low-spectrum transform estimate | For $\lvert t\rvert\le1$ and $Z>0$, both twisted transforms are $\ll_V1+\log^+(1/Z)$, uniformly in the real twist $r$. | Proved in v17. Statement 454-460; PDF p. 9; proof 462-491. |
| <a id="lem-weil"></a>**Lemma 2.5**<br>`lem:weil`<br>Weil bound for Kloosterman sums | For all integer $m,n$ and $c\ge1$, $\lvert S(m,n;c)\rvert\le(m,n,c)^{1/2}c^{1/2}\tau(c)$. | Cited input. Statement 501-506; PDF p. 10. |
| <a id="lem-selberg"></a>**Lemma 2.6**<br>`lem:selberg`<br>Selberg's identity | Expresses $S(m,n;c)$, for integer arguments, as a divisor sum of Kloosterman sums with one argument equal to one. The cumulative form is equation (2.6). | Cited input. Statement 510-515; PDF p. 10. |
| <a id="lem-farey"></a>**Lemma 2.7**<br>`lem:farey`<br>Consecutive Farey fractions | Consecutive fractions of Farey order $Q\ge1$ have determinant one and denominators whose sum exceeds $Q$. | Cited input. Statement 533-538; PDF p. 11. |
| <a id="lem-sieve"></a>**Lemma 2.8**<br>`lem:sieve`<br>Two-sided large-sieve remainder | For frequencies separated by $\lambda$ modulo one and any integer interval of length $H\ge1$, the absolute error from $H\sum_j\lvert y_j\rvert^2$ is at most $\lambda^{-1}\sum_j\lvert y_j\rvert^2$. | Proved in v17. Statement 554-559; PDF p. 11; proof 561-571. |
| <a id="lem-ks"></a>**Lemma 2.9**<br>`lem:ks`<br>Koksma-Szusz inequality with repetitions and general arcs | Bounds rectangular discrepancy of a nonempty finite sequence in $\mathbb T^2$ by a Fourier sum and a truncation term, allowing repeated points and closed or half-open arcs, including empty and full arcs. | Extension of a cited inequality, proved in v17. Statement 573-579; PDF p. 11; proof 581-587. |

### Section 3: Second moments averaged over the height

| Item | Summary | Basis and source |
| --- | --- | --- |
| <a id="lem-twist"></a>**Lemma 3.1**<br>`lem:twist`<br>Twisted second moment | For a fixed smooth compactly supported $W$, $C,N\ge1$ and real $r$, the second moment of the twisted smooth sums $B_\sigma(n,r)$ is $\ll_{\varepsilon,W}(NC(1+\lvert r\rvert))^\varepsilon(N+1+\lvert r\rvert)$. | Proved in v17. Statement 597-602; PDF p. 12; proof 604-680. |
| <a id="lem-annulus"></a>**Lemma 3.2**<br>`lem:annulus`<br>Height mean for moving annuli of moduli | Proves the moving-interval height mean at a base height $C\ge1$, with the factor $N\delta+\min(1,N\delta^2C)$. Theorem 1.2 is the corresponding formulation with signed frequencies. | Proved in v17. Statement 689-694; PDF p. 14; proof 696-778. |
| <a id="cor-weighted"></a>**Corollary 3.3**<br>`cor:weighted`<br>Weighted cumulative height mean | For $N,X\ge1$, inserting the weight $1/c$ in the cumulative sums gives height-averaged second moment $\ll_\varepsilon(NX)^\varepsilon N$. | Proved in v17. Statement 827-832; PDF p. 17; proof 834-852. |
| <a id="prop-two"></a>**Proposition 3.4**<br>`prop:two`<br>Height mean over a frequency rectangle | For $M,N,X\ge1$, the height-averaged second moment over $\lvert m\rvert\le M$, $\lvert n\rvert\le N$, excluding $(0,0)$, is $\ll_\varepsilon(MNX)^\varepsilon MNX^2$. Both coordinate axes are included. | Proved in v17. Statement 858-863; PDF p. 17; proof 865-888. |
| <a id="rem-weighted-two"></a>**Remark 3.5**<br>`rem:weighted-two`<br>Weighted height mean over a frequency rectangle | With the weight $1/c$, the same frequency rectangle has height-averaged second moment $\ll_\varepsilon(MNX)^\varepsilon MN$. The proof of Corollary 3.3 is reused with Proposition 3.4 as the input estimate. | Proof transfer stated in the remark. Statement 890-896; PDF p. 18; proof 891. |

### Section 4: Differences of modular inverses

| Item | Summary | Basis and source |
| --- | --- | --- |
| <a id="lem-pair-pointwise"></a>**Lemma 4.1**<br>`lem:pair-pointwise`<br>Pointwise discrepancy of the difference measure | For $Y\ge2$ and integer $K\ge1$, controls $\mathcal D_Y$ by weighted squared Fourier coefficients and $1/K$, and proves $\mathcal D_Y^*\le\mathcal D_Y+1/N_Y$. | Proved in v17. Statement 902-911; PDF p. 18; proof 913-925. |

### Section 5: Moments of the distance to the point set

| Item | Summary | Basis and source |
| --- | --- | --- |
| <a id="lem-farey-product"></a>**Lemma 5.1**<br>`lem:farey-product`<br>A modular-inverse point in a product of Farey gaps | If integers $Q,R\ge1$ satisfy $2QR\le X$, every product of open consecutive Farey gaps of orders $Q$ and $R$ contains a lift of a point of $\mathcal P_X$. | Proved in v17. Statement 961-963; PDF p. 20; proof 965-975. |
| <a id="lem-adaptive"></a>**Lemma 5.2**<br>`lem:adaptive`<br>Adaptive Farey orders and their tail | For $0<\rho\le1$ and irrational $x$, controls the least Farey order $R_\rho(x)$ giving a gap of length at most $\rho$. It proves the range $\rho^{-1/2}\le R_\rho(x)\le2/\rho$ and a quadratic tail estimate. | Proved in v17. Statement 989-1002; PDF p. 20; proof 1004-1012. |
| <a id="lem-product-tail"></a>**Lemma 5.3**<br>`lem:product-tail`<br>Tail of a product of adaptive Farey orders | Bounds the tail of $\rho R_\rho(x)R_\rho(y)$ by a quadratic decay times the smaller of two logarithmic factors, for $1\le z\le4/\rho$; above this range the tail is empty on irrational-coordinate pairs. | Proved in v17. Statement 1014-1020; PDF p. 21; proof 1022-1030. |
| <a id="lem-distance-tail"></a>**Lemma 5.4**<br>`lem:distance-tail`<br>Tail of the distance to modular-inverse points | For $X\ge2$ and $t>0$, the measure of $\{d_X>t\}$ is $\ll [1+\min\{\log(2+Xt),\log(2+1/(Xt^2))\}]/(X^2t^2)$. | Proved in v17. Statement 1032-1038; PDF p. 21; proof 1040-1046. |
| <a id="lem-empty"></a>**Lemma 5.5**<br>`lem:empty`<br>An arithmetic criterion for empty rectangles | Gives an explicit arithmetic inequality in the denominators of the rational corner and the side lengths that makes two oppositely oriented open rectangles empty of lifts of $\mathcal P_X$. | Proved in v17. Statement 1074-1084; PDF p. 22; proof 1086-1096. |
| <a id="rem-negative"></a>**Remark 5.6**<br>`rem:negative`<br>Negative distance moments | For $X\ge2$ and $-2<s<0$, the distance moment has order $X^{-s}$. For $s\le-2$ it diverges. The three assertions use disc counting, the positive first-moment upper bound, and a local singularity, respectively. | Proved in the remark. Statement 1143-1160; PDF p. 24; proof 1143-1160. |

### Section 6: Long ranges of the frequency

| Item | Summary | Basis and source |
| --- | --- | --- |
| <a id="prop-long"></a>**Proposition 6.1**<br>`prop:long`<br>Second moment over an arbitrary integer interval | For integer $Q\ge2$, $M\in\mathbb Z$ and integer $H\ge1$, the second moment over $M<n\le M+H$ differs from $HN_Q$ by at most $Q(Q-1)N_Q$. | Proved in v17. Statement 1174-1179; PDF p. 24; proof 1181-1183. |
| <a id="lem-poisson"></a>**Lemma 6.2**<br>`lem:poisson`<br>Poisson identity for the sinc-squared weight | For real $L\ge2$, the absolutely convergent Fourier series of $w(n/L)$ equals the triangular kernel $L(1-L\lVert\theta\rVert)_+$ for every real $\theta$. | Proved in v17. Statement 1189-1195; PDF p. 25; proof 1197-1207. |
| <a id="lem-exact"></a>**Lemma 6.3**<br>`lem:exact`<br>Exact contribution of determinant-one pairs | For integer $Q\ge2$ and real $L\ge Q^2/2$, evaluates the weighted second moment as the diagonal term $LN_Q$ plus the contribution of determinant-one Farey pairs. The correction vanishes for $L\ge Q(Q-1)$. | Proved in v17. Statement 1209-1215; PDF p. 25; proof 1217-1233. |
| <a id="lem-positive"></a>**Lemma 6.4**<br>`lem:positive`<br>Positivity of the Farey correction integral | For $1/2\le\tau<1$, reduces $I(\tau)$ to a one-dimensional integral and proves it is positive. On $[1/2,5/8]$ it gives the explicit lower bound $1/9000$. | Proved in v17. Statement 1237-1247; PDF p. 26; proof 1249-1267. |

## Direct dependencies of numbered statements

These are the predecessors in the complete documented graph. Where the proof is split into supporting calculations, follow the linked calculation to its inputs. The numbered-only graph suppresses those calculations and removes transitively redundant solid edges.

| Statement | Direct recorded inputs |
| --- | --- |
| [Theorem 1.1](#thm-height) | [Dyadic decomposition of the cumulative sum](#step-cumulative-dyadic-height) |
| [Theorem 1.2](#thm-short) | [Lemma 3.2](#lem-annulus); [Kloosterman symmetries](#eq-symmetries) |
| [Corollary 1.3](#cor-most) | [Exceptional set uniform over real cutoffs](#step-exceptional-real-cutoffs) |
| [Theorem 1.4](#thm-pair-height) | [Upper discrepancy bound](#geom-pair-upper); [Lower discrepancy bound from an empty strip](#geom-pair-lower) |
| [Corollary 1.5](#cor-pair-height-most) | [Theorem 1.4](#thm-pair-height) |
| [Theorem 1.6](#thm-distance) | [Upper covering bound from Farey products](#geom-covering-upper); [Upper bounds for positive distance moments](#geom-positive-moment-upper); [Counting lower bound for positive moments](#eq-counting-lower); [Supercritical lower bound from one empty square](#geom-supercritical-lower); [Critical second-moment lower bound](#geom-critical-lower); [Empty tangent disc and lower covering bound](#geom-empty-tangent-disc) |
| [Theorem 1.7](#thm-correction) | [Lemma 6.3](#lem-exact); [Lemma 6.4](#lem-positive); [Uniform coprime lattice sum](#step-coprime-lattice-sum) |
| [Corollary 1.8](#cor-obstruction) | [Abel summation and variation localization](#step-abel-variation-localization) |
| [Lemma 2.1](#lem-kuznetsov) | [Kuznetsov formula and local spectral large sieve](#external-brs-spectral) |
| [Lemma 2.2](#lem-window) | [Lemma 2.1](#lem-kuznetsov) |
| [Lemma 2.3](#lem-transforms) | [Twisted Bessel transform estimates](#external-brs-transforms) |
| [Lemma 2.4](#lem-low) | [Low-spectrum Bessel kernel bounds](#step-low-kernel-integrals) |
| [Lemma 2.5](#lem-weil) | [Weil bound](#external-weil) |
| [Lemma 2.6](#lem-selberg) | [Selberg identity for integer arguments](#external-selberg) |
| [Lemma 2.7](#lem-farey) | [Adjacent Farey fractions](#external-farey) |
| [Lemma 2.8](#lem-sieve) | [Endpoint sums in the large-sieve remainder](#step-large-sieve-endpoint-sums) |
| [Lemma 2.9](#lem-ks) | [Perturbation and arc approximation](#step-ks-repetition-and-arcs) |
| [Lemma 3.1](#lem-twist) | [Spectral decomposition of the twisted sums](#step-twisted-spectral-decomposition) |
| [Lemma 3.2](#lem-annulus) | [Removal of smoothing and comparison of bounds](#step-remove-annular-weights) |
| [Corollary 3.3](#cor-weighted) | [Theorem 1.1](#thm-height); [Vector partial summation for the weight 1/c](#step-vector-Abel-summation) |
| [Proposition 3.4](#prop-two) | [Divisor reduction and treatment of the axes](#step-two-frequency-reduction) |
| [Remark 3.5](#rem-weighted-two) | [Proposition 3.4](#prop-two); [Vector partial summation for the weight 1/c](#step-vector-Abel-summation); [Corollary 3.3](#cor-weighted) (proof method) |
| [Lemma 4.1](#lem-pair-pointwise) | [Lemma 2.9](#lem-ks); [Fourier coefficients of ordered differences](#geom-difference-fourier); [Removal of diagonal pairs](#geom-diagonal-removal) |
| [Lemma 5.1](#lem-farey-product) | [Lemma 2.7](#lem-farey) |
| [Lemma 5.2](#lem-adaptive) | [Lemma 2.7](#lem-farey); [Adaptive Farey intervals](#eq-gap-monotone) |
| [Lemma 5.3](#lem-product-tail) | [Lemma 5.2](#lem-adaptive) |
| [Lemma 5.4](#lem-distance-tail) | [Lemma 5.1](#lem-farey-product); [Lemma 5.3](#lem-product-tail) |
| [Lemma 5.5](#lem-empty) | Direct in-text argument; see the source locator. |
| [Remark 5.6](#rem-negative) | [Upper bound for negative moments](#geom-negative-upper); [Lower bound for negative moments](#geom-negative-lower); [Divergence of negative moments](#geom-negative-divergence) |
| [Proposition 6.1](#prop-long) | [Lemma 2.8](#lem-sieve); [Circular separation of reduced fractions](#eq-farey-separation); [Trigonometric-polynomial representation](#step-long-trig-polynomial) |
| [Lemma 6.2](#lem-poisson) | [Poisson summation](#external-poisson) |
| [Lemma 6.3](#lem-exact) | [Determinant-one pair calculation](#step-determinant-one-pairs) |
| [Lemma 6.4](#lem-positive) | Direct in-text argument; see the source locator. |

## Supporting steps

Identifiers beginning `step:`, `geom:` or `support:` are repository identifiers. They identify calculations already in v17; they do not rename or add manuscript results. Identifiers beginning `eq:` retain actual TeX labels.

### Spectral and height arguments

| Step and source | Content | Direct recorded inputs |
| --- | --- | --- |
| <a id="step-low-kernel-integrals"></a>**Low-spectrum Bessel kernel bounds**<br>`step:low-kernel-integrals`<br>Lines 462-484; equations (2.3), (2.4) | Bounds the Schlaefli remainder integral and both low-spectrum kernels by $1+\log^+(1/x)$, then integrates over the fixed scaled support. | [Integral representations of J and K Bessel functions](#external-dlmf) |
| <a id="eq-symmetries"></a>**Kloosterman symmetries**<br>`eq:symmetries`<br>Lines 495-498; equations (2.5) | Records reality, interchange of the two arguments, and simultaneous sign reversal of Kloosterman sums. In particular, $S(-n,1;c)=S(n,-1;c)$. | Direct in-text argument; see the source locator. |
| <a id="step-divisor-small-power"></a>**Small-power divisor bound**<br>`step:divisor-small-power`<br>Lines 508 | Uses $\tau(n)\ll_\eta n^\eta$ for every $\eta>0$. | [Divisor small-power bound](#external-divisor) |
| <a id="eq-selberg-sum"></a>**Cumulative Selberg identity**<br>`eq:selberg-sum`<br>Lines 517-521; equations (2.6) | Sums Selberg's identity over the modulus to reduce $A_Y(m,n)$ to divisor-weighted sums $A_{Y/d}(mn/d^2,1)$ for $mn\ne0$. Terms with $d>Y$ vanish. | [Lemma 2.6](#lem-selberg) |
| <a id="eq-axes"></a>**Ramanujan sums on the coordinate axes**<br>`eq:axes`<br>Lines 523-527; equations (2.7) | The Ramanujan-sum formula gives $\lvert A_Y(0,n)\rvert\le Y\tau(\lvert n\rvert)$ for $n\ne0$. Interchange of arguments covers the other axis. | [Kloosterman symmetries](#eq-symmetries); [Ramanujan-sum identity](#external-ramanujan) |
| <a id="step-twisted-spectral-decomposition"></a>**Spectral decomposition of the twisted sums**<br>`step:twisted-spectral-decomposition`<br>Lines 604-680; equations (3.1), (3.2), (3.3), (3.4), (3.5), (3.6), (3.7) | Applies Kuznetsov with a scalar of modulus one, separates low, holomorphic, and higher imaginary spectral ranges, and sums the window estimates by Minkowski. | [Lemma 2.1](#lem-kuznetsov); [Lemma 2.2](#lem-window); [Lemma 2.3](#lem-transforms); [Lemma 2.4](#lem-low) |
| <a id="eq-elementary"></a>**Elementary moving-interval estimate**<br>`eq:elementary`<br>Lines 699-707; equations (3.9) | Counts the moduli in a moving interval and the logarithmic height measure contributed by each modulus; the Weil and divisor bounds give the elementary mean-square estimate. | [Lemma 2.5](#lem-weil); [Small-power divisor bound](#step-divisor-small-power) |
| <a id="eq-mellin"></a>**Mellin transform of the smoothed interval**<br>`eq:mellin`<br>Lines 709-725; equations (3.10) | Constructs a smooth approximation to the moving interval and bounds its Mellin transform in terms of the interval length and the smoothing width. | Direct in-text argument; see the source locator. |
| <a id="eq-plancherel"></a>**Plancherel identity for the height average**<br>`eq:plancherel`<br>Lines 727-742; equations (3.11) | The substitution $Y=C\exp(u)$ converts the height mean of the smooth sums to a Fourier Plancherel integral in the twist parameter. | [Plancherel theorem](#external-plancherel) |
| <a id="eq-smooth-bound"></a>**Smooth moving-interval height mean**<br>`eq:smooth-bound`<br>Lines 744-759; equations (3.12) | Combines the twisted second moment, Mellin decay, and Plancherel to bound the smoothed height mean. | [Lemma 3.1](#lem-twist); [Mellin transform of the smoothed interval](#eq-mellin); [Plancherel identity for the height average](#eq-plancherel) |
| <a id="step-remove-annular-weights"></a>**Removal of smoothing and comparison of bounds**<br>`step:remove-annular-weights`<br>Lines 761-778 | The smoothing changes at most two boundary moduli on the relevant height block. Bounds this error by Weil, then combines the spectral and elementary estimates to obtain the minimum in Lemma 3.2. | [Lemma 2.5](#lem-weil); [Small-power divisor bound](#step-divisor-small-power); [Smooth moving-interval height mean](#eq-smooth-bound); [Elementary moving-interval estimate](#eq-elementary) |
| <a id="step-cumulative-dyadic-height"></a>**Dyadic decomposition of the cumulative sum**<br>`step:cumulative-dyadic-height`<br>Lines 788-806; equations (3.13) | Decomposes the cumulative modulus sum into dyadic annuli and uses Minkowski. At most two contributing blocks lie below base height one; these are treated directly. | [Lemma 3.2](#lem-annulus); [Kloosterman symmetries](#eq-symmetries) |
| <a id="step-exceptional-real-cutoffs"></a>**Exceptional set uniform over real cutoffs**<br>`step:exceptional-real-cutoffs`<br>Lines 808-823 | Applies Chebyshev on finitely many dyadic frequency blocks and covers each real interval $[N,2N)$ by two adjacent blocks. Their lengths sum to at most $3N$. | [Theorem 1.1](#thm-height) |
| <a id="step-vector-Abel-summation"></a>**Vector partial summation for the weight 1/c**<br>`step:vector-Abel-summation`<br>Lines 834-852; equations (3.14), (3.15) | Applies partial summation coordinatewise and Minkowski to a finite vector of frequencies. An unweighted height mean then supplies the corresponding mean with weight $1/c$. | Direct in-text argument; see the source locator. |
| <a id="step-two-frequency-reduction"></a>**Divisor reduction and treatment of the axes**<br>`step:two-frequency-reduction`<br>Lines 865-888; equations (3.17), (3.18) | Uses cumulative Selberg, Cauchy-Schwarz, and divisor counting to apply Theorem 1.1. Treats base heights below one directly and handles the coordinate axes separately. | [Cumulative Selberg identity](#eq-selberg-sum); [Theorem 1.1](#thm-height); [Ramanujan sums on the coordinate axes](#eq-axes); [Small-power divisor bound](#step-divisor-small-power) |

### Pair-difference discrepancy

| Step and source | Content | Direct recorded inputs |
| --- | --- | --- |
| <a id="step-ks-repetition-and-arcs"></a>**Perturbation and arc approximation**<br>`step:ks-repetition-and-arcs`<br>Lines 581-587 | Perturbs repeated points to distinct points and passes to limits. Monotone approximation then covers the stated arc conventions and degeneracies. | [Koksma-Szusz base inequality](#external-brs-discrepancy) |
| <a id="geom-difference-fourier"></a>**Fourier coefficients of ordered differences**<br>`geom:difference-fourier`<br>Lines 914-918 | The normalized Fourier coefficient of the multiset of ordered differences is the squared absolute value of the coefficient of the original point set. | Direct in-text argument; see the source locator. |
| <a id="geom-diagonal-removal"></a>**Removal of diagonal pairs**<br>`geom:diagonal-removal`<br>Lines 921-925 | Splits the difference measure into distinct pairs and a mass $1/N_Y$ at zero. The resulting discrepancy change is at most $1/N_Y$. | Direct in-text argument; see the source locator. |
| <a id="eq-pair-block"></a>**Dyadic frequency blocks for discrepancy**<br>`eq:pair-block`<br>Lines 929-936; equations (4.3) | Uses Proposition 3.4 and the cardinality comparison to bound each weighted dyadic frequency block. The blocks on the axes are retained; the origin is excluded. | [Proposition 3.4](#prop-two); [Size of the modular-inverse point set](#support-cardinality-comparison) |
| <a id="geom-pair-upper"></a>**Upper discrepancy bound**<br>`geom:pair-upper`<br>Lines 927-940 | Sums the frequency blocks, applies Lemma 4.1, and chooses the Fourier cutoff of order $X^2$ to prove the upper discrepancy bound. | [Lemma 4.1](#lem-pair-pointwise); [Dyadic frequency blocks for discrepancy](#eq-pair-block); [Size of the modular-inverse point set](#support-cardinality-comparison) |
| <a id="geom-first-coordinate-injectivity"></a>**Injectivity of the first coordinate**<br>`geom:first-coordinate-injectivity`<br>Lines 942 | The first coordinate determines the reduced denominator and then its unique modular inverse. Thus distinct points have distinct first coordinates, including the modulus-one origin. | Direct in-text argument; see the source locator. |
| <a id="geom-pair-lower"></a>**Lower discrepancy bound from an empty strip**<br>`geom:pair-lower`<br>Lines 942-943 | Circular separation gives a strip containing no differences, including no diagonal difference. Letting its left endpoint approach zero gives the lower discrepancy bound. | [Circular separation of reduced fractions](#eq-farey-separation); [Injectivity of the first coordinate](#geom-first-coordinate-injectivity) |
| <a id="support-cardinality-comparison"></a>**Size of the modular-inverse point set**<br>`support:cardinality-comparison`<br>Lines 143-148 | The summatory totient estimate gives $N_X=(3/\pi^2)X^2+O(X\log(2X))$, hence $N_Y\asymp X^2$ for $X\le Y\le2X$. The discrepancy proof needs the lower bound for normalization. | [Summatory totient asymptotic](#external-totient) |

### Elementary distance argument

| Step and source | Content | Direct recorded inputs |
| --- | --- | --- |
| <a id="eq-farey-gap"></a>**Lengths of adjacent Farey gaps**<br>`eq:farey-gap`<br>Lines 540-544; equations (2.8) | The length of an adjacent Farey gap is $1/(qq')$ and lies between $Q^{-2}$ and $Q^{-1}$. | [Lemma 2.7](#lem-farey) |
| <a id="step-farey-nesting"></a>**Nesting of Farey intervals**<br>`step:farey-nesting`<br>Lines 544 | Increasing the Farey order adds fractions, so every new gap is contained in an old gap. | Direct in-text argument; see the source locator. |
| <a id="geom-covering-upper"></a>**Upper covering bound from Farey products**<br>`geom:covering-upper`<br>Lines 977-979 | Takes $Q=\lfloor\sqrt{X/2}\rfloor$ and uses a point in every product of Farey gaps to obtain the upper covering bound, including rational endpoints by closure. | [Lemma 5.1](#lem-farey-product); [Lengths of adjacent Farey gaps](#eq-farey-gap) |
| <a id="eq-gap-monotone"></a>**Adaptive Farey intervals**<br>`eq:gap-monotone`<br>Lines 983-987; equations (5.1) | Combines the Farey gap bounds with nesting and defines the least order at which the gap containing an irrational coordinate is short enough. | [Lengths of adjacent Farey gaps](#eq-farey-gap); [Nesting of Farey intervals](#step-farey-nesting) |
| <a id="eq-layer-cake"></a>**Layer-cake identity for positive moments**<br>`eq:layer-cake`<br>Lines 1049-1052; equations (5.6) | Expresses a positive distance moment as the integral of its tail by Tonelli's theorem. | Direct in-text argument; see the source locator. |
| <a id="geom-positive-moment-upper"></a>**Upper bounds for positive distance moments**<br>`geom:positive-moment-upper`<br>Lines 1048-1068 | Integrates the distance-tail estimate in the three ranges of $s$, using the already proved upper covering bound for the support cutoff. | [Lemma 5.4](#lem-distance-tail); [Upper covering bound from Farey products](#geom-covering-upper); [Layer-cake identity for positive moments](#eq-layer-cake) |
| <a id="eq-counting-lower"></a>**Counting lower bound for positive moments**<br>`eq:counting-lower`<br>Lines 1099-1103; equations (5.8) | The union of small discs around the $N_X$ points covers at most half the torus. This gives a lower moment bound of order $X^{-s}$ for every fixed $s>0$. | [Elementary upper bound for the cardinality](#support-cardinality-upper) |
| <a id="eq-square-integral"></a>**Moment of the distance to a square boundary**<br>`eq:square-integral`<br>Lines 1105-1108; equations (5.9) | On an empty square, the distance to the point set is at least the distance to the boundary. Integrates this boundary distance explicitly. | Direct in-text argument; see the source locator. |
| <a id="geom-supercritical-lower"></a>**Supercritical lower bound from one empty square**<br>`geom:supercritical-lower`<br>Lines 1110 | One empty square of side $1/(2\sqrt X)$ gives the lower moment bound of order $X^{-1-s/2}$ for $s>2$. | [Lemma 5.5](#lem-empty); [Moment of the distance to a square boundary](#eq-square-integral) |
| <a id="eq-distance-lower"></a>**Disjoint empty-square packing**<br>`eq:distance-lower`<br>Lines 1112-1119; equations (5.10) | Packs disjoint empty squares near rational pairs with small denominators. Their contributions produce the square of a harmonic totient sum. | [Lemma 5.5](#lem-empty); [Circular separation of reduced fractions](#eq-farey-separation); [Moment of the distance to a square boundary](#eq-square-integral) |
| <a id="geom-totient-harmonic"></a>**Harmonic sum of totients**<br>`geom:totient-harmonic`<br>Lines 1120-1123 | Derives $\sum_{q\le y}\varphi(q)/q^2=(6/\pi^2)\log y+O(1)$ by the elementary Mobius formula and a harmonic-sum estimate. | Direct in-text argument; see the source locator. |
| <a id="geom-critical-lower"></a>**Critical second-moment lower bound**<br>`geom:critical-lower`<br>Lines 1112-1125 | Combines the disjoint-square packing with the totient sum to obtain the critical $X^{-2}(\log X)^2$ lower bound. The counting bound covers the remaining bounded range of heights. | [Disjoint empty-square packing](#eq-distance-lower); [Harmonic sum of totients](#geom-totient-harmonic); [Counting lower bound for positive moments](#eq-counting-lower) |
| <a id="geom-empty-tangent-disc"></a>**Empty tangent disc and lower covering bound**<br>`geom:empty-tangent-disc`<br>Lines 1127-1141 | Proves directly that a disc tangent at the origin contains no lift of the point set. This gives the lower covering bound independently of the empty-rectangle lemma. | Direct in-text argument; see the source locator. |
| <a id="geom-negative-upper"></a>**Upper bound for negative moments**<br>`geom:negative-upper`<br>Lines 1148-1155 | Disc counting and the layer-cake identity for negative powers establish finiteness and the upper bound for $-2<s<0$. | [Elementary upper bound for the cardinality](#support-cardinality-upper) |
| <a id="geom-negative-lower"></a>**Lower bound for negative moments**<br>`geom:negative-lower`<br>Lines 1155-1158 | Jensen's inequality and only the upper first-moment estimate in Theorem 1.6 give the lower bound for negative moments. | [Theorem 1.6](#thm-distance) |
| <a id="geom-negative-divergence"></a>**Divergence of negative moments**<br>`geom:negative-divergence`<br>Lines 1159 | The origin belongs to the point set, so a local polar integral proves divergence for $s\le-2$. | Direct in-text argument; see the source locator. |

### Long-frequency argument

| Step and source | Content | Direct recorded inputs |
| --- | --- | --- |
| <a id="step-large-sieve-endpoint-sums"></a>**Endpoint sums in the large-sieve remainder**<br>`step:large-sieve-endpoint-sums`<br>Lines 561-571 | Writes the off-diagonal interval sum as a difference of two cosecant bilinear forms and bounds each by the Montgomery-Vaughan inequality. | [Cosecant bilinear inequality and endpoint argument](#external-large-sieve) |
| <a id="step-long-trig-polynomial"></a>**Trigonometric-polynomial representation**<br>`step:long-trig-polynomial`<br>Lines 1164-1168; equations (6.1) | Opens the Kloosterman sums to express $A_Q(n,1)$ using the $N_Q$ distinct reduced fractions as frequencies and inverse phases of modulus one as coefficients. | Direct in-text argument; see the source locator. |
| <a id="step-determinant-one-pairs"></a>**Determinant-one pair calculation**<br>`step:determinant-one-pairs`<br>Lines 1218-1232; equations (6.3) | Compact support restricts the centered determinant residue to $+1$ or $-1$. The Chinese remainder theorem counts the pairs; their conjugate inverse phases give the cosine correction. | [Lemma 6.2](#lem-poisson); [Trigonometric-polynomial representation](#step-long-trig-polynomial) |
| <a id="step-coprime-lattice-sum"></a>**Uniform coprime lattice sum**<br>`step:coprime-lattice-sum`<br>Lines 1270-1284 | A uniform Lipschitz bound permits a Riemann-sum comparison on each sublattice. Mobius inversion produces the coprime main term and the $O(Q\log(2Q))$ error before multiplication by $2L$. | Direct in-text argument; see the source locator. |
| <a id="step-abel-variation-localization"></a>**Abel summation and variation localization**<br>`step:abel-variation-localization`<br>Lines 1289-1313; equations (6.5), (6.6), (6.7) | Combines the uniform sharp-interval remainder bound with the positive weighted correction. Abel summation and small variation near zero and in the far tail force a large remainder at radius comparable to $Q^2$. | [Proposition 6.1](#prop-long); [Theorem 1.7](#thm-correction); [Lemma 6.2](#lem-poisson); [Elementary upper bound for the cardinality](#support-cardinality-upper) |

### Shared elementary facts

| Step and source | Content | Direct recorded inputs |
| --- | --- | --- |
| <a id="eq-farey-separation"></a>**Circular separation of reduced fractions**<br>`eq:farey-separation`<br>Lines 544-548; equations (2.9) | Distinct reduced fractions modulo one, with denominators at most $Q\ge2$, are separated by at least $1/[Q(Q-1)]$. The proof uses denominator arithmetic directly. | Direct in-text argument; see the source locator. |
| <a id="support-cardinality-upper"></a>**Elementary upper bound for the cardinality**<br>`support:cardinality-upper`<br>Lines 143-148 | The identity $N_X=\sum_{c\le X}\varphi(c)$ and $\varphi(c)\le c$ give $N_X\le X^2$ for $X\ge1$. This is sufficient for the distance counting arguments and the interval remainder bound. | Direct in-text argument; see the source locator. |

## Literature inputs

Cited literature results are treated as trusted inputs and are not reproved here. Their precise statements, hypotheses, parameter ranges, and normalizations must match each application.

The entries below are inputs to the written proofs. Locators follow the citations in v17. Different uses of the same work remain separate nodes so the graph identifies the particular result being used.

| Input | Reference and locator | Used in |
| --- | --- | --- |
| <a id="external-brs-spectral"></a>**Kuznetsov formula and local spectral large sieve**<br>`external:brs-spectral` | [BRS](#ref-brs), Lemma 4.3 | [Lemma 2.1](#lem-kuznetsov) |
| <a id="external-brs-transforms"></a>**Twisted Bessel transform estimates**<br>`external:brs-transforms` | [BRS](#ref-brs), Lemma 4.2 | [Lemma 2.3](#lem-transforms) |
| <a id="external-brs-discrepancy"></a>**Koksma-Szusz base inequality**<br>`external:brs-discrepancy` | [BRS](#ref-brs), Lemma 2.1 | [Perturbation and arc approximation](#step-ks-repetition-and-arcs) |
| <a id="external-dlmf"></a>**Integral representations of J and K Bessel functions**<br>`external:dlmf` | [DLMF](#ref-dlmf), Equations (10.9.6) and (10.32.9) | [Low-spectrum Bessel kernel bounds](#step-low-kernel-integrals) |
| <a id="external-weil"></a>**Weil bound**<br>`external:weil` | [IK](#ref-ik), Corollary 11.12 | [Lemma 2.5](#lem-weil) |
| <a id="external-divisor"></a>**Divisor small-power bound**<br>`external:divisor` | [IK](#ref-ik), Equation (1.81) | [Small-power divisor bound](#step-divisor-small-power) |
| <a id="external-selberg"></a>**Selberg identity for integer arguments**<br>`external:selberg` | [Xi](#ref-xi), Equation (1.1) | [Lemma 2.6](#lem-selberg) |
| <a id="external-farey"></a>**Adjacent Farey fractions**<br>`external:farey` | [HW](#ref-hw), Theorems 28 and 30 | [Lemma 2.7](#lem-farey) |
| <a id="external-ramanujan"></a>**Ramanujan-sum identity**<br>`external:ramanujan` | [HW](#ref-hw), Theorem 271 | [Ramanujan sums on the coordinate axes](#eq-axes) |
| <a id="external-totient"></a>**Summatory totient asymptotic**<br>`external:totient` | [HW](#ref-hw), Theorem 330 | [Size of the modular-inverse point set](#support-cardinality-comparison) |
| <a id="external-large-sieve"></a>**Cosecant bilinear inequality and endpoint argument**<br>`external:large-sieve` | [MV](#ref-mv), Lemma 2, equation (2.1); proof of Theorem 1 | [Endpoint sums in the large-sieve remainder](#step-large-sieve-endpoint-sums) |
| <a id="external-plancherel"></a>**Plancherel theorem**<br>`external:plancherel` | [Grafakos](#ref-grafakos), Theorem 2.2.14 (4) | [Plancherel identity for the height average](#eq-plancherel) |
| <a id="external-poisson"></a>**Poisson summation**<br>`external:poisson` | [Grafakos](#ref-grafakos), Theorem 3.2.8 | [Lemma 6.2](#lem-poisson) |

### Bibliographic key

<a id="ref-brs"></a>**BRS.** Valentin Blomer, Morten S. Risager, Igor E. Shparlinski. *Triple sums of Kloosterman sums and the discrepancy of modular inverses*. J. Lond. Math. Soc. (2) 112 (2025), no. 3, e70291, 30 pp..

<a id="ref-dlmf"></a>**DLMF.** *NIST Digital Library of Mathematical Functions*. Release 1.2.8 of 2026-09-15.

<a id="ref-ik"></a>**IK.** Henryk Iwaniec and Emmanuel Kowalski. *Analytic number theory*. AMS Colloquium Publications 53 (2004).

<a id="ref-hw"></a>**HW.** G. H. Hardy and E. M. Wright. *An introduction to the theory of numbers*. 6th ed., Oxford University Press, 2008.

<a id="ref-mv"></a>**MV.** H. L. Montgomery and R. C. Vaughan. *The large sieve*. Mathematika 20 (1973), 119-134.

<a id="ref-grafakos"></a>**Grafakos.** Loukas Grafakos. *Classical Fourier analysis*. 3rd ed., Graduate Texts in Mathematics 249, Springer, 2014.

<a id="ref-xi"></a>**Xi.** Ping Xi. *An elementary proof of the Selberg identity for Kloosterman sums*. Preprint (2023), arXiv:2306.16929.

### Attribution and comparison references

BRS Lemma 4.4 and Corollary 4.5 are credited for the duality argument that v17 derives locally; BRS Section 4.4 is credited for the twisted spectral method. These attributions do not add a second independent input to the displayed proof. Selberg's 1938 paper and Kuznetsov are historical references for Selberg's identity; Xi (1.1) is the explicit modern locator used here.

The companion paper, the earlier mean estimates of Proskurin, Kueh and Vinogradov, the conjectural comparison of Sarnak and Tsimerman, the Farey-distribution work of Dress and Niederreiter, the distance comparisons of Kargaev-Zhigljavsky and Marklof, and the correlation and large-sieve-matrix work of Boca-Zaharescu and Boca-Radziwill provide context in the introduction or conclusion. They are not prerequisites of the new proofs merely because they are cited nearby. The graph starts from the spectral inputs as packaged in BRS; it does not expand the full literature ancestry of those inputs.

## Section 7: unnumbered discussion

Section 7 has no numbered theorem, lemma, proposition, corollary, or remark. Its proved consequences and open directions are recorded separately below.

| Subsection | Source lines | Content |
| --- | --- | --- |
| 7.1: Individual heights | 1320-1322 | Open pointwise bounds remain distinct from the proved height averages and exceptional-set corollaries. |
| 7.2: Small-power factors | 1324-1326 | Discusses replacing epsilon losses by logarithmic factors; no stronger bound is asserted. |
| 7.3: Distance constants | 1328-1338 | The sharper covering constants follow from the Farey-product upper calculation and the independent tangent-disc lower calculation. Existence of limiting normalized moments or a limiting covering constant remains open. |
| 7.4: Long ranges and a fixed second argument | 1340-1344 | Discusses unevaluated higher determinants and the open question of an unweighted asymptotic at scale $Q^2$. The final paragraph adapts the Section 6 proofs to fixed nonzero integer $h$, choosing $\tau=1-1/(4\sqrt{\lvert h\rvert})$; its constants depend on $h$. This is an unnumbered extension, not an extra theorem. |

## Maintenance

This file is generated from `docs/dependency_inventory.json` by `python3 scripts/build_dependency_graph.py`. Update the record and source fingerprint when changing the manuscript baseline, then regenerate the inventory and graphs together.
