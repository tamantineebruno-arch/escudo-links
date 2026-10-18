#!/usr/bin/env python3
"""Adiciona/atualiza o redirecionamento de um cliente no escudo-links."""
import argparse, sys
sys.path.insert(0, '/home/hatch/workspace/custom-connectors/custom.github/bin')
from gh_api import api

OWNER, REPO = "tamantineebruno-arch", "escudo-links"

def redirect_html(destino):
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="refresh" content="0; url={destino}">
<title>Redirecionando...</title>
<script>location.replace("{destino}");</script>
</head>
<body style="font-family:sans-serif;text-align:center;padding-top:40px">
<p>Redirecionando...<br><a href="{destino}">clique aqui se nao abrir automaticamente</a></p>
</body>
</html>
"""

ap = argparse.ArgumentParser()
ap.add_argument("--slug", required=True, help="identificador do cliente (ex.: hortifruti)")
ap.add_argument("--url", required=True, help="destino final do redirecionamento")
a = ap.parse_args()

path = f"repos/{OWNER}/{REPO}/contents/{a.slug}/index.html"
content = redirect_html(a.url).encode().decode('ascii', errors='xmlcharrefreplace')
import base64
payload = {"message": f"redirect: {a.slug} -> {a.url}",
           "content": base64.b64encode(content.encode()).decode()}
try:
    cur = api("GET", f"/{path}")
    payload["sha"] = cur["sha"]
except Exception:
    pass
api("PUT", f"/{path}", payload)
print(f"OK: https://{OWNER}.github.io/{REPO}/{a.slug}/ -> {a.url}")
