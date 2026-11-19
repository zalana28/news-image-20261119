#!/usr/bin/env python3
"""Draw the 19 November 2026 world-news poster as a 1024x1024 PNG.

Layout, top to bottom: a navy masthead with the paper name and the date,
a generated hero band, then six stories in a two-column grid, and a
one-line footer. Everything is drawn with Pillow; no network access.

Usage:
    python3 compose_poster.py [output-path]
If no output path is given, the poster is written to entry.png next to
this script.
"""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

CANVAS = 1024
MARGIN = 48
GUTTER = 48
COLUMN = (CANVAS - 2 * MARGIN - GUTTER) // 2

NAVY = (11, 27, 46)
GOLD = (201, 162, 39)
PAPER = (248, 243, 233)
INK = (16, 24, 40)
BODY_GREY = (91, 100, 112)
FAINT_GREY = (138, 131, 120)
DIVIDER = (196, 178, 150)

FONT_DIR = Path.home() / "workspace" / "fonts"
HERO_FILE = "media-generation-news-hero-20261119-0-bebf163a-f6e1-4d73-8980-888ce2972df7.png"

TAG_RED = (180, 35, 24)
TAG_TEAL = (14, 124, 107)
TAG_PURPLE = (105, 65, 198)
TAG_ORANGE = (181, 71, 8)
TAG_BLUE = (23, 92, 211)
TAG_SLATE = (54, 63, 114)


def _font_path(weight: str) -> str | None:
    """Return the first usable font file for the requested weight."""
    candidates = [
        FONT_DIR / f"PlusJakartaSans-{weight}.ttf",
        Path(f"/usr/share/fonts/truetype/dejavu/DejaVuSans-{weight}.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    ]
    for path in candidates:
        if path.is_file():
            return str(path)
    return None


def _load(size: int, weight: str) -> ImageFont.FreeTypeFont:
    path = _font_path(weight)
    if path is None:
        return ImageFont.load_default(size=size)
    return ImageFont.truetype(path, size)


class Typefaces:
    """All the fonts the poster needs, loaded once."""

    def __init__(self) -> None:
        self.masthead = _load(60, "Bold")
        self.dateline = _load(27, "Bold")
        self.tag = _load(22, "Bold")
        self.headline = _load(29, "Bold")
        self.body = _load(19, "Regular")
        self.credit = _load(16, "Medium")
        self.footer = _load(17, "Regular")


def wrap(draw: ImageDraw.ImageDraw, text: str, font, width: int) -> list[str]:
    """Greedy word wrap: split text into lines no wider than width."""
    lines: list[str] = []
    current = ""
    for word in text.split():
        trial = f"{current} {word}".strip()
        if draw.textlength(trial, font=font) <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def fit_hero(hero: Image.Image, width: int, height: int) -> Image.Image:
    """Centre-crop the hero to the band's aspect ratio, then resize."""
    target = width / height
    w, h = hero.size
    if w / h > target:
        new_w = int(h * target)
        left = (w - new_w) // 2
        hero = hero.crop((left, 0, left + new_w, h))
    else:
        new_h = int(w / target)
        top = (h - new_h) // 2
        hero = hero.crop((0, top, w, top + new_h))
    return hero.resize((width, height), Image.LANCZOS)


def paint_masthead(draw: ImageDraw.ImageDraw, fonts: Typefaces) -> None:
    """Navy bar with the paper name in white and the date in gold."""
    draw.rectangle([0, 0, CANVAS, 112], fill=NAVY)
    draw.text((MARGIN, 16), "THE WORLD IN ONE DAY", font=fonts.masthead, fill=(255, 255, 255))
    draw.text((MARGIN, 72), "THURSDAY \u00b7 19 NOVEMBER 2026", font=fonts.dateline, fill=GOLD)
    draw.rectangle([0, 112, CANVAS, 116], fill=GOLD)


def paint_story(
    draw: ImageDraw.ImageDraw,
    fonts: Typefaces,
    x: int,
    y: int,
    story: dict,
) -> None:
    """One story cell: coloured tag, two-line headline, body, source."""
    colour = story["colour"]
    draw.text((x, y), story["tag"], font=fonts.tag, fill=colour)
    tag_width = draw.textlength(story["tag"], font=fonts.tag)
    draw.line([(x, y + 30), (x + tag_width, y + 30)], fill=colour, width=3)

    cursor = y + 38
    for line in wrap(draw, story["headline"], fonts.headline, COLUMN)[:2]:
        draw.text((x, cursor), line, font=fonts.headline, fill=INK)
        cursor += 32

    cursor += 4
    for line in wrap(draw, story["body"], fonts.body, COLUMN)[:2]:
        draw.text((x, cursor), line, font=fonts.body, fill=BODY_GREY)
        cursor += 22

    cursor += 6
    draw.text((x, cursor), f"Source: {story['source']}", font=fonts.credit, fill=FAINT_GREY)


STORIES = [
    {
        "tag": "GULF",
        "colour": TAG_RED,
        "headline": "Iran strikes US bases in Kuwait and Bahrain",
        "body": "Drones hit Patriot systems at Ali Al Salem; Bahrain repels a fourth attack in six days.",
        "source": "Reuters / BBC",
    },
    {
        "tag": "APEC",
        "colour": TAG_TEAL,
        "headline": "Trump, Xi and Putin hold first three-way summit",
        "body": "Xi opens APEC with a $20m pledge; the trio meet for an hour on nuclear arms and Iran.",
        "source": "Reuters / BBC",
    },
    {
        "tag": "ICJ",
        "colour": TAG_PURPLE,
        "headline": "World court finds Myanmar forces killed 10,000 Rohingya",
        "body": "ICJ delivers its Rohingya genocide judgment in The Hague, finding mass killings and systematic hate speech in 2017.",
        "source": "BBC / Reuters",
    },
    {
        "tag": "BANGLADESH",
        "colour": TAG_ORANGE,
        "headline": "Yunus home torched as lockdown grips Bangladesh",
        "body": "Arson in Chattogram and blasts in Dhaka as the Awami League strike shuts down the country.",
        "source": "Reuters / TBS",
    },
    {
        "tag": "TECH",
        "colour": TAG_BLUE,
        "headline": "Anthropic's $81.3bn IPO debuts on Nasdaq",
        "body": "The Claude maker prices at $83 a share in the biggest listing ever, at about $1.5 trillion.",
        "source": "Reuters / CNBC",
    },
    {
        "tag": "CRIMEA",
        "colour": TAG_SLATE,
        "headline": "Crimean Bridge hit for third time this week",
        "body": "Traffic halted again overnight, days after a road span collapsed into the strait.",
        "source": "The Independent / BBC",
    },
]


def build_poster() -> Image.Image:
    """Compose the full poster and return it as a Pillow image."""
    fonts = Typefaces()
    sheet = Image.new("RGB", (CANVAS, CANVAS), PAPER)
    draw = ImageDraw.Draw(sheet)

    paint_masthead(draw, fonts)

    hero_path = Path(__file__).resolve().parent / "assets" / HERO_FILE
    hero = fit_hero(Image.open(hero_path).convert("RGB"), CANVAS, 292)
    sheet.paste(hero, (0, 116))
    draw.rectangle([0, 408, CANVAS, 412], fill=GOLD)

    rows = [436, 616, 796]
    for index, story in enumerate(STORIES):
        column = index % 2
        row = index // 2
        x = MARGIN + column * (COLUMN + GUTTER)
        paint_story(draw, fonts, x, rows[row], story)

    divider_x = MARGIN + COLUMN + GUTTER // 2
    draw.line([(divider_x, 440), (divider_x, 968)], fill=DIVIDER, width=1)

    draw.line([(MARGIN, 988), (CANVAS - MARGIN, 988)], fill=DIVIDER, width=1)
    footer = "Six stories that defined the day \u00b7 Headlines as reported 19 Nov 2026"
    footer_width = draw.textlength(footer, font=fonts.footer)
    draw.text(((CANVAS - footer_width) / 2, 998), footer, font=fonts.footer, fill=FAINT_GREY)

    return sheet


def main(argv: list[str]) -> int:
    out = Path(argv[1]) if len(argv) > 1 else Path(__file__).resolve().parent / "entry.png"
    poster = build_poster()
    poster.save(out, format="PNG", optimize=True)
    print(f"wrote {out} ({out.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
