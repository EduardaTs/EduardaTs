import os
import random
import re
import sys
import urllib.request
from datetime import datetime, timezone

USUARIO = os.environ.get("USUARIO", "EduardaTs")
ANO = int(os.environ.get("ANO", datetime.now(timezone.utc).year))
SAIDA = os.environ.get("SAIDA", "dist")

CORES = ["#1A0A0E", "#4A1020", "#7D2236", "#D8425C", "#C8AA6E"]
BRILHO = ["#3A1A22", "#FF6FA8", "#FF6FA8", "#FFC2DA", "#FFF1C9"]
PASSO = 14
TAM = 8.5
X0, Y0 = 46, 100
DURACAO = 9


def baixar():
    req = urllib.request.Request(f"https://github.com/users/{USUARIO}/contributions?from={ANO}-01-01&to={ANO}-12-31",
                                 headers={"User-Agent": "Mozilla/5.0"})
    html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8")
    dias = {}
    for tag in re.findall(r"<td[^>]*ContributionCalendar-day[^>]*>", html):
        pos = re.search(r"contribution-day-component-(\d+)-(\d+)", tag)
        nivel = re.search(r'data-level="(\d)"', tag)
        if pos and nivel:
            dias[(int(pos.group(2)), int(pos.group(1)))] = int(nivel.group(1))
    total = re.search(r"([\d,.]+)\s+contributions?", html)
    return dias, (total.group(1) if total else "0")


def losango(cx, cy, r):
    return f"M{cx:.1f} {cy - r:.1f}L{cx + r:.1f} {cy:.1f}L{cx:.1f} {cy + r:.1f}L{cx - r:.1f} {cy:.1f}Z"


def petala(i, largura, altura):
    rnd = random.Random(i * 97 + 13)
    x = rnd.uniform(30, largura - 30)
    deriva = rnd.uniform(-60, 60)
    dur = rnd.uniform(9, 15)
    atraso = rnd.uniform(0, 9)
    esc = rnd.uniform(0.9, 1.5)
    cor = rnd.choice(["#7D2236", "#D8425C", "#5A1424"])
    return f'''<g opacity="0">
<path d="M0 0 C4 -6 10 -4 8 3 C6 8 1 7 0 0Z" fill="{cor}" transform="scale({esc:.2f})"/>
<animateMotion path="M{x:.0f} -12 C{x + deriva:.0f} {altura * 0.35:.0f} {x - deriva:.0f} {altura * 0.7:.0f} {x + deriva / 2:.0f} {altura + 12:.0f}" dur="{dur:.1f}s" begin="{atraso:.1f}s" repeatCount="indefinite" rotate="auto"/>
<animate attributeName="opacity" values="0;.85;.85;0" keyTimes="0;.1;.85;1" dur="{dur:.1f}s" begin="{atraso:.1f}s" repeatCount="indefinite"/>
</g>'''


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


def svg(dias, total):
    colunas = (max(c for c, _ in dias) + 1) if dias else 53
    largura = X0 * 2 + colunas * PASSO
    altura = Y0 + 7 * PASSO + 58
    fim_x = X0 + colunas * PASSO
    meio_y = Y0 + 3.5 * PASSO
    celulas = []
    for (col, lin), nivel in sorted(dias.items()):
        cx = X0 + col * PASSO + PASSO / 2
        cy = Y0 + lin * PASSO + PASSO / 2
        d = losango(cx, cy, TAM / 2 + 1)
        atraso = DURACAO * 0.75 * (cx - X0) / (fim_x - X0)
        if nivel == 0:
            celulas.append(f'<path d="{d}" fill="{CORES[0]}" stroke="#3A1A22" stroke-width=".6"/>')
        else:
            celulas.append(
                f'<path d="{d}" fill="{CORES[nivel]}" class="n" style="animation-delay:{atraso:.2f}s;'
                f'--b:{BRILHO[nivel]};--c:{CORES[nivel]}"/>')
    petalas = "".join(petala(i, largura, altura) for i in range(18))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{largura}" height="{altura}" viewBox="0 0 {largura} {altura}">
<defs>
<radialGradient id="fundo" cx=".5" cy="0" r="1.2"><stop offset="0" stop-color="#5A1424"/><stop offset=".55" stop-color="#2A0810"/><stop offset="1" stop-color="#12040A"/></radialGradient>
<linearGradient id="ouro" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#5A1424"/><stop offset=".5" stop-color="#C8AA6E"/><stop offset="1" stop-color="#5A1424"/></linearGradient>
<radialGradient id="selo"><stop offset="0" stop-color="#FFE3F1"/><stop offset=".3" stop-color="#FF4FA3"/><stop offset=".7" stop-color="#9B2CFF" stop-opacity=".55"/><stop offset="1" stop-color="#9B2CFF" stop-opacity="0"/></radialGradient>
<linearGradient id="rastro" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#9B2CFF" stop-opacity="0"/><stop offset="1" stop-color="#FF4FA3" stop-opacity=".8"/></linearGradient>
<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="2.6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<style>
.n{{animation:floresce {DURACAO}s linear infinite}}
@keyframes floresce{{0%,14%,100%{{fill:var(--c);filter:none}}2%{{fill:var(--b);filter:url(#glow)}}}}
.t{{font-family:'Beaufort for LOL',Cinzel,Georgia,serif;letter-spacing:3px}}
</style>
<rect width="{largura}" height="{altura}" rx="10" fill="url(#fundo)"/>
{petalas}
<rect x="6" y="6" width="{largura - 12}" height="{altura - 12}" rx="6" fill="none" stroke="url(#ouro)" stroke-width="1.5"/>
<rect x="11" y="11" width="{largura - 22}" height="{altura - 22}" rx="4" fill="none" stroke="#7D2236" stroke-opacity=".7"/>
{rosa(largura / 2, 30, 1.55)}
<text x="{largura / 2:.0f}" y="76" text-anchor="middle" class="t" font-size="18" font-weight="700" fill="#C8AA6E">CONTRIBUIÇÕES</text>
<text x="{largura / 2:.0f}" y="92" text-anchor="middle" class="t" font-size="10.5" fill="#A89880">{total} {"CONTRIBUIÇÃO" if total == "1" else "CONTRIBUIÇÕES"} EM {ANO}</text>
{''.join(celulas)}
<g filter="url(#glow)" opacity="0">
<animateTransform attributeName="transform" type="translate" values="0 0;{fim_x - X0} 0;{fim_x - X0} 0" keyTimes="0;0.75;1" dur="{DURACAO}s" repeatCount="indefinite"/>
<animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0;0.03;0.75;0.8;1" dur="{DURACAO}s" repeatCount="indefinite"/>
<rect x="{X0 - 70}" y="{meio_y - 2:.1f}" width="70" height="4" rx="2" fill="url(#rastro)"/>
<circle cx="{X0}" cy="{meio_y:.1f}" r="9" fill="url(#selo)"/>
<g transform="translate({X0},{meio_y:.1f})">
<path d="M0 -6 L1.6 -1.6 6 0 1.6 1.6 0 6 -1.6 1.6 -6 0 -1.6 -1.6Z" fill="#FFE3F1">
<animateTransform attributeName="transform" type="rotate" values="0;360" dur="2.4s" repeatCount="indefinite"/>
</path>
</g>
</g>
<g transform="translate({largura - X0 - 150},{altura - 26})" class="t" font-size="9.5" fill="#A89880">
<text x="-8" y="4" text-anchor="end">MENOS</text>
{''.join(f'<path d="{losango(i * 14 + 5, 0, TAM / 2 + 1)}" fill="{c}"/>' for i, c in enumerate(CORES))}
<text x="76" y="4">MAIS</text>
</g>
</svg>'''


def main():
    dias, total = baixar()
    if not dias:
        sys.exit("sem dados")
    os.makedirs(SAIDA, exist_ok=True)
    with open(os.path.join(SAIDA, "rosa-negra.svg"), "w", encoding="utf-8") as f:
        f.write(svg(dias, total))
    print(len(dias), "dias,", total, "contribuições")


if __name__ == "__main__":
    main()
