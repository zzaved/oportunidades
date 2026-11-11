# Oportunidades do Daily Pull Request

Página com as oportunidades postadas no Instagram [@dailypullrequest](https://www.instagram.com/dailypullrequest/) que ainda estão com inscrição aberta. É o link que vai na resposta automática do "comenta QUERO".

## Como atualizar

1. Edite `dados/oportunidades.json`:
   - `abertas`: inscrição aberta agora, com `prazo` (AAAA-MM-DD), `prazo_texto`, `pra_quem`, `valor`, `link` oficial, `posts` (onde apareceu) e `conferido_em`.
   - `no_radar`: abre em breve (sem prazo ainda).
   - Atualize `atualizado_em`.
2. Rode `python3 build.py` (gera `index.html`).
3. Commit e push na `main`: o GitHub Pages publica sozinho.

Toda semana: abrir o link oficial de cada item, tirar o que fechou, mover do radar pra `abertas` o que abriu e acrescentar as oportunidades novas que foram postadas. A página também esconde sozinha, no navegador, o que passou do prazo.
