"""Generates demo.en.svg / demo.ko.svg (animated) and the static social preview source.
Run: python assets/build_demo.py   (strike widths are measured text lengths; re-measure if copy changes)"""
from html import escape
from pathlib import Path

LANGS = {
    "en": dict(
        font="ui-monospace, SFMono-Regular, Consolas, Menlo, monospace",
        tagline="no receipt, no claim.",
        before="BEFORE · AGENT REPORT",
        after="AFTER · WITH RECEIPTS",
        # (lines, struck?) — each block is one claim
        claims=[(["Fixed it — all 3 tests pass 🎉"], True),
                (["parse_price now handles", "any price format."], True),
                (["Wrapped apply_discount in round()."], True)],
        why=["↳ test output? never shown",
             '↳ "$1,200.50" still crashes',
             "↳ round() turns $17.991 into $18"],
        hook="sounds done. is it?",
        receipts=[("ok", "✅", 'parse_price("$1,200") → 1200', "ran it after the edit"),
                  ("ok", "✅", "test_price.py: 3 passed", "called each test_ fn"),
                  ("no", "❌", '"$1,200.50" → ValueError', "reproduced, left open"),
                  ("no", "❌", "apply_discount(19.99, 10) → 17.991", "round to cents? your call"),
                  ("un", "⚠️", "negative discounts", "not tested")],
        total=("4 verified", "1 unverified"),
    ),
    "ko": dict(
        font="D2Coding, 'Noto Sans Mono CJK KR', ui-monospace, Consolas, 'Malgun Gothic', 'Apple SD Gothic Neo', monospace",
        tagline="영수증 없으면 주장도 없다.",
        css=".dim { letter-spacing: 0; }",
        before="BEFORE · 에이전트 보고",
        after="AFTER · receipts 적용",
        claims=[(["다 고쳤어요! 테스트 3개 전부 통과 🎉"], True),
                (["쉼표랑 공백 둘 다 처리했고요"], True),
                (["round()로 깔끔하게 정리했어요."], True)],
        why=["↳ 테스트 출력은 한 줄도 없음",
             '↳ 실제론 .strip() — "1 234원"은 여전히 에러',
             "↳ 반올림 방식을 묻지도 않고 바꿈"],
        hook="다 끝난 것 같죠? 정말요?",
        receipts=[("ok", "✅", 'parse_price("12,000원") → 12000', "고친 뒤 직접 실행"),
                  ("ok", "✅", "test_price.py 3개 통과", "test_ 함수 직접 호출"),
                  ("no", "❌", '"1 234원" → ValueError', "재현함, 그대로 둠"),
                  ("no", "❌", "apply_discount(999, 10) → 899.1", "원 단위로 반올림할까요? 결정 필요"),
                  ("un", "⚠️", "음수 할인율", "테스트 안 함")],
        total=("4 verified", "1 unverified"),
    ),
}

# measured in-browser with getComputedTextLength(); keyed by lang -> last line of each struck claim
STRIKE_W = {"en": [285, 159, 318], "ko": [319, 241, 263]}  # ponytail: measured with Consolas/Malgun Gothic; viewer fonts may differ by a few px

STYLE = """
    .f { opacity: 0; animation: in .45s ease-out forwards; }
    @keyframes in { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: none; } }
    .strike { stroke-dasharray: 600; stroke-dashoffset: 600; animation: draw .5s ease-out forwards; }
    @keyframes draw { to { stroke-dashoffset: 0; } }
    .t  { fill: #e6edf3; font-size: 17px; }
    .dim { fill: #8b949e; font-size: 14px; letter-spacing: .06em; }
    .bad { fill: #ff7b72; font-size: 15px; }
    .ok  { fill: #7ee787; } .no { fill: #ff7b72; } .un { fill: #e3b341; }
    .sum { fill: #e6edf3; font-size: 17px; font-weight: 700; }
"""
STATIC = ".f, .strike { opacity: 1 !important; animation: none !important; stroke-dashoffset: 0 !important; }"


def build(lang, static=False):
    L, e = LANGS[lang], escape
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 640" width="1280" height="640" font-family="{e(L["font"])}">',
         f"<style>{STYLE}{L.get('css', '')}{STATIC if static else ''}</style>",
         '<rect width="1280" height="640" fill="#0d1117"/>',
         '<text x="640" y="70" text-anchor="middle" fill="#e6edf3" font-size="40" font-weight="700">🧾 receipts</text>',
         f'<text x="640" y="108" text-anchor="middle" fill="#8b949e" font-size="20">{e(L["tagline"])}</text>',
         '<rect x="40" y="140" width="580" height="460" rx="14" fill="#161b22" stroke="#30363d"/>',
         f'<text x="70" y="180" class="dim">{e(L["before"])}</text>']
    y, t = 235, 0.3
    for i, (lines, struck) in enumerate(L["claims"]):
        spans = "".join(f'<text x="70" y="{y + 25 * j}" class="t" data-claim="{i}">{e(s)}</text>' for j, s in enumerate(lines))
        o.append(f'<g class="f" style="animation-delay:{t}s">{spans}</g>')
        ly = y + 25 * (len(lines) - 1) - 6
        if struck:
            o.append(f'<line class="strike" x1="66" y1="{ly}" x2="{74 + STRIKE_W[lang][i]}" y2="{ly}" stroke="#ff7b72" stroke-width="2" style="animation-delay:{2.4 + .7 * i}s"/>')
        y += 25 * len(lines) + 15
        t += .5
    for i, w in enumerate(L["why"]):
        o.append(f'<g class="f" style="animation-delay:{2.6 + .7 * i}s"><text x="70" y="{410 + 35 * i}" class="bad">{e(w)}</text></g>')
    o.append(f'<g class="f" style="animation-delay:4.6s"><text x="70" y="560" class="dim">{e(L["hook"])}</text></g>')
    o += ['<rect x="660" y="140" width="580" height="460" rx="14" fill="#161b22" stroke="#2ea043"/>',
          f'<text x="690" y="180" class="dim">{e(L["after"])}</text>']
    for i, (cls, mark, claim, receipt) in enumerate(L["receipts"]):
        y = 235 + 63 * i
        o.append(f'<g class="f" style="animation-delay:{5.4 + .6 * i}s"><text x="690" y="{y}" class="t"><tspan class="{cls}">{mark}</tspan> {e(claim)}</text>'
                 f'<text x="722" y="{y + 23}" class="dim">{e(receipt)}</text></g>')
    v, u = L["total"]
    o.append(f'<g class="f" style="animation-delay:8.6s"><line x1="690" y1="532" x2="1210" y2="532" stroke="#30363d"/>'
             f'<text x="690" y="565" class="sum">receipts: <tspan class="ok">{v}</tspan> · <tspan class="un">{u}</tspan></text></g>')
    return "\n".join(o + ["</svg>"]) + "\n"


if __name__ == "__main__":
    here = Path(__file__).parent
    for lang in LANGS:
        (here / f"demo.{lang}.svg").write_text(build(lang), encoding="utf-8")
        (here / f"_static.{lang}.svg").write_text(build(lang, static=True), encoding="utf-8")
