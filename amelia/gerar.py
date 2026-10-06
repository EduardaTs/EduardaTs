import os

SAIDA = os.path.join(os.path.dirname(__file__), "..", "img")
FONTE = "'Cinzel','Trajan Pro','Georgia',serif"
TEXTO = "'Segoe UI','Helvetica Neue',Arial,sans-serif"
ROSA = "#E85A8E"


def rosto(cx, cy, s):
    return f'''<g transform="translate({cx} {cy}) scale({s})">
<circle r="96" fill="#3A0C18" stroke="#C8AA6E" stroke-width="3"/>
<circle r="88" fill="none" stroke="{ROSA}" stroke-opacity=".35" stroke-width="2"/>
<path d="M-58 22 C-66 -38 -40 -70 0 -70 C40 -70 66 -38 58 22 C62 46 52 64 40 72 L-40 72 C-52 64 -62 46 -58 22Z" fill="#2A0A12"/>
<ellipse cx="0" cy="10" rx="46" ry="52" fill="#F6D7C3"/>
<path d="M-50 -6 C-46 -52 -14 -60 6 -56 C30 -54 48 -38 50 -8 C38 -24 24 -30 10 -30 C14 -22 12 -16 6 -12 C2 -26 -12 -32 -26 -28 C-34 -24 -44 -16 -50 -6Z" fill="#3B0F1C"/>
<path d="M-22 -50 C-12 -56 6 -58 18 -52" stroke="#5A1424" stroke-width="3" fill="none" stroke-linecap="round"/>
<g fill="#2A0A12">
<ellipse cx="-18" cy="10" rx="9.5" ry="12"/><ellipse cx="18" cy="10" rx="9.5" ry="12"/>
</g>
<g fill="{ROSA}" fill-opacity=".9"><ellipse cx="-18" cy="13" rx="6" ry="7.5"/><ellipse cx="18" cy="13" rx="6" ry="7.5"/></g>
<g fill="#FFFFFF"><circle cx="-21" cy="6" r="3.6"/><circle cx="15" cy="6" r="3.6"/><circle cx="-15" cy="16" r="1.6"/><circle cx="21" cy="16" r="1.6"/></g>
<path d="M-29 -4 C-24 -9 -14 -9 -9 -5 M9 -5 C14 -9 24 -9 29 -4" stroke="#2A0A12" stroke-width="2.4" fill="none" stroke-linecap="round"/>
<ellipse cx="-30" cy="30" rx="9" ry="5" fill="{ROSA}" fill-opacity=".35"/><ellipse cx="30" cy="30" rx="9" ry="5" fill="{ROSA}" fill-opacity=".35"/>
<path d="M-9 36 C-4 42 4 42 9 36" stroke="#7D2236" stroke-width="2.6" fill="none" stroke-linecap="round"/>
<path d="M-52 4 C-56 -46 -24 -74 0 -74 C24 -74 56 -46 52 4" stroke="#C8AA6E" stroke-width="5" fill="none" stroke-linecap="round"/>
<rect x="-62" y="-4" width="16" height="30" rx="7" fill="#5A1424" stroke="#C8AA6E" stroke-width="2"/>
<rect x="46" y="-4" width="16" height="30" rx="7" fill="#5A1424" stroke="#C8AA6E" stroke-width="2"/>
<path d="M-54 24 C-54 48 -36 56 -18 54" stroke="#C8AA6E" stroke-width="3" fill="none" stroke-linecap="round"/>
<circle cx="-15" cy="54" r="5" fill="{ROSA}" stroke="#C8AA6E" stroke-width="1.5"/>
<path d="M-6 -62 l5 -9 5 9 -5 -3z" fill="#C8AA6E"/>
</g>'''


def ondas(x, y, cor=ROSA):
    alturas = [8, 16, 26, 14, 30, 18, 10, 22, 12, 6]
    partes = []
    for i, h in enumerate(alturas):
        partes.append(f'<rect x="{x + i * 9}" y="{y - h / 2}" width="5" height="{h}" rx="2.5" fill="{cor}" opacity=".85">'
                      f'<animate attributeName="height" values="{h};{max(4, h * .4):.0f};{h}" dur="{1 + (i % 3) * .3:.1f}s" repeatCount="indefinite"/>'
                      f'<animate attributeName="y" values="{y - h / 2};{y - max(4, h * .4) / 2:.0f};{y - h / 2}" dur="{1 + (i % 3) * .3:.1f}s" repeatCount="indefinite"/></rect>')
    return "".join(partes)


def balao(x, y, w, texto, dela):
    cor, borda, txt = ("#3A0C18", "#C8AA6E", "#EDE3D2") if dela else ("#5A1424", ROSA, "#FFFFFF")
    rotulo = "AMÉLIA" if dela else "EDUARDA"
    return (f'<rect x="{x}" y="{y}" width="{w}" height="46" rx="14" fill="{cor}" stroke="{borda}" stroke-opacity=".7"/>'
            f'<text x="{x + 16}" y="{y + 17}" font-family="{FONTE}" font-size="10" letter-spacing="2" fill="{borda}">{rotulo}</text>'
            f'<text x="{x + 16}" y="{y + 35}" font-family="{TEXTO}" font-size="14" fill="{txt}">{texto}</text>')


def avatar():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="220" height="220" viewBox="0 0 220 220">
<defs><radialGradient id="f" cx=".5" cy=".35" r=".8"><stop offset="0" stop-color="#5A1424"/><stop offset="1" stop-color="#12040A"/></radialGradient></defs>
<rect width="220" height="220" rx="40" fill="url(#f)"/>
{rosto(110, 108, 0.95)}
</svg>'''


def banner():
    L, A = 900, 352
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{L}" height="{A}" viewBox="0 0 {L} {A}">
<defs>
<radialGradient id="f" cx=".2" cy=".3" r="1.2"><stop offset="0" stop-color="#5A1424"/><stop offset=".55" stop-color="#2A0810"/><stop offset="1" stop-color="#12040A"/></radialGradient>
<linearGradient id="o" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#5A1424"/><stop offset=".5" stop-color="#C8AA6E"/><stop offset="1" stop-color="#5A1424"/></linearGradient>
</defs>
<rect width="{L}" height="{A}" rx="12" fill="url(#f)"/>
<rect x="6" y="6" width="{L - 12}" height="{A - 12}" rx="8" fill="none" stroke="url(#o)" stroke-width="1.5"/>
{rosto(150, 150, 1.05)}
{ondas(105, 290)}
<text x="300" y="72" font-family="{FONTE}" font-size="38" font-weight="700" letter-spacing="6" fill="#C8AA6E">AMÉLIA</text>
<text x="302" y="100" font-family="{TEXTO}" font-size="15" fill="#E6CF9C">Agente de IA por voz para o computador</text>
{balao(300, 122, 420, "Mel, meu top sabe jogar com esse boneco?", False)}
{balao(330, 178, 470, "Sabe sim! 104 partidas de Irelia e 49% de vitória.", True)}
{balao(300, 234, 360, "Bota Make You Mine no Spotify.", False)}
{balao(330, 290 - 2, 300, "Prontinho, tocando agora.", True)}
</svg>'''


def main():
    os.makedirs(SAIDA, exist_ok=True)
    for nome, f in [("amelia-rosto", avatar), ("amelia-banner", banner)]:
        with open(os.path.join(SAIDA, f"{nome}.svg"), "w", encoding="utf-8") as arq:
            arq.write(f())
    print("ok")


if __name__ == "__main__":
    main()
