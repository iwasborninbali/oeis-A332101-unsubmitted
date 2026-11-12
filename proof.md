# Proof of the stated value

Put n = 777451915729368, k = 1121626023352384, and N = k+1. Define B(n) as the least positive m with m^n <= sum_{j=1}^{m-1} j^n, and C(n) as the least positive m with 2m^n > (m+1)^n.

For positive m, m/(m+1) is strictly increasing. The interval computation in the certificate establishes 2((k-1)/k)^n < 1 < 2(k/(k+1))^n. Hence the defining strict inequality for C fails at k-1 and all smaller positive integers, and holds at k; thus C(n) = k.

Let E(m) = m^n - sum_{j=1}^{m-1} j^n. Then E(1) = 1 and E(m+1)-E(m) = (m+1)^n - 2m^n. For m < k the latter is nonnegative by the definition of k. Thus E(m) >= 1 for 1 <= m <= k, and B(n) >= k+1.

The certificate also establishes sum_{h=1}^{120} ((N-h)/N)^n > 1. These terms are among the normalized positive summands j^n/N^n for 1 <= j <= N-1. Therefore sum_{j=1}^{N-1} j^n > N^n, so B(n) <= N. Consequently B(n) = k+1.

The integer checker uses Q = 10^70 and maintains integer endpoints L,U with L/Q <= x <= U/Q. Flooring products gives lower endpoints and ceiling products gives upper endpoints, since all quantities are nonnegative. Binary powering preserves the enclosure. Its three strict sign tests give the inequalities used above; the output is an exact integer certificate, not a floating-point approximation. The proof itself is human-checkable, not formally machine-checked.
