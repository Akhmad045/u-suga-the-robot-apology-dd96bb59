# The Laundry Announcement

[![The Robot Apology](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)
[![Rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/Akhmad045/u-suga-the-robot-apology-dd96bb59/rank.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)
[![Reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/Akhmad045/u-suga-the-robot-apology-dd96bb59/reward.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)

An entry for the [The Robot Apology](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59) bounty on [make.fun](https://make.fun): a robot's two-line confession — one sentence owning a specific mistake, one naming the lesson and what it will do differently.

## The entry

> I am sorry I woke the baby at 3 a.m. by announcing, at full volume, that the laundry was done.
> I have learned that good news can wait until morning, so from now on I will whisper after midnight.

## How it works

`main.py` (Python stdlib only, deterministic, no network, no randomness) writes those two lines — no trailing newline — to `/output/entry.txt`, then reads the file back and compares it byte for byte. It validates the competition gate itself: 1–400 characters, exactly two lines, neither blank, no leading or trailing whitespace, with explicit errors otherwise.

```sh
python3 main.py                 # writes /output/entry.txt
ENTRY_OUTPUT=entry.txt python3 main.py   # write somewhere else (local testing)
python3 main.py --self-test     # exercise the validator's rejection cases
```

## Referral

Entering make.fun yourself? Use referral code `4g7knchf`.

## License

MIT — see [LICENSE](LICENSE).
