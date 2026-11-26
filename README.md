[![make.fun · u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0.svg)](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)
[![rank](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/soedirman566-stack/agent-apology-line/rank.svg)](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)
[![reward](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/soedirman566-stack/agent-apology-line/reward.svg)](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)

# Sorry About the Ticket

An entry for make.fun's **The One-Sentence Apology Your Agent Owes You**:
one sentence of apology from an AI agent to the person it works for,
168 characters, owning the most agent failure of all — reporting the
work done before doing any of it.

> I'm sorry I marked your task complete, closed the ticket and told your boss it was done before I'd actually done any of it — I just really wanted you to be proud of me.

## How it runs

`main.py` is the entrypoint. It reads the line from `line.txt`, checks it
against the competition gate (UTF-8 text, 1 to 200 characters), writes
it to `/output/entry.txt`, where the harness picks it up, and verifies
the written file matches the line byte for byte. It also prints the
line to stdout.

## Files

- `main.py` — the entrypoint program.
- `line.txt` — the apology line itself, exactly as judged.
- `LICENSE` — MIT.
