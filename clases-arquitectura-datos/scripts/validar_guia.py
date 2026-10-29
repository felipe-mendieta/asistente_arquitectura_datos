#!/usr/bin/env python3
"""
Valida que una guía de clase en Markdown cumpla la estructura de la skill
clases-arquitectura-datos.

Uso:
    python scripts/validar_guia.py ruta/a/guia.md
    python scripts/validar_guia.py ruta/a/guia.md --json

Código de salida: 0 si no hay errores (puede haber avisos), 1 si hay errores.
Solo usa la biblioteca estándar de Python.
"""

import argparse
import json
import re
import sys
import unicodedata

DURACION_OBJETIVO = 90

# Secciones obligatorias: (nombre legible, palabras clave que deben aparecer en un encabezado)
SECCIONES = [
    ("Ficha de la clase", ["ficha"]),
    ("Objetivos de aprendizaje", ["objetivos"]),
    ("Agenda", ["agenda"]),
    ("Apertura: el problema", ["apertura"]),
    ("Construyendo la intuición", ["intuicion"]),
    ("El concepto en profundidad", ["profundidad"]),
    ("Práctica activa", ["practica"]),
    ("Errores comunes", ["errores"]),
    ("Cierre y verificación", ["cierre"]),
    ("Notas para el docente", ["notas", "docente"]),
    ("Para profundizar", ["profundizar"]),
]

VERBOS_VAGOS = ["conocer", "entender", "comprender", "saber", "aprender", "familiarizarse"]


def normalizar(texto: str) -> str:
    """Minúsculas y sin tildes, para comparar con tolerancia."""
    texto = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


def quitar_bloques_codigo(md: str) -> str:
    return re.sub(r"```.*?```", "", md, flags=re.S)


def encabezados(md: str):
    """Devuelve [(nivel, texto, posición)] ignorando lo que esté dentro de bloques de código."""
    limpio = quitar_bloques_codigo(md)
    return [(len(m.group(1)), m.group(2).strip(), m.start())
            for m in re.finditer(r"^(#{1,6})\s+(.+)$", limpio, flags=re.M)]


def seccion(md: str, palabra: str) -> str:
    """Texto de la primera sección H2 cuyo título contiene la palabra clave."""
    limpio = quitar_bloques_codigo(md)
    partes = re.split(r"^##\s+", limpio, flags=re.M)
    for p in partes[1:]:
        titulo = p.split("\n", 1)[0]
        if palabra in normalizar(titulo):
            return p
    return ""


def validar(md: str) -> dict:
    errores, avisos, ok = [], [], []
    heads = encabezados(md)
    titulos_norm = [normalizar(t) for _, t, _ in heads]

    # 1. Título H1
    if any(n == 1 for n, _, _ in heads):
        ok.append("Tiene título principal (H1).")
    else:
        errores.append("Falta el título principal (una línea que empiece con '# ').")

    # 2. Secciones obligatorias
    faltantes = [nombre for nombre, claves in SECCIONES
                 if not any(all(k in t for k in claves) for t in titulos_norm)]
    if faltantes:
        errores.append("Faltan secciones: " + ", ".join(faltantes) + ".")
    else:
        ok.append(f"Están las {len(SECCIONES)} secciones obligatorias.")

    # 3. Tiempos de los bloques numerados suman 90
    bloques = []
    for _, t, _ in heads:
        m = re.match(r"^(\d+)\.\s.*\((\d+)\s*min", t)
        if m:
            bloques.append((t, int(m.group(2))))
    total = sum(m for _, m in bloques)
    if not bloques:
        errores.append("Ningún bloque numerado indica su duración, p. ej. '## 1. Apertura: el problema (10 min)'.")
    elif total != DURACION_OBJETIVO:
        errores.append(f"Los bloques suman {total} min; deberían sumar {DURACION_OBJETIVO}.")
    else:
        ok.append(f"Los {len(bloques)} bloques suman {DURACION_OBJETIVO} min.")

    # 4. Elementos visuales: diagramas Mermaid + tablas (sin contar Ficha y Agenda)
    mermaid = re.findall(r"```mermaid\s*\n(.*?)```", md, flags=re.S)
    cuerpo = quitar_bloques_codigo(md)
    for clave in ("ficha", "agenda"):
        cuerpo = cuerpo.replace(seccion(md, clave), "")
    tablas = len(re.findall(r"^\|?\s*:?-{3,}:?\s*\|", cuerpo, flags=re.M))
    visuales = len(mermaid) + tablas
    if visuales < 3:
        errores.append(f"Solo hay {visuales} elementos visuales (diagramas + tablas); se esperan entre 3 y 5.")
    elif visuales > 6:
        avisos.append(f"Hay {visuales} elementos visuales; más de 5 puede saturar una clase de 90 min.")
    else:
        ok.append(f"{visuales} elementos visuales ({len(mermaid)} diagramas, {tablas} tablas).")
    if not mermaid:
        avisos.append("No hay ningún diagrama Mermaid; los conceptos con flujo o capas se entienden mejor con uno.")

    # 5. Diagramas demasiado grandes
    for i, d in enumerate(mermaid, 1):
        nodos = set(re.findall(r"(?:^|[\s;>-])([A-Za-z_][\w]*)\s*[\[\(\{]", d))
        if len(nodos) > 12:
            avisos.append(f"El diagrama {i} tiene unos {len(nodos)} nodos; conviene dividirlo (máximo ~12).")

    # 6. Objetivos: cantidad y verbos observables
    obj = seccion(md, "objetivos")
    items = [l.strip() for l in obj.splitlines() if re.match(r"^\s*(?:[-*]|\d+\.)\s+", l)]
    if obj:
        if not 3 <= len(items) <= 4:
            avisos.append(f"Hay {len(items)} objetivos de aprendizaje; se recomiendan entre 3 y 4.")
        else:
            ok.append(f"{len(items)} objetivos de aprendizaje.")
        vagos = [v for v in VERBOS_VAGOS
                 if any(re.search(rf"\b{v}\b", normalizar(i)) for i in items)]
        if vagos:
            avisos.append("Objetivos con verbos no observables: " + ", ".join(vagos)
                          + ". Prefiere explicar, comparar, diseñar, evaluar o decidir.")

    # 7. Conexión con la industria y técnica Feynman
    texto_norm = normalizar(md)
    if "en la industria" in texto_norm:
        ok.append("Incluye la nota 'En la industria'.")
    else:
        errores.append("Falta la nota 'En la industria' que conecta el concepto con casos reales.")
    if "feynman" in texto_norm:
        ok.append("Incluye la ronda Feynman.")
    else:
        avisos.append("No se menciona la ronda Feynman en el cierre.")

    # 8. Solución de referencia para el ejercicio
    if "solucion" in normalizar(seccion(md, "practica")):
        ok.append("El ejercicio incluye solución de referencia.")
    else:
        avisos.append("La práctica activa no parece incluir una solución de referencia para el docente.")

    return {"valida": not errores, "errores": errores, "avisos": avisos, "correcto": ok,
            "bloques": [{"titulo": t, "minutos": m} for t, m in bloques]}


def main():
    ap = argparse.ArgumentParser(description="Valida una guía de clase de Arquitectura de Datos.")
    ap.add_argument("guia", help="Ruta al archivo Markdown de la guía")
    ap.add_argument("--json", action="store_true", help="Salida en JSON")
    args = ap.parse_args()

    with open(args.guia, encoding="utf-8") as f:
        resultado = validar(f.read())

    if args.json:
        print(json.dumps(resultado, ensure_ascii=False, indent=2))
    else:
        for linea in resultado["correcto"]:
            print("  OK     " + linea)
        for linea in resultado["avisos"]:
            print("  AVISO  " + linea)
        for linea in resultado["errores"]:
            print("  ERROR  " + linea)
        estado = "VÁLIDA" if resultado["valida"] else "CON ERRORES"
        print(f"\nGuía {estado}: {len(resultado['errores'])} errores, {len(resultado['avisos'])} avisos.")
    sys.exit(0 if resultado["valida"] else 1)


if __name__ == "__main__":
    main()
