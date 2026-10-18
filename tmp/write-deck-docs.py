"""Write the reconstruction spec first; facilitator notes on explicit --notes."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
slides = json.loads((ROOT / 'deck/content.json').read_text())
assert len(slides) == 18 and sum(s['minutes'] for s in slides) == 120
header = '''# Especificación de la presentación — Prototipado Digital

## Contexto y audiencia

Taller virtual de 120 minutos del programa de preincubación Científica Sprint, Universidad Científica del Sur. Facilitador: Edhú Nuñez Alvarado. Aproximadamente 30 participantes organizados en equipos universitarios con ideas de negocio. Ya trabajaron problemas, soluciones, entrevistas, descubrimiento y priorización de hipótesis. Recuperar esos insumos; no volver a impartir ideación ni asumir demanda validada.

## Objetivos

Comprender prototipo y su diferencia con idea/MVP; identificar la funcionalidad principal; describir el camino feliz; generar individualmente un prototipo en Google AI Studio; comparar versiones y elegir una por equipo; observar dificultades y recopilar retroalimentación temprana.

Un único procedimiento para todos: en productos físicos, representar presentación, selección, personalización, solicitud o interés, no el funcionamiento físico. En proyectos complejos, simular la lógica con resultados ficticios explícitos. No añadir recorridos ni actividades separados.

## Tiempo total: 120 minutos

| Bloque | Slides | Minutos | Acumulado |
| --- | --- | ---: | ---: |
| Introducción y fundamentos | 1–6 | 16 | 16 |
| Tanda | 7 | 4 | 20 |
| Funcionalidad principal | 8–10 | 13 | 33 |
| Camino feliz y dinámica | 11–13 | 15 | 48 |
| Trabajo en salas | 14 | 23 | 71 |
| Google Docs + Google AI Studio en vivo | 15 | 38 | 109 |
| Comparación, validación y cierre | 16–18 | 11 | 120 |

No descansos, rondas de exposición ni slides adicionales. La demo de 38 minutos transcurre fuera del deck al compartir pantalla, sin agregar diapositivas.

## Identidad y reconstrucción

Heredar `branding/brand-spec.md` sin modificarlo. Reutilizar el marcado y CSS aprobados de `tmp/brand-proof-a.html`, `tmp/brand-proof-c.html` y `tmp/brand-proof.css`; se adaptan identificadores repetidos a clases. Base técnica: `.agents/skills/html-slides/assets/viewport-base.css`, incrustada sin modificar la skill. Lienzo 1920 × 1080, 16:9 centrado, bandas negras fuera de proporción. Cabecera C de 215 px; margen lateral 108 px; área editorial desde y=269. Montserrat 400/700 incrustada con licencia OFL; nunca Gotham .fntdata. Azul #00358E, naranja #F68D20 como acento, blanco y negro. Títulos de referencia 64 px, cuerpo 36 px, apoyo 32 px; reducciones locales documentadas para títulos largos y etiquetas, manteniendo legibilidad.

Poco texto, sin tarjetas ni sombras decorativas. Diagramas semánticos e ilustraciones propias. Fondo y logos institucionales no se transforman. Las capturas de Tanda tienen una excepción explícita al máximo genérico de 400 px: pueden medir hasta 620 px de alto a Full HD dentro de una zona reservada, siempre proporcionales y completas, para permitir leer la interfaz.

Los recursos personales conservan originales. Aplicar únicamente las adaptaciones ya autorizadas por el usuario en `assets/content/presenter/assets-manifest.md`: partes blancas a azul oscuro en copias derivadas y recorte de márgenes vacíos. Las nueve marcas disponibles de la lista final se utilizan; Wichay sigue ausente y previamente excluido. No añadir CIDE ni logos de empleadores a la nube. Microsoft se muestra como la insignia recibida, sin recortar su leyenda ni inferir cargos; su procedencia y texto de asociación quedan señalados en QA. No inventar sustitutos.

## Inventario y rutas reales

- PPTX original: `sources/Copy of PPT Plantila - Científica Sprint.pptx`; cinco slides institucionales, hash verificado contra el inventario de extracción.
- Institucionales: `assets/institutional/originals/image2.png` (A), `image3.png`, `image4.png`, `image6.svg` con `image5.png` como respaldo (C). `image7.png` queda disponible, fuera del cierre editable.
- Perfil y foto: `assets/content/presenter/profile.md`, `photo/perfil.png` (400 × 400); logos en `assets/content/presenter/logos/`. Derivados trazables en `assets/content/presenter/derived/`.
- Fuentes aprobadas: copias sin modificar en `assets/content/fonts/Montserrat-Regular.ttf`, `Montserrat-Bold.ttf`, `OFL.txt`, `provenance.json`, procedentes de `tmp/brand-proof-fonts/`.
- Tanda: `assets/content/tanda/mockup.html`, `tanda-mark.svg`, `screen-01.png` … `screen-05.png`, `README.md`. Pantalla 1 también introduce el caso en 7 y acompaña 10.
- Ilustraciones originales: `assets/content/illustrations/` (boceto, digital, físico y símbolos explicativos).
- Datos estructurados de cada slide: `deck/content.json`. Renderizador: `tmp/build-deck.py`; estilos y navegación fuente: `deck/deck.css` y `deck/deck.js`. HTML final: `output/deck.html`.

## Tanda: contenido exacto de las capturas

Caso ficticio, nombre Tanda, web app mobile-first. Paleta propia: verde #174C40, tinta #152C27, crema #F7F6F0, blanco. Montserrat 400/700, misma familia en las cinco vistas. Captura íntegra de viewport 390 × 640 CSS px, exportada a 780 × 1280 PNG (DPR 2). No es una barbería real ni una reserva real.

Elementos comunes: marca «Tanda», distintivo «DEMO», indicador «1 / 5» … «5 / 5», pie «Simulación · Datos ficticios». Pantallas:

1. «Elige tu servicio»; «Corte clásico», «30 min · S/ 35» seleccionado; «Barba», «20 min · S/ 25»; «Corte + barba», «50 min · S/ 55»; botón «Continuar».
2. «Elige tu horario»; «Noviembre 2026»; selector «Jue 19», «Vie 20» seleccionado, «Sáb 21»; «10:00», «11:00», «16:00» seleccionado, «17:00»; «Corte clásico · 30 min»; botón «Continuar».
3. «Tus datos»; «Nombre» → «Alex Rivera»; «Correo» → «alex@example.com»; «Corte clásico», «Vie 20 nov · 16:00»; botón «Revisar reserva». Identidad y contacto ficticios; no correo a un destinatario real.
4. «Revisa tu reserva»; «Corte clásico», «30 min · S/ 35»; «Vie 20 nov 2026», «16:00»; «Alex Rivera», «alex@example.com»; botón «Confirmar reserva».
5. «¡Reserva realizada!»; «Corte clásico», «Vie 20 nov · 16:00», «Alex Rivera»; «Reserva de demostración. No se registró una cita real.»; botón «Volver al inicio».

No perfiles, reseñas, pago, fidelización, notificaciones, autenticación o funciones adicionales. Las capturas son maquetas explicativas, no controles interactivos dentro de la presentación.

## Interactividad y navegación

18 slides, 9 avances internos: 5 en la 12 y 4 en la 13. Las demás son estáticas con transición discreta. Flecha derecha, espacio y PageDown: un estado o una diapositiva. Flecha izquierda y PageUp: deshacer un estado; si está en el primero, ir a la diapositiva previa. Cada entrada a 12/13 comienza en estado 0 para poder repetir; R reinicia la actividad actual. Home/End: primera/última. F y botón de pantalla completa: API del navegador; Escape sale de pantalla completa. Botones anterior/siguiente y clic en el cuerpo avanzan una sola vez, excluyendo enlaces, botones y selección de texto; ignorar repetición de tecla. Swipe horizontal para pantallas táctiles. Indicador discreto de slide, sin tapar el arte de portada ni cabecera.

Slide 12: 0=pantalla 1 sin respuesta; 1=revela «Seleccionar servicio»; 2=pantalla 2 sin respuesta nueva; 3=revela «Elegir fecha y horario»; 4=pantalla 3 sin respuesta nueva; 5=revela «Ingresar datos de reserva». Respuestas anteriores persisten; ninguna futura está visible ni expuesta al lector de pantalla.

Slide 13: 0=pantalla 4 sin respuesta; 1=revela «Revisar y confirmar la reserva»; 2=pantalla 5 sin respuesta nueva; 3=revela «Ver la confirmación de la cita»; 4=muestra el recorrido completo: Seleccionar servicio → Elegir horario → Ingresar datos → Confirmar → Ver confirmación. La pantalla 5 permanece. Las cajas de captura, pregunta y respuestas tienen posiciones reservadas; ninguna revelación mueve cabecera ni resto del layout.

Notas del facilitador solo en `deck/presenter-notes.md`, nunca visibles en el deck. El estado es temporal en memoria, sin almacenamiento. La presentación se abre por file:// y funciona sin red. Google Docs y AI Studio son actividades externas en vivo y sí requieren acceso/conexión.

## Materiales y accesibilidad

`materials/plantilla-trabajo-equipo.md`: campos y prompt reutilizable; `materials/ejemplo-tanda.md`: caso completo y prompt final; `materials/guia-validacion.md`: tarea, observación y registro breve. Copiar manualmente la plantilla a un Google Docs real antes del taller; no se inventan documentos ni enlaces.

HTML lang=es, estructura de secciones y títulos, imágenes con alternativas, botones con nombres accesibles y foco visible, teclado completo, control de foco/inert en slides ocultas, región de estado accesible. Las respuestas futuras usan hidden/aria-hidden. Se respeta prefers-reduced-motion sin alterar el orden ni revelar respuestas automáticamente. Sin JS, el contenido permanece consultable como documento con todas las respuestas y sin navegación falsa; con JS, modo presentación sin scroll.

## Criterios de aceptación y QA

Exactamente 18 slides en este orden, 120 minutos; contenido visible exacto indicado abajo y textos de las capturas de esta sección. Reutilizar A/C, conservar todos los archivos aprobados. Renderizar las 18 en 1920 × 1080 y 1366 × 768; revisar lectura, espacios, contraste, intersecciones y recorte real, no solo límites. Guardar PNG de todos los slides y todos los estados de 12/13. Probar avance/retroceso, reinicio, Home/End, clic sin saltos, botones, fullscreen, modo offline, imágenes/fuentes, ausencia de errores y de peticiones externas. Hoja general `output/deck-contact-sheet.png`, resultados `output/qa.md` y evidencias en `output/qa/`.

No backend, bases de datos, APIs, autenticación ni despliegue. No Google Drive ficticio. No fuentes Gotham. No alterar logos institucionales ni skill. No agregar slides para cubrir fallos de composición; redistribuir elementos dentro de las 18 sin modificar pedagogía. Los pendientes reales se registran fuera de las diapositivas.

## Especificación slide por slide

En los listados siguientes, el título aparece aparte y los textos se muestran en el orden de lectura; los textos incrustados de Tanda se especifican arriba. Las nueve marcas son gráficos, no etiquetas añadidas. Los controles globales muestran anterior, siguiente, pantalla completa y el número de slide. Los números de pasos son marcadores de orden.
'''
if '--notes' not in sys.argv:
    pieces = [header]
    for s in slides:
        pieces.append(f'### {s["number"]:02} — {s["title"]}\n\n**Objetivo:** {s["objective"]}\n\n**Título visible:** {s["title"]}\n\n**Contenido visible exacto:**\n\n' + '\n'.join('- ' + t for t in s['text']) + f'\n\n**Layout:** {s["layout"]}. **Composición:** {s["composition"]}\n\n**Interacción:** ' + (f'{s["reveals"]} avances internos, según la secuencia determinista anterior.' if s['reveals'] else 'Navegación estándar; sin revelaciones internas.') + f'\n\n**Notas:** {s["notes"]}\n\n**Tiempo:** {s["minutes"]} min.\n\n**Archivos:** ' + ', '.join('`' + x + '`' for x in s['dependencies']) + ('; ' if s['dependencies'] else '') + ('recursos de layout A y fuente común.' if s['layout']=='A' else 'cabecera C y fuente común.') + '\n\n')
    (ROOT / 'deck/deck-spec.md').write_text(''.join(pieces))
    print('deck/deck-spec.md: 18 slides, 120 min, 9 internal advances')
else:
    text = '# Notas del facilitador — Prototipado Digital\n\nSolo para el facilitador; no se muestran en la presentación.\n\nAntes de comenzar: abrir el deck local, comprobar pantalla compartida y audio, preparar salas, copiar la plantilla a un Google Docs real y comprobar permisos. Verificar el acceso a Google AI Studio y su entorno de construcción de aplicaciones web. Tener los tres materiales abiertos. Las herramientas en vivo requieren Internet; el deck no.\n\nNavegación: →/espacio avanzan un estado; ← retrocede; Home/End van al inicio/final; R reinicia una dinámica; F alterna pantalla completa. Cada regreso a 12/13 reinicia sus respuestas.\n\n'
    elapsed = 0
    for s in slides:
        text += f'## {s["number"]:02} · {s["title"]}\n\n**{s["minutes"]} min · minuto {elapsed}–{elapsed+s["minutes"]}**\n\n{s["notes"]}\n\n'
        elapsed += s['minutes']
    (ROOT / 'deck/presenter-notes.md').write_text(text)
    print('deck/presenter-notes.md generated')
