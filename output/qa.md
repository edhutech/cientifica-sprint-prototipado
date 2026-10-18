> **Reporte histórico de la versión de 18 diapositivas.** Para el HTML vigente de 22, consultar [QA de revisión](qa-revision.md).

# QA final — Prototipado Digital

## Resultado general

**Construcción completada: 18 diapositivas, 120 minutos orientativos y 9 avances internos de revelación.** QA técnico aprobado y revisión visual realizada para todas las diapositivas en **1920 × 1080** y **1366 × 768**. Las cinco pantallas de Tanda son recursos ficticios originales y coherentes.

- Navegador: Chromium 155.0.8059.39 Built from source for Fedora release 44 (Forty Four).
- Método: Chromium real mediante DevTools Protocol; viewport CSS exacto, DPR 1; red desactivada antes de abrir el archivo local; espera a fuentes, decodificación de imágenes y fin de animaciones.
- **54 estados visuales verificados**, sin fallos métricos: 27 por resolución, incluyendo todos los estados de 12 y 13.
- **129 comprobaciones aprobadas**, con eventos reales de teclado, ratón y touch.
- **0 errores JavaScript y 0 solicitudes HTTP/HTTPS de ejecución**.
- Los límites y comprobaciones geométricas se complementaron con inspección visual de las seis hojas de revisión (las 18 slides en ambas resoluciones), las secuencias de revelación, las cinco pantallas móviles y capturas individuales de detalle. No se declara éxito únicamente por el encaje en el viewport.

## Revisión slide por slide

Cada fila fue revisada en ambos tamaños. Las capturas base de 12/13 muestran el estado final; los estados iniciales e intermedios están en archivos separados.

| Slide | Full HD | 1366 × 768 | Revisión visual |
| --- | --- | --- | --- |
| 01 | [Captura](qa/1920x1080/slide-01.png) | [Captura](qa/1366x768/slide-01.png) | Correcta. Portada reutilizada; Taller en pestaña; título y ponente separados; foto y firma libres. |
| 02 | [Captura](qa/1920x1080/slide-02.png) | [Captura](qa/1366x768/slide-02.png) | Correcta. Foto real proporcionada, sin ampliar; perfil exacto; nueve marcas en nube única, sin categorías. |
| 03 | [Captura](qa/1920x1080/slide-03.png) | [Captura](qa/1366x768/slide-03.png) | Correcta. Tres resultados diferenciados, progresión y entregable concreto; espacio amplio. |
| 04 | [Captura](qa/1920x1080/slide-04.png) | [Captura](qa/1366x768/slide-04.png) | Correcta. Definición completa; tres símbolos originales y distinción de producto terminado. |
| 05 | [Captura](qa/1920x1080/slide-05.png) | [Captura](qa/1366x768/slide-05.png) | Correcta. Tres columnas legibles; flechas de progresión sin interferir con el texto. |
| 06 | [Captura](qa/1920x1080/slide-06.png) | [Captura](qa/1366x768/slide-06.png) | Correcta. Tres ilustraciones nítidas, sin marcas ajenas ni apariencia de evidencia fotográfica. |
| 07 | [Captura](qa/1920x1080/slide-07.png) | [Captura](qa/1366x768/slide-07.png) | Correcta. Problema y solución diferenciados; caso ficticio explícito; pantalla completa y proporcional. |
| 08 | [Captura](qa/1920x1080/slide-08.png) | [Captura](qa/1366x768/slide-08.png) | Correcta. Definición dominante y prioridad clara; no se usa «experiencia principal». |
| 09 | [Captura](qa/1920x1080/slide-09.png) | [Captura](qa/1366x768/slide-09.png) | Correcta. Tres preguntas grandes, completas y separadas; sin matrices ni saturación. |
| 10 | [Captura](qa/1920x1080/slide-10.png) | [Captura](qa/1366x768/slide-10.png) | Correcta. Funcionalidad de Tanda protagonista; funciones complementarias fuera de alcance. |
| 11 | [Captura](qa/1920x1080/slide-11.png) | [Captura](qa/1366x768/slide-11.png) | Correcta. Definición y cuatro características; flujo abstracto sin anticipar respuestas de Tanda. |
| 12 | [Captura](qa/1920x1080/slide-12.png) | [Captura](qa/1366x768/slide-12.png) | Correcta. Seis estados inspeccionados; una pantalla a la vez, respuestas retenidas y futuras ocultas. |
| 13 | [Captura](qa/1920x1080/slide-13.png) | [Captura](qa/1366x768/slide-13.png) | Correcta. Cinco estados inspeccionados; confirmación simulada y recorrido completo al final. |
| 14 | [Captura](qa/1920x1080/slide-14.png) | [Captura](qa/1366x768/slide-14.png) | Correcta. Tres instrucciones, color opcional y 20 minutos; cifra corregida para contener la tipografía. |
| 15 | [Captura](qa/1920x1080/slide-15.png) | [Captura](qa/1366x768/slide-15.png) | Correcta. Flujo insumos → prompt → herramienta → prototipo; demostración en vivo e instrucción individual visibles. |
| 16 | [Captura](qa/1920x1080/slide-16.png) | [Captura](qa/1366x768/slide-16.png) | Correcta. Cuatro instrucciones y criterios simples; no evaluación técnica compleja. |
| 17 | [Captura](qa/1920x1080/slide-17.png) | [Captura](qa/1366x768/slide-17.png) | Correcta. Procedimiento y tarea separados; distinción de usabilidad y demanda visible. |
| 18 | [Captura](qa/1920x1080/slide-18.png) | [Captura](qa/1366x768/slide-18.png) | Correcta. Cierre C limpio; mensaje editable y complemento breve, sin texto sobre image7.png. |

## Interacciones verificadas

- →, ↓, espacio y PageDown: siguiente estado o slide; ←, ↑ y PageUp: retroceso. Las pruebas ejercitan específicamente →, ←, espacio y PageDown/PageUp; ↑/↓ comparten los mismos manejadores.
- Home/End: primera y última; límites del recorrido sin exceder 1…18.
- Un clic en el cuerpo avanza una sola vez; doble clic y repetición de tecla no saltan la secuencia. Los botones no propagan el avance al cuerpo. El teclado sigue funcionando después de usar un botón.
- R reinicia la dinámica; regresar a 12 o 13 reinicia su estado 0. Retroceso interno probado en los cinco estados de 12 y secuencia completa de 13 comprobada durante el recorrido.
- Slide 12: cinco avances desde su estado inicial, con tres respuestas reveladas y dos cambios de pantalla. Slide 13: cuatro avances, con dos respuestas, un cambio de pantalla y el resumen final. **No hay saltos de posición o tamaño en las cajas de captura**.
- Pantalla completa mediante clic real y salida mediante API comprobadas. F utiliza el mismo manejador; Escape/F11 son capacidades del navegador. El control no avanza diapositiva.
- Swipe horizontal comprobado; un gesto avanza una diapositiva sin clic duplicado.
- Reduced motion elimina las animaciones y conserva el orden de respuestas.
- IDs únicos, botones accesibles con foco visible, imágenes alternativas, slides ocultas con inert/aria-hidden. Respuestas futuras ocultas también al árbol accesible. Sin JS, documento consultable con 18 slides y sin controles inertes ni superposición del resumen.

## Calidad visual y fidelidad

- Se reutilizó la portada HTML aprobada; la cabecera C conserva coordenadas y recortes del PPTX. La fotografía de cabecera se incrusta una sola vez como fondo CSS con el mismo tamaño 100% × 502,325%, evitando repetir nueve megabytes por slide.
- Los textos generales usan Montserrat 400/700, azul #00358E/negro sobre blanco, tamaños de referencia del brand-spec. Los títulos largos de 6, 9, 12 y 13 usan 58 px a Full HD para mantener una línea. Las capturas llegan a 620 px de alto dentro del cuerpo, excepción documentada al límite genérico de imágenes de la skill, necesaria para lectura. Ninguna tapa cabecera ni logos.
- Contrastes de texto sobre blanco: azul institucional 11,05:1; negro 21:1; gris #444444 aproximadamente 9,74:1. Tanda conserva contraste alto con su verde y tinta. El naranja se utiliza como acento gráfico, no como texto pequeño sobre blanco. Los pequeños textos integrados en logos conservan las limitaciones de los archivos suministrados; no son contenido pedagógico.
- Nube de logos: tamaños ópticos equilibrados, márgenes exteriores de BASF recortados, versiones blancas de SENATI/NEXUM/HUB UDEP adaptadas a azul en copias derivadas, según autorización explícita previa. Los demás colores y leyendas se conservan.
- Foto de 400 × 400 usada a 400 × 400 en Full HD, sin ampliación ni necesidad de recortar. La versión recibida mantiene su nitidez limitada; calidad aceptada por el usuario.
- Las cinco pantallas Tanda se exportaron a 780 × 1280, desde viewport 390 × 640 a DPR 2. Mismo servicio, fecha, hora, nombre y correo en todas las vistas. Reserva ficticia declarada; ninguna captura presenta una operación real.

## Correcciones realizadas

1. El bloque «20» de la slide 14 extendía sus métricas verticales con interlineado 1. Se ajustó a 1,15 y se añadió espacio inferior; la nueva ejecución pasó en ambos tamaños y se revisaron ambas capturas corregidas.
2. La navegación por flechas se mantiene operativa después de enfocar botones; espacio/Enter sobre un botón conservan su activación nativa.
3. En la alternativa sin JavaScript, se oculta el resumen superpuesto de la slide 13 para conservar lectura del documento estático.
4. El test de recarga sin JS se hizo tolerante al instante sin documentElement durante navegación. Era un fallo del verificador, no del deck. La ejecución final completa terminó sin errores.

No se añadieron diapositivas ni se cambió el orden pedagógico. `branding/brand-spec.md`, PPTX, todos los originales institucionales/personales y la skill permanecen sin cambios; evidencia de hashes en [integrity.json](qa/integrity.json). El registro inicial de hashes está en `tmp/deck-original-hashes.json`.

## Recursos personales y pendientes reales

- **Wichay:** archivo ausente y previamente excluido por el usuario. Se omite y no se sustituye; la nube contiene nueve marcas. Aunque aparece de nuevo en la lista del encargo, no se ha fabricado un recurso ni reservado un hueco.
- **Microsoft for Startups:** se usa íntegra la insignia aportada, incluida su leyenda «Proud to partner with». No se inventó un logo aislado ni se eliminó la leyenda. Confirmar que esa insignia corresponde al contexto del presentador antes de exponer; si no, sustituir por un recurso adecuado proporcionado por él.
- **Procedencia de logos:** todos aportados manualmente, sin URLs originales ni documentación de licencias. Identidad y carga verificadas visual/técnicamente, no certificación de versión oficial vigente. No se añaden organizaciones ni cargos.
- **Google Docs:** copiar la plantilla a un documento real y configurar permisos antes del taller. No se creó ningún documento de Drive ni enlace ficticio.
- **Google AI Studio:** el facilitador debe comprobar acceso al entorno de construcción de apps web y disponibilidad antes de la sesión. No se ejecutó una generación remota con una cuenta real. La demo y Google Docs requieren Internet; el deck local funciona offline.
- QA realizado en Chromium y las dos resoluciones pedidas. No certifica otros navegadores, lectura en móvil vertical ni apariencia idéntica a PowerPoint. Los renderizados originales de referencia provienen de LibreOffice.

## Evidencias y entregables

- [Deck final](deck.html), [hoja general de 18 slides](deck-contact-sheet.png).
- Estados: `qa/1920x1080/slide-12-state-00.png` … `05.png`; `slide-13-state-00.png` … `04.png`, también en `qa/1366x768/`.
- [Secuencia 12](qa/reveals-12.png) y [secuencia 13](qa/reveals-13.png).
- [Comprobaciones completas](qa/checks.json), [Tanda](qa/tanda-checks.json), [integridad y contrastes](qa/integrity.json).
- [Especificación](../deck/deck-spec.md), [notas](../deck/presenter-notes.md).
- [Plantilla de equipos](../materials/plantilla-trabajo-equipo.md), [ejemplo Tanda](../materials/ejemplo-tanda.md), [guía de validación](../materials/guia-validacion.md).
- [Registro de derivados personales](../assets/content/presenter/derived/manifest.md).

## Abrir y presentar

Desde la raíz del repositorio:

```bash
chromium-browser --new-window "file://$(pwd)/output/deck.html"
```

También puede abrirse `output/deck.html` directamente desde el explorador de archivos. No necesita servidor ni conexión. Zoom del navegador al 100%; pulsar F o el botón de pantalla completa. →/espacio/clic para avanzar; ← para retroceder; R reinicia una dinámica; Home/End inicio/final. Las notas se consultan por separado, fuera de la ventana compartida.

Para reconstruir recursos, documentos y presentación desde las fuentes locales, ejecutar por separado y en este orden:

```bash
python tmp/write-deck-docs.py
python tmp/build-tanda.py
node tmp/render-tanda.mjs
python tmp/write-deck-docs.py --notes
python tmp/prepare-deck-assets.py
python tmp/build-deck.py
node tmp/qa-deck.mjs
python tmp/deck-contact-sheets.py
python tmp/finalize-deck.py
```

Los materiales en `materials/` son fuentes Markdown editables. La revisión visual humana de nuevas versiones debe repetirse si cambian contenido o composición; el verificador automático por sí solo no la reemplaza.
