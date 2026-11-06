# Gera o HTML do curso de Nail Designer com ilustrações em SVG e exporta para PDF.
import pathlib, random

OUT = pathlib.Path(__file__).resolve().parent.parent
_uid = [0]
def uid(p="n"):
    _uid[0] += 1
    return f"{p}{_uid[0]}"

# ---------- Ilustrações: unhas ----------
FREE_EDGE = {
    "quadrada":  "L20,24 Q20,14 30,14 L70,14 Q80,14 80,24",
    "redonda":   "L20,46 C20,6 80,6 80,46",
    "oval":      "L20,52 C17,-6 83,-6 80,52",
    "amendoada": "L20,52 C20,28 42,0 50,-4 C58,0 80,28 80,52",
    "stiletto":  "L20,54 C24,32 46,-8 50,-18 C54,-8 76,32 80,54",
    "bailarina": "L20,52 L33,6 Q34,2 38,2 L62,2 Q66,2 67,6 L80,52",
    "squoval":   "L20,30 Q20,12 36,12 L64,12 Q80,12 80,30",
}
def nail_path(shape):
    return f"M20,140 L20,70 {FREE_EDGE[shape]} L80,140 Q50,160 20,140 Z"

def finger(shape="oval", art="solid", color="#C9667A", w=90, label=None, color2="#ffffff"):
    i = uid()
    p = nail_path(shape)
    defs, overlay = "", ""
    fill = color
    if art == "french":
        overlay = f'<g clip-path="url(#c{i})"><path d="M0,-30 L100,-30 L100,62 Q50,40 0,62 Z" fill="{color2}"/></g>'
        fill = "#F4D3CF"
    elif art == "baby":
        defs = f'<linearGradient id="g{i}" x1="0" y1="1" x2="0" y2="0"><stop offset="0.25" stop-color="#F2CBC7"/><stop offset="0.85" stop-color="#FFFFFF"/></linearGradient>'
        fill = f"url(#g{i})"
    elif art == "degrade":
        defs = f'<linearGradient id="g{i}" x1="0" y1="1" x2="0" y2="0"><stop offset="0.1" stop-color="{color}"/><stop offset="0.95" stop-color="{color2}"/></linearGradient>'
        fill = f"url(#g{i})"
    elif art == "glitter":
        random.seed(len(color) + _uid[0])
        dots = "".join(f'<circle cx="{random.uniform(15,85):.1f}" cy="{random.uniform(-15,150):.1f}" r="{random.uniform(0.8,2.4):.1f}" fill="{random.choice(["#fff","#E8C98E","#F7E3B5"])}" opacity="0.95"/>' for _ in range(90))
        overlay = f'<g clip-path="url(#c{i})">{dots}</g>'
    elif art == "flor":
        def flower(cx, cy, r, c):
            petals = "".join(f'<ellipse cx="{cx}" cy="{cy-r}" rx="{r*0.55}" ry="{r*0.9}" fill="{c}" transform="rotate({a} {cx} {cy})"/>' for a in range(0, 360, 72))
            return petals + f'<circle cx="{cx}" cy="{cy}" r="{r*0.4}" fill="#E8B04B"/>'
        overlay = f'<g clip-path="url(#c{i})">{flower(42,70,12,"#fff")}{flower(64,108,8,"#fff")}<path d="M30,120 Q40,100 42,82" stroke="#7FA37A" stroke-width="2" fill="none"/><ellipse cx="34" cy="104" rx="5" ry="2.5" fill="#7FA37A" transform="rotate(-50 34 104)"/></g>'
    elif art == "marmore":
        overlay = (f'<g clip-path="url(#c{i})" fill="none" stroke-linecap="round">'
                   f'<path d="M10,20 C35,40 30,70 60,90 S75,130 95,150" stroke="#8E8E95" stroke-width="1.6" opacity=".7"/>'
                   f'<path d="M5,80 C25,85 40,60 70,40" stroke="#A9A9B0" stroke-width="1" opacity=".7"/>'
                   f'<path d="M40,0 C45,20 60,30 90,25" stroke="#C9A26A" stroke-width="1.4"/></g>')
    elif art == "encapsulada":
        overlay = (f'<g clip-path="url(#c{i})"><circle cx="40" cy="60" r="5" fill="#C9A26A"/><circle cx="58" cy="75" r="3" fill="#C9A26A"/>'
                   f'<path d="M45,95 l4,8 l9,1 l-7,6 l2,9 l-8,-5 l-8,5 l2,-9 l-7,-6 l9,-1z" fill="#fff" opacity=".9"/></g>')
    elif art == "nu":
        fill = "#F1D2CC"
    shine = f'<path d="M30,120 L30,60 Q31,40 38,30" stroke="#fff" stroke-width="5" stroke-linecap="round" fill="none" opacity=".35"/>'
    lab = f'<div class="nlabel">{label}</div>' if label else ""
    return (f'<div class="finger"><svg viewBox="0 -24 100 224" width="{w}" xmlns="http://www.w3.org/2000/svg">'
            f'<defs><clipPath id="c{i}"><path d="{p}"/></clipPath>{defs}</defs>'
            f'<rect x="6" y="36" width="88" height="200" rx="44" fill="#F3C9B4"/>'
            f'<path d="M14,200 L14,120 Q14,92 30,82" stroke="#E2AE96" stroke-width="2" fill="none" opacity=".6"/>'
            f'<path d="{p}" fill="{fill}" stroke="#00000018" stroke-width="1"/>{overlay}{shine}'
            f'</svg>{lab}</div>')

# ---------- Ilustrações: ícones ----------
ICONS = {
"lixa": '<rect x="10" y="40" width="80" height="20" rx="10" fill="#E9C9C1"/><rect x="10" y="40" width="40" height="20" rx="10" fill="#C9667A"/><rect x="30" y="40" width="20" height="20" fill="#C9667A"/><text x="30" y="54" font-size="8" fill="#fff" text-anchor="middle" font-family="Inter">100</text><text x="70" y="54" font-size="8" fill="#4A2C3A" text-anchor="middle" font-family="Inter">180</text>',
"buffer": '<rect x="18" y="34" width="64" height="32" rx="6" fill="#F3E3B9"/><rect x="18" y="34" width="64" height="8" rx="4" fill="#E2C67E"/><path d="M26,52 h48 M26,58 h48" stroke="#D1B26A" stroke-width="2" stroke-dasharray="2 3"/>',
"alicate": '<path d="M50,52 L30,92" stroke="#7A7F8A" stroke-width="7" stroke-linecap="round"/><path d="M50,52 L70,92" stroke="#7A7F8A" stroke-width="7" stroke-linecap="round"/><path d="M50,52 Q44,30 47,12 L50,10 L50,52Z" fill="#A4A9B3"/><path d="M50,52 Q56,30 53,12 L50,10 L50,52Z" fill="#8C919C"/><circle cx="50" cy="52" r="5" fill="#C9A26A"/><path d="M38,74 Q50,62 62,74" stroke="#C9A26A" stroke-width="3" fill="none"/>',
"espatula": '<rect x="46" y="22" width="8" height="66" rx="4" fill="#A4A9B3"/><path d="M42,24 Q50,6 58,24 Z" fill="#7A7F8A"/><path d="M46,86 l4,8 l4,-8z" fill="#7A7F8A"/>',
"pincel": '<rect x="46" y="36" width="8" height="58" rx="3" fill="#4A2C3A"/><rect x="45" y="28" width="10" height="10" fill="#C9A26A"/><path d="M45,28 Q44,14 50,6 Q56,14 55,28 Z" fill="#E9C9C1"/>',
"cabine": '<path d="M12,80 L12,56 Q12,24 50,24 Q88,24 88,56 L88,80 Z" fill="#F7F1F0" stroke="#C9667A" stroke-width="3"/><path d="M26,80 L26,60 Q26,40 50,40 Q74,40 74,60 L74,80" fill="#4A2C3A"/><rect x="8" y="78" width="84" height="8" rx="4" fill="#C9667A"/><g fill="#9B7BE0"><circle cx="38" cy="46" r="2.5"/><circle cx="50" cy="43" r="2.5"/><circle cx="62" cy="46" r="2.5"/></g><path d="M40,60 l-3,8 M50,58 v9 M60,60 l3,8" stroke="#9B7BE0" stroke-width="2"/>',
"molde": '<path d="M10,40 h80 v36 h-80z" fill="#F7E3B5"/><path d="M38,40 h24 v20 q-12,10 -24,0z" fill="#fff" stroke="#C9A26A"/><path d="M50,40 v36 M42,50 h16 M42,58 h16 M42,66 h16" stroke="#C9667A" stroke-width="1"/>',
"tips": '<g fill="#fff" stroke="#C9A26A" stroke-width="1.5"><path d="M20,80 L20,40 Q20,20 30,20 Q40,20 40,40 L40,80 Q30,86 20,80Z"/><path d="M45,80 L45,34 Q45,14 56,14 Q67,14 67,34 L67,80 Q56,86 45,80Z"/><path d="M72,80 L72,44 Q72,28 80,28 Q88,28 88,44 L88,80 Q80,85 72,80Z"/></g>',
"gel": '<rect x="28" y="40" width="44" height="46" rx="8" fill="#C9667A"/><rect x="34" y="22" width="32" height="20" rx="4" fill="#4A2C3A"/><rect x="34" y="52" width="32" height="18" rx="3" fill="#fff" opacity=".85"/><text x="50" y="65" font-size="9" text-anchor="middle" fill="#4A2C3A" font-family="Inter" font-weight="700">GEL</text>',
"motor": '<rect x="40" y="10" width="20" height="60" rx="10" fill="#4A2C3A"/><rect x="44" y="70" width="12" height="10" fill="#A4A9B3"/><path d="M48,80 h4 v12 l-2,4 l-2,-4z" fill="#7A7F8A"/><circle cx="50" cy="30" r="3" fill="#C9A26A"/>',
"luvas": '<path d="M30,92 L30,50 Q30,44 35,44 Q40,44 40,50 L40,30 Q40,24 45,24 Q50,24 50,30 L50,26 Q50,20 55,20 Q60,20 60,26 L60,32 Q60,26 65,26 Q70,26 70,32 L70,70 Q70,92 50,92Z" fill="#8FB5E8"/><rect x="28" y="88" width="44" height="8" rx="2" fill="#6E98D2"/>',
"mascara": '<path d="M22,40 Q50,30 78,40 L76,68 Q50,82 24,68 Z" fill="#9FD3C7"/><path d="M28,50 Q50,44 72,50 M28,58 Q50,52 72,58" stroke="#fff" stroke-width="2" fill="none"/><path d="M22,42 Q8,44 12,58 Q14,64 24,64 M78,42 Q92,44 88,58 Q86,64 76,64" stroke="#7FB5A9" stroke-width="2" fill="none"/>',
"autoclave": '<rect x="14" y="30" width="72" height="56" rx="8" fill="#DCE1E8"/><circle cx="44" cy="58" r="18" fill="#fff" stroke="#A4A9B3" stroke-width="4"/><circle cx="44" cy="58" r="8" fill="#C9667A" opacity=".3"/><rect x="70" y="40" width="10" height="6" rx="2" fill="#7FA37A"/><rect x="70" y="52" width="10" height="6" rx="2" fill="#C9667A"/><text x="50" y="24" font-size="9" text-anchor="middle" fill="#4A2C3A" font-family="Inter" font-weight="700">121°C</text>',
"alcool": '<rect x="34" y="34" width="32" height="56" rx="6" fill="#E3F0FA" stroke="#8FB5E8" stroke-width="2"/><rect x="42" y="20" width="16" height="14" fill="#8FB5E8"/><rect x="46" y="12" width="14" height="8" fill="#6E98D2"/><text x="50" y="66" font-size="11" text-anchor="middle" fill="#4A2C3A" font-family="Inter" font-weight="700">70%</text>',
"descarte": '<path d="M24,36 h52 l-6,56 h-40z" fill="#F7D774"/><rect x="20" y="28" width="60" height="10" rx="3" fill="#E2B93B"/><path d="M50,52 l12,22 h-24z" fill="none" stroke="#4A2C3A" stroke-width="3"/><text x="50" y="72" font-size="9" text-anchor="middle" fill="#4A2C3A" font-family="Inter" font-weight="700">!</text>',
"lavar": '<path d="M50,14 Q66,36 66,48 A16,16 0 0 1 34,48 Q34,36 50,14Z" fill="#8FB5E8"/><path d="M20,80 Q35,64 50,74 Q65,84 80,70" stroke="#C9667A" stroke-width="5" fill="none" stroke-linecap="round"/><circle cx="30" cy="62" r="4" fill="#E3F0FA" stroke="#8FB5E8"/><circle cx="72" cy="58" r="3" fill="#E3F0FA" stroke="#8FB5E8"/>',
"celular": '<rect x="32" y="12" width="36" height="76" rx="7" fill="#4A2C3A"/><rect x="36" y="20" width="28" height="56" rx="2" fill="#F6E7E4"/><path d="M50,58 C40,50 40,40 46,40 C49,40 50,43 50,43 C50,43 51,40 54,40 C60,40 60,50 50,58Z" fill="#C9667A"/>',
"moeda": '<circle cx="50" cy="52" r="32" fill="#E8C98E"/><circle cx="50" cy="52" r="25" fill="none" stroke="#C9A26A" stroke-width="3"/><text x="50" y="62" font-size="28" text-anchor="middle" fill="#8A6A35" font-family="Inter" font-weight="800">R$</text>',
"agenda": '<rect x="18" y="24" width="64" height="62" rx="6" fill="#fff" stroke="#C9667A" stroke-width="3"/><rect x="18" y="24" width="64" height="16" rx="6" fill="#C9667A"/><g fill="#E9C9C1"><rect x="26" y="48" width="10" height="9"/><rect x="45" y="48" width="10" height="9"/><rect x="64" y="48" width="10" height="9"/><rect x="26" y="64" width="10" height="9"/><rect x="45" y="64" width="10" height="9" fill="#C9667A"/></g>',
"estrela": '<path d="M50,14 l10,22 24,3 -18,16 5,24 -21,-12 -21,12 5,-24 -18,-16 24,-3z" fill="#E8C98E"/>',
"foto": '<rect x="14" y="30" width="72" height="50" rx="8" fill="#4A2C3A"/><circle cx="50" cy="55" r="16" fill="#F6E7E4"/><circle cx="50" cy="55" r="9" fill="#C9667A"/><rect x="24" y="24" width="18" height="8" rx="2" fill="#4A2C3A"/>',
}
def icon(name, w=64):
    return f'<svg viewBox="0 0 100 100" width="{w}" height="{w}" xmlns="http://www.w3.org/2000/svg">{ICONS[name]}</svg>'

# ---------- Diagramas ----------
ANATOMIA_TOPO = '''
<svg viewBox="0 0 360 330" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter" font-size="11" fill="#4A2C3A">
 <rect x="110" y="70" width="140" height="300" rx="70" fill="#F3C9B4"/>
 <path d="M135,240 L135,110 C135,40 225,40 225,110 L225,240 Q180,270 135,240Z" fill="#F7D9D4" stroke="#E2AE96"/>
 <path d="M135,110 C135,40 225,40 225,110 Q180,95 135,110Z" fill="#FBF3F1"/>
 <path d="M150,236 Q180,206 210,236 Q180,252 150,236Z" fill="#FBEFED"/>
 <path d="M133,242 Q180,276 227,242" stroke="#C98C78" stroke-width="5" fill="none" stroke-linecap="round"/>
 <path d="M130,240 L130,120 M230,240 L230,120" stroke="#E2AE96" stroke-width="3"/>
 <g stroke="#C9667A" stroke-width="1.2" fill="none">
  <path d="M180,70 L290,40"/><path d="M200,170 L300,150"/><path d="M180,238 L300,250"/>
  <path d="M150,252 L60,290"/><path d="M130,180 L60,170"/><path d="M180,262 L250,305"/>
 </g>
 <g fill="#C9667A"><circle cx="180" cy="70" r="3"/><circle cx="200" cy="170" r="3"/><circle cx="180" cy="238" r="3"/><circle cx="150" cy="252" r="3"/><circle cx="130" cy="180" r="3"/><circle cx="180" cy="262" r="3"/></g>
 <text x="294" y="38" font-weight="700">Borda livre</text>
 <text x="304" y="146" font-weight="700">Lâmina</text><text x="304" y="160">ungueal</text>
 <text x="304" y="248" font-weight="700">Lúnula</text>
 <text x="4" y="300" font-weight="700">Cutícula</text>
 <text x="4" y="166" font-weight="700">Paredes</text><text x="4" y="180">laterais</text>
 <text x="254" y="312" font-weight="700">Eponíquio</text>
</svg>'''

ANATOMIA_LADO = '''
<svg viewBox="0 0 360 220" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter" font-size="11" fill="#4A2C3A">
 <path d="M10,90 L230,70 Q300,66 312,120 Q316,170 260,180 L10,190Z" fill="#F3C9B4"/>
 <path d="M30,140 L200,128 Q236,128 240,146 Q236,160 200,160 L30,166Z" fill="#F3E9DC" stroke="#E3D5C3"/>
 <path d="M120,82 Q140,74 160,76 Q156,90 120,96Z" fill="#E8A3A3"/>
 <path d="M150,78 L250,70 Q296,68 330,82 L330,88 Q296,76 250,80 L156,88Z" fill="#F7D9D4" stroke="#C9667A" stroke-width="1"/>
 <path d="M160,88 L250,80 Q290,78 300,92" stroke="#E7A9A0" stroke-width="5" fill="none"/>
 <path d="M300,92 Q318,92 330,88" stroke="#E2AE96" stroke-width="3" fill="none"/>
 <path d="M110,76 Q140,64 160,74" stroke="#C98C78" stroke-width="4" fill="none"/>
 <g stroke="#C9667A" stroke-width="1.2" fill="none">
  <path d="M138,86 L110,30"/><path d="M135,68 L80,50"/><path d="M220,76 L220,30"/><path d="M250,84 L250,200"/><path d="M314,92 L330,140"/><path d="M200,145 L160,205"/>
 </g>
 <text x="70" y="24" font-weight="700">Matriz</text><text x="70" y="38" font-size="9.5">(onde a unha nasce)</text>
 <text x="10" y="54" font-weight="700">Eponíquio</text>
 <text x="190" y="24" font-weight="700">Lâmina ungueal</text>
 <text x="258" y="210" font-weight="700">Leito ungueal</text>
 <text x="300" y="155" font-weight="700">Hiponíquio</text>
 <text x="120" y="215" font-weight="700">Falange distal (osso)</text>
</svg>'''

ESTRUTURA = '''
<svg viewBox="0 0 360 170" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter" font-size="11" fill="#4A2C3A">
 <path d="M10,120 L200,110 Q240,108 250,135 Q252,160 210,160 L10,165Z" fill="#F3C9B4"/>
 <path d="M60,112 L200,104 Q230,103 260,104 L340,106 L340,112 L260,112 Q232,112 200,114 L64,118Z" fill="#F7D9D4"/>
 <path d="M64,112 Q140,72 210,96 Q280,104 340,104 L340,112 L260,112 L200,114 L64,118Z" fill="#C9667A" opacity=".55"/>
 <path d="M64,112 Q140,72 210,96 Q280,104 340,104" stroke="#C9667A" stroke-width="2" fill="none"/>
 <g stroke="#4A2C3A" stroke-width="1.2" fill="none"><path d="M150,86 L150,40"/><path d="M212,98 L250,50"/><path d="M335,104 L335,70"/><path d="M80,108 L50,60"/></g>
 <circle cx="150" cy="86" r="4" fill="#4A2C3A"/>
 <text x="110" y="34" font-weight="700">Ápice (apex)</text>
 <text x="230" y="44" font-weight="700">Ponto de tensão</text>
 <text x="300" y="64" font-weight="700">Borda livre</text>
 <text x="10" y="54" font-weight="700">Cutícula</text><text x="10" y="68" font-size="9.5">(fina, sem degrau)</text>
</svg>'''

CCURVE = '''
<svg viewBox="0 0 200 120" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter" font-size="11" fill="#4A2C3A">
 <path d="M30,90 Q100,10 170,90" stroke="#C9667A" stroke-width="10" fill="none" stroke-linecap="round"/>
 <path d="M30,90 Q100,40 170,90" stroke="#4A2C3A" stroke-width="1" stroke-dasharray="3 3" fill="none"/>
 <text x="100" y="114" text-anchor="middle" font-weight="700">Curvatura em C</text>
</svg>'''

# ---------- Componentes ----------
def page(body, cls="", num=None, title=None):
    foot = f'<div class="foot"><span>Curso de Nail Designer</span><span>{num}</span></div>' if num else ""
    return f'<section class="page {cls}">{body}{foot}</section>'

def module_head(n, title, sub):
    return f'<div class="mhead"><div class="mnum">Módulo {n:02d}</div><h1>{title}</h1><p class="lead">{sub}</p></div>'

def steps(items):
    return '<ol class="steps">' + "".join(f'<li><b>{t}</b><span>{d}</span></li>' for t, d in items) + '</ol>'

def tip(text, kind="Dica de profissional"):
    return f'<div class="tip"><div class="tiph">{kind}</div><p>{text}</p></div>'

def warn(text):
    return f'<div class="tip warn"><div class="tiph">Atenção</div><p>{text}</p></div>'

pages = []

# Capa
cover_fingers = "".join([
    finger("amendoada", "solid", "#C9667A", 92), finger("stiletto", "glitter", "#4A2C3A", 92),
    finger("bailarina", "french", w=92), finger("oval", "flor", "#E7A9B5", 92), finger("squoval", "marmore", "#F4F1EE", 92)])
pages.append(page(f'''
<div class="cover">
  <div class="cover-top"><span class="pill">Apostila completa · 12 módulos</span></div>
  <h1 class="ctitle">Curso de<br><em>Nail Designer</em></h1>
  <p class="csub">Do zero ao profissional: anatomia, biossegurança, esmaltação em gel, alongamentos, nail art e como montar seu negócio.</p>
  <div class="cover-hand">{cover_fingers}</div>
  <div class="cover-bottom"><span>Apostila ilustrada</span><span>Edição 2026</span></div>
</div>''', "cover-page"))

# Sumário
mods = [("Anatomia da unha", "Estrutura e funções"), ("Biossegurança", "Higiene, EPIs e esterilização"),
        ("Materiais e ferramentas", "Seu kit de trabalho"), ("Formatos de unha", "Como escolher o ideal"),
        ("Preparação e cutilagem", "A base de tudo"), ("Esmaltação em gel", "Passo a passo"),
        ("Tipos de alongamento", "Fibra, gel, tips, polygel"), ("Alongamento em gel no molde", "Técnica e estrutura"),
        ("Manutenção e remoção", "Durabilidade com saúde"), ("Nail art", "Técnicas decorativas"),
        ("Problemas e contraindicações", "Quando não atender"), ("Seu negócio", "Preço, atendimento e redes")]
toc = "".join(f'<div class="toc-row"><span class="toc-n">{i+1:02d}</span><span class="toc-t">{t}<small>{s}</small></span><span class="toc-p">{i+3}</span></div>' for i, (t, s) in enumerate(mods))
pages.append(page(f'''
<div class="mhead"><div class="mnum">Boas-vindas</div><h1>Seja bem-vinda à profissão</h1>
<p class="lead">O nail designer vai além de "fazer unhas": é uma profissional que entende a saúde das unhas, domina técnicas de estrutura e transforma cada atendimento em uma experiência. Esta apostila acompanha você do primeiro contato com os materiais até a gestão do seu próprio espaço.</p></div>
<div class="two">
 <div><h3>Conteúdo</h3><div class="toc">{toc}</div></div>
 <div>
  <h3>Como estudar</h3>
  <ul class="checks">
   <li>Leia um módulo por vez e pratique antes de avançar.</li>
   <li>Treine primeiro em <b>tips de treino</b> ou em um dedo de prática.</li>
   <li>Fotografe seus trabalhos para comparar a evolução.</li>
   <li>Faça os exercícios do final de cada módulo.</li>
   <li>Biossegurança não é opcional: aplique desde o primeiro treino.</li>
  </ul>
  <div class="stack-fingers">{finger("oval","nu",w=70)}{finger("oval","solid","#C9667A",w=70)}{finger("oval","glitter","#C9667A",w=70)}</div>
  <p class="cap">Da unha natural à unha finalizada: o caminho deste curso.</p>
 </div>
</div>''', num=2))

# 1 Anatomia
pages.append(page(f'''
{module_head(1, "Anatomia da unha", "Conhecer cada parte da unha é o que permite trabalhar com segurança, sem ferir a cliente e garantindo durabilidade ao serviço.")}
<div class="two">
 <figure class="card">{ANATOMIA_TOPO}<figcaption>Vista superior</figcaption></figure>
 <figure class="card">{ANATOMIA_LADO}<figcaption>Corte lateral</figcaption></figure>
</div>
<table class="tbl">
 <tr><th>Parte</th><th>O que é</th><th>Cuidado no atendimento</th></tr>
 <tr><td>Matriz</td><td>Região sob a pele onde a unha é produzida.</td><td>Nunca pressionar ou lesionar: danos podem deformar a unha de forma permanente.</td></tr>
 <tr><td>Lâmina ungueal</td><td>A placa de queratina visível, sem terminações nervosas.</td><td>Lixar apenas para tirar o brilho; não afinar demais.</td></tr>
 <tr><td>Leito ungueal</td><td>Pele sob a lâmina, rica em vasos sanguíneos.</td><td>Não forçar o descolamento da lâmina ao remover produtos.</td></tr>
 <tr><td>Lúnula</td><td>Meia-lua esbranquiçada, parte visível da matriz.</td><td>Área sensível: evitar pressão excessiva com brocas.</td></tr>
 <tr><td>Cutícula e eponíquio</td><td>Pele que sela e protege a matriz contra infecções.</td><td>Remover só a película solta; preservar a pele viva.</td></tr>
 <tr><td>Hiponíquio</td><td>Selo sob a borda livre que protege o leito.</td><td>Não limpar por baixo com instrumentos pontiagudos.</td></tr>
</table>
{tip("A unha cresce cerca de 3 mm por mês nas mãos. Por isso a manutenção de alongamentos é indicada a cada 15 a 21 dias.", "Você sabia?")}
''', num=3))

# 2 Biossegurança
bio = [("lavar","Higienização das mãos","Lave as mãos antes e depois de cada cliente e peça que ela também lave."),
       ("luvas","Luvas descartáveis","Uso individual: um par por cliente, descartado ao final."),
       ("mascara","Máscara e óculos","Protegem contra pó de lixamento e vapores dos produtos."),
       ("alcool","Álcool 70%","Para bancada, frascos e superfícies. Não substitui a esterilização."),
       ("autoclave","Autoclave","Esteriliza alicates e metais por vapor sob pressão. Estufa não é recomendada pela vigilância sanitária."),
       ("descarte","Descarte correto","Lâminas e agulhas em caixa de perfurocortantes; lixas são de uso único.")]
biocards = "".join(f'<div class="icard">{icon(n,58)}<div><b>{t}</b><p>{d}</p></div></div>' for n, t, d in bio)
pages.append(page(f'''
{module_head(2, "Biossegurança", "Unhas e cutículas são portas de entrada para fungos, bactérias e vírus como hepatites B e C. A biossegurança protege a cliente, você e o seu negócio.")}
<div class="grid3">{biocards}</div>
<h3>Ciclo de reprocessamento dos instrumentos metálicos</h3>
<div class="flow">
 <div class="fstep"><span>1</span>Limpeza<small>Lavar com detergente enzimático e escova</small></div>
 <div class="farrow">→</div>
 <div class="fstep"><span>2</span>Secagem<small>Secar bem com papel toalha</small></div>
 <div class="farrow">→</div>
 <div class="fstep"><span>3</span>Embalagem<small>Envelope grau cirúrgico com indicador</small></div>
 <div class="farrow">→</div>
 <div class="fstep"><span>4</span>Esterilização<small>Ciclo completo na autoclave</small></div>
 <div class="farrow">→</div>
 <div class="fstep"><span>5</span>Abertura<small>Abrir o envelope na frente da cliente</small></div>
</div>
<div class="two">
{warn("Itens porosos (lixas, palitos, buffers) não podem ser esterilizados: são <b>descartáveis</b> ou devem ser entregues à cliente. Nunca reutilize em outra pessoa.")}
{tip("Consulte as normas da vigilância sanitária do seu município: elas definem as exigências para o alvará do seu espaço e podem variar de cidade para cidade.", "Legislação")}
</div>
''', num=4))

# 3 Materiais
tools = [("lixa","Lixas 100/180","Grão menor = mais abrasiva. 100/180 para modelar, 180/240 para natural."),
         ("buffer","Buffer","Remove o brilho da lâmina e alisa a superfície."),
         ("alicate","Alicate de cutícula","Remove apenas as peles soltas. Sempre esterilizado."),
         ("espatula","Espátula / empurrador","Afasta a cutícula e retira a película da lâmina."),
         ("pincel","Pincéis","Chato para gel, liner para detalhes, oval para esmaltação."),
         ("cabine","Cabine LED/UV","Polimeriza (seca) o gel. Respeite o tempo do fabricante."),
         ("gel","Géis e esmaltes em gel","Base, construção, cor e top coat."),
         ("molde","Moldes de papel","Guia para alongar além da borda livre."),
         ("tips","Tips","Ponteiras plásticas para alongamento rápido."),
         ("motor","Motor (lixa elétrica)","Agiliza remoção e acabamento. Exige treino.")]
toolcards = "".join(f'<div class="tcard">{icon(n,70)}<b>{t}</b><p>{d}</p></div>' for n, t, d in tools)
pages.append(page(f'''
{module_head(3, "Materiais e ferramentas", "Um kit bem escolhido facilita o trabalho e melhora o resultado. Comece com o essencial e invista aos poucos em itens de maior qualidade.")}
<div class="grid5">{toolcards}</div>
<div class="two">
 <div class="card pad">
  <h3>Kit inicial essencial</h3>
  <ul class="checks cols2">
   <li>Cabine LED 48W ou mais</li><li>Primer e prep (desidratador)</li><li>Base e top coat em gel</li>
   <li>Gel de construção (clear e nude)</li><li>3 a 5 cores de esmalte em gel</li><li>Lixas 100/180 e buffers</li>
   <li>Alicate e espátula de inox</li><li>Pincéis chato e liner</li><li>Moldes e tips de treino</li>
   <li>Algodão, papel toalha, luvas</li><li>Álcool 70% e removedor</li><li>Autoclave (ou parceria)</li>
  </ul>
 </div>
 {tip("Prefira produtos de uma mesma linha (prep, primer, base e gel): eles são formulados para trabalhar juntos, o que reduz descolamentos e alergias.")}
</div>
''', num=5))

# 4 Formatos
shapes = [("quadrada","Quadrada","Pontas retas. Elegante, ideal para dedos longos."),
          ("squoval","Squoval","Quadrada com cantos suaves. Versátil e resistente."),
          ("redonda","Redonda","Acompanha o dedo. Ótima para unhas curtas."),
          ("oval","Oval","Alonga visualmente os dedos. Clássica."),
          ("amendoada","Amendoada","Laterais afinadas e ponta arredondada. Delicada."),
          ("bailarina","Bailarina","Afunila e termina reta. Moderna; pede comprimento."),
          ("stiletto","Stiletto","Ponta fina. Ousada; exige estrutura reforçada.")]
shapecards = "".join(f'<div class="scard">{finger(s,"solid","#C9667A",52)}<b>{t}</b><p>{d}</p></div>' for s, t, d in shapes)
pages.append(page(f'''
{module_head(4, "Formatos de unha", "O formato certo valoriza a mão da cliente e combina com a rotina dela. Antes de lixar, sempre pergunte: o que você faz no dia a dia?")}
<div class="shapes">{shapecards}</div>
<div class="two">
 <div class="card pad">
  <h3>Como indicar o formato</h3>
  <table class="tbl small">
   <tr><th>Perfil da cliente</th><th>Sugestão</th></tr>
   <tr><td>Dedos curtos ou largos</td><td>Oval, amendoada</td></tr>
   <tr><td>Dedos longos e finos</td><td>Quadrada, squoval</td></tr>
   <tr><td>Digita muito ou trabalha com as mãos</td><td>Redonda, squoval curta</td></tr>
   <tr><td>Quer impacto e comprimento</td><td>Bailarina, stiletto</td></tr>
  </table>
 </div>
 {tip("Para lixar com simetria, olhe a unha de frente e de perfil, e compare com as outras mãos. Lixe sempre das laterais para o centro, em um único sentido.")}
</div>
''', num=6))

# 5 Preparação
pages.append(page(f'''
{module_head(5, "Preparação e cutilagem", "Até 80% da durabilidade de um serviço em gel depende de uma boa preparação. Uma unha mal preparada descola, mesmo com o melhor produto.")}
<div class="two wide-left">
 {steps([("Anamnese","Converse com a cliente, verifique alergias, medicamentos e o estado das unhas. Registre na ficha."),
         ("Higienização","Cliente e profissional higienizam as mãos. Borrife álcool 70% nas unhas."),
         ("Formato e comprimento","Lixe a borda livre com lixa 180, no formato combinado."),
         ("Afastar a cutícula","Com a espátula em ângulo de 45°, empurre suavemente a cutícula."),
         ("Remover a película","Retire a pele morta aderida à lâmina (cutilagem a seco ou com amolecedor)."),
         ("Retirar o excesso","Com o alicate, remova apenas as peles soltas, sem cortar pele viva."),
         ("Tirar o brilho","Passe o buffer em toda a lâmina, sem afinar. Remova o pó com escovinha."),
         ("Desidratar e preparar","Aplique o prep (desidratador) e, se indicado, o primer.")])}
 <div>
  <figure class="card center">
   <div class="row-fingers">{finger("oval","nu",w=74)}<div class="arrow">→</div>{finger("oval","nu",w=74)}</div>
   <figcaption>Antes: cutícula sobre a lâmina · Depois: lâmina limpa e sem brilho</figcaption>
  </figure>
  {warn("Nunca corte a cutícula viva nem cause sangramento. Se houver feridas, inflamação ou suspeita de micose, não realize o serviço e oriente a cliente a buscar um médico dermatologista.")}
  {tip("Depois do prep, não toque mais na lâmina: a oleosidade dos dedos prejudica a aderência.")}
 </div>
</div>
''', num=7))

# 6 Esmaltação em gel
gel_steps = [("nu","Unha preparada"),("base","Base em gel"),("cor1","1ª camada de cor"),("cor2","2ª camada"),("top","Top coat")]
def gel_vis(k):
    m = {"nu":finger("oval","nu",w=70),"base":finger("oval","solid","#F4D7D3",w=70),
         "cor1":finger("oval","solid","#DE93A2",w=70),"cor2":finger("oval","solid","#C9667A",w=70),
         "top":finger("oval","solid","#B8506A",w=70)}
    return m[k]
gelrow = "".join(f'<div class="gstep">{gel_vis(k)}<span>{i+1}. {t}</span></div>' for i, (k, t) in enumerate(gel_steps))
pages.append(page(f'''
{module_head(6, "Esmaltação em gel", "Esmalte que só seca na cabine, com brilho intenso e duração de 15 a 21 dias. É o serviço de entrada mais procurado do mercado.")}
<div class="card gelrow">{gelrow}</div>
<div class="two">
 {steps([("Base fina","Aplique uma camada fina, sem encostar na cutícula. Sele a borda livre. Cabine: 60 s (LED)."),
         ("Primeira camada de cor","Camada fina e uniforme, deixando 1 mm de distância da cutícula. Cabine: 60 s."),
         ("Segunda camada","Corrige falhas e dá a cor final. Sele novamente a ponta. Cabine: 60 s."),
         ("Top coat","Dá brilho e proteção. Cabine conforme o fabricante (de 60 a 90 s)."),
         ("Finalização","Remova a camada pegajosa com álcool, se o top tiver dispersão. Hidrate as cutículas com óleo.")])}
 <div>
  {tip("Camadas grossas não secam por completo no fundo, enrugam e causam alergia. Sempre prefira duas camadas finas a uma grossa.", "Regra de ouro")}
  {warn("Gel que escorre para a pele precisa ser limpo <b>antes</b> de ir à cabine, com um pincel ou palito. O contato frequente do gel não curado com a pele é a principal causa de alergia aos produtos.")}
  <div class="card pad">
   <h3>Por que descascou?</h3>
   <ul class="checks">
    <li>Preparação incompleta ou película não removida</li>
    <li>Produto encostado na cutícula</li>
    <li>Borda livre não selada</li>
    <li>Tempo de cabine insuficiente ou lâmpada fraca</li>
   </ul>
  </div>
 </div>
</div>
''', num=8))

# 7 Tipos de alongamento
pages.append(page(f'''
{module_head(7, "Tipos de alongamento", "Cada técnica tem vantagens. Conhecer todas permite indicar a melhor opção para cada cliente e ampliar seu cardápio de serviços.")}
<div class="grid4">
 <div class="acard">{icon("molde",64)}<b>Gel no molde</b><p>Gel moldado sobre um molde de papel. Leve, natural e resistente.</p></div>
 <div class="acard">{icon("tips",64)}<b>Tips</b><p>Ponteira plástica colada e coberta com gel. Rápido e uniforme.</p></div>
 <div class="acard">{icon("pincel",64)}<b>Fibra de vidro</b><p>Fios de fibra fixados com gel. Muito fina e natural.</p></div>
 <div class="acard">{icon("gel",64)}<b>Polygel</b><p>Massa entre gel e acrílico, modelada com pincel. Não escorre.</p></div>
</div>
<table class="tbl">
 <tr><th>Técnica</th><th>Durabilidade</th><th>Aparência</th><th>Dificuldade</th><th>Indicação</th></tr>
 <tr><td>Gel no molde</td><td>Alta</td><td>Natural, leve</td><td>Média</td><td>Todos os formatos e comprimentos</td></tr>
 <tr><td>Tips + gel</td><td>Alta</td><td>Uniforme</td><td>Baixa</td><td>Iniciantes, atendimentos rápidos</td></tr>
 <tr><td>Fibra de vidro</td><td>Média a alta</td><td>A mais natural</td><td>Alta</td><td>Comprimentos curtos e médios</td></tr>
 <tr><td>Polygel</td><td>Alta</td><td>Natural</td><td>Média</td><td>Quem quer mais controle do produto</td></tr>
 <tr><td>Acrílico</td><td>Muito alta</td><td>Mais espessa</td><td>Alta</td><td>Unhas longas e esculturas</td></tr>
</table>
<div class="two">
 {tip("Comece pela técnica de tips + gel para entender a estrutura. Depois, avance para o molde, que é a mais pedida.", "Por onde começar")}
 {tip("Banho de gel (blindagem) é uma camada de gel sobre a unha natural, sem alongar. Ótimo para quem quer fortalecer a unha e mantê-la curta.", "Serviço extra")}
</div>
''', num=9))

# 8 Alongamento no molde
pages.append(page(f'''
{module_head(8, "Alongamento em gel no molde", "A técnica mais completa do nail designer. O segredo está na estrutura: uma unha bonita precisa ser também resistente.")}
<div class="two">
 <figure class="card">{ESTRUTURA}<figcaption>Perfil lateral: a estrutura correta</figcaption></figure>
 <figure class="card">{CCURVE}<figcaption>Vista frontal: 30% a 50% de um círculo</figcaption></figure>
</div>
<div class="two wide-left">
 {steps([("Preparação completa","Siga todo o Módulo 5, com prep e primer."),
         ("Base fina","Aplique base em gel e polimerize. Ela cria aderência para o gel de construção."),
         ("Encaixar o molde","Ajuste o molde sob a borda livre, sem frestas e alinhado ao dedo. Confira de frente e de perfil."),
         ("Desenhar o comprimento","Com o gel de construção, puxe o comprimento sobre o molde e cure por 30 s."),
         ("Construir o ápice","Aplique uma gota no ponto de tensão e espalhe, deixando o ponto mais alto no centro da unha. Cure de cabeça para baixo por 10 s para o gel não escorrer, depois cure completo."),
         ("Remover o molde e pinçar","Retire o molde e, se desejar, use a pinça de curvatura nos primeiros segundos de cura."),
         ("Lixar e modelar","Lixe as laterais, a borda livre e a superfície até ficar lisa e simétrica."),
         ("Finalizar","Esmaltação em gel e top coat. Hidrate as cutículas.")])}
 <div>
  <div class="row-fingers">{finger("bailarina","solid","#F1C7C5",w=56)}{finger("amendoada","solid","#C9667A",w=56)}</div>
  {tip("A espessura deve ser fina na cutícula, mais alta no ápice e fina novamente na borda livre. Olhe sempre a unha de perfil.")}
  {warn("Não lixe a lâmina natural com motor em alta rotação: o calor e a pressão podem afinar e lesionar a unha.")}
 </div>
</div>
''', num=10))

# 9 Manutenção
pages.append(page(f'''
{module_head(9, "Manutenção e remoção", "A manutenção mantém o alongamento equilibrado à medida que a unha cresce. A remoção correta preserva a unha natural da cliente.")}
<div class="two">
 <div class="card pad">
  <h3>Manutenção (a cada 15 a 21 dias)</h3>
  {steps([("Avaliar","Verifique descolamentos, rachaduras e a nova área crescida."),
          ("Desgastar","Retire a cor e afine o gel antigo, sem expor a unha natural."),
          ("Remover descolamentos","Elimine todo o produto solto: nunca cubra descolamentos."),
          ("Preparar a área nova","Cutilagem, buffer e prep apenas na parte que cresceu."),
          ("Reequilibrar","Reposicione o ápice, que se deslocou com o crescimento."),
          ("Finalizar","Lixe, esmalte e aplique o top coat.")])}
 </div>
 <div>
  <figure class="card center">
   <div class="row-fingers">{finger("amendoada","solid","#C9667A",w=72)}<div class="arrow">→</div>{finger("amendoada","solid","#C9667A",w=72)}</div>
   <figcaption>Com o crescimento, surge um espaço na cutícula e o ápice vai para a frente.</figcaption>
  </figure>
  <div class="card pad">
   <h3>Remoção segura</h3>
   <ul class="checks">
    <li>Desgaste o top e a cor com lixa ou motor em baixa rotação.</li>
    <li>Para géis removíveis, use algodão com removedor e papel alumínio por 10 a 15 min.</li>
    <li>Retire o produto amolecido com a espátula, sem raspar a unha.</li>
    <li>Nunca arranque ou descole o produto com força.</li>
    <li>Finalize com hidratação e oriente o uso de óleo de cutícula.</li>
   </ul>
  </div>
 </div>
</div>
{tip("Entregue à cliente um cartão com os cuidados em casa: usar luvas para limpeza, não usar a unha como ferramenta, aplicar óleo diariamente e não arrancar o produto.", "Pós-atendimento")}
''', num=11))

# 10 Nail art
arts = [("french","bailarina","Francesinha","Ponta branca em sorriso. Use pincel liner ou fita guia."),
        ("baby","amendoada","Baby boomer","Degradê do nude ao branco, feito com esponja ou pincel."),
        ("degrade","oval","Degradê colorido","Duas ou mais cores mescladas suavemente."),
        ("glitter","stiletto","Glitter","Pó ou gel com glitter, concentrado na ponta ou em toda a unha."),
        ("flor","oval","Pintura à mão","Flores e traços com pincel liner e gel de pintura."),
        ("marmore","squoval","Efeito mármore","Veios feitos com gel espalhado sobre base ainda úmida."),
        ("encapsulada","amendoada","Encapsulada","Pedrinhas, folhas ou flores secas presas entre camadas de gel.")]
artcards = "".join(f'<div class="scard">{finger(s, a, "#C9667A" if a!="degrade" else "#9B7BE0", 64, color2="#F7B7C5" if a=="degrade" else "#ffffff") if a!="glitter" else finger(s,a,"#4A2C3A",64)}<b>{t}</b><p>{d}</p></div>' for a, s, t, d in arts)
pages.append(page(f'''
{module_head(10, "Nail art", "A nail art é o seu diferencial criativo e o que mais aparece nas redes sociais. Domine as técnicas clássicas antes de criar as suas.")}
<div class="shapes">{artcards}</div>
<div class="two">
 <div class="card pad">
  <h3>Materiais de nail art</h3>
  <ul class="checks cols2">
   <li>Pincel liner fino</li><li>Pincel de degradê</li><li>Gel de pintura</li><li>Pó cromado e glitter</li>
   <li>Pedrarias e strass</li><li>Carimbo (stamping)</li><li>Adesivos e películas</li><li>Esponja de maquiagem</li>
  </ul>
 </div>
 {tip("Monte uma cartela com 10 a 20 artes que você faz com perfeição e preço definido. Assim a cliente escolhe rápido e o seu tempo fica previsível.", "Cardápio de artes")}
</div>
''', num=12))

# 11 Problemas
pages.append(page(f'''
{module_head(11, "Problemas e contraindicações", "O nail designer não diagnostica nem trata doenças. Mas precisa reconhecer sinais de alerta para proteger a cliente e encaminhá-la a um médico.")}
<table class="tbl">
 <tr><th>Sinal observado</th><th>Possível causa</th><th>Conduta</th></tr>
 <tr><td>Unha amarelada, espessa ou quebradiça</td><td>Micose (onicomicose)</td><td><b>Não atender.</b> Orientar a procurar dermatologista.</td></tr>
 <tr><td>Vermelhidão, inchaço ou pus ao redor</td><td>Inflamação ou infecção (paroníquia)</td><td><b>Não atender.</b> Encaminhar ao médico.</td></tr>
 <tr><td>Coceira, bolhas ou vermelhidão após o gel</td><td>Alergia aos produtos (dermatite de contato)</td><td>Suspender o uso, remover com cuidado e encaminhar ao médico.</td></tr>
 <tr><td>Manchas esverdeadas sob o produto</td><td>Infiltração com contaminação por bactéria</td><td>Remover todo o produto e não reaplicar até a avaliação médica.</td></tr>
 <tr><td>Lâmina descolada do leito</td><td>Trauma ou excesso de lixamento (onicólise)</td><td>Não cobrir com produto; recomendar avaliação médica.</td></tr>
 <tr><td>Unha fina e sensível</td><td>Lixamento excessivo ou remoção forçada</td><td>Pausa nos alongamentos e hidratação; rever sua técnica.</td></tr>
</table>
<div class="two">
 {warn("Clientes diabéticas, gestantes, em quimioterapia ou com problemas de circulação exigem cuidado redobrado. Na dúvida, peça uma liberação do médico da cliente antes de atender.")}
 {tip("Mantenha uma ficha de anamnese assinada para cada cliente, com alergias e observações. Ela protege você e melhora o atendimento.", "Ficha de anamnese")}
</div>
<div class="card pad">
 <h3>Ficha de anamnese: itens mínimos</h3>
 <ul class="checks cols3">
  <li>Nome e contato</li><li>Alergias conhecidas</li><li>Uso de medicamentos</li>
  <li>Diabetes ou problemas de circulação</li><li>Gestação</li><li>Histórico de micose</li>
  <li>Reações a serviços anteriores</li><li>Profissão e rotina</li><li>Assinatura da cliente</li>
 </ul>
</div>
''', num=13))

# 12 Negócio
pages.append(page(f'''
{module_head(12, "Seu negócio", "Técnica atrai a primeira visita. Atendimento, organização e preço justo fazem a cliente voltar e indicar você.")}
<div class="two">
 <div class="card pad">
  <h3>{icon("moeda",34)} Como calcular o seu preço</h3>
  <p class="small">Preço = custo de material + custo do seu tempo + parcela dos custos fixos + lucro.</p>
  <table class="tbl small">
   <tr><th>Exemplo: alongamento em gel</th><th>Valor</th></tr>
   <tr><td>Material usado (gel, lixas, luvas, etc.)</td><td>R$ 18,00</td></tr>
   <tr><td>Custos fixos por hora (aluguel, luz, internet) × 2 h</td><td>R$ 30,00</td></tr>
   <tr><td>Seu pró-labore por hora × 2 h</td><td>R$ 60,00</td></tr>
   <tr><td>Subtotal</td><td>R$ 108,00</td></tr>
   <tr><td>Margem de lucro (30%)</td><td>R$ 32,40</td></tr>
   <tr class="total"><td>Preço sugerido</td><td>R$ 140,00</td></tr>
  </table>
  <p class="small muted">Valores apenas ilustrativos. Pesquise a média da sua região e calcule com os seus custos reais.</p>
 </div>
 <div class="biz">
  <div class="icard">{icon("foto",52)}<div><b>Portfólio</b><p>Fotografe com luz natural, fundo neutro e mãos hidratadas.</p></div></div>
  <div class="icard">{icon("celular",52)}<div><b>Redes sociais</b><p>Poste com frequência: antes e depois, vídeos curtos e bastidores.</p></div></div>
  <div class="icard">{icon("agenda",52)}<div><b>Agenda organizada</b><p>Use agendamento online e confirme na véspera para reduzir faltas.</p></div></div>
  <div class="icard">{icon("estrela",52)}<div><b>Fidelização</b><p>Lembre a cliente da manutenção e ofereça vantagens por indicação.</p></div></div>
 </div>
</div>
{tip("Formalize-se: como MEI você pode emitir nota fiscal, contribuir para a aposentadoria e ter mais credibilidade. Verifique as atividades permitidas e as regras atuais no Portal do Empreendedor.", "Formalização")}
''', num=14))

# Exercícios + certificado
pages.append(page(f'''
<div class="mhead"><div class="mnum">Prática</div><h1>Exercícios e plano de treino</h1>
<p class="lead">A prática constante é o que transforma conhecimento em habilidade. Siga este plano de quatro semanas e marque cada etapa concluída.</p></div>
<div class="grid4 plan">
 <div class="card pad"><div class="wk">Semana 1</div><ul class="checks"><li>Montar e organizar o kit</li><li>Treinar os 7 formatos em tips</li><li>Praticar o ciclo de esterilização</li></ul></div>
 <div class="card pad"><div class="wk">Semana 2</div><ul class="checks"><li>Cutilagem em 5 pessoas</li><li>10 esmaltações em gel</li><li>Cronometrar o tempo</li></ul></div>
 <div class="card pad"><div class="wk">Semana 3</div><ul class="checks"><li>10 alongamentos com tips</li><li>5 alongamentos no molde</li><li>Avaliar o ápice de perfil</li></ul></div>
 <div class="card pad"><div class="wk">Semana 4</div><ul class="checks"><li>Francesinha e baby boomer</li><li>Montar a cartela de artes</li><li>Fotografar o portfólio</li></ul></div>
</div>
<div class="card pad quiz">
 <h3>Teste seus conhecimentos</h3>
 <ol>
  <li>Qual parte da unha não pode ser lesionada, porque pode deformar a unha para sempre?</li>
  <li>Qual é o equipamento indicado para esterilizar alicates?</li>
  <li>Por que o gel não deve encostar na cutícula?</li>
  <li>Onde fica o ápice de um alongamento bem estruturado?</li>
  <li>Qual deve ser a conduta diante de uma unha com sinais de micose?</li>
  <li>Quais itens compõem o cálculo do preço de um serviço?</li>
 </ol>
 <p class="small muted">Respostas: 1. Matriz · 2. Autoclave · 3. Causa descolamento e aumenta o risco de alergia · 4. Na região do ponto de tensão, próximo ao centro da unha · 5. Não atender e orientar a procurar um dermatologista · 6. Material, tempo, custos fixos e lucro.</p>
</div>
<div class="cert">
 <div class="cert-in">
  <div class="mnum">Certificado de conclusão</div>
  <p>Certificamos que</p>
  <div class="line"></div>
  <p>concluiu o <b>Curso de Nail Designer</b>, com os 12 módulos desta apostila.</p>
  <div class="sig"><div><div class="line s"></div>Instrutora</div><div><div class="line s"></div>Data</div></div>
 </div>
</div>
''', num=15))

CSS = '''
@page { size: A4; margin: 0; }
:root { --rose:#C9667A; --plum:#4A2C3A; --nude:#F6E7E4; --gold:#C9A26A; --ink:#3A2A31; --soft:#FBF5F3; }
* { box-sizing: border-box; }
html, body { margin:0; padding:0; background:#fff; }
body { font-family: 'Inter', sans-serif; color: var(--ink); font-size: 10.2pt; line-height: 1.45; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.page { width:210mm; height:297mm; padding:16mm 15mm 18mm; position:relative; overflow:hidden; page-break-after:always; background: var(--soft); }
.page:last-child { page-break-after:auto; }
h1,h2,h3 { font-family:'Playfair Display', serif; color: var(--plum); margin:0; }
h1 { font-size: 27pt; line-height:1.1; margin: 2mm 0 3mm; }
h3 { font-size: 13pt; margin: 0 0 2.5mm; display:flex; align-items:center; gap:6px; }
p { margin: 0 0 2mm; }
.mhead { margin-bottom: 6mm; border-bottom: 1.5px solid #E9C9C1; padding-bottom: 4mm; }
.mnum { font-size: 8.5pt; letter-spacing: .18em; text-transform: uppercase; color: var(--rose); font-weight: 700; }
.lead { font-size: 11pt; color:#5C4650; max-width: 165mm; }
.foot { position:absolute; bottom:8mm; left:15mm; right:15mm; display:flex; justify-content:space-between; font-size:8pt; color:#A88C94; border-top:1px solid #EBD7D2; padding-top:2mm; }
.two { display:grid; grid-template-columns: 1fr 1fr; gap: 5mm; margin-bottom: 5mm; align-items:start; }
.two.wide-left { grid-template-columns: 1.15fr 1fr; }
.card { background:#fff; border-radius: 4mm; box-shadow: 0 1px 0 #EBD7D2, 0 4px 14px rgba(74,44,58,.06); margin:0 0 4mm; }
.card.pad { padding: 5mm; }
.card.center { text-align:center; padding: 4mm; }
figure { margin:0; padding: 3mm; }
figcaption, .cap { font-size: 8.5pt; color:#8E737B; text-align:center; margin-top:1mm; }
.tip { background: #fff; border-left: 4px solid var(--gold); border-radius: 0 3mm 3mm 0; padding: 3.5mm 4.5mm; margin-bottom: 4mm; }
.tip .tiph { font-size: 8pt; font-weight: 800; letter-spacing: .12em; text-transform: uppercase; color: #A07C3F; margin-bottom: 1mm; }
.tip p { margin:0; font-size: 9.6pt; }
.tip.warn { border-left-color: var(--rose); background:#FDF0F2; }
.tip.warn .tiph { color: var(--rose); }
.tbl { width:100%; border-collapse: separate; border-spacing:0; background:#fff; border-radius:3mm; overflow:hidden; margin-bottom:5mm; font-size:9.2pt; }
.tbl th { background: var(--plum); color:#fff; text-align:left; padding: 2.4mm 3mm; font-weight:600; }
.tbl td { padding: 2.2mm 3mm; border-bottom: 1px solid #F1E2DE; vertical-align:top; }
.tbl tr:last-child td { border-bottom:0; }
.tbl td:first-child { font-weight:600; color: var(--plum); }
.tbl.small { font-size: 8.8pt; margin-bottom:2mm; }
.tbl.small td:last-child { white-space:nowrap; }
.tbl tr.total td { background: var(--nude); font-weight:800; color: var(--rose); }
.small { font-size: 8.8pt; } .muted { color:#9A8189; }
.steps { list-style:none; counter-reset: s; padding:0; margin:0 0 4mm; }
.steps li { counter-increment: s; position:relative; padding: 0 0 3mm 11mm; }
.steps li::before { content: counter(s); position:absolute; left:0; top:0; width:7.5mm; height:7.5mm; border-radius:50%; background: var(--rose); color:#fff; font-weight:700; font-size:9pt; display:flex; align-items:center; justify-content:center; }
.steps li:not(:last-child)::after { content:""; position:absolute; left:3.6mm; top:8mm; bottom:0; width:1px; background:#E9C9C1; }
.steps b { display:block; color: var(--plum); font-size: 10pt; }
.steps span { font-size: 9.3pt; color:#5C4650; }
.checks { list-style:none; padding:0; margin:0; }
.checks li { position:relative; padding-left: 6mm; margin-bottom: 1.6mm; font-size: 9.4pt; }
.checks li::before { content:""; position:absolute; left:0; top:1.3mm; width:3mm; height:3mm; border:1.5px solid var(--rose); border-radius:1mm; }
.checks.cols2 { columns:2; column-gap: 5mm; } .checks.cols3 { columns:3; column-gap: 4mm; }
.finger { display:inline-flex; flex-direction:column; align-items:center; }
.finger svg { display:block; }
.nlabel { font-size: 8pt; }
.cover-page { background: linear-gradient(160deg, #F8E9E6 0%, #F1D3D0 55%, #E6B8BC 100%); padding:0; }
.cover { height:100%; padding: 20mm 18mm; display:flex; flex-direction:column; }
.pill { display:inline-block; background: var(--plum); color:#fff; padding: 2mm 4mm; border-radius: 10mm; font-size: 9pt; letter-spacing:.08em; }
.ctitle { font-size: 54pt; line-height: 1.0; margin: 18mm 0 6mm; }
.ctitle em { color: var(--rose); font-style: italic; }
.csub { font-size: 13pt; max-width: 140mm; color:#5C4650; }
.cover-hand { margin-top:auto; display:flex; justify-content:center; align-items:flex-end; gap: 4mm; }
.cover-hand .finger:nth-child(1) { transform: translateY(14mm) rotate(-8deg); }
.cover-hand .finger:nth-child(2) { transform: translateY(2mm) rotate(-3deg); }
.cover-hand .finger:nth-child(4) { transform: translateY(2mm) rotate(3deg); }
.cover-hand .finger:nth-child(5) { transform: translateY(14mm) rotate(8deg); }
.cover-bottom { display:flex; justify-content:space-between; border-top:1px solid rgba(74,44,58,.25); padding-top:4mm; margin-top: 4mm; font-size:9pt; letter-spacing:.12em; text-transform:uppercase; color: var(--plum); position:relative; z-index:2; background: transparent; }
.cover-hand { height: 95mm; overflow:hidden; }
.toc-row { display:flex; align-items:center; gap: 3mm; padding: 1.8mm 0; border-bottom: 1px dashed #E3C9C3; }
.toc-n { font-family:'Playfair Display', serif; color: var(--rose); font-size: 13pt; width: 9mm; }
.toc-t { flex:1; font-weight:600; color: var(--plum); font-size:9.6pt; }
.toc-t small { display:block; font-weight:400; color:#9A8189; font-size: 8pt; }
.toc-p { font-size:9pt; color:#9A8189; }
.stack-fingers, .row-fingers { display:flex; justify-content:center; align-items:flex-end; gap: 5mm; margin: 6mm 0 1mm; }
.row-fingers { margin: 2mm 0 2mm; }
.arrow { font-size: 22pt; color: var(--rose); align-self:center; }
.grid3 { display:grid; grid-template-columns: repeat(3,1fr); gap: 4mm; margin-bottom: 6mm; }
.grid4 { display:grid; grid-template-columns: repeat(4,1fr); gap: 4mm; margin-bottom: 5mm; }
.grid5 { display:grid; grid-template-columns: repeat(5,1fr); gap: 3mm; margin-bottom: 5mm; }
.icard { display:flex; gap: 3mm; align-items:center; background:#fff; border-radius:3.5mm; padding: 3.5mm; box-shadow: 0 1px 0 #EBD7D2; }
.icard svg { flex: 0 0 auto; background: var(--nude); border-radius: 50%; padding: 2mm; }
.icard b { color: var(--plum); font-size: 10pt; } .icard p { margin: .5mm 0 0; font-size: 8.8pt; color:#5C4650; }
.biz { display:flex; flex-direction:column; gap: 3mm; }
.tcard, .acard, .scard { background:#fff; border-radius:3.5mm; padding: 3mm; text-align:center; box-shadow: 0 1px 0 #EBD7D2; }
.tcard svg, .acard svg { background: var(--nude); border-radius: 50%; padding: 2mm; margin-bottom: 1.5mm; }
.tcard b, .acard b, .scard b { display:block; color: var(--plum); font-size: 9.6pt; margin-bottom: .8mm; }
.tcard p, .acard p, .scard p { font-size: 8.2pt; color:#5C4650; margin:0; line-height:1.35; }
.shapes { display:grid; grid-template-columns: repeat(4,1fr); gap: 3.5mm; margin-bottom: 5mm; }
.scard { padding: 3mm 3mm 3.5mm; }
.flow { display:flex; align-items:stretch; gap: 1.5mm; margin-bottom: 6mm; }
.fstep { flex:1; background:#fff; border-radius:3mm; padding: 3mm; font-weight:700; color: var(--plum); font-size: 9.5pt; text-align:center; box-shadow: 0 1px 0 #EBD7D2; }
.fstep span { display:flex; width:7mm; height:7mm; margin: 0 auto 1.5mm; border-radius:50%; background: var(--rose); color:#fff; align-items:center; justify-content:center; font-size:9pt; }
.fstep small { display:block; font-weight:400; font-size: 8pt; color:#5C4650; margin-top:1mm; }
.farrow { align-self:center; color: var(--rose); font-size: 14pt; }
.gelrow { display:flex; justify-content:space-around; padding: 4mm; margin-bottom: 5mm; }
.gstep { display:flex; flex-direction:column; align-items:center; gap: 1.5mm; font-size: 8.8pt; font-weight:600; color: var(--plum); }
.wk { font-family:'Playfair Display', serif; font-size: 13pt; color: var(--rose); margin-bottom: 2mm; }
.plan .card { margin:0; }
.quiz ol { margin: 0 0 3mm; padding-left: 5mm; font-size: 9.5pt; } .quiz li { margin-bottom: 1.2mm; }
.cert { background: var(--plum); border-radius: 4mm; padding: 3mm; color:#fff; }
.cert-in { border: 1px solid var(--gold); border-radius: 3mm; padding: 5mm 8mm; text-align:center; }
.cert .mnum { color: var(--gold); font-size: 10pt; margin-bottom: 2mm; }
.cert p { margin: 1mm 0; font-size: 9.8pt; }
.cert .line { height: 1px; background: var(--gold); margin: 6mm 20mm 2mm; }
.cert .sig { display:flex; justify-content:space-around; font-size: 8.5pt; color:#E8D5DB; margin-top: 3mm; }
.cert .sig > div { width: 55mm; } .cert .line.s { margin: 6mm 0 1.5mm; }
'''

html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Curso de Nail Designer</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>{"".join(pages)}</body></html>'''

(OUT / "build").mkdir(exist_ok=True)
(OUT / "build" / "curso-nail-designer.html").write_text(html, encoding="utf-8")
print("HTML ok,", len(pages), "páginas")
