#!/usr/bin/env python3
"""Compose the 19 November 2026 world-news poster (1024x1024).

Own work: headlines researched from Reuters / BBC / Al Jazeera / The
Independent / TBS briefings of 19 Nov 2026; hero illustration generated
for this entry; layout and typography composed here with PIL. No copied
news photos.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = "/home/hatch/workspace/fonts"
HERO = os.path.join(
    HERE, "assets",
    "media-generation-news-hero-20261119-0-bebf163a-f6e1-4d73-8980-888ce2972df7.png",
)

W, H = 1024, 1024
NAVY = (13, 27, 46)
NAVY2 = (18, 38, 62)
GOLD = (212, 160, 60)
PAPER = (247, 243, 234)
INK = (18, 24, 33)
MUTED = (90, 96, 104)
RULE = (200, 192, 172)
WHITE = (255, 255, 255)

TAG_COLORS = {
    "GULF": (168, 42, 42),
    "APEC": (24, 96, 74),
    "ICJ": (110, 60, 130),
    "BANGLADESH": (150, 60, 20),
    "TECH": (30, 90, 140),
    "CRIMEA": (58, 74, 140),
}


def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)


F_MAST = font("PlusJakartaSans-Bold.ttf", 58)
F_DATE = font("PlusJakartaSans-SemiBold.ttf", 30)
F_TAG = font("PlusJakartaSans-Bold.ttf", 21)
F_HEAD = font("PlusJakartaSans-Bold.ttf", 27)
F_BODY = font("PlusJakartaSans-Regular.ttf", 19)
F_FOOT = font("PlusJakartaSans-Regular.ttf", 17)

STORIES = [
    ("GULF", "Iran strikes US bases in\nKuwait and Bahrain",
     "Drones hit Patriot systems at Ali Al Salem; Bahrain repels a "
     "fourth attack in six days.",
     "Reuters / BBC"),
    ("APEC", "Trump, Xi and Putin hold\nfirst three-way summit",
     "Xi opens APEC with a $20m pledge; the trio meet for an hour on "
     "nuclear arms and Iran.",
     "Reuters / BBC"),
    ("ICJ", "World court rules on\nRohingya genocide",
     "The Hague delivers its verdict in Gambia v. Myanmar; a first-ever "
     "state finding is possible.",
     "Al Jazeera / Reuters"),
    ("BANGLADESH", "Yunus home torched as\nlockdown grips Bangladesh",
     "Arson in Chattogram and blasts in Dhaka as the Awami League strike "
     "shuts down the country.",
     "Reuters / TBS"),
    ("TECH", "Anthropic's $81.3bn IPO\ndebuts on Nasdaq",
     "The Claude maker prices at $83 a share in the biggest listing ever, "
     "at about $1.5 trillion.",
     "Reuters / CNBC"),
    ("CRIMEA", "Crimean Bridge hit for\nthird time this week",
     "Traffic halted again overnight, days after a road span collapsed "
     "into the strait.",
     "The Independent / BBC"),
]


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- masthead ---
    d.rectangle([0, 0, W, 118], fill=NAVY)
    d.rectangle([0, 118, W, 122], fill=GOLD)
    d.text((48, 22), "THE WORLD IN ONE DAY", font=F_MAST, fill=WHITE)
    d.text((48, 84), "THURSDAY  \u00b7  19 NOVEMBER 2026", font=F_DATE, fill=GOLD)

    # --- hero illustration ---
    hero = Image.open(HERO).convert("RGB")
    # cover-crop to 1024x300
    tw, th = 1024, 300
    scale = max(tw / hero.width, th / hero.height)
    hero = hero.resize((int(hero.width * scale) + 1, int(hero.height * scale) + 1),
                       Image.LANCZOS)
    x0 = (hero.width - tw) // 2
    y0 = (hero.height - th) // 2
    hero = hero.crop((x0, y0, x0 + tw, y0 + th))
    img.paste(hero, (0, 122))
    d.rectangle([0, 422, W, 426], fill=GOLD)

    # --- story grid: 2 cols x 3 rows ---
    gx, gy = 48, 448
    cw, ch = 448, 168
    gapx, gapy = 32, 10
    for i, (tag, head, body, src) in enumerate(STORIES):
        col, row = i % 2, i // 2
        x = gx + col * (cw + gapx)
        y = gy + row * (ch + gapy)
        color = TAG_COLORS[tag]
        d.text((x, y), tag, font=F_TAG, fill=color)
        d.line([(x, y + 30), (x + 64, y + 30)], fill=color, width=3)
        yy = y + 42
        for line in head.split("\n"):
            d.text((x, yy), line, font=F_HEAD, fill=INK)
            yy += 32
        for line in wrap(d, body, F_BODY, cw):
            d.text((x, yy), line, font=F_BODY, fill=MUTED)
            yy += 24
        d.text((x, yy + 2), "Source: " + src, font=F_FOOT, fill=(140, 130, 110))
        if col == 0:
            d.line([(x + cw + 16, y + 4), (x + cw + 16, y + ch - 8)], fill=RULE, width=1)

    # --- footer ---
    d.line([(48, 994), (976, 994)], fill=RULE, width=1)
    d.text((48, 1001), "Six stories that defined the day  \u00b7  Headlines as reported 19 Nov 2026",
           font=F_FOOT, fill=MUTED)

    out = os.path.join(HERE, "entry.png")
    img.save(out, "PNG", optimize=True)
    return out


if __name__ == "__main__":
    path = build()
    im = Image.open(path)
    print(path, im.size, os.path.getsize(path), "bytes")
