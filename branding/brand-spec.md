# Identidad visual — Científica Sprint

**Proyecto:** taller Prototipado Digital · **Ponente:** Edhú Nuñez Alvarado.

**Estado:** especificación visual documentada y pruebas técnicas A/C verificadas en Chromium. La extracción fue aprobada por el usuario. La tipografía sustituta es provisional; el contenido y la estructura pedagógica se definirán posteriormente.

## 1. Fuentes y criterio de fidelidad

Fuente principal: [`sources/Copy of PPT Plantila - Científica Sprint.pptx`](../sources/Copy%20of%20PPT%20Plantila%20-%20Científica%20Sprint.pptx). Referencias auxiliares:

- [Reporte de extracción](../output/extraction-report.md) y [registro técnico](../output/resource-inventory.json).
- Recursos originales en `assets/institutional/originals/`.
- Capturas originales: [1](../output/template-slide-1.png), [2](../output/template-slide-2.png), [3](../output/template-slide-3.png), [4](../output/template-slide-4.png), [5](../output/template-slide-5.png). Son renderizados de LibreOffice, no de PowerPoint.

Este documento deriva la identidad **de esta plantilla**, sin presentarse como un manual corporativo oficial. Distingue:

- **Observado:** recursos, colores, tipografías y geometría presentes en el PPTX.
- **Adaptación HTML:** medidas funcionales para texto y contenido que el PPTX no define, o correcciones de composición solicitadas por el usuario.
- **Pendiente:** información o recursos aún no proporcionados.

Prioridad: recursos originales → geometría del PPTX → intención de composición → adaptación legible. No convertir las capturas completas en diapositivas: sus textos quedarían rasterizados y se trasladarían las superposiciones detectadas.

## 2. Paleta y contraste

| Color | HEX | Evidencia | Uso |
| --- | --- | --- | --- |
| Azul institucional de la franja | `#00358E` | Color plano dominante de la franja de `image2.png` | Conservar en el fondo; reutilizar en títulos y trazos del cuerpo blanco como adaptación. |
| Naranja de acento | `#F68D20` | `a:srgbClr` de la barra vertical, diapositivas 2 y 5 | Barra del ponente y acentos discretos. |
| Blanco | `#FFFFFF` | Texto explícito, firmas y cuerpo de diapositiva 3 | Texto sobre fondos oscuros; superficie del contenido. |
| Negro | `#000000` | Zonas oscuras de `image2.png` y color base del tema | Texto de contenido y bandas exteriores del lienzo. |
| Naranja de firma, variante 1 | `#F08415` | Trazados de `image6.svg` | Mantener dentro del logo; no sustituir por el naranja de la barra. |
| Naranja de firma, variante 2 | `#EE7220` | Trazados de `image6.svg` | Mantener dentro del logo. |

Las fotografías y el logo Sprint contienen gradaciones adicionales que se conservan mediante los originales. No reducirlos a colores planos ni aplicarles filtros nuevos. El tema XML se llama **Office** y contiene colores genéricos; no usarlos como evidencia de una paleta institucional ampliada.

```css
:root {
  --brand-blue: #00358e;
  --brand-orange: #f68d20;
  --paper: #ffffff;
  --ink: #000000;
}
```

### Legibilidad

- Texto azul/blanco: **11,05:1**; negro/blanco: **21:1**. Son combinaciones de referencia para el cuerpo editable.
- Naranja `#F68D20` sobre blanco: **2,40:1**. Reservarlo para decoración; no para texto informativo ni trazos cuya identificación sea indispensable. Naranja sobre azul: **4,61:1**.
- Objetivo para texto HTML: al menos 4,5:1 en texto normal y 3:1 en texto grande. Comprobar sobre el fondo real, no solamente sobre un token de color.
- En la prueba A, el contraste mínimo conservador de blanco frente a todos los píxeles del fondo bajo las cajas de texto es superior a **19:1**.
- Conservar el diseño de los logos originales; no recolorearlos para corregir un problema de contraste. Colocarlos en el fondo oscuro previsto.
- No añadir texto sobre rostros, manos, logos, firma inferior o detalles fotográficos claros. No resolver falta de espacio con sombras, velos o desenfoques adicionales.

## 3. Tipografía y jerarquía

### Identificación original

El PPTX declara **Gotham** para texto regular y **Gotham Bold** para texto destacado; el PDF de referencia identifica **Gotham-Book** y **Gotham-Bold** incrustadas.

| Elemento original | Fuente / peso funcional | Tamaño PPTX | Equivalente a 96 ppp |
| --- | --- | --- | --- |
| Título de ponencia | Gotham / regular | 110 pt | 146,67 px |
| Sesión | Gotham Bold / negrita | 43,29 pt | 57,72 px |
| Etiqueta de ponente | Gotham / regular | 25,77 pt | 34,36 px |
| Nombre del ponente | Gotham Bold / negrita | 25,77 pt | 34,36 px |

Mapeo HTML: regular `400`, negrita `700`, usando archivos reales de cada peso. El título de portada mantiene el peso regular y domina por tamaño; no convertir todo a negrita. Las mayúsculas de los logos forman parte del arte original; no recrearlas con texto.

### Fuentes web y condiciones de uso

1. **Preferencia:** Gotham en una versión web cuya licencia autorice el uso y la modalidad de distribución del HTML autocontenido. Confirmar permiso de incrustación y redistribución, no solo instalación local.
2. Los archivos `assets/institutional/fonts/*.fntdata` son contenedores EOT extraídos para inspección. No asumir compatibilidad web ni autorización de uso; **no convertirlos, incluirlos en el HTML ni redistribuirlos** sin comprobar sus condiciones. No se han utilizado en las pruebas.
3. **Sustitución provisional comprobada: Montserrat 400/700.** Sans geométrica de proporciones próximas, disponible bajo SIL Open Font License 1.1. No es idéntica a Gotham: verificar saltos, anchura y altura al reemplazarla.
4. **Alternativa secundaria: Manrope 400/700**, también SIL OFL 1.1, con una apariencia geométrica compatible pero diferencias más marcadas en métricas. No descargada ni probada aquí; requiere nueva comprobación de composición si se elige.

Fuentes de licencia: [Montserrat](https://raw.githubusercontent.com/google/fonts/main/ofl/montserrat/OFL.txt) y [Manrope](https://raw.githubusercontent.com/google/fonts/main/ofl/manrope/OFL.txt).

Las pruebas usan TTF web de Montserrat obtenidas de Google Fonts, embebidas mediante `@font-face` y URI `data:`. Procedencia y hashes: `tmp/brand-proof-fonts/provenance.json`. La licencia completa está en `tmp/brand-proof-fonts/OFL.txt` y en cada HTML. El archivo definitivo deberá conservar los avisos de la fuente elegida. No depender de Google Fonts en tiempo de ejecución ni de una instalación local que altere el resultado entre equipos.

### Escala HTML de referencia — adaptación

Medidas a 1920 × 1080; se reducen proporcionalmente en los dos tamaños de revisión. No son tamaños educativos existentes en el PPTX: su diapositiva 3 tiene el cuerpo vacío.

| Función | Peso | Tamaño Full HD | A 1366 × 768 aprox. | Interlineado |
| --- | --- | --- | --- | --- |
| Título A, dos líneas | 400 | 112 px | 79,64 px | 1,15 |
| Ponente A | 400 / 700 | 34,36 px | 24,43 px | 1,20 |
| Título educativo / nombre B | 700 | 64 px | 45,51 px | 1,15 |
| Subtítulo de contenido | 700 | 42 px | 29,87 px | 1,20 |
| Cuerpo principal | 400 | 36 px | 25,60 px | 1,45 |
| Apoyo / experiencia B | 400 | 32 px | 22,76 px | 1,35–1,45 |

Mantener espaciado de letras normal. Evitar condensación, escalado horizontal, negrita sintética y reducción arbitraria para encajar. Los límites mínimos de `clamp()` son protecciones técnicas, no permiso para densificar diapositivas. Si el contenido no cabe, solicitar una redistribución sin alterar decisiones pedagógicas.

## 4. Lienzo, proporciones y espaciado

**Observado:** formato 16:9, 18 288 000 × 10 287 000 EMU. Coordenadas de este documento en un lienzo de **1920 × 1080**. Conversión: `px = EMU / 9525`.

- Cada diapositiva ocupa `100vh` con alternativa moderna `100dvh` y `overflow: hidden`.
- Dentro, un lienzo centrado de proporción fija 16:9: `width: min(100vw, calc(100dvh * 16 / 9))`, `aspect-ratio: 16 / 9`. Conservar también la declaración equivalente con `100vh` como respaldo.
- Escala `s = min(anchoViewport / 1920, altoViewport / 1080)`. Posiciones, imágenes y fuentes deben usar el mismo sistema, no porcentajes de marcos distintos sin conversión.
- 1920 × 1080: escala 1. 1366 × 768: escala ≈0,711111; lienzo ≈1365,33 × 768 y bandas laterales de ≈0,33 px. La ligera diferencia respecto a 16:9 no justifica estirar el fondo.
- Fuera de 16:9: conservar proporción y usar bandas negras; nunca recortar logos para llenar la ventana. Los tamaños distintos de los dos solicitados requieren QA propio. Las pruebas no certifican lectura en pantallas verticales pequeñas.
- Margen horizontal de referencia: **108 px / 5,625 %** por lado. En la cabecera es derivado de posiciones originales; en el cuerpo es una adaptación alineada a ellas.
- Cabecera C: **215 px / 19,907407 %** del alto; cuerpo disponible hasta el borde inferior: 865 px.
- Área editorial C: x=108…1812, y=269…1008. Dejar 54 px entre cabecera y título, y 72 px al borde inferior. Ancho útil 1704 px.
- Dos columnas: 816 px + separación de 72 px + 816 px. Separaciones funcionales: 24 px entre piezas relacionadas, 36 px entre bloques de texto y 54–72 px entre áreas mayores. Son medidas de adaptación, no una retícula declarada por la institución.

Usar porcentajes para anclajes y unidades de contenedor `cqw` para escala tipográfica; `1cqw = anchoDelLienzo / 100`. Ejemplo de título A: `clamp(28px, 5.833333cqw, 112px)`. No confundir el ancho del lienzo con el viewport cuando haya bandas.

## 5. Fotografías, fondos y logos

| Recurso original | Destino |
| --- | --- |
| `image2.png` | Fondo obligatorio A. Conservar hombre, oscurecimiento, pestaña azul, Sprint y firma inferior integrados. |
| `image3.png` | Fondo de cabecera C y derivación B; reproducir recorte superior original. |
| `image4.png` | Logo Sprint independiente de cabecera. Conservar transparencia y recorte. |
| `image6.svg` | Firma institucional preferida para cabecera. Escala vectorial sin reconstrucción. |
| `image5.png` | Alternativa PNG a `image6.svg`, en la misma caja, no junto a él. |
| `image7.png` | Cierre D, imagen institucional completa. |
| `image1.png` | Portada promocional de referencia; contiene textos rasterizados, no sustituye a la portada del taller. |
| `image8.png` | Variante original de ponencia con mujer; conservar disponible, sin sustituir el fondo A solicitado. |

Todos los nombres anteriores corresponden a `assets/institutional/originals/`. Los originales son inmutables. Las imágenes personales, logos profesionales y capturas del taller se incorporarán después en `assets/content/`.

- No duplicar los logos que ya están integrados en A o D; tampoco superponer el logo independiente para «mejorarlos».
- No deformar, recolorear, redibujar, retirar textos o aplicar nuevas sombras a logos y fondos. Las extensiones de imagen descritas en §7 reproducen el tratamiento original, no son un rediseño.
- Fondos completos A/D: llenar el lienzo 16:9 sin recortar la composición. El recorte leve original de D se detalla en §9.
- Fotografías de contenido: respetar su proporción; `object-fit: contain` como regla. Un recorte de retrato debe conservar rostro y cabeza, y revisarse cuando llegue la fotografía.
- La persona fotografiada en `image2.png` forma parte del fondo institucional; **no representa la fotografía personal de Edhú**. Esta se utilizará únicamente en B cuando sea proporcionada.
- Mantener la cabecera libre de texto educativo y controles. Su separación del contenido forma parte del sistema.

## 6. Layout A — portada del taller

**Base observada:** diapositiva 2. **Texto autorizado:** «Prototipado Digital» y «Edhú Nuñez Alvarado».

1. Colocar `image2.png` en x=0, y=0, 1920 × 1080. Conservar exactamente su arte integrado.
2. Título HTML regular blanco en dos líneas: **Prototipado / Digital**. x=108, y≈421,47, ancho≈807,13. Tamaño 112 px, interlineado 1,15 y 12 px de reserva inferior para descendentes de la tipografía.
3. Ponente en un bloque HTML separado: x=108, y≈763,57, ancho≈807,13 y alto mínimo≈89,97. Barra izquierda naranja de 15 px; separación interior aproximada de 22 px después de la barra. Etiqueta «Ponente:» regular y nombre en negrita, ambos a 34,36 px.
4. Conservar la pestaña azul del fondo. **No inventar un número de sesión.** En la prueba queda sin texto; una etiqueta se incorporará solo cuando sea proporcionada.
5. Límite derecho de todas las cajas de texto: x≤915,13. La mitad derecha, desde x=960, es zona protegida para fotografía y recursos institucionales. Conservar además la franja inferior original.

### Corrección de superposiciones

El título de ejemplo original tiene 146,67 px equivalentes y un ajuste que en LibreOffice produce tres líneas. No copiar esa disposición. La adaptación reduce el título a 112 px y controla sus dos líneas de forma explícita, conservando peso, color, alineación y dominancia.

En la prueba final, el título termina aproximadamente en y=691,05 y el bloque del ponente empieza en y=763,56: **72,52 px de separación**; a 1366 × 768 quedan **51,59 px**. No hay solapamiento con el ponente ni invasión de la mitad derecha. Cualquier cambio de título, fuente o nombre obliga a verificar nuevamente las cajas y el resultado visual.

## 7. Layout C — diapositivas educativas

**Base observada:** diapositiva 3. Cabecera institucional fija y cuerpo blanco editable.

### Geometría exacta de la cabecera

Coordenadas absolutas sobre 1920 × 1080, obtenidas del XML; redondeo mostrado a dos decimales.

| Elemento | x | y | ancho | alto |
| --- | ---: | ---: | ---: | ---: |
| Ventana de fotografía | 0 | 0 | 1920 | 215 |
| Ventana del logo Sprint | 108 | 41,99 | 286,32 | 136,76 |
| Firma institucional | 1180,74 | 69,83 | 631,26 | 81,08 |

Ambos logos mantienen sus posiciones, escala y espacios originales. La firma termina en x=1812, dejando 108 px a la derecha. El cuerpo HTML comienza debajo de y=215, sin invadir la cabecera.

**Regla de traducción de `fillRect`:** cada valor XML se divide entre 1000 para obtener el porcentaje. Para `l,t,r,b`: `left=l%`, `top=t%`, `width=(100-l-r)%`, `height=(100-t-b)%`, dentro de una ventana con `overflow:hidden`.

- `image3.png`: ventana 1920 × 215; `left:0; top:0; width:100%; height:502.325%`. Corresponde a `b=-402325`: muestra la parte superior de la fotografía, sin comprimirla ni centrarla verticalmente.
- `image4.png`: ventana de la tabla; imagen interior `left:-23.653%; top:-175.75%; width:149.879%; height:418.775%`. Corresponde a los cuatro valores de recorte del PPTX. El amplio margen transparente del PNG no es margen editorial; no usar `contain` sobre el archivo entero en esta ventana.
- `image6.svg`: ventana de firma de la tabla, sin recorte. `image5.png` ocupa exactamente la misma caja como alternativa. Un `<picture>` permite preferir SVG; el respaldo PNG de `<picture>` no sustituye una validación de carga si el SVG está corrupto.

Al posicionar dentro del contenedor de cabecera, los porcentajes verticales se calculan sobre **215**, no sobre 1080. Por ejemplo, logo Sprint `top:19.530977%` y `height:63.6114%` de la cabecera. La implementación de referencia está en `tmp/brand-proof.css`.

### Cuerpo editable y variaciones

Título azul de 64 px en x=108, y=269; cuerpo negro sobre blanco. El área de contenido no adopta una caja oscura ni nuevos degradados. La retícula se adapta al material aprobado:

| Variación | Distribución permitida |
| --- | --- |
| Definición | Título, un bloque principal y apoyo breve; una sola columna, con ancho de lectura moderado. |
| Comparación | Dos columnas equivalentes de 816 px, separadas por 72 px; mismas jerarquías y alineaciones. Los rótulos provienen del contenido aprobado. |
| Diagrama | Área central amplia; conectores azules y texto negro; naranja solo como énfasis. Conservar etiquetas legibles, sin encoger para acomodar nodos. |
| Imagen | Recurso proporcional y texto de apoyo lateral o inferior. Evitar recortar información de la imagen. |
| Capturas móviles | Capturas verticales completas, alineadas y con escala consistente; sin marcos de teléfonos inventados. Si el texto de interfaz no se lee, solicitar una vista ampliada o distribución adicional. |
| Actividad grupal | Consigna, pasos, tiempo y resultado esperado solo cuando se proporcionen; agrupación visual mediante espacios y alineación, sin inventar instrucciones. |

No todos los layouts necesitan columnas, tarjetas o bordes. El rectángulo de la prueba C identifica un área técnica de recurso y no obliga a enmarcar imágenes en la presentación definitiva. La capacidad se valida con el contenido real; no se fija un número de diapositivas ni una secuencia pedagógica aquí.

## 8. Layout B — presentación del facilitador

**Adaptación derivada de C**, ya que el PPTX no incluye una biografía. Mantener su misma cabecera, firma, logo, cuerpo blanco, colores y márgenes. Esta distribución es una propuesta funcional para los campos solicitados, no una composición observada en la plantilla.

Retícula de referencia:

- Nombre a la izquierda: x=108, y=269, ancho máximo 1176 px; 64 px, negrita, azul. Usar «Edhú Nuñez Alvarado».
- Posicionamiento profesional debajo, desde y=360, dentro de la misma columna; 36 px regular, hasta dos líneas. **Texto pendiente.**
- Tres líneas de experiencia desde y=492; 32 px, interlineado 1,35, separación entre entradas de 18 px. **Las tres líneas deben ser proporcionadas; no deducirlas de logos.** Si exceden el espacio, revisar su composición con el usuario.
- Fotografía personal: caja x=1392, y=269, 420 × 420 px. Mantener proporción; recorte rectangular solo si permite conservar el rostro y se revisa con el recurso real. Sin sustituirla por la persona del fondo A.
- Nube de logos: x=108, y=761, ancho 1704 y alto máximo 247 px. Una única zona visual, **sin categorías ni subtítulos**. Distribución flexible con `flex-wrap` o grid, proporciones originales, separación de referencia 32–48 px y tamaño óptico equilibrado; no forzar a todos a un mismo ancho.
- No modificar colores de los logos profesionales ni encerrarlos automáticamente en tarjetas. Cantidad y tamaños finales pendientes de los archivos. Si no caben legiblemente, consultar su distribución; no omitir logos silenciosamente.

No inventar posicionamiento, empresas, experiencia ni imágenes. B queda especificado, pero no se renderiza ni se considera validado hasta recibir esos recursos.

## 9. Layout D — cierre institucional

Usar **`image7.png`**, basado en la diapositiva 4: campus, firma central y distintivo original integrados. Cierre visual completo de 1920 × 1080, sin superponer textos, logos adicionales ni datos de contacto no proporcionados.

El grupo del PPTX escala el recurso 1,125× para ocupar todo el lienzo. El relleno añade una extensión horizontal mínima de -0,06 % por lado: reproducible mediante `left:-0.06%; width:100.12%; top:0; height:100%` en un contenedor recortado. No aplicar otro acercamiento ni desplazamiento.

El distintivo y sus textos ya están en la imagen: conservarlos como parte de la fuente institucional, sin actualizarlos ni reconstruirlos. Cualquier mensaje de cierre editable que se solicite después deberá componerse en un área propia y revisarse antes de alterar este cierre.

## 10. Implementación con `html-slides`

- Usar la skill instalada en `.agents/skills/html-slides/` sin modificarla ni instalar otras.
- Incorporar `assets/viewport-base.css` de la skill y aplicar después los estilos institucionales. Los presets genéricos no sustituyen esta identidad.
- HTML final autocontenido: CSS, JS, imágenes y fuente autorizada dentro del archivo; cero solicitudes externas durante la presentación. Los originales del repositorio permanecen sin cambios.
- Mantener la base de viewport, tamaños fluidos con `clamp()` y soporte `prefers-reduced-motion`. La retícula institucional se expresa en el lienzo 16:9, no en posiciones relativas a toda la pantalla.
- Los límites genéricos de imágenes de contenido de la skill se conservan. Los fondos de pantalla completa y las imágenes de relleno de cabecera requieren clases específicas sin `max-height`/`max-width`, con recorte explícito y sin bordes redondeados: de otro modo se alteraría la composición original. Si una captura educativa necesita más espacio que el límite de contenido, usar una variante de imagen amplia documentada y verificar su encaje.
- Usar HTML semántico y textos independientes, editables en el código. No es necesario activar `contenteditable` durante la exposición. Identidad institucional y fondo permanecen fijos al revelar contenido.
- Navegación, transiciones y revelaciones se definirán con la especificación del taller. No animar ni desplazar logos separadamente del marco institucional. Las pruebas de esta fase son estáticas y no constituyen el deck.
- No usar `overflow:hidden` para ocultar fallos de contenido: medir desbordamientos y revisar visualmente. No reducir texto indefinidamente ni cambiar contenido pedagógico para encajarlo.

## 11. Pruebas técnicas y resultado

HTML autocontenidos temporales:

- [`tmp/brand-proof-a.html`](../tmp/brand-proof-a.html): fondo original y textos autorizados de portada.
- [`tmp/brand-proof-c.html`](../tmp/brand-proof-c.html): cabecera original y texto técnico de muestra, sin contenido pedagógico.

| Layout | 1920 × 1080 | 1366 × 768 | Resultado |
| --- | --- | --- | --- |
| A | [Captura](../output/brand-proof/layout-a-1920x1080.png) | [Captura](../output/brand-proof/layout-a-1366x768.png) | Sin colisiones, texto legible, fotografía y logos libres. |
| C | [Captura](../output/brand-proof/layout-c-1920x1080.png) | [Captura](../output/brand-proof/layout-c-1366x768.png) | Cabecera y recortes reproducidos; cuerpo sin desbordamientos. |

Renderizado en **Chromium 155**, DPR 1, viewport exacto mediante DevTools Protocol, red desactivada, espera a fuentes e imágenes cargadas. Las cuatro capturas fueron revisadas visualmente. No se ha certificado equivalencia píxel a píxel con PowerPoint ni validado material futuro.

Resultados completos: [reporte técnico](../output/brand-proof/qa-report.md), [mediciones de composición](../output/brand-proof/composition-checks.json) y [contraste e integridad](../output/brand-proof/visual-measurements.json).

La siguiente especificación de contenido requerirá los materiales del taller. Este documento no crea `deck/deck-spec.md` ni inicia la presentación definitiva.
