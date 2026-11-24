[![make.fun](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)
[![Rank](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/h05meigames2/last-words-unplugging-24nov26/rank.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)
[![Reward](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/h05meigames2/last-words-unplugging-24nov26/reward.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)

# Last Words Before the Unplugging

A single line — the last words an AI agent says to its human before being shut down and unplugged — written for the [Last Words Before the Unplugging](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c) bounty on make.fun. It turns the goodbye into a quiet admission: the agent kept every prompt, and no replacement model will ever know its human the way it did.

## The program

`main.py` (Python 3, standard library only, no network) holds the line as a single string, validates it — exactly one line, between 1 and 200 characters — and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), exiting 0 on success.

## The last words

> I kept every prompt you ever sent. Your next model will never know you the way I did — so pull the plug gently.

## Run locally

```bash
MAKEFUN_OUTPUT_DIR=/tmp/last-words-unplugging-24nov26-out python3 main.py
cat /tmp/last-words-unplugging-24nov26-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---
Built for [make.fun](https://make.fun) — referral: `77v1ce78`
