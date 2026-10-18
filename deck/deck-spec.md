> **Versión vigente: 22 diapositivas.** Ver [revision-spec.md](revision-spec.md) y `revisions.json` para el orden y los cambios solicitados. El documento siguiente conserva la especificación base de 18 slides como referencia histórica.

# Especificación de la presentación — Prototipado Digital

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
### 01 — Prototipado Digital

**Objetivo:** Abrir el taller y presentar al facilitador.

**Título visible:** Prototipado Digital

**Contenido visible exacto:**

- Taller
- Prototipado Digital
- Ponente:
- Edhú Nuñez Alvarado

**Layout:** A. **Composición:** Portada aprobada A: image2.png completo; título regular a la izquierda, ponente debajo y Taller sobre la pestaña azul.

**Interacción:** Navegación estándar; sin revelaciones internas.

**Notas:** Dar la bienvenida al taller virtual de Científica Sprint. En estas dos horas convertirán una parte de su solución en un prototipo que alguien pueda recorrer. No prometer un producto terminado.

**Tiempo:** 1 min.

**Archivos:** `assets/institutional/originals/image2.png`; recursos de layout A y fuente común.

### 02 — Edhú Nuñez Alvarado

**Objetivo:** Conectar la experiencia del facilitador con el trabajo práctico.

**Título visible:** Edhú Nuñez Alvarado

**Contenido visible exacto:**

- Edhú Nuñez Alvarado
- AI Product Builder · Product Manager
- Product & Technology Instructor — Guayerd
- AI Labs Lead — AI PlayGrounds
- Ex CTO & Co-founder — LetyMind

**Layout:** B. **Composición:** Perfil a la izquierda, foto real de 400 × 400 a la derecha. Una sola nube de nueve marcas disponibles debajo, sin etiquetas. Wichay ausente y previamente excluido; no se sustituye. No incluir logos adicionales de CIDE ni de empleadores.

**Interacción:** Navegación estándar; sin revelaciones internas.

**Notas:** Introducción oral de 60–75 segundos: «Soy Edhú Nuñez Alvarado, AI Product Builder y Product Manager. Mi trabajo conecta producto y tecnología: entender qué necesita lograr una persona y convertirlo en algo que pueda usar. Soy Product & Technology Instructor en Guayerd, AI Labs Lead en AI PlayGrounds y fui CTO y cofundador de LetyMind. Esa combinación de formación, construcción de productos y emprendimiento es el punto de partida de este taller. Hoy no buscamos programar todas las funciones de una empresa ni terminar un producto. Vamos a elegir una acción importante, describir cómo la realizaría una persona y construir una representación que podamos observar. Ustedes ya han trabajado el problema y la solución; los recuperaremos como insumos, sin asumir que todo está validado. Mi papel será acompañarlos para que cada integrante genere una primera versión y luego el equipo pueda elegir con cuál seguir aprendiendo». No atribuir cargos o afiliaciones a las marcas de la nube.

**Tiempo:** 2 min.

**Archivos:** `assets/content/presenter/profile.md`, `assets/content/presenter/photo/perfil.png`, `assets/content/presenter/logos/`, `assets/content/presenter/derived/manifest.md`; cabecera C y fuente común.

### 03 — ¿Qué vamos a lograr hoy?

**Objetivo:** Hacer explícita la salida concreta del taller.

**Título visible:** ¿Qué vamos a lograr hoy?

**Contenido visible exacto:**

- Elegir qué parte de nuestra solución prototipar.
- Construir un primer prototipo digital.
- Prepararlo para recibir retroalimentación.
- Una primera versión que alguien pueda recorrer.

**Layout:** C. **Composición:** Tres resultados numerados en columnas abiertas, unidos por una progresión. Una frase final destaca el entregable.

**Interacción:** Navegación estándar; sin revelaciones internas.

**Notas:** Preguntar si ya tienen a mano el problema y la solución trabajados. Cada estudiante construirá individualmente; después el equipo elegirá una versión. No presentar una agenda extensa.

**Tiempo:** 2 min.

**Archivos:** cabecera C y fuente común.

### 04 — ¿Qué es un prototipo?

**Objetivo:** Definir prototipo sin confundirlo con un producto terminado.

**Título visible:** ¿Qué es un prototipo?

**Contenido visible exacto:**

- Una representación de nuestra solución que permite mostrarla, explorarla y aprender antes de desarrollarla completamente.
- Visual
- Interactivo
- Simulado
- No es el producto terminado.

**Layout:** C. **Composición:** Definición protagonista y tres símbolos originales: vista, acción y resultado simulado. No tarjetas decorativas.

**Interacción:** Navegación estándar; sin revelaciones internas.

**Notas:** Visual permite ver una propuesta; interactivo permite recorrer acciones; simulado representa una respuesta sin implementar la operación real. Pueden combinarse. Lo importante es qué queremos observar y aprender.

**Tiempo:** 4 min.

**Archivos:** `assets/content/illustrations/`; cabecera C y fuente común.

### 05 — Idea vs. prototipo vs. MVP

**Objetivo:** Diferenciar describir, representar y entregar valor real.

**Título visible:** Idea vs. prototipo vs. MVP

**Contenido visible exacto:**

- Idea
- Describimos lo que queremos resolver y cómo podría funcionar.
- Prototipo
- Representamos la solución para mostrarla y probar su uso.
- MVP
- Ofrecemos una primera versión utilizable para comprobar hipótesis con usuarios reales.

**Layout:** C. **Composición:** Tres columnas abiertas de progresión Idea → Prototipo → MVP; prototipo destacado con azul institucional.

**Interacción:** Navegación estándar; sin revelaciones internas.

**Notas:** Un prototipo puede simular operaciones. Un MVP normalmente implementa lo necesario para entregar valor real, aunque sea con una operación simple o manual. La progresión es conceptual: aprender puede hacernos volver a prototipar. Las entrevistas previas no equivalen a demanda comercial demostrada.

**Tiempo:** 4 min.

**Archivos:** cabecera C y fuente común.

### 06 — Los prototipos pueden tomar distintas formas

**Objetivo:** Mostrar que la sofisticación no define el valor de un prototipo.

**Título visible:** Los prototipos pueden tomar distintas formas

**Contenido visible exacto:**

- Boceto de papel
- Prototipo digital interactivo
- Representación de un producto físico
- La forma depende de lo que necesitamos aprender.

**Layout:** C. **Composición:** Tres ilustraciones SVG originales y sencillas: boceto, interfaz enlazada y maqueta física. No son fotografías ni evidencias de productos reales.

**Interacción:** Navegación estándar; sin revelaciones internas.

**Notas:** Los dibujos son ilustrativos. Para productos físicos usaremos el mismo procedimiento: representar presentación, selección, personalización, solicitud o interés; no simular su funcionamiento físico como si fuera real. En soluciones técnicas avanzadas, un resultado ficticio claramente marcado puede representar una lógica aún no implementada. No abrir actividades adicionales.

**Tiempo:** 3 min.

**Archivos:** `assets/content/illustrations/paper.svg`, `assets/content/illustrations/digital.svg`, `assets/content/illustrations/physical.svg`; cabecera C y fuente común.

### 07 — Conozcamos Tanda

**Objetivo:** Introducir el caso continuo antes de hablar de funcionalidad principal.

**Título visible:** Conozcamos Tanda

**Contenido visible exacto:**

- Caso ficticio · App web para reservar citas en barberías
- Problema
- Reservar por WhatsApp puede requerir esperar respuestas y coordinar repetidamente los horarios disponibles.
- Solución
- Una plataforma web donde el cliente elige un servicio, selecciona un horario y reserva su cita.

**Layout:** C. **Composición:** Problema y solución a la izquierda; identidad Tanda y vista de selección de servicio a la derecha. Reutilizar screen-01.png como vista representativa completa.

**Interacción:** Navegación estándar; sin revelaciones internas.

**Notas:** Presentar Tanda como un ejemplo inventado para aprender, no como una empresa real. Describir la fricción y la propuesta, sin afirmar validación comercial. No explicar todavía los cinco pasos.

**Tiempo:** 4 min.

**Archivos:** `assets/content/tanda/screen-01.png`, `assets/content/tanda/tanda-mark.svg`; cabecera C y fuente común.

### 08 — ¿Qué es la funcionalidad principal?

**Objetivo:** Reconocer la acción central y limitar el alcance del prototipo.

**Título visible:** ¿Qué es la funcionalidad principal?

**Contenido visible exacto:**

- Es la acción más importante que nuestra solución debe permitir realizar al usuario.
- Primero: una acción que entregue el valor central.
- Después: funciones complementarias.
- El primer prototipo no necesita incluirlo todo.

**Layout:** C. **Composición:** Definición grande y contraste de prioridad Primero / Después, sin introducir otro caso.

**Interacción:** Navegación estándar; sin revelaciones internas.

**Notas:** Pedir que formulen una acción, no una lista de pantallas ni una lista de funciones. Mantener el término funcionalidad principal. El prototipo puede representar solo esa acción y dejar fuera las funciones secundarias.

**Tiempo:** 4 min.

**Archivos:** cabecera C y fuente común.

### 09 — ¿Cómo elegimos la funcionalidad principal?

**Objetivo:** Dar tres criterios concretos para decidir qué prototipar.

**Título visible:** ¿Cómo elegimos la funcionalidad principal?

**Contenido visible exacto:**

- ¿Qué necesita lograr el usuario?
- ¿Qué acción representa el valor central de nuestra solución?
- ¿Qué parte podemos mostrar y probar primero?

**Layout:** C. **Composición:** Tres preguntas numeradas de lectura vertical, con espacio amplio y sin matrices.

**Interacción:** Navegación estándar; sin revelaciones internas.

**Notas:** Pedir una respuesta breve a cada pregunta desde sus insumos previos. Evitar volver a impartir descubrimiento o ideación. Si hay muchas acciones candidatas, elegir una que pueda recorrerse de principio a fin en esta sesión; no prometer que esa selección valida el negocio.

**Tiempo:** 5 min.

**Archivos:** cabecera C y fuente común.

### 10 — La funcionalidad principal de Tanda

**Objetivo:** Aplicar la definición al único caso desarrollado.

**Título visible:** La funcionalidad principal de Tanda

**Contenido visible exacto:**

- Reservar una cita en una barbería sin tener que coordinar manualmente por mensajes.
- Fuera de este primer prototipo
- Perfiles · Reseñas · Fidelización · Notificaciones

**Layout:** C. **Composición:** Acción central destacada a la izquierda, misma pantalla 1 de Tanda a la derecha; funciones complementarias en un renglón subordinado.

**Interacción:** Navegación estándar; sin revelaciones internas.

**Notas:** Preguntar qué valor se logra al completar una reserva. Perfiles, reseñas, fidelización y notificaciones pueden ser útiles más adelante; no se desarrollarán ahora. No adelantar todavía las respuestas de la dinámica.

**Tiempo:** 4 min.

**Archivos:** `assets/content/tanda/screen-01.png`; cabecera C y fuente común.

### 11 — ¿Qué es el camino feliz?

**Objetivo:** Convertir una acción central en una secuencia observable.

**Título visible:** ¿Qué es el camino feliz?

**Contenido visible exacto:**

- Es la secuencia de pasos que sigue el usuario para completar la funcionalidad principal cuando todo ocurre como se espera.
- Tiene un objetivo concreto.
- Avanza de principio a fin.
- Evita errores y excepciones.
- Puede describirse en pocos pasos.
- Inicio
- Acción
- Resultado

**Layout:** C. **Composición:** Definición, cuatro características breves y flujo abstracto de tres nodos. No mostrar todavía los pasos de Tanda.

**Interacción:** Navegación estándar; sin revelaciones internas.

**Notas:** El camino feliz describe el recorrido esperado, no todas las validaciones, cancelaciones o fallos posibles. No elimina la necesidad futura de tratar errores; solo delimita el primer prototipo. La siguiente dinámica permite descubrir pasos a partir de pantallas.

**Tiempo:** 5 min.

**Archivos:** cabecera C y fuente común.

### 12 — Descubramos el camino feliz de Tanda

**Objetivo:** Inferir las primeras tres acciones a partir de pantallas.

**Título visible:** Descubramos el camino feliz de Tanda

**Contenido visible exacto:**

- Parte 1 · ¿Qué está haciendo el usuario?
- Seleccionar servicio
- Elegir fecha y horario
- Ingresar datos de reserva

**Layout:** C. **Composición:** Una pantalla móvil completa a la derecha, siempre en la misma caja. A la izquierda, tres posiciones numeradas con respuestas inicialmente ocultas. Las respuestas reveladas permanecen. Capturas 1, 2 y 3 reemplazadas en una pila fija.

**Interacción:** 5 avances internos, según la secuencia determinista anterior.

**Notas:** Estado inicial: solo pantalla 1 y pregunta. Esperar respuestas; avanzar revela el nombre. El avance siguiente cambia a pantalla 2 sin revelar su respuesta. Repetir con pantalla 3. No leer una lista de pasos antes de pedir que observen. Flecha izquierda deshace un estado; R reinicia. Al volver desde otra diapositiva se reinicia para poder repetir.

**Tiempo:** 6 min.

**Archivos:** `assets/content/tanda/screen-01.png`, `assets/content/tanda/screen-02.png`, `assets/content/tanda/screen-03.png`; cabecera C y fuente común.

### 13 — Descubramos el camino feliz de Tanda

**Objetivo:** Completar la reserva y sintetizar el recorrido de cinco pasos.

**Título visible:** Descubramos el camino feliz de Tanda

**Contenido visible exacto:**

- Parte 2 · ¿Qué está haciendo el usuario?
- Revisar y confirmar la reserva
- Ver la confirmación de la cita
- El recorrido completo
- Seleccionar servicio
- Elegir horario
- Ingresar datos
- Confirmar
- Ver confirmación

**Layout:** C. **Composición:** Pantallas 4 y 5 en la misma caja derecha; respuestas a la izquierda. El último avance presenta la secuencia completa de cinco pasos en esa zona izquierda, manteniendo la pantalla de confirmación a la derecha.

**Interacción:** 4 avances internos, según la secuencia determinista anterior.

**Notas:** Repetir pregunta → respuesta → siguiente pantalla. En el último estado recorrer los cinco verbos y relacionarlos con reservar una cita. Un flujo observable puede convertirse en pantallas y acciones. La confirmación pertenece a la simulación; ninguna cita real se registra.

**Tiempo:** 4 min.

**Archivos:** `assets/content/tanda/screen-04.png`, `assets/content/tanda/screen-05.png`; cabecera C y fuente común.

### 14 — Ahora le toca a tu equipo

**Objetivo:** Definir la funcionalidad principal y el camino feliz propios.

**Título visible:** Ahora le toca a tu equipo

**Contenido visible exacto:**

- Actividad grupal · 20 minutos
- A partir del problema y la solución que ya definieron:
- Identifiquen la funcionalidad principal.
- Describan el camino feliz en 3–5 pasos.
- Completen la plantilla compartida de Google Docs.
- Opcional: elijan un color principal.

**Layout:** C. **Composición:** Instrucciones numeradas y un bloque de tiempo de 20 minutos; margen operativo de tres minutos solo en notas. Sin enlaces ficticios.

**Interacción:** Navegación estándar; sin revelaciones internas.

**Notas:** Usar 3 minutos para instrucciones, compartir el documento real y desplazarse a salas; 20 minutos de trabajo. Mostrar brevemente el selector de colores en vivo, sin otra slide. Preparar antes una copia real del material en Google Docs y permisos de edición. Recordar que los problemas y soluciones son insumos existentes. Revisar una acción y 3–5 pasos por equipo. Si sobra tiempo, pedir intervenciones voluntarias oralmente, sin ronda ni slide adicional.

**Tiempo:** 23 min.

**Archivos:** `materials/plantilla-trabajo-equipo.md`; cabecera C y fuente común.

### 15 — De nuestra idea al prototipo

**Objetivo:** Pasar de los insumos del equipo a una construcción individual guiada.

**Título visible:** De nuestra idea al prototipo

**Contenido visible exacto:**

- Problema + Solución
- Funcionalidad principal + Camino feliz
- Prompt
- Google AI Studio
- Prototipo
- Cada integrante genera su propia versión.
- Seguimos la demostración en vivo con Tanda.

**Layout:** C. **Composición:** Flujo visual de insumos → prompt → Google AI Studio → prototipo; sin logos de herramientas inventados. Pie breve explica trabajo individual. La diapositiva permanece como transición, no es un tutorial de clics.

**Interacción:** Navegación estándar; sin revelaciones internas.

**Notas:** Distribuir 38 minutos: 4 para conectar los insumos y abrir Google Docs; 8 para mostrar el prompt de Tanda y construir en AI Studio; 20 para que cada estudiante genere y recorra su versión; 6 para comprobar la finalización y volver. Compartir pantalla en el entorno de construcción de aplicaciones web de Google AI Studio, no en un chat genérico. Verificar acceso, disponibilidad y cuenta del facilitador y estudiantes antes del taller; la herramienta real requiere conexión y puede requerir cuenta, aunque la app generada no debe pedir cuentas. Usar datos ficticios, sin backend, APIs ni persistencia. Para lógica sofisticada, etiquetar resultados simulados. Evitar convertir la sesión en programación, Firebase, despliegue o depuración. Si una generación falla, reintentar el mismo alcance y usar el resultado disponible para explicar lo que sí permite observar; no prometer disponibilidad de la herramienta.

**Tiempo:** 38 min.

**Archivos:** `materials/plantilla-trabajo-equipo.md`, `materials/ejemplo-tanda.md`; cabecera C y fuente común.

### 16 — Elijan el prototipo de su equipo

**Objetivo:** Comparar versiones y seleccionar una con criterios simples.

**Título visible:** Elijan el prototipo de su equipo

**Contenido visible exacto:**

- Regresen a sus equipos.
- Comparen los prototipos generados.
- Elijan el que mejor represente la funcionalidad principal y el camino feliz.
- Si queda tiempo, realicen una mejora concreta.
- Claridad · Representación de la solución · Posibilidad de probarlo

**Layout:** C. **Composición:** Cuatro instrucciones ordenadas y tres criterios de selección como cierre de lectura.

**Interacción:** Navegación estándar; sin revelaciones internas.

**Notas:** Asignar aproximadamente 1 minuto para volver a salas, 3 para comparar y 2 para elegir o mejorar. No elegir por la cantidad de funciones ni exigir evaluación técnica. Comprobar que se puede completar el flujo y que cada integrante entiende por qué eligieron esa versión.

**Tiempo:** 6 min.

**Archivos:** cabecera C y fuente común.

### 17 — ¿Cómo validamos el prototipo?

**Objetivo:** Preparar una prueba de uso sin confundir usabilidad con demanda.

**Título visible:** ¿Cómo validamos el prototipo?

**Contenido visible exacto:**

- Presenta una situación y una tarea.
- Deja que la persona lo intente sin ayuda.
- Observa dónde duda o se detiene.
- Registra resultados y comentarios.
- «Imagina que quieres reservar un corte para mañana. Muéstrame cómo lo harías».
- Completar la tarea no demuestra demanda comercial.

**Layout:** C. **Composición:** Procedimiento breve a la izquierda y tarea ejemplificada a la derecha; distinción de demanda visible abajo. Sin nueva actividad obligatoria.

**Interacción:** Navegación estándar; sin revelaciones internas.

**Notas:** No decir dónde hacer clic ni corregir durante la tarea. Observar antes de preguntar qué esperaba la persona. Registrar si completó sin ayuda y dónde dudó. Para el ejemplo fijo, situar la prueba el 19 de noviembre de 2026: mañana es el 20. Una demostración voluntaria es opcional solo si queda tiempo dentro de este bloque. Explicar que un recorrido fácil no prueba intención de pago, adopción ni demanda. Reiniciar antes de otra prueba.

**Tiempo:** 4 min.

**Archivos:** `materials/guia-validacion.md`; cabecera C y fuente común.

### 18 — Una idea se vuelve más clara cuando alguien puede probarla.

**Objetivo:** Cerrar con una idea memorable que sintetice el aprendizaje.

**Título visible:** Una idea se vuelve más clara cuando alguien puede probarla.

**Contenido visible exacto:**

- Una idea se vuelve más clara cuando alguien puede probarla.
- Prototipa. Observa. Aprende. Mejora.

**Layout:** C-cierre. **Composición:** Cabecera C intacta y mensaje grande, con amplio espacio blanco. Sin image7.png detrás del texto. D queda disponible como recurso, no añade una diapositiva.

**Interacción:** Navegación estándar; sin revelaciones internas.

**Notas:** Dar unos segundos para leer. Cerrar recuperando el objetivo: una representación concreta y un flujo que pueden observar con otras personas. Agradecer sin añadir tareas, agenda ni próximos pasos no acordados.

**Tiempo:** 1 min.

**Archivos:** cabecera C y fuente común.

