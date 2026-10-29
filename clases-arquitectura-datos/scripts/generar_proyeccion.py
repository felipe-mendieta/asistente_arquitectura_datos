#!/usr/bin/env python3
"""
Convierte una guía de clase (Markdown) en un HTML de "modo proyección" para usar
en el aula: una lámina por bloque, diagramas Mermaid renderizados, riel de agenda
proporcional a los minutos y cronómetro por bloque. Las notas del docente quedan
ocultas hasta que se activan.

Uso:
    python scripts/generar_proyeccion.py guia.md                # crea guia_proyeccion.html
    python scripts/generar_proyeccion.py guia.md -o clase.html

El HTML resultante es un solo archivo; carga marked y mermaid desde cdn.jsdelivr.net
y las fuentes desde Google Fonts, así que necesita internet al abrirse.
Solo usa la biblioteca estándar de Python.
"""

import argparse
import html
import json
import re
from pathlib import Path

PLANTILLA = Path(__file__).resolve().parent.parent / "assets" / "plantilla_proyeccion.html"


def generar(md: str) -> str:
    titulo = re.search(r"^#\s+(.+)$", md, flags=re.M)
    titulo = titulo.group(1).strip() if titulo else "Clase de Arquitectura de Datos"
    # json.dumps produce un literal JS válido; escapar "</" evita cerrar el <script> antes de tiempo.
    guia_json = json.dumps(md, ensure_ascii=False).replace("</", "<\\/")
    plantilla = PLANTILLA.read_text(encoding="utf-8")
    return plantilla.replace("__TITULO__", html.escape(titulo)).replace("__GUIA_JSON__", guia_json)


def main():
    ap = argparse.ArgumentParser(description="Genera el modo proyección de una guía de clase.")
    ap.add_argument("guia", help="Ruta al Markdown de la guía")
    ap.add_argument("-o", "--salida", help="Ruta del HTML de salida")
    args = ap.parse_args()

    origen = Path(args.guia)
    destino = Path(args.salida) if args.salida else origen.with_name(origen.stem + "_proyeccion.html")
    destino.write_text(generar(origen.read_text(encoding="utf-8")), encoding="utf-8")
    print(f"Modo proyección creado: {destino}")


if __name__ == "__main__":
    main()
