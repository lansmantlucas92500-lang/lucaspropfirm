#!/usr/bin/env python3
"""Peuple le lien bio Metricool (Linkin Bio Service) de la marque LucasPropfirm.

API officielle : https://app.metricool.com/api  (Swagger : /api/swagger.json)
Auth : header X-Mc-Auth = userToken (Compte > Paramètres > API, plan Advanced/Custom)
       + userId et blogId en paramètres de requête.

Usage :
  METRICOOL_TOKEN=xxx python3 metricool_bio_buttons.py check   # lecture seule : boutons actuels
  METRICOOL_TOKEN=xxx python3 metricool_bio_buttons.py apply   # ajoute les boutons manquants, dans l'ordre
  METRICOOL_TOKEN=xxx python3 metricool_bio_buttons.py apply --reset   # supprime tout puis recrée

Le token n'est jamais écrit sur disque ni loggé.
"""
from __future__ import annotations

import json
import os
import sys
import urllib.parse
import urllib.request

BASE = "https://app.metricool.com/api"
USER_ID = "5200334"      # lansmantlucas92500@gmail.com (getBrandSettings)
BLOG_ID = "6758811"      # marque LucasPropfirm

GOLD = "#FFD700"

# Ordre = ordre d'affichage. (texte, lien, couleur ou None)
BUTTONS: list[tuple[str, str, str | None]] = [
    ("🔑 Code LUCAS → jusqu'à -80 % chez Phidias", "https://phidiaspropfirm.com", GOLD),
    ("📌 Discord & formation", "https://lucaspropfirm.fr", GOLD),
    ("📒 Journal de trading PropLog", "https://www.proplog.fr/", None),
    ("📰 Newsletter lucaspropfirm", "https://lucaspropfirm.fr/newsletters.html", None),
    ("📰 Newsletter Proplog", "https://proplog.fr/newsletter/", None),
    ("🤝 Programme d'affiliation", "https://lucaspropfirm.fr/Affiliation.html", None),
    ("🎬 Higgsfield — génération vidéo IA", "https://higgsfield.ai?fpr=lucas17", None),
    ("🎁 Limova — code PROFILM30",
     "https://limova.ai/?linkId=lp_079563&sourceId=lucas-lansmant&tenantId=limova", None),
    ("🤖 Wisewand.ai — code LUCAS10 (-10 %)", "https://wisewand.ai/?fpr=lucas", None),
    ("🤖 Wisewand.ai (EN) — code LUCAS10 (-10 %)", "https://wisewand.ai/en/?fpr=lucas", None),
]


def token() -> str:
    t = os.environ.get("METRICOOL_TOKEN", "").strip()
    if not t:
        sys.exit("METRICOOL_TOKEN manquant (Compte > Paramètres > API).")
    return t


def call(method: str, path: str, **params: str | None):
    q = {"userId": USER_ID, "blogId": BLOG_ID, "blogid": BLOG_ID}
    q.update({k: v for k, v in params.items() if v is not None})
    url = f"{BASE}{path}?{urllib.parse.urlencode(q)}"
    req = urllib.request.Request(url, method=method, headers={
        "X-Mc-Auth": token(), "Accept": "application/json",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            raw = r.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")[:500]
        sys.exit(f"HTTP {e.code} sur {method} {path} : {body}")
    try:
        return json.loads(raw) if raw else []
    except json.JSONDecodeError:
        return raw


def norm(u: str) -> str:
    return u.strip().rstrip("/").lower()


def current() -> list[dict]:
    data = call("GET", "/linkinbio/instagram/getbioButtons")
    return data if isinstance(data, list) else []


def show(items: list[dict]) -> None:
    if not items:
        print("(aucun bouton)")
        return
    for i, it in enumerate(items, 1):
        print(f"{i:2d}. id={it.get('id') or it.get('itemid')} | {it.get('text') or it.get('textbutton')} → {it.get('link') or it.get('linkbutton')}")


def cmd_check() -> None:
    items = current()
    print(f"Boutons actuels du bio link (blogId {BLOG_ID}) :")
    show(items)
    print("\nRéponse brute (1er élément) :")
    print(json.dumps(items[0], indent=2, ensure_ascii=False) if items else "[]")


def cmd_apply(reset: bool) -> None:
    items = current()
    if reset and items:
        for it in items:
            iid = it.get("id") or it.get("itemid")
            call("DELETE", "/linkinbio/instagram/deletecatalogitem", itemid=str(iid))
            print(f"supprimé id={iid}")
        items = []
    existing = {norm(it.get("link") or it.get("linkbutton") or ""): it for it in items}
    for pos, (text, link, color) in enumerate(BUTTONS):
        if norm(link) in existing:
            print(f"déjà présent : {text}")
            continue
        call("GET", "/linkinbio/instagram/addcatalogButton",
             textbutton=text, linkbutton=link, positionbutton=str(pos), colorbutton=color)
        print(f"ajouté [{pos}] {text}")
    print("\nÉtat final :")
    show(current())


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] not in {"check", "apply"}:
        sys.exit(__doc__)
    if args[0] == "check":
        cmd_check()
    else:
        cmd_apply(reset="--reset" in args)
