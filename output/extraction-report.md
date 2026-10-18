# Reporte de extracción — plantilla Científica Sprint

**Estado: fases 1 y 2 realizadas y aprobadas por el usuario.** La Fase 3 visual se documenta en [`branding/brand-spec.md`](../branding/brand-spec.md). Los hallazgos siguientes se conservan como registro de la extracción.

## Fuente y método

- Archivo: `sources/Copy of PPT Plantila - Científica Sprint.pptx`.
- 5 diapositivas, formato **16:9**, 18 288 000 × 10 287 000 EMU (20 × 11,25 pulgadas; equivalente a 1920 × 1080 px a 96 ppp).
- Extracción directa del paquete ZIP y análisis de relaciones y XML de diapositivas, grupos, patrón y diseños. Los recursos gráficos están en rellenos de formas `p:sp`, no en objetos de imagen convencionales `p:pic`.
- Se conservaron los nombres y bytes originales. Las 8 imágenes y 2 fuentes extraídas coinciden byte a byte con el PPTX; el SHA-256 del archivo fuente no cambió.
- SHA-256: `1bed81e8e4c05aee049221e16f72208922f7b6bd308a883e1ffcebc9e3fdba36`.
- Script reproducible: `tmp/inspect-pptx.py`. La skill permanece intacta; su extractor estándar solo contempla imágenes convencionales, por lo que se utilizó inspección directa para incluir estos rellenos.

## Inventario visual

Todos los gráficos están en `assets/institutional/originals/`; su ubicación interna original es `ppt/media/` con el mismo nombre.

| Archivo | Dimensiones | Ubicación en plantilla | Recurso y reutilización |
| --- | --- | --- | --- |
| `image1.png` | 3072 × 1728 px | Diapositiva 1, Freeform 2 | Portada completa con fotografía, marca y textos integrados. Reutilizable como imagen completa; esos textos no son editables. |
| `image2.png` | 3072 × 1728 px | Diapositiva 2, Freeform 2 | Fondo de ponencia con hombre, pestaña azul, logos y franja inferior integrados. Los textos de sesión, título y ponente son objetos separados. |
| `image3.png` | 3072 × 1728 px | Diapositiva 3, Freeform 2 | Fotografía oscurecida del campus, recortada como cabecera horizontal. |
| `image4.png` | 623 × 831 px | Diapositiva 3, Freeform 3 | Logo Científica Sprint con transparencia y amplios márgenes transparentes. Preservar su recorte y escala. |
| `image5.png` | 1417 × 182 px | Diapositiva 3, Freeform 4 | Firma Universidad Científica / Unidad de Empleabilidad y Emprendimiento, PNG transparente de respaldo. |
| `image6.svg` | 1417 × 182; viewBox 0 0 1417.32 181.92 | Diapositiva 3, Freeform 4, extensión SVG | Versión vectorial original de la misma firma. Preferible para escalado. Solo contiene grupos y trazados, sin referencias externas. |
| `image7.png` | 1920 × 1080 px | Diapositiva 4, Group 2 / Freeform 3 | Imagen institucional completa, campus, logo y distintivo de ranking integrados. |
| `image8.png` | 3072 × 1728 px | Diapositiva 5, Freeform 2 | Variante del fondo de ponencia con mujer; textos editables separados. |

Fuentes originales en `assets/institutional/fonts/`:

| Archivo | Referencia | Tamaño | Estado |
| --- | --- | --- | --- |
| `font11.fntdata` | `ppt/fonts/font11.fntdata`, Gotham, rId11 de presentación | 138 448 bytes | Contenedor EOT incrustado; no es una fuente WOFF2 lista para HTML. |
| `font12.fntdata` | `ppt/fonts/font12.fntdata`, Gotham Bold, rId12 de presentación | 135 724 bytes | Contenedor EOT incrustado; requiere preparar y verificar una versión web derivada. |

Inventario técnico completo: [resource-inventory.json](resource-inventory.json). Incluye hashes, tamaños, relaciones, dimensiones, XML de formas, transformaciones de grupos, recortes, textos y referencias tipográficas originales.

## Composición que debe preservarse

- **Diapositiva 1:** una única imagen a pantalla completa. El logo y los textos promocionales forman parte del raster.
- **Diapositivas 2 y 5:** fondo completo y tres bloques editables: sesión, título y ponente. Una barra naranja `#F68D20` es una forma independiente agrupada, reconstruible con CSS. El XML declara Gotham/Gotham Bold y texto blanco; conserva tamaños de 43,29 pt para sesión, 110 pt para título y 25,77 pt para ponente.
- **Diapositiva 3:** cuerpo blanco y cabecera de 1920 × 215 px en el lienzo equivalente. El fondo se extiende dentro de la forma mediante `fillRect b="-402325"`: no debe comprimirse toda la fotografía en la franja. El logo Sprint también usa extensión y recorte (`l=-23653`, `t=-175750`, `r=-26226`, `b=-143025`, en unidades de 1/1000 %). Sus píxeles no transparentes ocupan aproximadamente x=99…506, y=349…541 del PNG; colocar el archivo completo sin este tratamiento haría el logo demasiado pequeño. La firma institucional derecha tiene PNG de respaldo y SVG alternativo.
- **Diapositiva 4:** imagen a pantalla completa dentro de un grupo escalado 1,125×. El relleno tiene una extensión horizontal leve (`l=r=-60`, equivalente a -0,06 % por lado).
- Transiciones originales: cobertura hacia la izquierda, lenta, en 2 y 3; fundido rápido en 4; sin transición explícita en 1 y 5. Son observaciones de la fuente, no decisiones aún para el taller.

**Reutilizables directamente:** fondos completos, fotografías, logos PNG y firma SVG. **A reproducir en HTML tras aprobación:** posiciones, recortes, texto editable, barra naranja y comportamiento interactivo. No hace falta rediseñar logos ni recrear fondos originales. Las franjas integradas en los fondos no existen como imágenes independientes en el paquete.

## Verificación y hallazgos

| Comprobación | Resultado |
| --- | --- |
| Integridad del PPTX y extracción | Correcta; fuente sin cambios y 10 archivos extraídos idénticos. |
| Lectura de PNG | 7/7 decodificados con Pillow. |
| Uso de imágenes en HTML autocontenido | 8/8 cargadas en Chromium 155 mediante URI `data:`; dimensiones naturales correctas. Evidencia: [asset-compatibility.json](asset-compatibility.json). |
| SVG autónomo | XML válido, solo `svg`, `g`, `path`; sin enlaces externos. |
| Calidad de imágenes | Fondos de 3072 × 1728 y 1920 × 1080 adecuados para un lienzo Full HD. El logo Sprint es raster; mantener su escala prevista. |
| Composición visual | Revisadas las 5 diapositivas renderizadas y la hoja de recursos. Cabecera, firmas, fondos y variantes identificados. |
| Tipografía web | Pendiente de preparar y verificar; los `.fntdata` no se probaron como fuentes web. |

### Punto a contrastar con PowerPoint

Las vistas previas se generaron con **LibreOffice → PDF → PNG**, no con Microsoft PowerPoint. En las diapositivas **2 y 5**, el título de ejemplo ocupa tres líneas y se superpone al bloque del ponente. El PDF sí incluye Gotham-Book y Gotham-Bold incrustadas, según `pdffonts`; no se atribuye este problema a una sustitución de fuente. Puede depender del ajuste de texto entre motores o de la composición de la propia plantilla. Conviene confirmar su aspecto en PowerPoint antes de fijar la disposición definitiva.

La igualdad de los recursos extraídos está verificada; la equivalencia visual exacta con PowerPoint y la composición final en HTML siguen pendientes. El chequeo de navegador es una prueba temporal de carga de recursos, no la presentación del taller.

Los gráficos originales suman aproximadamente **13,69 MiB** (unos 18,25 MiB al codificar todos en base64). Esta medida sirve para planificar el archivo autocontenido; no se han comprimido ni alterado originales.

## Evidencias para revisión

- [Vista conjunta de la plantilla](template-contact-sheet.png).
- [Vista conjunta de recursos PNG originales](assets-contact-sheet.png); el SVG se registra aparte en el inventario y en la prueba de navegador.
- Vistas individuales: [1](template-slide-1.png), [2](template-slide-2.png), [3](template-slide-3.png), [4](template-slide-4.png), [5](template-slide-5.png).
- PDF intermedio: `tmp/Copy of PPT Plantila - Científica Sprint.pdf`.
- Prueba reproducible de carga en navegador: `tmp/check-assets.py`.

## Revisión requerida

La extracción y los recursos propuestos fueron aprobados. Para HTML, el usuario indicó corregir la composición de los textos sin reproducir las superposiciones detectadas; la especificación visual y las pruebas de Fase 3 documentan ese tratamiento. El contenido y la estructura pedagógica del taller deberán ser proporcionados por el usuario.
