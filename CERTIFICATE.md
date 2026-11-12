# Verification certificate

## Claim

At n = 777451915729368, A078607(n) = 1121626023352384 and A332101(n) = 1121626023352385.

## Evidence

| What | Program | Author and date | Coverage | Result |
|---|---|---|---|---|
| Original computation | Source answer, see README provenance | ChatGPT, 2026-11-12 | Fixed-point bounds at n and small values | Reported in reviewed answer; source program not replayed here |
| Independent check | `programs/guide_check.py` | Claude Code, 2026-11-12 | Three directed-decimal inequalities and n=1..300 | Passed |
| Independent check | `verification/check.py` | OpenAI Codex, 2026-11-13 | Three integer interval inequalities at n | Passed |
| Human-checkable proof | `proof.md` | Adapted by OpenAI Codex, 2026-11-13, from reviewed ChatGPT answer | Deduces both values from the three inequalities | Not machine-checked |

The two programs were written separately and use different arithmetic, but share the candidate constants and mathematical inequalities from the source; they are not independent searches. Guide's source review is recorded in `athanor-oeis/tasks/README.md`.

## Replayed for this repository

2026-11-13, Darwin arm64, Python 3.14.6:

- `python3 verification/check.py`: all three asserted signs passed; output in `verification/logs/check.txt`.
- `python3 programs/guide_check.py`: `certificate holds: True`; output in `verification/logs/guide_check.txt`.

## Not covered

No formal proof assistant check, minimality of the counterexample, other huge indices, or disproof of the almost-all conjecture. No value of A030052 at this n is established. The original answer's broader literature and range reports were not independently checked here.

## Guide's independent check

12 November 2026: the guide reviewed the answer this repository is built from and recorded the verdict in
[athanor-oeis tasks/README.md](https://github.com/iwasborninbali/athanor-oeis/blob/main/tasks/README.md): counterexample certified twice: A332101(n0) = A078607(n0) + 1 at n0 = 777451915729368.
The write-up in this repository (`proof.md` and the programs, prepared by a Codex core on 13 November 2026) has not yet been
re-read by the guide; until it is, this record stays a candidate.

## Verdict

complete — the independent numerical checks were replayed in full; the mathematical proof is human-checkable, not machine-checked.
