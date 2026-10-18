# QA — revisión de la presentación

**22 diapositivas y 9 avances internos.** Archivo vigente: `deck.html`.

## Cambios

- 2: logos de Guayerd, AI PlayGrounds y LetyMind junto a sus roles; foto y nube inferior conservadas.
- 4 y 12: aperturas azules con pregunta y una ilustración original de interfaces, no solo iconos.
- 16: nueva transición naranja «Ahora vamos a trabajar».
- 17: instrucciones grupales sobre naranja, después de la transición.
- 18: apertura azul «De nuestra idea al prototipo» con logo original de Google AI Studio, obtenido del recurso enlazado por su web oficial. Procedencia en `../assets/content/sections/README.md`.
- 19: actividad individual guiada paso a paso, fondo naranja.
- 20: selección en equipo, fondo naranja y contenido conservado.
- 22: «Muchas gracias», LinkedIn, correo y web con enlaces.

## Comprobación

Chromium real, offline antes de cargar, 1920 × 1080 y 1366 × 768. **62 estados capturados**, incluyendo todas las revelaciones. Sin desbordamientos o colisiones de texto detectados, imágenes y fuentes cargadas, cero errores JavaScript y cero solicitudes HTTP/HTTPS durante renderizado. Avance y retroceso de cada revelación, Home/End y orden de los 22 slides comprobados.

Revisión visual de las cuatro hojas de contacto Full HD: cabeceras intactas, composiciones equilibradas, preguntas legibles, naranja con texto oscuro, cierre y contactos completos. Evidencias de ambas resoluciones en `qa/revision/`. Los enlaces externos necesitan conexión al abrirse; no son dependencias del deck. No se ha probado entrega de correo ni disponibilidad de los perfiles externos.

Fuentes: `qa/revision/checks.json`, `qa/revision/contact-1.png` … `contact-4.png`. Hoja general actualizada: `deck-contact-sheet.png`. El QA anterior de 129 comprobaciones corresponde a la versión inicial, no a esta revisión.

## Reproducir

```bash
python tmp/build-deck.py
node tmp/qa-revision.mjs
python tmp/document-revision.py
```

Abrir: `chromium-browser --new-window "file://$(pwd)/output/deck.html"`.
