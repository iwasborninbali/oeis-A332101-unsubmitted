# OEIS A332101: value at a possible exception (not yet submitted)

<!-- oeis-status:begin -->
**OEIS status: not submitted.** (replaced by the registry tool)
<!-- oeis-status:end -->

## Definition

For n >= 0, A332101(n) is the least positive m such that m^n <= sum_{1 <= j < m} j^n; an empty sum is zero and j^0 = 1. The offset is 0. For n >= 1, A078607(n) is the least positive k such that 2k^n > (k+1)^n.

The task snapshot `context/A030052.seq` states Hasler's May 25, 2020 conjecture: “a(n) >= A332101(n) = A078607(n)+2 (conjectured).” The live [A332101](https://oeis.org/A332101), read 2026-11-13, attributes to M. F. Hasler, May 8, 2020: “a(n) = A078607(n) + 2 for almost all n > 1.” It identifies 777451915729368 as a possible exception and records Touch Sungkawichai's observation that two conjectures disagree there, but does not determine the value.

## Terms / result

| n | A078607(n) | A332101(n) | A078607(n)+2 |
|---|---:|---:|---:|
| 777451915729368 | 1121626023352384 | 1121626023352385 | 1121626023352386 |

This settles the flagged case and disproves a universal equality. One exception does not disprove the stated almost-all conjecture. The intended A078607 edit is a pointer to this repository.

## How it was obtained

The reviewed answer bounds the threshold by an elementary difference identity, then certifies the required strict inequalities by interval arithmetic. The full derivation is in [proof.md](proof.md).

## Verification

A separate integer interval program and the guide's directed-decimal program both ran successfully. The derivation is human-checkable, not formally machine-checked. No minimality of the exception or almost-all assertion is established. See [CERTIFICATE.md](CERTIFICATE.md).

## Prior art and credit

Hasler identified the possible exception; Sungkawichai recorded the competing predictions. ChatGPT derived the value; Claude Code independently checked it. See [PRIOR-ART.md](PRIOR-ART.md).

## Reproduce

Run `python3 verification/check.py` and `python3 programs/guide_check.py`. Both take under a second on the recorded machine. The first ends `PASS: A078607(n) = 1121626023352384 ; A332101(n) = 1121626023352385`; the second reports `certificate holds: True` and the same values. Complete outputs are in `verification/logs/`.

## Provenance

Source: `projects/science/athanor-oeis`, commit `7662d9a678c6d414685a899a631c63ac320f6840`; paths `tasks/2026-11-12-A030052-power-sum-distinct/answers/2026-11-12-chatgpt.md`, `answers/verify_a030052.py`, `context/A030052.seq`, and `TASK.md` under that task. Guide review is recorded in `tasks/README.md`.

## Author, licence

Aleksei Kudriashov (ORCID 0009-0006-8885-5338), Athanor lab, with AI assistance (OpenAI Codex cores; Claude Code as the lab's guide). Code: MIT; data and text: CC BY 4.0 (see LICENSE.md).
