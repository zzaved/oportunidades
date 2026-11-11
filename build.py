"""Gera index.html a partir de dados/oportunidades.json.
Uso: python3 build.py
A página esconde sozinha (no navegador) o que passou do prazo, mas a fonte da verdade é o JSON:
toda semana confira cada link oficial, tire o que fechou e acrescente o que foi postado."""
import html
import json
from datetime import date
from pathlib import Path

AQUI = Path(__file__).resolve().parent
D = json.loads((AQUI / "dados" / "oportunidades.json").read_text(encoding="utf-8"))
e = lambda s: html.escape(str(s), quote=True)


def data_br(iso):
    y, m, d = iso.split("-")
    return f"{d}/{m}/{y}"


def card(o):
    tags = "".join(f'<span class="tag">{e(p)}</span>' for p in o.get("posts", []))
    return f"""
    <article class="card" data-prazo="{e(o['prazo'])}">
      <div class="topo">{tags}<span class="falta" aria-live="polite"></span></div>
      <h2>{e(o['nome'])}</h2>
      <p class="chamada">{e(o['chamada'])}</p>
      <dl>
        <dt>Pra quem</dt><dd>{e(o['pra_quem'])}</dd>
        <dt>O que ganha</dt><dd>{e(o['valor'])}</dd>
        <dt>Prazo</dt><dd><strong>{e(o['prazo_texto'])}</strong></dd>
      </dl>
      <a class="botao" href="{e(o['link'])}" target="_blank" rel="noopener">Ver no site oficial</a>
      <p class="conf">Conferido no site oficial em {e(data_br(o['conferido_em']))}</p>
    </article>"""


def radar(o):
    tags = "".join(f'<span class="tag">{e(p)}</span>' for p in o.get("posts", []))
    return f"""
    <li><div>{tags}<strong>{e(o['nome'])}</strong><span>{e(o['chamada'])}</span></div>
      <a href="{e(o['link'])}" target="_blank" rel="noopener">site oficial</a></li>"""


abertas = sorted(D["abertas"], key=lambda o: o["prazo"])
pagina = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Oportunidades do Daily Pull Request</title>
<meta name="description" content="Bolsas, estágios, competições e cursos com inscrição aberta, conferidos no site oficial toda semana pelo @dailypullrequest.">
<meta property="og:title" content="Oportunidades do Daily Pull Request">
<meta property="og:description" content="Só o que está com inscrição aberta, conferido no site oficial toda semana.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Silkscreen&family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
<style>
  :root {{ --fundo:#0B0E24; --card:#141A3D; --linha:#2A3366; --lima:#C8FF2E; --azul:#2433FF; --texto:#EEF0FF; --suave:#A9B0D6; --rosa:#FF5AB4; }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--fundo); color:var(--texto); font:16px/1.5 Inter, system-ui, sans-serif; }}
  .wrap {{ max-width:720px; margin:0 auto; padding:28px 18px 56px; }}
  header h1 {{ font-family:Silkscreen, monospace; font-weight:400; font-size:30px; line-height:1.15; margin:0 0 10px; color:var(--lima); }}
  header p {{ margin:0 0 18px; color:var(--suave); }}
  .seguir {{ display:inline-block; background:var(--azul); color:#fff; padding:12px 16px; border-radius:12px; text-decoration:none; font-weight:800; }}
  .aviso {{ margin:22px 0 8px; padding:12px 14px; border:2px dashed var(--linha); border-radius:12px; color:var(--suave); font-size:14px; }}
  h3 {{ font-family:Silkscreen, monospace; font-weight:400; font-size:18px; margin:34px 0 12px; color:var(--texto); }}
  .card {{ background:var(--card); border:2px solid var(--linha); border-radius:16px; padding:18px; margin:14px 0; }}
  .card.acaba {{ border-color:var(--rosa); }}
  .topo {{ display:flex; flex-wrap:wrap; gap:6px; align-items:center; }}
  .tag {{ background:#222a5c; color:var(--lima); font-size:12px; font-weight:800; padding:3px 8px; border-radius:999px; margin-right:6px; }}
  .falta {{ margin-left:auto; font-size:13px; font-weight:800; color:var(--lima); }}
  .card.acaba .falta {{ color:var(--rosa); }}
  .card h2 {{ margin:10px 0 4px; font-size:20px; }}
  .chamada {{ margin:0 0 12px; color:var(--texto); }}
  dl {{ margin:0 0 14px; display:grid; grid-template-columns:auto 1fr; gap:6px 12px; font-size:15px; }}
  dt {{ color:var(--suave); }}
  dd {{ margin:0; }}
  .botao {{ display:block; text-align:center; background:var(--lima); color:#0B0E24; padding:12px; border-radius:12px; font-weight:800; text-decoration:none; }}
  .conf {{ margin:10px 0 0; font-size:12px; color:var(--suave); }}
  ul.radar {{ list-style:none; padding:0; margin:0; }}
  ul.radar li {{ display:flex; justify-content:space-between; gap:12px; align-items:center; background:var(--card); border:2px solid var(--linha); border-radius:14px; padding:12px 14px; margin:10px 0; }}
  ul.radar li div {{ display:flex; flex-direction:column; gap:3px; }}
  ul.radar li span {{ color:var(--suave); font-size:14px; }}
  ul.radar li .tag {{ align-self:flex-start; }}
  ul.radar a {{ color:var(--lima); font-weight:800; white-space:nowrap; }}
  footer {{ margin-top:40px; color:var(--suave); font-size:13px; }}
  footer a {{ color:var(--lima); }}
</style>
</head>
<body>
<main class="wrap">
  <header>
    <h1>Oportunidades do Daily Pull Request</h1>
    <p>Só o que está com inscrição aberta. Cada uma é conferida no site oficial toda semana. O número no topo de cada card é o post onde ela apareceu.</p>
    <a class="seguir" href="https://www.instagram.com/dailypullrequest/" target="_blank" rel="noopener">Segue o @dailypullrequest pra não perder a próxima</a>
  </header>
  <p class="aviso">Antes de se inscrever, leia as regras no site oficial: prazos e valores podem mudar.</p>

  <h3>Inscrições abertas</h3>
  <section id="abertas">{''.join(card(o) for o in abertas)}
  </section>
  <p id="vazio" class="aviso" hidden>Nenhuma inscrição aberta agora. Segue o perfil que a próxima chega logo.</p>

  <h3>Abre em breve</h3>
  <ul class="radar">{''.join(radar(o) for o in D['no_radar'])}
  </ul>

  <footer>
    <p>Atualizado em {e(data_br(D['atualizado_em']))}. Achou algo errado? Manda no direct do <a href="https://www.instagram.com/dailypullrequest/" target="_blank" rel="noopener">@dailypullrequest</a>.</p>
  </footer>
</main>
<script>
  // esconde o que já fechou e mostra quantos dias faltam
  const hoje = new Date(); hoje.setHours(0, 0, 0, 0);
  let visiveis = 0;
  document.querySelectorAll('.card[data-prazo]').forEach((c) => {{
    const [y, m, d] = c.dataset.prazo.split('-').map(Number);
    const dias = Math.round((new Date(y, m - 1, d) - hoje) / 86400000);
    if (dias < 0) {{ c.remove(); return; }}
    visiveis++;
    const f = c.querySelector('.falta');
    f.textContent = dias === 0 ? 'último dia' : dias === 1 ? 'falta 1 dia' : 'faltam ' + dias + ' dias';
    if (dias <= 7) c.classList.add('acaba');
  }});
  if (!visiveis) document.getElementById('vazio').hidden = false;
</script>
</body>
</html>
"""
(AQUI / "index.html").write_text(pagina, encoding="utf-8")
print("ok", len(abertas), "abertas,", len(D["no_radar"]), "no radar")
