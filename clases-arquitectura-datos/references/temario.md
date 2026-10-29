# Temario de referencia: Arquitectura de Datos

Úsalo para ubicar una clase dentro de una secuencia lógica, decidir qué prerrequisitos asumir y acotar temas demasiado amplios. No es obligatorio seguirlo en orden.

## Módulo 1: Fundamentos
| Tema | Prerrequisitos | Núcleo de 90 min |
|---|---|---|
| ¿Qué es arquitectura de datos? | Ninguno | Del dato operativo al dato analítico; OLTP vs OLAP |
| Modelado relacional y normalización | SQL básico | Formas normales 1FN–3FN y por qué se desnormaliza en analítica |
| Tipos de datos y formatos | Ninguno | Estructurado, semiestructurado, no estructurado; CSV, JSON, Parquet, Avro |

## Módulo 2: Almacenamiento analítico
| Tema | Prerrequisitos | Núcleo de 90 min |
|---|---|---|
| Data Warehouse | OLTP vs OLAP | Arquitectura Inmon vs Kimball |
| Modelado dimensional | Data Warehouse | Hechos, dimensiones, esquema estrella y copo de nieve |
| Dimensiones lentamente cambiantes (SCD) | Modelado dimensional | SCD tipos 1, 2 y 3 |
| Data Lake | Formatos | Esquema en lectura vs en escritura; riesgo de "data swamp" |
| Lakehouse y formatos de tabla abiertos | Data Lake, DW | Delta Lake, Apache Iceberg, Hudi; arquitectura medallón |

## Módulo 3: Movimiento y procesamiento
| Tema | Prerrequisitos | Núcleo de 90 min |
|---|---|---|
| ETL vs ELT | Data Warehouse | Dónde ocurre la transformación y por qué cambió con la nube |
| Pipelines y orquestación | ETL/ELT | DAGs, dependencias, idempotencia, reintentos |
| Batch vs streaming | Pipelines | Latencia, ventanas, arquitecturas Lambda y Kappa |
| Change Data Capture (CDC) | Batch vs streaming | Captura basada en logs vs consultas |
| Transformación como código | ELT | dbt, pruebas y versionado de modelos |

## Módulo 4: Gobierno y calidad
| Tema | Prerrequisitos | Núcleo de 90 min |
|---|---|---|
| Calidad de datos | Pipelines | Dimensiones de calidad y contratos de datos |
| Metadatos, catálogo y linaje | Calidad | Por qué saber de dónde viene un dato |
| Gobierno de datos | Catálogo | Roles (owner, steward), políticas, cumplimiento |
| Seguridad y privacidad | Gobierno | Control de acceso, enmascaramiento, datos personales |

## Módulo 5: Arquitecturas modernas
| Tema | Prerrequisitos | Núcleo de 90 min |
|---|---|---|
| Arquitecturas en la nube | Módulos 2 y 3 | Separación de cómputo y almacenamiento; costos |
| Data Mesh | Gobierno | Dominios, dato como producto, plataforma de autoservicio |
| Data Fabric | Catálogo, gobierno | Integración guiada por metadatos; comparación con Data Mesh |
| Arquitectura para IA/ML | Lakehouse, pipelines | Feature stores, datos para entrenamiento, vector stores |
