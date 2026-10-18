> **Actualización vigente:** 22 diapositivas, 9 avances internos. Nuevas aperturas azules y actividades naranjas; ver [revisión](deck/revision-spec.md) y [QA actualizado](output/qa-revision.md). Para reconstruir: `python tmp/build-deck.py`; verificar: `node tmp/qa-revision.mjs`. Los scripts QA anteriores corresponden a la versión histórica de 18 slides.

# Prototipado Digital — Científica Sprint

Proyecto de presentación HTML interactiva con fidelidad a la plantilla institucional PPTX, utilizando la skill instalada en `.agents/skills/html-slides/`.

## Estructura

```text
sources/                Plantilla PPTX y documentos de referencia originales
branding/               Especificación visual aprobada: brand-spec.md
assets/institutional/   Fondos, franjas, logos y recursos extraídos del PPTX
assets/content/         Imágenes y recursos específicos del taller
deck/                   Especificación, contenido, estilos, navegación y notas
materials/              Plantilla de equipos, ejemplo Tanda y guía de validación
output/                 HTML final y reportes de extracción y QA
tmp/                    Scripts y archivos temporales
```

Colocar el archivo PPTX institucional en `sources/`, junto con los documentos de referencia.

## Procedimiento

1. **Análisis de fuentes.** Inspeccionar el PPTX y su composición; extraer imágenes originales, incluidos fondos y recursos incrustados en formas. Identificar elementos reutilizables y aquellos que requieren reconstrucción. Inventariar recursos con sus ubicaciones y dimensiones.
2. **Verificación.** Comprobar compatibilidad con HTML, calidad visual y fidelidad a la plantilla. Presentar un reporte de extracción en `output/` y **detenerse hasta recibir aprobación**.
3. **Especificaciones.** Elaborar `branding/brand-spec.md` a partir de la plantilla y `deck/deck-spec.md` a partir de la información y estructura del taller proporcionadas por el usuario. No inventar contenido ni modificar decisiones pedagógicas sin aprobación.
4. **Construcción.** Usar `html-slides` para generar HTML autocontenido con navegación, transiciones y revelaciones progresivas, reutilizando los recursos institucionales originales siempre que sea posible.
5. **QA.** Revisar visualmente cada diapositiva, verificar navegación e interacciones y detectar desbordamientos, errores de composición y recursos ausentes. Entregar el reporte de calidad en `output/`.

## Criterios y estado actual

- Priorizar la fidelidad institucional; no rediseñar logos ni fondos originales innecesariamente.
- Conservar intactos los archivos originales y la skill instalada; no instalar otras skills.
- Extracción y verificación aprobadas por el usuario: [`output/extraction-report.md`](output/extraction-report.md).
- Identidad visual documentada en [`branding/brand-spec.md`](branding/brand-spec.md). Pruebas técnicas A/C y capturas: [`output/brand-proof/qa-report.md`](output/brand-proof/qa-report.md).
- Presentación completa: [`output/deck.html`](output/deck.html), 18 diapositivas y 9 avances internos de revelación, con Montserrat 400/700 y licencia incrustada. Duración orientativa: 120 minutos.
- Contenido: [`deck/deck-spec.md`](deck/deck-spec.md). Facilitación: [`deck/presenter-notes.md`](deck/presenter-notes.md). Recursos Tanda: `assets/content/tanda/`.
- QA visual y funcional realizado en Chromium a 1920 × 1080 y 1366 × 768: [`output/qa.md`](output/qa.md). Vista general: [`output/deck-contact-sheet.png`](output/deck-contact-sheet.png).
- Pendientes operativos: preparar el Google Docs real y comprobar acceso a Google AI Studio. Wichay se omite por ausencia y decisión previa; la insignia de Microsoft y la procedencia de los logos se documentan en QA. Se utiliza la calidad personal disponible, con originales intactos.

## Presentar

Desde la raíz del repositorio:

```bash
chromium-browser --new-window "file://$(pwd)/output/deck.html"
```

No requiere servidor ni conexión para mostrar el deck. **F** alterna pantalla completa; **→ / espacio / clic** avanza; **←** retrocede; **R** reinicia la dinámica; **Home / End** van al inicio o final. Google Docs y Google AI Studio se utilizan en vivo y requieren conexión.

La reproducción del build y del QA está documentada en `output/qa.md`. La skill, la especificación de marca y los recursos originales permanecen intactos.
