import os

SAIDA = os.path.join(os.path.dirname(__file__), "..", "img")
FONTE = "'Cinzel','Trajan Pro','Georgia',serif"
TEXTO = "'Segoe UI','Helvetica Neue',Arial,sans-serif"
NUMEROS = [("4", "projetos"), ("170+", "testes automatizados"), ("5", "provedores de IA"), ("4", "idiomas no DUDA")]


def faixa():
    L, A = 900, 120
    w = (L - 40 - 3 * 16) / 4
    caixas = []
    for i, (n, rotulo) in enumerate(NUMEROS):
        x = 20 + i * (w + 16)
        caixas.append(
            f'<rect x="{x:.0f}" y="18" width="{w:.0f}" height="84" rx="10" fill="#3A0C18" stroke="#C8AA6E" stroke-opacity=".55"/>'
            f'<text x="{x + w / 2:.0f}" y="62" text-anchor="middle" font-family="{FONTE}" font-size="34" font-weight="700" fill="#C8AA6E">{n}'
            '</text>'
            f'<text x="{x + w / 2:.0f}" y="88" text-anchor="middle" font-family="{TEXTO}" font-size="13.5" fill="#EDE3D2">{rotulo}</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{L}" height="{A}" viewBox="0 0 {L} {A}">
<defs><linearGradient id="f" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2A0810"/><stop offset=".5" stop-color="#3A0C18"/><stop offset="1" stop-color="#2A0810"/></linearGradient></defs>
<rect width="{L}" height="{A}" rx="12" fill="url(#f)"/>
{"".join(caixas)}
</svg>'''


def main():
    os.makedirs(SAIDA, exist_ok=True)
    with open(os.path.join(SAIDA, "numeros.svg"), "w", encoding="utf-8") as arq:
        arq.write(faixa())
    print("ok")


if __name__ == "__main__":
    main()
