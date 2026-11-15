#!/usr/bin/env python3
"""Bangun aset README dari assets/src/*.svg menjadi SVG animasi yang ringan dan tajam.

Dua hal yang dilakukan:
1. Teks diubah jadi path (outline), jadi selalu tajam di layar berapa pun
   dan tampil sama di semua perangkat tanpa bergantung font terpasang.
2. Ratusan tetes hujan yang dianimasikan satu per satu digabung jadi beberapa
   layer. Gerakannya identik, tapi browser hanya menganimasikan 2 sampai 4 grup
   per gambar, bukan ratusan garis.

Syarat: rsvg-convert (librsvg) dan font Inter, Liberation Serif, DejaVu Sans Mono.
Pakai:  python3 build.py <folder src> <folder output>
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

FONT_BY_CLASS = {"s": "Liberation Serif", "m": "DejaVu Sans Mono"}
DEFAULT_FONT = "Inter"
FONT_ATTRS = {"x", "y", "font-size", "font-weight", "font-style", "text-anchor",
              "letter-spacing", "fill", "fill-opacity", "class", "style", "opacity", "transform"}


def r(v, nd=2):
    s = f"{float(v):.{nd}f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


def round_numbers(s):
    # rapikan angka berekor panjang seperti -1.7999999999999998s
    return re.sub(r"-?\d+\.\d{3,}", lambda m: r(m.group(0)), s)


def compact_path(d):
    """Presisi 0.05px sudah cukup tajam, lalu ringkas perintah path."""
    d = re.sub(r"-?\d+\.\d+", lambda m: r(m.group(0), 1), d)
    d = re.sub(r"\s*([MLCZ])\s*", r"\1", d)
    return re.sub(r"\s+", " ", d).strip()


# ---------------------------------------------------------------- hujan
LINE_RE = re.compile(r'<line class="rn"([^>]*?)/>')
RUN_RE = re.compile(r'(?:<line class="rn"[^>]*?/>)+')


def attr(s, name):
    m = re.search(r'(?<![\w-])' + re.escape(name) + r'="([^"]*)"', s)
    return m.group(1) if m else None


def build_rain(svg):
    """Ganti tiap deretan <line class="rn"> dengan layer beranimasi."""
    keyframes = {}
    counter = [0]

    def convert(run_match):
        run = run_match.group(0)
        layers = {}  # (T, h) -> list of line markup
        for m in LINE_RE.finditer(run):
            a = m.group(1)
            style = attr(a, "style")
            h = float(re.search(r"--h:([\d.]+)px", style).group(1))
            T = float(re.search(r"animation:fall ([\d.]+)s", style).group(1))
            d = float(re.search(r"animation-delay:(-?[\d.]+)s", style).group(1))
            D = h + 90
            elapsed = (-d) % T if d <= 0 else 0
            phi = elapsed / T
            x1, y1, x2, y2 = (float(attr(a, k)) for k in ("x1", "y1", "x2", "y2"))
            dx, dy = -26 * phi, -90 + D * phi
            keep = " ".join(f'{k}="{attr(a, k)}"' for k in
                            ("stroke", "stroke-opacity", "stroke-width", "stroke-linecap") if attr(a, k))
            keep = keep.replace(' stroke-linecap="round"', "")
            line = (f'<line x1="{r(x1 + dx)}" y1="{r(y1 + dy)}" '
                    f'x2="{r(x2 + dx)}" y2="{r(y2 + dy)}" {keep}/>')
            layers.setdefault((T, D), []).append(line)
        out = []
        for (T, D), lines in layers.items():
            counter[0] += 1
            n = counter[0]
            kf = f"fl{int(D)}"
            keyframes[kf] = (f"@keyframes {kf}{{from{{transform:translate(0,0)}}"
                             f"to{{transform:translate(-26px,{r(D)}px)}}}}")
            out.append(
                f'<g class="rl" style="animation:{kf} {r(T)}s linear infinite">'
                f'<g id="rd{n}" stroke-linecap="round">{"".join(lines)}</g>'
                f'<use href="#rd{n}" transform="translate(26 {r(-D)})"/></g>')
        return "".join(out)

    svg = RUN_RE.sub(convert, svg)
    if keyframes:
        svg = svg.replace("</style>", "".join(keyframes.values()) + "</style>", 1)
    # buang keyframes lama yang bergantung var(--h), sudah tidak dipakai
    svg = re.sub(r"@keyframes fall\{.*?\}\}", "", svg, count=1)
    return svg


# ---------------------------------------------------------------- teks
def hex_from_rgb(s):
    m = re.match(r"rgb\(([\d.]+)%,\s*([\d.]+)%,\s*([\d.]+)%\)", s)
    if not m:
        return s
    return "#%02X%02X%02X" % tuple(round(float(g) * 2.55) for g in m.groups())


def outline_text(svg, workdir):
    root = re.search(r"<svg[^>]*>", svg).group(0)
    vb = attr(root, "viewBox")
    w, h = attr(root, "width"), attr(root, "height")
    text_re = re.compile(r"<text([^>]*)>(.*?)</text>", re.S)

    def convert(m):
        attrs, inner = m.group(1), m.group(2)
        classes = (attr(attrs, "class") or "").split()
        font = next((FONT_BY_CLASS[c] for c in classes if c in FONT_BY_CLASS), DEFAULT_FONT)
        render_attrs = " ".join(f'{k}="{attr(attrs, k)}"' for k in
                                ("x", "y", "font-size", "font-weight", "font-style",
                                 "text-anchor", "letter-spacing", "fill") if attr(attrs, k))
        doc = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{w}" height="{h}">'
               f'<text font-family="{font}" {render_attrs}>{inner}</text></svg>')
        src = workdir / "t.svg"
        src.write_text(doc)
        res = subprocess.run(["rsvg-convert", "-f", "svg", str(src)],
                             capture_output=True, text=True, check=True).stdout
        paths = re.findall(r"<path ([^>]*?)/>", res)
        if not paths:
            return ""
        parts = []
        for p in paths:
            d = compact_path(attr(p, "d"))
            fill = hex_from_rgb(attr(p, "fill"))
            fo = attr(p, "fill-opacity")
            extra = f' fill-opacity="{r(fo)}"' if fo and float(fo) != 1 else ""
            parts.append(f'<path fill="{fill}"{extra} d="{d}"/>')
        keep_classes = [c for c in classes if c not in FONT_BY_CLASS]
        wrap = []
        if keep_classes:
            wrap.append(f'class="{" ".join(keep_classes)}"')
        for k in ("style", "opacity", "transform"):
            if attr(attrs, k):
                wrap.append(f'{k}="{attr(attrs, k)}"')
        if wrap:
            return f'<g {" ".join(wrap)}>{"".join(parts)}</g>'
        return "".join(parts)

    return text_re.sub(convert, svg)


def clean_style(svg):
    # aturan font tidak diperlukan lagi setelah teks jadi path
    svg = re.sub(r"\ntext\{font-family:[^\n]*\n", "\n", svg)
    svg = re.sub(r"\n\.s\{font-family:[^\n]*\n", "\n", svg)
    svg = re.sub(r"\n\.m\{font-family:[^\n]*\n", "\n", svg)
    # keyframes bawaan yang tidak dipakai file ini
    for name in ("glow", "nudge"):
        used = re.search(r"animation:\s*" + name + r"\b", svg.split("</style>", 1)[1]) or \
               re.search(r"\.[\w-]+\{[^}]*animation:" + name + r"\b", svg)
        if not used:
            svg = re.sub(r"@keyframes " + name + r"\{.*?\}\}\n?", "", svg, count=1)
    return svg


def main(src_dir, out_dir):
    src_dir, out_dir = Path(src_dir), Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        for f in sorted(src_dir.glob("*.svg")):
            svg = f.read_text()
            svg = build_rain(svg)
            svg = outline_text(svg, Path(tmp))
            svg = clean_style(svg)
            svg = round_numbers(svg)
            (out_dir / f.name).write_text(svg)
            print(f"{f.name:28s} {f.stat().st_size:>7} -> {len(svg.encode()):>7} bytes")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
