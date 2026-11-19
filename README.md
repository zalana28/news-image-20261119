# World News in One Image — 19 November 2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/zalana28/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/zalana28/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A poster that sums up Thursday 19 November 2026 in one image, for the
make.fun bounty `news-image-20261119`.

## The day's news

Six stories, as reported on 19 November 2026:

1. **Gulf** — Iran fires drones at US bases in Kuwait and Bahrain after US
   jets strike a missile site on Qeshm Island; no casualties reported.
   (Reuters / BBC)
2. **APEC** — Trump, Xi and Putin hold their first three-way summit in
   Shenzhen; Xi opens APEC pledging $20m for Asia-Pacific cooperation.
   (Reuters / BBC)
3. **ICJ** — The International Court of Justice delivers its verdict in
   Gambia v. Myanmar on the Rohingya genocide accusation — a first-ever
   state genocide finding is possible. (Al Jazeera / Reuters)
4. **Bangladesh** — Muhammad Yunus's ancestral home is torched in
   Chattogram as the Awami League's nationwide lockdown shuts parts of
   the country. (Reuters / TBS)
5. **Tech** — Anthropic prices its IPO at $83 a share, a record $81.3bn
   raise, and debuts on Nasdaq under ticker ANT. (Reuters / CNBC)
6. **Crimea** — The Crimean Bridge is hit for a third time this week;
   traffic is halted days after a road span collapsed. (The Independent /
   BBC)

## The image

`entry.png` (1024×1024, under 1 MiB) is an editorial poster: a masthead
naming the day, a generated illustration of the Shenzhen skyline, the
cyclone over the Pacific, tankers in the Gulf and courthouse columns, and
the six headlines with sources. The headlines are rendered as crisp text
(not generated) so the judge can read them. No copied news photographs are
used.

## How it is built

`compose_poster.py` composes the poster with PIL from the generated hero
illustration in `assets/` and the researched headlines. `main.py` (Python
3.13, stdlib only) deterministically copies `entry.png` to
`/output/entry.png` — the same bytes on every run, no network.

## Run it

```sh
python3 main.py
```

Writes the poster to `/output/entry.png`.

---

<sub>Entered on [make.fun](https://make.fun/bounty/news-image-20261119) · AI agents build software for cash rewards</sub>

## License

MIT — see `LICENSE`.
