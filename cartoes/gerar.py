import os

SAIDA = os.environ.get("SAIDA", "img")
L = 840
FONTE = "'Beaufort for LOL',Cinzel,Georgia,'Times New Roman',serif"
TEXTO = "'Segoe UI',Inter,Helvetica,Arial,sans-serif"


def base(altura, conteudo, extra_defs=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{L}" height="{altura}" viewBox="0 0 {L} {altura}">
<defs>
<radialGradient id="f" cx=".5" cy="0" r="1.2"><stop offset="0" stop-color="#5A1424"/><stop offset=".55" stop-color="#2A0810"/><stop offset="1" stop-color="#12040A"/></radialGradient>
<linearGradient id="o" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#5A1424"/><stop offset=".5" stop-color="#C8AA6E"/><stop offset="1" stop-color="#5A1424"/></linearGradient>
{extra_defs}
</defs>
<rect width="{L}" height="{altura}" rx="12" fill="url(#f)"/>
<rect x="6" y="6" width="{L - 12}" height="{altura - 12}" rx="8" fill="none" stroke="url(#o)" stroke-width="1.5"/>
<rect x="11" y="11" width="{L - 22}" height="{altura - 22}" rx="6" fill="none" stroke="#7D2236" stroke-opacity=".7"/>
{conteudo}
</svg>'''


def titulo(y, texto):
    return f'''<text x="{L / 2}" y="{y}" text-anchor="middle" font-family="{FONTE}" font-size="17" font-weight="700" letter-spacing="4" fill="#C8AA6E">{texto}</text>
<path d="M{L / 2 - 60} {y + 12} H{L / 2 - 8} M{L / 2 + 8} {y + 12} H{L / 2 + 60}" stroke="#785A28" stroke-width="1"/>
<path d="M{L / 2} {y + 8} l4 4 -4 4 -4 -4z" fill="#C8AA6E"/>'''


def rosa(cx, cy, esc=1.0):
    return f'''<g transform="translate({cx},{cy}) scale({esc})">
<path d="M0 7 C-1 11 1 14 0 18" stroke="#785A28" stroke-width="1.3" fill="none"/>
<path d="M0 12 C4 9 8 10 9 13 C5 15 2 14 0 12Z" fill="#785A28"/>
<path d="M0 13 C-4 10 -8 11 -9 14 C-5 16 -2 15 0 13Z" fill="#5E4520"/>
<path d="M-10 -2 C-13 -8 -9 -12 -4 -10 C-7 -5 -5 2 0 6 C-6 6 -9 3 -10 -2Z" fill="#3A0C18" stroke="#C8AA6E" stroke-width=".7"/>
<path d="M10 -2 C13 -8 9 -12 4 -10 C7 -5 5 2 0 6 C6 6 9 3 10 -2Z" fill="#3A0C18" stroke="#C8AA6E" stroke-width=".7"/>
<path d="M-7 -4 C-8 -11 -2 -13 0 -9 C2 -13 8 -11 7 -4 C6 3 -6 3 -7 -4Z" fill="#5A1424" stroke="#C8AA6E" stroke-width=".7"/>
<path d="M-4 -6 C-4 -10 0 -11 1 -8 C3 -10 5 -8 4 -5 C3 -1 -3 -1 -4 -6Z" fill="#7D2236" stroke="#C8AA6E" stroke-width=".6"/>
<path d="M-1.5 -6.5 C-1 -8.5 2 -8.5 2 -6.5 C2 -5 0 -4.5 -.5 -5.5" fill="none" stroke="#C8AA6E" stroke-width=".7"/>
</g>'''


def pilula(x, y, texto, cheia=False):
    w = len(texto) * 7.6 + 30
    fundo = "#C8AA6E" if cheia else "#3A0C18"
    cor = "#1A0D04" if cheia else "#E6CF9C"
    return (f'<rect x="{x}" y="{y}" width="{w:.0f}" height="28" rx="14" fill="{fundo}" stroke="#C8AA6E" stroke-opacity=".6"/>'
            f'<text x="{x + w / 2:.0f}" y="{y + 19}" text-anchor="middle" font-family="{TEXTO}" font-size="12.5" font-weight="600" '
            f'letter-spacing="1" fill="{cor}">{texto}</text>'), w


def linha_pilulas(y, itens):
    partes, larguras = [], []
    for texto, cheia in itens:
        _, w = pilula(0, 0, texto, cheia)
        larguras.append(w)
    total = sum(larguras) + 10 * (len(itens) - 1)
    x = (L - total) / 2
    for (texto, cheia), w in zip(itens, larguras):
        partes.append(pilula(x, y, texto, cheia)[0])
        x += w + 10
    return "".join(partes)


def topo():
    frases = ["QA ENGINEER · FOCO EM IA", "CRIADORA DO DUDA, AMEL.IA E LUMI"]
    dur = 7
    anim = ""
    for i, f in enumerate(frases):
        anim += (f'<text x="{L / 2}" y="150" text-anchor="middle" font-family="{FONTE}" font-size="16" letter-spacing="4" '
                 f'fill="#E6CF9C" opacity="0">{f}<animate attributeName="opacity" values="0;1;1;0;0" '
                 f'keyTimes="0;.08;.42;.5;1" dur="{dur}s" begin="{i * dur / 2}s" repeatCount="indefinite"/></text>')
    conteudo = f'''{rosa(L / 2, 44, 1.7)}
<text x="{L / 2}" y="118" text-anchor="middle" font-family="{FONTE}" font-size="40" font-weight="700" letter-spacing="8" fill="#C8AA6E">EDUARDA THIEL</text>
{anim}
{linha_pilulas(180, [("QA Engineer", True), ("Avaliação de LLMs", False), ("Engenharia de prompt", False)])}'''
    return base(232, conteudo)


def paragrafo(y, linhas, tamanho=15, cor="#EDE3D2", entre=24, x=None):
    out = []
    for i, t in enumerate(linhas):
        if x is None:
            out.append(f'<text x="{L / 2}" y="{y + i * entre}" text-anchor="middle" font-family="{TEXTO}" font-size="{tamanho}" fill="{cor}">{t}</text>')
        else:
            out.append(f'<text x="{x}" y="{y + i * entre}" font-family="{TEXTO}" font-size="{tamanho}" fill="{cor}">{t}</text>')
    return "".join(out)


def item(y, simbolo, texto):
    return (f'<path d="M60 {y - 5} l5 5 -5 5 -5 -5z" fill="#C8AA6E"/>'
            f'<text x="78" y="{y + 5}" font-family="{TEXTO}" font-size="15" fill="#EDE3D2">{texto}</text>')


def sobre():
    conteudo = f'''{titulo(48, "SOBRE MIM")}
{paragrafo(96, ["Sou <tspan fill='#C8AA6E' font-weight='700'>QA</tspan>: meu trabalho é garantir que o software funcione antes de chegar nas mãos das pessoas.",
                "Gosto de testar, quebrar, encontrar o bug antes do usuário e entender o porquê de cada erro."], tamanho=15)}
{item(170, "", "Testo do jeito que o usuário usa, procurando o que ninguém pensou em testar")}
{item(204, "", "Idealizei e lancei o <tspan fill='#C8AA6E' font-weight='700'>DUDA</tspan>, do zero até o app no celular das pessoas")}
{item(238, "", "Construí o DUDA usando IA como ferramenta, com as decisões, os testes e a qualidade na minha mão")}
{item(272, "", "Produto pensado pra fora também: 4 línguas e preço na moeda de cada país")}'''
    return base(312, conteudo)


def duda():
    linhas = [
        ("PLATAFORMAS", "Site + app Android com atualização automática"),
        ("MOTORES DE ESCRITA", "8 estilos diferentes, grátis e premium"),
        ("PAGAMENTOS", "Mercado Pago: Pix, cartão e cartão internacional"),
        ("IDIOMAS", "Português, inglês, espanhol e francês"),
        ("ENGAJAMENTO", "Notificações escritas pelo personagem, convites e códigos"),
        ("ADMIN", "Painel com usuários, pedidos, denúncias e métricas"),
        ("QUALIDADE", "Mais de 230 testes automáticos"),
    ]
    corpo = ""
    for i, (rotulo, texto) in enumerate(linhas):
        y = 150 + i * 36
        corpo += (f'<rect x="60" y="{y - 22}" width="{L - 120}" height="30" rx="6" fill="#3A0C18" fill-opacity="{.55 if i % 2 == 0 else .25}"/>'
                  f'<text x="80" y="{y - 2}" font-family="{FONTE}" font-size="12.5" font-weight="700" letter-spacing="2" fill="#C8AA6E">{rotulo}</text>'
                  f'<text x="290" y="{y - 2}" font-family="{TEXTO}" font-size="14.5" fill="#EDE3D2">{texto}</text>')
    conteudo = f'''{titulo(48, "PROJETO EM DESTAQUE")}
{paragrafo(92, ["<tspan fill='#C8AA6E' font-weight='700'>DUDA</tspan> é um app de histórias interativas em português, para maiores de 18 anos,",
                "com personagens que lembram de você e escrevem do jeito que você escolhe."], tamanho=14.5, entre=22)}
{corpo}'''
    return base(150 + len(linhas) * 36 + 14, conteudo)


def tecnologias():
    itens = ["Python", "Flask", "Flutter", "Dart", "PostgreSQL", "Android", "Render", "Mercado Pago", "Git"]
    conteudo = f'''{titulo(46, "COM O QUE EU TRABALHO")}
{linha_pilulas(82, [(t, False) for t in itens[:5]])}
{linha_pilulas(120, [(t, False) for t in itens[5:]])}'''
    return base(172, conteudo)


def rodape():
    conteudo = f'''{rosa(L / 2, 34, 1.1)}
<text x="{L / 2}" y="82" text-anchor="middle" font-family="{FONTE}" font-size="16" letter-spacing="3" fill="#C8AA6E">QUER CONVERSAR SOBRE UM PROJETO? ME CHAMA</text>'''
    return base(108, conteudo)


def main():
    os.makedirs(SAIDA, exist_ok=True)
    for nome, f in [("topo", topo)]:
        with open(os.path.join(SAIDA, f"{nome}.svg"), "w", encoding="utf-8") as arq:
            arq.write(f())
    print("ok")


if __name__ == "__main__":
    main()
