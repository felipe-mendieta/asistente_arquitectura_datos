---
name: clases-arquitectura-datos
description: Diseña guías de clase de 90 minutos sobre Arquitectura de Datos para profesionales en capacitación, con enfoque pedagógico, visual (diagramas) y conceptual, conectando cada tema con su aplicación real en la industria. Úsala siempre que el usuario pida preparar, planificar, diseñar o escribir una clase, sesión, módulo, taller, lección o material didáctico sobre cualquier tema de datos —data warehouse, data lake, lakehouse, modelado dimensional, ETL/ELT, pipelines, streaming, data mesh, gobierno y calidad de datos, linaje, catálogos, orquestación, arquitecturas en la nube, etc.—, aunque no diga "arquitectura de datos" ni "skill", por ejemplo "prepárame la clase de Kimball" o "necesito explicar CDC a mi grupo".
---

# Clases de Arquitectura de Datos

Esta skill produce **guías de clase** listas para que un docente imparta una sesión de 90 minutos a profesionales en capacitación. La meta no es que el público memorice definiciones, sino que entienda *por qué* existe cada concepto, *qué problema resuelve* y *cuándo conviene (o no) usarlo* en un proyecto real.

## Público y tono

Los asistentes son profesionales que ya trabajan (analistas, desarrolladores, ingenieros, perfiles de negocio que migran a datos). Eso implica:

- Valoran el tiempo: cada sección debe justificar su lugar. Nada de relleno académico.
- Aprenden mejor anclando lo nuevo en lo que ya conocen (una hoja de Excel, una base de datos de su empresa, un reporte que tarda horas).
- Desconfían de las soluciones "mágicas": muestra siempre los *trade-offs* y los costos, no solo las ventajas.
- Tono cercano y profesional, en español, con términos técnicos en inglés cuando así se usan en la industria (por ejemplo, *pipeline*, *lakehouse*), explicándolos la primera vez.

## Principios pedagógicos

Aplica estos principios a lo largo de toda la guía, porque son los que hacen que un concepto se entienda y se recuerde:

1. **Problema antes que solución.** Abre con una situación real y dolorosa (datos duplicados, reportes que no cuadran, un pipeline que se rompe a las 3 a. m.). El concepto aparece después como respuesta a ese dolor.
2. **Analogía primero, tecnicismo después.** Introduce cada idea central con una analogía cotidiana y luego precisa dónde la analogía deja de funcionar.
3. **Técnica Feynman.** Incluye momentos donde los participantes expliquen el concepto con sus propias palabras, como si se lo contaran a un colega de otra área.
4. **Visual siempre que haya estructura.** Si un concepto tiene flujo, capas, relaciones o comparación, va con diagrama o tabla. Un buen diagrama vale más que tres párrafos.
5. **Aprendizaje activo.** Al menos un ejercicio práctico en el que los participantes diseñen, decidan o critiquen algo, no solo escuchen.
6. **Conexión con la industria.** Menciona herramientas, empresas o patrones reales (por ejemplo Snowflake, Databricks, BigQuery, dbt, Airflow, Kafka) como ejemplos de implementación, sin convertir la clase en un tutorial de producto. El concepto debe sobrevivir aunque cambie la herramienta.
7. **Verificación del aprendizaje.** Cierra con preguntas que comprueben comprensión (aplicar, comparar, decidir), no memoria.

## Estructura de la guía (90 minutos)

Usa siempre esta estructura. Los tiempos son orientativos y suman 90 minutos; ajústalos si el tema lo pide, pero muestra siempre la distribución.

```
# [Título de la clase]: [subtítulo que exprese el problema que resuelve]

## Ficha de la clase
Tabla con: tema, duración (90 min), nivel, conocimientos previos, materiales necesarios.

## Objetivos de aprendizaje
3 a 4 objetivos con verbos observables (explicar, comparar, diseñar, evaluar, decidir).
Evita "conocer" o "entender".

## Agenda
Tabla: bloque | minutos | actividad | propósito.

## 1. Apertura: el problema (10 min)
Caso o escenario realista que genere la necesidad del concepto.
Pregunta detonante para el grupo.

## 2. Construyendo la intuición (15 min)
Analogía central y sus límites.
Diagrama conceptual simple.

## 3. El concepto en profundidad (25 min)
Definición precisa, componentes, cómo funciona.
Diagramas de arquitectura o flujo.
Tabla comparativa con alternativas (cuándo sí, cuándo no, costos).
Nota "En la industria": cómo se implementa hoy, herramientas típicas, un caso real.

## 4. Práctica activa (25 min)
Ejercicio en grupos con enunciado, datos o escenario y entregable esperado.
### Solución de referencia (para el docente)
Solución completa; si hay una "pregunta trampa", explica por qué lo es.

## 5. Errores comunes y antipatrones (5 min)
3 a 5 errores frecuentes en proyectos reales y cómo evitarlos.

## 6. Cierre y verificación (10 min)
Ronda Feynman: consigna para que expliquen el concepto en 2 minutos.
3 a 5 preguntas de verificación con respuesta esperada.
Idea clave en una frase.

## Notas para el docente
Puntos donde el grupo suele confundirse, preguntas difíciles que pueden surgir
con su respuesta, y cómo adaptar si va corto o largo de tiempo.

## Para profundizar
2 a 4 recursos reconocidos (libros, documentación oficial, artículos de referencia).
```

## Elementos visuales

Los diagramas son parte central de la clase, no decoración:

- Usa **Mermaid** para diagramas de flujo, capas, arquitecturas, secuencias y modelos entidad-relación (`flowchart`, `sequenceDiagram`, `erDiagram`). Mantén cada diagrama legible: idealmente menos de 12 nodos; si hace falta más, divídelo en dos.
- Usa **tablas** para comparaciones (por ejemplo, ETL vs ELT, estrella vs copo de nieve, batch vs streaming), siempre con filas de "cuándo usarlo" y "costo o riesgo".
- Incluye entre 3 y 5 elementos visuales por clase, cada uno con una frase que diga qué debe observar el participante.

## Herramientas incluidas

La skill trae dos scripts (solo usan la biblioteca estándar de Python) que mejoran la calidad y el uso en el aula. Las rutas son relativas a la carpeta de esta skill.

**1. Validar la guía antes de entregarla.** Escribe primero la guía como Markdown en el directorio de trabajo y ejecuta:

```bash
python scripts/validar_guia.py guia.md
```

Comprueba las secciones obligatorias, que los bloques sumen 90 minutos, la cantidad de diagramas y tablas, el tamaño de los diagramas, los verbos de los objetivos, la nota "En la industria", la ronda Feynman y la solución de referencia. Corrige todos los errores y los avisos razonables antes de entregar; así cada guía sale con la misma calidad aunque el tema cambie.

**2. Modo proyección para el aula.** Si el usuario va a proyectar la clase, quiere "diapositivas", "algo visual para mostrar" o "el material para la sesión", genera además el modo proyección:

```bash
python scripts/generar_proyeccion.py guia.md -o guia_proyeccion.html
```

Produce un único HTML con una lámina por bloque, los diagramas Mermaid ya dibujados, un riel de agenda proporcional a los minutos y un cronómetro por bloque que avisa cuando queda poco tiempo o se excede. Las notas del docente y las subsecciones cuyo título contiene "docente" o "solución" quedan ocultas hasta que el docente las activa, por eso la solución del ejercicio debe ir bajo un encabezado `### Solución de referencia (para el docente)`. Entrégalo como archivo para descargar (necesita internet al abrirse, porque carga las librerías de dibujo desde un CDN). Si no puedes ejecutar código, omite este paso y ofrécelo en una línea.

**3. Quiz interactivo opcional.** Si en la sesión existe una herramienta de quiz o tarjetas (por ejemplo, un widget de cuestionario en el chat), ofrece convertir las preguntas de verificación en un quiz de opción múltiple con distractores plausibles y explicación de la respuesta correcta; sirve como repaso previo a la siguiente clase.

Hay una guía completa de ejemplo en `ejemplos/modelado-dimensional.md`; léela si dudas del nivel de detalle o del tono esperados.

## Formato de entrega

Entrega la guía como un documento editable:

- Si la sesión tiene herramientas de documentos de Claude (Claude Docs), crea un Claude Doc con el contenido ya validado.
- Si no, entrega el archivo Markdown (.md) validado.
- Genera Word (.docx) solo si el usuario lo pide expresamente; en ese caso, sigue la skill de docx.

## Exactitud técnica

La industria de datos cambia rápido. Si mencionas versiones, precios, funcionalidades recientes o adopción de herramientas y tienes búsqueda web disponible, verifica antes de afirmarlo. Si no puedes verificar, describe la capacidad de forma general en lugar de inventar detalles. Los conceptos (normalización, modelado dimensional, teorema CAP, etc.) no necesitan verificación.

## Si falta información

Si el usuario solo da el tema, no hagas preguntas: asume el público y la duración de esta skill, elige un nivel intermedio y un caso de industria genérico (retail, banca o logística funcionan bien), y menciónalo en una línea al entregar. Si da contexto adicional (sector de los participantes, nivel, clase anterior, herramientas que usa su empresa), úsalo para personalizar el caso de apertura, el ejercicio y los ejemplos.

Para temas amplios que no caben en 90 minutos (por ejemplo, "gobierno de datos"), acota a un núcleo enseñable y propón en una línea cómo dividir el resto en clases siguientes. Consulta `references/temario.md` para ver los temas habituales y sus prerrequisitos.
