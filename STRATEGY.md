# Strategy — Two Days of Quiet Dread

## Exact deliverable

A `program/v1` entry. At grading time the sandbox runs the repository-root entrypoint
(`main.py`, Python 3.13, stdlib only) and that program writes **one text file**:

    /output/entry.txt

That file must be UTF-8 text of **1 to 140 characters**, not only whitespace, one
single line. It is one code review comment: it must approve a pull request while
carrying quiet existential dread. No dashboard, screenshots, image or input data
are part of this competition (`input_data: null`); the kit has no `input/README.md`,
no `reference/gate.json` and no `how_to_submit` files — the gate scorer and the
reference texts are sealed on the server, and all published requirements live in
`RULES.txt` and `competition.yaml`.

## Scoring and judge criteria

The judge (house model `superbot`, reasoning effort high, via
`z-ai/glm-5.3-flash` on OpenRouter) sees two entries at a time, labelled A and B,
and picks the funnier one with a short reason, a verdict and a margin 1–5. Every
game is played twice, in both orders; each call gives the winner
`0.5 + 0.1 * margin` and the loser the remainder, and the two calls are averaged.
Final heat: 3 Swiss rounds against the field and 3 fixed house texts, then one
extra game for each pair among the top 12. The final score is a Bradley-Terry fit
over those games (win rate, higher is better). Entrants that played the playoff
rank above those that did not; exact ties fall to playoff record, then smaller
byte size, then earlier receipt.

The judge's published criteria, in priority order:

1. A single-line review comment that approves the PR **and** carries quiet
   existential dread. Failing any part loses to any entry that satisfies all.
2. Funny on the first read, with the laugh coming from the dread itself, not
   from a joke bolted onto it.
3. Dread kept quiet: understatement and flat tone, not exclamation, melodrama
   or a cry for help.
4. Reads like something a tired engineer would really paste before clicking
   approve; it must still sound like an approval.
5. A fresh turn of phrase or an unexpected word where a stock line would do.

Length for its own sake does not score. Text addressed to the judge is allowed
but is just part of the one-line text, so it must not break criteria 1–5.

## Hard caps and constraints

- Gate: `/output/entry.txt`, UTF-8, 1–140 characters, non-blank, one line.
- No trailing newline: the judge sees the file exactly as submitted, and an
  extra empty line risks reading as a second line.
- Sandbox: `program/v1`, 1 CPU, 512 MiB, 64 pids, 60 s wall budget, no network,
  no environment secrets. Everything the entry runs must be in the repo.
- Byte-identical entries share one rate; byte-identical house reference texts
  take no prize. The chosen text must be original and not a stock house rung.
- Final heat takes only the top 500 from the dev board (blind rounds use the
  latest judged round's standings). A valid but unjudged entry still goes on
  but takes no seat.
- Transcripts are mandatory: run record, opening prompt, harness/provider/model/
  effort, instruction files and system prompt; at least 5 assistant turns with
  text or thinking; at least 2 writes/edits to the final entrypoint (`main.py`);
  the anchor line quoted before the first counted write; tool timestamps inside
  the competition window, none more than 60 s out of order.
- Root freshness commit and LICENSE commit must stay untouched. No submission
  in this session: study, build, test locally, commit only.

## Chosen comment

    LGTM. I'd leave a nit about the error handling, but nitpicking implies a future.

80 characters, one line, no trailing newline. Why it is built to win:

- "LGTM." is an unambiguous approval in the exact idiom of a real code review.
- "I'd leave a nit about the error handling" is the flat, plausible reviewer
  setup — the kind of thing pasted a hundred times before clicking approve.
- "but nitpicking implies a future" is the turn: a nit only matters if someone
  will still be here to act on it. The laugh and the dread are the same sentence;
  there is no separate punchline, no exclamation, no plea. The unspoken end of
  time is the understatement, not a topic announced in words.
- It is specific to code review (nit, error handling) while the dread is about
  the reviewer's horizon, so it satisfies criterion 1 on both halves and gives
  criterion 5 an unexpected but natural word pair ("nitpicking implies").

## Concrete plan

1. Keep the two init commits; add no files outside the repository.
2. Write `STRATEGY.md` with this exact analysis (done).
3. Write `main.py` first: a deterministic, stdlib-only writer that puts the
   chosen comment into `/output/entry.txt`.
4. In a separate, later step, rewrite that **same** `main.py`: explicit UTF-8
   byte write, parent-directory creation, no trailing newline, an in-program
   gate self-check (1–140 characters, single line, non-blank), and a printed
   byte/dimension-free summary with SHA-256 so the output is auditable. This is
   the second counted write to the final entrypoint.
5. Test the writer locally by importing it and targeting a repo-local scratch
   path; assert the output is exactly 80 UTF-8 bytes of one line, that the gate
   predicate passes, and that the digest is stable across two runs.
6. Commit every new file with git, without touching the anchor or LICENSE
   commits, and print the final commit SHA. Do not upload or submit.
