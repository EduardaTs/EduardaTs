import os

SAIDA = os.path.join(os.path.dirname(__file__), "..", "img")
L, A = 900, 150
DUR = 9.0
INICIO, FIM = -80, L + 80
CHAO = 104


def poro():
    pelos = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#F4EFE8"/>' for x, y, r in [
        (-26, 4, 13), (26, 4, 13), (-18, -18, 14), (18, -18, 14), (0, -26, 15), (-22, 18, 11), (22, 18, 11), (0, 22, 14)])
    return f'''<g>
<ellipse cx="0" cy="34" rx="30" ry="5" fill="#000" opacity=".35"/>
<path d="M-14 -30 C-24 -46 -12 -52 -8 -40Z M14 -30 C24 -46 12 -52 8 -40Z" fill="#C8AA6E" stroke="#785A28" stroke-width="1.2"/>
{pelos}
<circle cx="0" cy="0" r="27" fill="#FFFFFF"/>
<ellipse cx="-11" cy="-6" rx="6.5" ry="8" fill="#2A0A12"/><ellipse cx="11" cy="-6" rx="6.5" ry="8" fill="#2A0A12"/>
<circle cx="-13" cy="-9" r="2.4" fill="#fff"/><circle cx="9" cy="-9" r="2.4" fill="#fff"/>
<ellipse cx="-19" cy="5" rx="5" ry="3" fill="#E85A8E" opacity=".45"/><ellipse cx="19" cy="5" rx="5" ry="3" fill="#E85A8E" opacity=".45"/>
<ellipse cx="0" cy="9" rx="7" ry="4" fill="#5A1424">
<animate attributeName="ry" values="4;9;4" dur=".45s" repeatCount="indefinite"/></ellipse>
<path d="M-4 11 Q0 22 5 12 Z" fill="#E85A8E"><animateTransform attributeName="transform" type="translate" values="0 0;0 3;0 0" dur=".45s" repeatCount="indefinite"/></path>
<circle cx="-12" cy="30" r="5" fill="#F4EFE8"><animate attributeName="cy" values="30;26;30" dur=".3s" repeatCount="indefinite"/></circle>
<circle cx="12" cy="30" r="5" fill="#F4EFE8"><animate attributeName="cy" values="26;30;26" dur=".3s" repeatCount="indefinite"/></circle>
</g>'''


def moeda(x, grande):
    t = (x - INICIO) / (FIM - INICIO)
    t1, t2 = max(0.0001, t - 0.004), min(0.9999, t + 0.004)
    r = 9 if grande else 5
    forma = (f'<path d="M{x} {CHAO - 14} l6 9 -6 9 -6 -9z" fill="#E85A8E" stroke="#C8AA6E" stroke-width="1.2"/>' if grande
             else f'<circle cx="{x}" cy="{CHAO - 5}" r="{r}" fill="#C8AA6E" stroke="#F0DCA8" stroke-width="1"/>')
    some = (f'<animate attributeName="opacity" values="1;1;0;0;1" keyTimes="0;{t1:.4f};{t2:.4f};.985;1" '
            f'dur="{DUR}s" repeatCount="indefinite"/>')
    pontos = (f'<text x="{x}" y="{CHAO - 30}" text-anchor="middle" font-family="Segoe UI,Arial" font-size="13" font-weight="700" '
              f'fill="{"#E85A8E" if grande else "#E6CF9C"}" opacity="0">+{50 if grande else 10}'
              f'<animate attributeName="opacity" values="0;0;1;0;0" keyTimes="0;{t1:.4f};{t2:.4f};{min(.98, t + .06):.4f};1" dur="{DUR}s" repeatCount="indefinite"/>'
              f'<animate attributeName="y" values="{CHAO - 20};{CHAO - 20};{CHAO - 22};{CHAO - 42};{CHAO - 42}" keyTimes="0;{t1:.4f};{t2:.4f};{min(.98, t + .06):.4f};1" dur="{DUR}s" repeatCount="indefinite"/></text>')
    return f'<g>{forma}{some}</g>{pontos}'


def cena():
    moedas = "".join(moeda(x, i % 6 == 3) for i, x in enumerate(range(60, L - 40, 44)))
    estrelas = "".join(f'<circle cx="{x}" cy="{y}" r="1.3" fill="#E6CF9C" opacity=".6"><animate attributeName="opacity" values=".1;.8;.1" dur="{2 + i % 3}s" repeatCount="indefinite"/></circle>'
                       for i, (x, y) in enumerate([(40, 26), (130, 50), (250, 20), (380, 44), (520, 22), (640, 52), (760, 28), (860, 46)]))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{L}" height="{A}" viewBox="0 0 {L} {A}">
<defs>
<linearGradient id="f" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2A0810"/><stop offset="1" stop-color="#12040A"/></linearGradient>
<linearGradient id="o" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#5A1424"/><stop offset=".5" stop-color="#C8AA6E"/><stop offset="1" stop-color="#5A1424"/></linearGradient>
<clipPath id="c"><rect width="{L}" height="{A}" rx="12"/></clipPath>
</defs>
<g clip-path="url(#c)">
<rect width="{L}" height="{A}" fill="url(#f)"/>
{estrelas}
<path d="M0 {CHAO + 12} H{L}" stroke="#5A1424" stroke-width="2"/>
{moedas}
<g><animateTransform attributeName="transform" type="translate" values="{INICIO} {CHAO - 22};{FIM} {CHAO - 22}" dur="{DUR}s" repeatCount="indefinite"/>
<g><animateTransform attributeName="transform" type="translate" values="0 0;0 -6;0 0" dur=".3s" repeatCount="indefinite"/>{poro()}</g></g>
</g>
<rect x="1" y="1" width="{L - 2}" height="{A - 2}" rx="12" fill="none" stroke="url(#o)" stroke-width="1.5"/>
</svg>'''


def main():
    os.makedirs(SAIDA, exist_ok=True)
    with open(os.path.join(SAIDA, "poro.svg"), "w", encoding="utf-8") as arq:
        arq.write(cena())
    print("ok")


if __name__ == "__main__":
    main()
