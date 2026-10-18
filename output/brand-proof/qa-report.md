# QA de composición — Fase 3 visual

**Resultado:** 4/4 pruebas de A/C correctas en Chromium 155. Se revisaron visualmente las cuatro capturas. Las pruebas son HTML técnicos estáticos, no la presentación del taller.

## Evidencias

| Prueba | Captura | Resultado |
| --- | --- | --- |
| A · 1920 × 1080 | [Portada Full HD](layout-a-1920x1080.png) | Correcta |
| A · 1366 × 768 | [Portada 1366](layout-a-1366x768.png) | Correcta |
| C · 1920 × 1080 | [Educativa Full HD](layout-c-1920x1080.png) | Correcta |
| C · 1366 × 768 | [Educativa 1366](layout-c-1366x768.png) | Correcta |

### Comprobaciones realizadas

- Tamaño de viewport fijado mediante Chromium DevTools Protocol, DPR 1; las capturas tienen las dimensiones solicitadas.
- Carga con red desactivada. Todos los gráficos son URI `data:`; Montserrat 400/700 está incrustada con su licencia SIL OFL. Se esperó `document.fonts.ready` y `image.decode()` antes de medir y capturar.
- Sin excepciones JavaScript, imágenes ausentes, desbordamiento de página, desbordamiento de cajas de texto ni intersecciones entre textos.
- A: todos los textos permanecen a la izquierda de la zona protegida de fotografía/logos. Separación entre título y bloque del ponente: 72,52 px en Full HD y 51,59 px en 1366 × 768. Se conservaron fotografía, pestaña y franja inferior originales.
- C: cabecera de 215 px en Full HD; logo Sprint en x=108, y≈41,99, ventana≈286,32 × 136,76. Firma en x≈1180,74, y≈69,83, tamaño≈631,26 × 81,08. El logo Sprint mantiene el recorte necesario para compensar sus márgenes transparentes. El cuerpo está separado de la cabecera.
- Revisión visual: jerarquía legible, acentos del nombre correctos, fondos proporcionados, logos sin deformaciones apreciables, franja sin compresión vertical y texto de prueba legible a ambas resoluciones.
- Contraste: azul sobre blanco 11,05:1; negro sobre blanco 21:1. En A, el blanco supera 19:1 incluso usando el píxel más claro del fondo dentro de cada caja de texto.
- Integridad: el PPTX y los diez archivos extraídos mantienen los hashes del inventario original. No se utilizaron ni convirtieron las fuentes `.fntdata`.

Durante la primera comprobación, la caja del título A registró extensión vertical de la tipografía con el interlineado inicial. Se ajustó a 1,15 y se añadió una reserva inferior de 12 px; las cuatro pruebas se volvieron a ejecutar y pasaron. No se ocultó el excedente dentro del título.

## Fidelidad y alcance

Las coordenadas y recortes de la cabecera proceden del XML del PPTX. Como contraste adicional, se comparó la cabecera Full HD con el render de LibreOffice: diferencia media absoluta RGB **3,50/255**. Es una medida descriptiva entre motores con distintos métodos de rasterización; no prueba igualdad píxel a píxel con PowerPoint.

Montserrat es una sustitución provisional de Gotham. Los tamaños del cuerpo educativo son una adaptación del área blanca vacía de la plantilla. B y D están documentados, pero no forman parte de las dos pruebas solicitadas. La nube de logos y fotografía personal de B quedan pendientes de recursos reales.

La pestaña azul de A permanece sin texto porque no se ha proporcionado número de sesión. El contenido de C está marcado como muestra técnica. No se ha generado contenido del taller, navegación ni presentación final.

## Reproducción

Desde la raíz del proyecto, ejecutar en este orden:

```bash
python tmp/build-brand-proofs.py
node tmp/render-brand-proofs.mjs
python tmp/measure-brand-proof.py
```

El generador descarga Montserrat y su licencia solamente si faltan en `tmp/brand-proof-fonts/`. Requiere Python; el medidor usa Pillow. El renderizador usa Node con WebSocket nativo y `chromium-browser`; no instala dependencias ni skills.

- HTML: `tmp/brand-proof-a.html`, `tmp/brand-proof-c.html`.
- Estilos de prueba: `tmp/brand-proof.css`; incorpora además el CSS base intacto de la skill.
- Procedencia y licencia tipográfica: `tmp/brand-proof-fonts/`.
- [Resultados geométricos](composition-checks.json).
- [Contrastes e integridad](visual-measurements.json).
- [Especificación visual](../../branding/brand-spec.md).
