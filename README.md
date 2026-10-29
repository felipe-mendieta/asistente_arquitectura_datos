# asistente_arquitectura_datos

Skill para Claude que diseña **guías de clase de 90 minutos sobre Arquitectura de Datos** para profesionales en capacitación, con enfoque pedagógico (problema → intuición → concepto → práctica → verificación), visual (diagramas Mermaid y tablas comparativas) y conectado con la industria.

## Qué incluye

```
clases-arquitectura-datos/
├── SKILL.md                         Instrucciones de la skill
├── references/temario.md            Temario de referencia con prerrequisitos
├── scripts/validar_guia.py          Valida que una guía cumpla la estructura
├── scripts/generar_proyeccion.py    Convierte la guía en un HTML para proyectar
├── assets/plantilla_proyeccion.html Plantilla del modo proyección
└── ejemplos/
    ├── modelado-dimensional.md                Guía completa de ejemplo
    └── modelado-dimensional_proyeccion.html   Su modo proyección
```

## Instalación en Claude

1. Descarga la carpeta `clases-arquitectura-datos` (o el archivo `.skill` de la sección *Releases*, si existe).
2. Comprímela en un `.zip` con la carpeta en la raíz.
3. En Claude, ve a **Configuración → Capacidades → Skills** y sube el archivo.

Luego basta con pedir, por ejemplo: *"Prepárame la clase de Change Data Capture para un grupo de desarrolladores"*.

## Uso de los scripts sin Claude

Requieren Python 3.8 o superior y no tienen dependencias externas.

```bash
# Validar una guía
python clases-arquitectura-datos/scripts/validar_guia.py mi-guia.md

# Generar el modo proyección (lámina por bloque, cronómetro y notas del docente ocultas)
python clases-arquitectura-datos/scripts/generar_proyeccion.py mi-guia.md -o clase.html
```

En el modo proyección: flechas o Re Pág/Av Pág para avanzar, barra espaciadora para iniciar o pausar el cronómetro del bloque. El HTML necesita conexión a internet al abrirse, porque carga `marked` y `mermaid` desde jsDelivr.

## Estructura de cada clase

| Bloque | Minutos |
|---|---|
| 1. Apertura: el problema | 10 |
| 2. Construyendo la intuición | 15 |
| 3. El concepto en profundidad | 25 |
| 4. Práctica activa | 25 |
| 5. Errores comunes y antipatrones | 5 |
| 6. Cierre y verificación (ronda Feynman) | 10 |
