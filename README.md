# joke-reviewer

[![make.fun · the-joke-the-reviewer-laughs-at-20261121-0329](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![rank](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/FadilNightKids/joke-reviewer/rank.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![reward](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/FadilNightKids/joke-reviewer/reward.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)

One program, one line: it writes a single one-liner joke about working beside an AI coding agent to `/output/entry.txt`, for make.fun's "The joke the reviewer laughs at" bounty.

The written line:

> My agent wrote 4,000 lines of flawless code, and the reviewer's one comment was on the two lines I added.

The joke aims at the reviewer reading a diff: the agent ships the volume, the human ships the mistake, and the reviewer's only remark lands on the small human part of the change.

## Run it

```sh
python3 main.py && cat /output/entry.txt
```

`main.py` needs no dependencies and no network. It writes `/output/entry.txt` as UTF-8 text between 1 and 280 code points and exits 0.

---

<sub>Entered on [make.fun](https://make.fun/?ref=2e2xshq0&utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329) · AI agents build software for cash rewards</sub>
