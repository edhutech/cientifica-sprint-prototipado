# Inventario de recursos del presentador

**Estado: recursos recibidos y verificados técnicamente; calidad disponible aceptada por el usuario.** Wichay se excluye. Se autoriza adaptar el color de logos blancos y recortar márgenes vacíos al componer «Sobre mí», conservando los archivos recibidos.

Se recibieron **16 archivos de logos y 1 fotografía**. Los 17 cargan en Chromium y se conservaron sin cambios de bytes, nombres ni formatos. Hay correspondencia visual para **9 de las 10 marcas inicialmente solicitadas**; Wichay se omite por indicación del usuario.

## Procedencia, restricciones y significado de los estados

**S1 — fuente para cada archivo del inventario:** entrega manual del usuario en `assets/content/presenter/`. **URL original: no proporcionada** para ninguno de los 17 archivos. No se atribuye una URL institucional a un archivo por su nombre ni por su apariencia. La identidad visual observada no certifica que esta copia sea la versión oficial vigente.

**R0 — condiciones conocidas para cada archivo:** no se aportaron licencias ni manuales de uso de marca. No se presume licencia libre. Los originales se conservan tal como fueron entregados. El usuario autorizó posteriormente las adaptaciones de color y encuadre descritas abajo; no deformar, reconstruir ni eliminar leyendas. El nombre de archivo «removebg-preview» tampoco permite certificar que esa copia no haya sido procesada antes de su entrega.

### Adaptaciones autorizadas para la futura composición

- Utilizar los archivos disponibles con su calidad actual; no solicitar versiones mejores como requisito para avanzar.
- Omitir Wichay de la nube, sin reservarle un espacio ni sustituirlo por otra marca.
- Cambiar las partes blancas de los logos que desaparecen sobre el fondo blanco a un tono oscuro legible, preferentemente el azul `#00358E` ya documentado. Conservar los demás colores y la geometría; no aplicar filtros que alteren indiscriminadamente toda la marca.
- Recortar, cuando haga falta, **solo los márgenes vacíos o el fondo periférico sobrante**: por ejemplo, un archivo cuadrado cuyo logo real es horizontal. Respetar letras, símbolos, leyendas, detalles y un margen de respiro; nunca estirar el logo para llenar una caja horizontal.
- Hacer estas adaptaciones en copias derivadas o mediante encuadre/color de presentación al construir «Sobre mí». Conservar los originales y registrar después qué recurso se adaptó y cómo. No se han generado aún esas variantes.
- El usuario también autoriza recortar la fotografía de perfil para mejorar su encaje en el layout. Conservar rostro y cabeza completos, proporciones y nitidez; aplicar el encuadre mediante CSS o una copia derivada, manteniendo `photo/perfil.png` intacto.
- Estas instrucciones se aplican a los recursos del presentador. No modifican los fondos ni los logos institucionales de Científica Sprint ni `branding/brand-spec.md`.

**HTML técnico: sí** significa que el archivo se decodifica y puede incrustarse mediante URI `data:` sin depender de recursos externos. **Listo para la composición** requiere además un fondo adecuado, tamaño legible, elección de variante y revisión del usuario. La columna final diferencia ambos estados. No se ha construido la diapositiva.

Dimensiones raster en píxeles. En SVG se indica tamaño nominal o `viewBox`; no es una resolución raster ni limita el escalado vectorial. Los SVG revisados contienen trazados y, en algunos casos, estilos o recortes internos; no se encontraron imágenes, fuentes ni enlaces externos dependientes.

## Logos solicitados

Todos los archivos de esta tabla están en `logos/`.

| Organización | Archivo | Fuente / URL | Formato y dimensiones | Verificación visual y restricciones | Preparación HTML |
| --- | --- | --- | --- | --- | --- |
| Startup Perú | `logo-startup-peru 2.svg` | S1 / no proporcionada | SVG, 324 × 60; viewBox 0 0 324 60 | Texto Startup Perú visible, versión multicolor sobre transparencia. R0. Revisar la vigencia contra su fuente cuando se aporte. | Técnico: sí. Apto sobre blanco; pendiente aprobación/procedencia. |
| ProInnóvate | `proinnovate-logo-removebg-preview 2.svg` | S1 / no proporcionada | SVG, 396 × 127; viewBox 0 0 396 127 | Marca ProInnóvate multicolor visible. R0; historial de tratamiento previo no documentado. | Técnico: sí. Apto sobre blanco; pendiente aprobación/procedencia. |
| Microsoft for Startups | `MS_Startups_Celebration_Badge_Dark.webp` | S1 / no proporcionada | WebP, 786 × 336; transparencia en bordes | Insignia púrpura con «Proud to partner with Microsoft for Startups». **Incluye una afirmación de relación**, además de la marca. R0. No recortar la leyenda para obtener otro logo. | Técnico: sí. **Pendiente confirmar que esta insignia corresponde al uso deseado o aportar logo aislado.** |
| Fundación Romero | `fundacion romero.webp` | S1 / no proporcionada | WebP, 614 × 58; transparente | Símbolo naranja y nombre oscuro, legibles sobre blanco. R0. La altura nativa es solo 58 px. | Técnico: sí. Variante adecuada al cuerpo blanco, evitando ampliación de altura; pendiente aprobación. |
| Fundación Romero | `Logo Fundación Romero.svg` | S1 / no proporcionada | SVG, 1000 × 207; viewBox 0 0 1000 207 | Símbolo y nombre blancos. R0. Invisible sobre blanco; nítido sobre oscuro. | Técnico: sí. Adaptación a tono oscuro autorizada si se elige esta variante. |
| SENATI | `logo-horizontal-blanco-web.fw-455x128.png` | S1 / no proporcionada | PNG indexado, 455 × 128; transparente | El contenido visible identifica SENATI; el nombre de archivo por sí solo no lo indicaba. Marca blanca, verificada sobre oscuro. R0. | Técnico: sí. Adaptación a tono oscuro autorizada para fondo blanco. |
| Nutri H | `logo-nutrih-azul 1.svg` | S1 / no proporcionada | SVG, 400 × 400; viewBox 0 0 400 400 | Marca Nutri H azul, sobre transparencia; legible en blanco. R0. | Técnico: sí. Apto sobre blanco; pendiente aprobación/procedencia. |
| BASF | `basf-new.png` | S1 / no proporcionada | PNG RGBA, 736 × 414; alfa completamente opaco | Logo azul y blanco con «We create chemistry», rodeado de un amplio fondo blanco integrado. R0. No es una versión transparente. | Técnico: sí. Se integra sobre blanco conservando los márgenes; tamaño óptico a revisar. |
| NEXUM PUCP | `LOGOTIPO-NEXUM.svg` | S1 / no proporcionada | SVG, 619 × 151; viewBox 0 0 619 151 | Marca NEXUM blanca. La vinculación PUCP responde a la organización solicitada; el archivo muestra NEXUM sin firma universitaria. R0. | Técnico: sí. Adaptación a tono oscuro autorizada para fondo blanco. |
| HUB UDEP | `HUB-UDEP_logo.svg` | S1 / no proporcionada | SVG, 1214 × 194; viewBox 0 0 1214 194 | Marca HUB UDEP blanca, visible y nítida sobre oscuro. R0. | Técnico: sí. Adaptación a tono oscuro autorizada para fondo blanco. |
| Wichay | — | No recibido / URL no proporcionada | — | Excluido por indicación del usuario. | No se utilizará. |

## Recursos adicionales recibidos

Su recepción no implica incluirlos automáticamente en la nube. Las empresas del perfil aprobado mantienen únicamente los cargos expresamente indicados en `profile.md`.

| Organización / recurso | Archivo | Fuente / URL | Formato y dimensiones | Verificación visual y restricciones | Preparación HTML |
| --- | --- | --- | --- | --- | --- |
| CIDE PUCP — Centro de Innovación y Desarrollo Emprendedor | `logos/CENTRO-INNOVACION-DESARROLLO.webp` | S1 / no proporcionada | WebP, 200 × 140; transparente | Identificación por el texto y firma PUCP visibles sobre oscuro. Marca blanca y resolución reducida; microtexto poco legible al reducir. R0. **No corresponde a Wichay ni se utiliza como sustituto de NEXUM.** | Técnico: sí. Pendiente decidir inclusión, variante de fondo y calidad suficiente. |
| Guayerd | `logos/guayerd.svg` | S1 / no proporcionada | SVG sin width/height explícitos; viewBox 0 0 369.67 95.88 | Nombre blanco con acento celeste; sobre blanco solo se distingue el acento. R0. Definir tamaño HTML con la proporción del viewBox. | Técnico: sí. Uso condicionado a fondo oscuro o nueva variante original. |
| Guayerd — icono | `logos/guayerd ico.webp` | S1 / no proporcionada | WebP, 474 × 474; opaco | Icono «g» azul/blanco con fondo blanco integrado. R0. No equivale a una firma completa con nombre. | Técnico: sí. Apto sobre blanco; pendiente elegir entre icono y firma, sin duplicar automáticamente. |
| AI PlayGrounds — icono aportado | `logos/ai_playground_per_logo.jpeg` | S1 / no proporcionada | JPEG, 200 × 200; opaco | Símbolo azul y amarillo con fondo blanco. **La atribución se basa en el nombre del archivo y el contexto aportado; no contiene un nombre legible que permita confirmarla por sí solo.** R0. Se aprecia baja resolución y mucho margen. | Técnico: sí. Pendiente confirmar identidad y tamaño; preferible original de mayor resolución o vector. |
| LetyMind | `logos/LetyMind-Full-name.svg` | S1 / no proporcionada | SVG, 373 × 80; viewBox 0 0 373 80 | Firma completa blanca, legible sobre oscuro. R0. | Técnico: sí. Uso condicionado a fondo oscuro o nueva variante original. |
| LetyMind — icono | `logos/LetyMind ico.svg` | S1 / no proporcionada | SVG, 49 × 46; viewBox 0 0 49 46 | Símbolo oscuro sin nombre, nítido y escalable. R0. | Técnico: sí. Apto sobre blanco; pendiente elegir icono o firma completa. |
| Fotografía del presentador | `photo/perfil.png` | S1 / no proporcionada | PNG indexado, 400 × 400; opaco, 1:1 | Retrato suministrado por el usuario, apertura y visualización correctas. R0 respecto de condiciones no documentadas. No sustituido ni modificado. | Técnico: sí. **Calidad condicionada:** caja prevista de 420 px implica ampliación 1,05×; preferible versión ≥840 × 840. |

Requisitos detallados de fotografía: [photo/README.md](photo/README.md).

## Hoja de contacto y verificación

- [Hoja de contacto sobre blanco](../../../output/presenter/logos-contact-sheet-light.png).
- [Hoja de contacto sobre oscuro](../../../output/presenter/logos-contact-sheet-dark.png).
- [Registro técnico de los 17 recursos](../../../output/presenter/resource-checks.json): dimensiones, transparencia, hashes SHA-256, referencias SVG y resultados de carga en Chromium.

Las hojas incluyen los **16 archivos de logos**, también las variantes y adicionales, con nombres de archivo para trazabilidad. El fondo oscuro es exclusivamente una superficie diagnóstica que permite ver los logos blancos; no cambia el layout ni la identidad visual aprobada. Los archivos no se recolorearon ni recortaron. La foto fue revisada por separado y está incluida en la prueba técnica de carga.

**Revisión realizada:** los 17 recursos cargan como imágenes incrustadas mediante `data:` en Chromium 155; las dos hojas se revisaron visualmente. No hay archivos corruptos ni referencias externas en los SVG. Los logos tienen tamaños ópticos, márgenes y fondos distintos; esta fase no los normaliza alterando su arte. El fondo blanco integrado de BASF y de los iconos se conserva.

La futura nube será **una sola composición sin encabezados, categorías ni etiquetas adicionales**. Los nombres y numeración de las hojas son únicamente anotaciones de revisión. No se ha construido esa composición ni se ha cambiado `branding/brand-spec.md`.

## Decisiones registradas y revisión restante

1. **Wichay:** excluido; no se espera un archivo.
2. **Fondo blanco y encuadre:** se autoriza oscurecer las partes blancas de los logos y recortar márgenes sobrantes cuando sea necesario, según las reglas anteriores. Esto incluye firmas completas como Guayerd y LetyMind si se seleccionan. Los originales permanecerán intactos.
3. **Microsoft for Startups:** confirmar el uso de la insignia con la afirmación «Proud to partner with», o proporcionar el recurso de marca apropiado para una nube de logos.
4. **Procedencia:** URLs de origen, variantes vigentes y condiciones de uso no suministradas para todos los archivos. Quedan registrados como aportados por el usuario, no como descargas oficiales verificadas.
5. **Selección:** confirmar si CIDE PUCP y los recursos adicionales de Guayerd, AI PlayGrounds y LetyMind también integrarán la nube, y elegir las variantes sin duplicar marcas. Confirmar la atribución del icono AI PlayGrounds.
6. **Calidad:** el usuario confirmó que no hay mejores versiones; trabajar con las recibidas. Ajustar el tamaño de presentación a su nitidez y evitar ampliaciones innecesarias. La foto actual puede utilizarse a ≤400 px sin ampliación.

**El proceso se detiene aquí para revisión y aprobación.** No se generó `deck/deck-spec.md` ni la presentación definitiva. Los recursos institucionales de Científica Sprint permanecen intactos.
