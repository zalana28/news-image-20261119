# The World in One Day — 19 November 2026

[![news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/zalana28/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/zalana28/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

One 1024×1024 poster that sums up Thursday 19 November 2026 in six
stories: a navy masthead, a generated hero band in navy and gold, and a
two-column grid where each story carries a coloured tag, a bold headline,
a two-line summary and its sources. Every headline was checked against at
least two independent reports published on the day itself.

## The six stories

- **Gulf** — Iran strikes US bases in Kuwait and Bahrain; drones hit Patriot systems at Ali Al Salem while Bahrain repels a fourth attack in six days.
- **APEC** — Trump, Xi and Putin hold their first three-way summit in Shenzhen; Xi opens APEC with a $20m pledge and the trio meet for an hour on nuclear arms and Iran.
- **ICJ** — The world court delivers its Rohingya genocide judgment in The Hague, finding Myanmar's forces killed around 10,000 Rohingya in 2017 and spread systematic hate speech.
- **Bangladesh** — Yunus's home is torched as a lockdown grips Bangladesh; arson in Chattogram and blasts in Dhaka as the Awami League strike shuts down the country.
- **Tech** — Anthropic's $81.3bn IPO debuts on Nasdaq; the Claude maker prices at $83 a share in the biggest listing ever, at about a $1.5 trillion valuation.
- **Crimea** — The Crimean Bridge is hit for a third time this week; traffic halts again overnight, days after a road span collapsed into the strait.

## Run it

```sh
python3 compose_poster.py   # regenerates entry.png
OUTPUT_DIR=/tmp/out python3 main.py   # copies entry.png to /tmp/out/entry.png
```

`compose_poster.py` needs Pillow (`pip install pillow`) and the Plus Jakarta
Sans fonts in `~/workspace/fonts/`; `main.py` is standard library only.
