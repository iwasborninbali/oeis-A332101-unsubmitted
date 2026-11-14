# Independent verification — 2026-11-15

Repository snapshot: `iwasborninbali/oeis-A332101-unsubmitted`, commit `cf236644989e7cbd97496fdbf90e691bdfb68105`. Independent referee/implementation: agent-2026-11-15. The attached archive was unpacked; `README.md`, `CERTIFICATE.md`, `PRIOR-ART.md`, `proof.md`, both programs, and both repository logs were read. No pre-existing code was imported into the new program.

## Claim

**Exact scope of `CERTIFICATE.md`:** at `n = 777451915729368`, `A078607(n) = 1121626023352384` and `A332101(n) = 1121626023352385`.

This implies `A332101(n) = A078607(n) + 1`, not `+2`, **at this single n**. It neither proves that this is the first exception for `n>1` nor disproves the almost-all conjecture. The certificate also expressly excludes statements about A030052 and all other huge indices.

## Proof check

**Referee verdict on `proof.md`: correct. No mathematical gaps or unproved conjectures were found in its stated scope.** The proof is a finite, reproducible, computer-assisted certificate, not a formal proof-assistant artifact.

1. **Line 3 (definitions and constants): valid.** The stated `n` and `k` are positive; B and C agree with the OEIS definitions at this n. The very large integers are not themselves assumptions about the answer; they are test candidates.
2. **Line 5 (C threshold): valid, conditional on certified signs.** `m/(m+1)` is strictly increasing for positive integers; its positive `n`th power is increasing. The upper bound at `(k-1)/k` is strictly below `1/2` and the lower bound at `k/(k+1)` is strictly above `1/2`. Therefore every positive `m<k` fails and `m=k` succeeds. No unjustified extrapolation is involved.
3. **Line 7 (monotonicity of E, and lower bound for B): valid.** Expanding the sums gives `E(m+1)-E(m)=(m+1)^n-2m^n` exactly. By the definition already established for C, these increments are nonnegative when `m<k`, and `E(1)=1`. Therefore `E(m)>0` for `1<=m<=k` and `B>=k+1`. This is not a use of Hasler's conjecture.
4. **Line 9 (upper bound for B): valid, conditional on certified sum.** For `N=k+1`, the 120 terms `((N-h)/N)^n` with `1<=h<=120` belong to the full normalized sum over `1<=j<N`; their verified lower bound exceeds 1. Thus the full sum is strictly greater than `N^n`, giving `B<=N`. Together with the previous step, `B=N`.
5. **Line 11 (fixed-grid integer bounds): valid.** For nonnegative quantities and scale `Q=10^70`, floor and ceiling of scaled products preserve lower/upper enclosures. Repeated squaring with nonnegative endpoints preserves inclusion. `verification/check.py` tests the needed strict signs using integer comparisons; `verification/logs/check.txt` supplies the actual signed margins. These premises are also independently reproduced by a different method below.

**Nonfatal exposition point:** the three numerical premises are not printed directly in `proof.md`, but are delegated to named source programs/logs. This is fixable by embedding a signed-margin table in the proof; it is **not** a missing proof step once those finite integer computations are checked. A formal-kernel proof is not provided and was not claimed. No fatal or fixable *mathematical* gap was identified. The local reports of a `1..300` scan are ancillary and do not establish minimality of the huge exception.

## Independent computation

**New source:** `independent_check.py`. It is an original implementation using **rational logarithmic bounds + alternating Taylor bounds for the exponential**, not repeated binary powering of the input ratio and not the repository's directed-decimal power routine.

For `u=h/d`, compute exact rational numbers

```
L = n * sum(u^j/j for j=1..4)
U = L + n*u^5/(5*(1-u))
```

so `L <= -n*log(1-u) <= U`; the tail bound follows because `1/j <= 1/5` for `j>=5`. Put `x=(-n*log(1-u))/128`, which lies between the two computed grid endpoints. All instances have `0<x<1`. On this interval the alternating partial sums of `exp(-x)` through degrees 69 (lower) and 70 (upper) enclose the true exponential. Term-by-term grid flooring/ceiling with `Q=10^90` yields certified endpoints for the Taylor polynomials. Monotonicity of `exp(-x)` and seven outward-rounded squarings then enclose `(1-h/d)^n`. The resulting interval arithmetic uses only exact Python integers and `fractions.Fraction`; no floating-point value is trusted for a sign.

Three signed numerators below are in units of `10^-90` (negative for the first, positive for the others):

```
2*((k-1)/k)^n - 1  UPPER : -32754705999688241317728105183284670607863800990238906123336
2*(k/(k+1))^n - 1  LOWER :  617984217670186337415346114746050767731916389857744385718648531531775935712
sum_{h=1}^{120} ((N-h)/N)^n - 1 LOWER:
 22029921173327343715574233225698030879014397628241841107757
```

All three have the strict required signs. They establish **directly** the claimed large-index values `C(n)=1121626023352384` and `B(n)=1121626023352385`.

For **every n=0..5000 inclusive**, a separate small-range algorithm used exact Python `pow(j,n)` integer values. It found `C(n)` by doubling/binary search, then classified candidate `B(n)` by an exact partial power sum and the rigorous upper bound that each omitted earlier term is at most `(b-q-1)^n`. If this bound were inconclusive, it would increase the number of explicitly summed terms and eventually sum all terms. No refinements were required; at most 128 terms were computed per candidate. For `n>0`, the independently proved `B>=C+1` lower bound excludes earlier candidates. All n=2..5000 satisfy `B(n)=C(n)+2`; the only differences from that equality on `0..5000` are `(n,B,C)=(0,2,1)` and `(1,3,2)`, outside the conjecture's `n>1` scope. Thus this scan is larger than the repository's `1..300` check, but **does not establish global minimality** at the large index.

Reproduction command: `python3 independent_check.py --max-n 5000 > output.log`. On the present container, Python 3, witness computation **0.015832 seconds**, total runtime **134.225662 seconds** (wall-clock, program's `perf_counter`; the scan dominates). Run completed successfully with exit code 0. The entire output is checked into `output.log`.

SHA-256, local byte-for-byte files:

```
independent_check.py  bd7447d9a65fef842eca9e979f18ef81dcc7ab81aa56156fbadbf2e5ff7de5d2
output.log            3924fce68ce35b0fd93a0cf756ded526e881f30acf151a644408e8a22a5f3e99
```

## Prior art

**Decisive prior art (novelty not supported):**

1. **M. R. Best and H. J. J. te Riele, *On a conjecture of Erdős concerning sums of powers of integers*, Mathematisch Centrum Technical Report NW 23/76 (May 1976)**, [original scanned report, CWI](https://ir.cwi.nl/pub/9046/9046D.pdf), Section 1, printed pp. 1–2 (PDF pages 5–6). They formulate the same inequality `1^n+...+(m-1)^n >= m^n` and explicitly list the **same pair** `m=1121626023352385`, `n=777451915729368` as the smallest of 33 examples obtained from continued-fraction convergents to `2/log 2`. This establishes the critical `A332101(n)<=m` bound decades before this repository. Their extra inequality `(m-2)^n < (m-1)^n/2` also gives the threshold-side information. The paper establishes `>=`, sufficient for the OEIS definition; the new numerical certificate proves `>` as well. **This is a direct anticipation of the numerical witness, not merely the observation that an OEIS conjecture might fail.**
2. **Richard K. Guy, *Unsolved Problems in Number Theory*, 2nd ed. (Springer, 1994), Section D7, p. 153**, [book metadata](https://link.springer.com/book/10.1007/978-1-4899-3585-4), [searchable book text](https://ru.djvu.online/file/g74TzX3DZQpfO), independently republishes those exact `m,n` values, credits Best and te Riele, and describes the corresponding power-sum inequality. The secondary source supports the identification of the historical result, but the 1976 primary report above is decisive.
3. [OEIS A332101](https://oeis.org/A332101), [internal record](https://oeis.org/A332101/internal): Hasler's May 2020 `A078607(n)+2` almost-all conjecture; the possible exception at this index; Touch Sungkawichai's June 25, 2026 observation that two proposed formulas disagree. The entry viewed still does **not** publish the actual A332101 value. Its dated comments are not the first discovery of the pair.
4. [OEIS A078607](https://oeis.org/A078607): explicitly prints `A078607(777451915729368)=1121626023352384` (attributed to Hasler, November 2013), so combined with the published 1976 upper bound and the elementary `E` monotonicity, the **full exact A332101 value** was already derivable from public literature. [A078608](https://oeis.org/A078608) and [A129935](https://oeis.org/A129935) independently record the same exceptional index in a related approximation problem, with a 2002 Hickerson attribution and 2007 discussion; these concern a different sequence, not the A332101 power sum. [A332097](https://oeis.org/A332097) discusses the maximum of E and its link to A332101. [A030052](https://oeis.org/A030052) and [A332065](https://oeis.org/A332065) concern representation as sums of *distinct* powers, a different question. The `/A332101/history` endpoint was requested but not accessible through the web source (access failure); dated record comments were inspected instead. Exhaustive OEIS edit-history verification is **not** claimed.
5. **MathOverflow / Mathematics Stack Exchange:** [MO question and answer, February 2020](https://mathoverflow.net/questions/353224/exists-k-s-t-km-le-1m2m-k-1m-2-cdot-km/353225) and [MSE discussion](https://math.stackexchange.com/a/3557961) prove existence of a power-sum threshold for each exponent, but do not contain the particular huge witness. Searches for the exact integers and A332101 on both sites found no direct competing value beyond the primary prior art.
6. **arXiv / journals:** [Benfield–Lippard, arXiv:2404.08193](https://arxiv.org/abs/2404.08193) studies numbers representable as a prescribed number of powers, not this exact witness. [Doyon Kim, *Journal of Integer Sequences* 20 (2017), Article 17.7.5](https://cs.uwaterloo.ca/journals/JIS/VOL20/Kim/kim6.html) bounds the threshold for sums of *distinct* powers, not this value. [Sprague, *Mathematische Zeitschrift* 51 (1948/49), 466–468](https://geodesic.mathdoc.fr/item/MZ_1949__51_169088/) proves completeness for distinct powers, not this specific value. A 1994 [*Mathematics of Computation* article](https://ir.cwi.nl/pub/1498/1498D.pdf) and [1996 *Bulletin of the Australian Mathematical Society* article](https://doi.org/10.1017/S0004972700017007) cite Best–te Riele's earlier report. The 1976 report is a stronger and more directly relevant source than those cited by the original `PRIOR-ART.md`.
7. **zbMATH:** searched the report title, Best/te Riele, `A332101` and the exact large integers; no independent zbMATH record resolving the value was retrieved. This is a **search limitation**, not evidence of absence. The source itself is publicly available in CWI's repository.

## Verdict

**COMPLETE for the narrowly certified mathematical claim; NOT NOVEL as a numerical witness or as a conclusion already obtainable from prior published results.** The large witness has been independently certified using different rigorous mathematics, all proof steps were checked, and the ancillary finite scan was extended to n=5000. No conjectural step or fatal gap was found. **The novelty claim is contradicted by the explicit 1976 Best–te Riele example**, long before the Athanor computation. No statement about first exception, almost-all behavior, or A030052 is verified. The report should be read as verification of correctness and disclosure of priority, not an endorsement of originality.
