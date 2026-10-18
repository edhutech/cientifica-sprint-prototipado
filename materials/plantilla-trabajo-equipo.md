# De la solución al prototipo — plantilla de equipo

Copien este contenido a un Google Docs real compartido con su equipo. Durante el trabajo en salas, completen los campos usando sus insumos previos. No necesitan volver a definir todo el proyecto. Tiempo: 20 minutos de trabajo.

## Datos del equipo

**Nombre del equipo/proyecto:** [Completar]

**Integrantes (opcional):** [Completar]

## Problema

[Pegar o resumir el problema previamente definido y quién lo enfrenta. Las entrevistas son insumos; no afirmar demanda demostrada si aún no se ha comprobado.]

## Solución

[Pegar o resumir la solución previamente definida.]

## Funcionalidad principal

[Una oración: ¿qué acción importante debe poder completar el usuario?]

## Camino feliz

Usen entre tres y cinco pasos. Cada paso debe describir una acción o un resultado observable del recorrido esperado. Dejen vacíos los pasos que no necesiten.

1. [Paso]
2. [Paso]
3. [Paso]
4. [Opcional]
5. [Opcional]

## Color principal — opcional

**Nombre o código HEX:** [Completar o dejar vacío]

## Prompt para Google AI Studio

Cada integrante copia el siguiente prompt, reemplaza los campos entre corchetes con lo acordado por el equipo y lo usa en el entorno de construcción de aplicaciones web de Google AI Studio, siguiendo la demostración. Eliminen los pasos vacíos. La herramienta de generación requiere acceso y conexión; las restricciones siguientes corresponden a la aplicación que se generará.

---

Construye un prototipo de aplicación web responsive para este proyecto. Debe permitir a una persona recorrer la funcionalidad principal y completar el camino feliz descrito. Prioriza la interfaz móvil sin descuidar el escritorio.

**Nombre del proyecto:** [Nombre del equipo/proyecto]

**Problema y usuario:** [Problema previamente definido]

**Solución:** [Solución previamente definida]

**Funcionalidad principal:** [Acción principal que debe poder completar el usuario]

**Camino feliz, en este orden:**

1. [Paso 1]
2. [Paso 2]
3. [Paso 3]
4. [Paso 4, eliminar si no se utiliza]
5. [Paso 5, eliminar si no se utiliza]

**Color principal opcional:** [Nombre o HEX; si se deja vacío, elige un color legible y consistente]

### Interfaz y comportamiento

- Crea las pantallas necesarias para estos pasos, con navegación y acciones interactivas reales dentro del prototipo. No entregues solo una imagen ni una lista de pantallas.
- Usa una jerarquía visual clara, etiquetas comprensibles, botones identificables, contraste adecuado y un diseño sencillo y consistente. La interfaz estará en español.
- Permite seleccionar opciones, introducir datos ficticios cuando el flujo lo necesite, revisar lo elegido y completar el objetivo. Conserva temporalmente las selecciones entre pantallas y permite volver sin perderlas durante el mismo recorrido.
- Utiliza datos ficticios razonables cuando sean necesarios y márcalos como datos de demostración. No solicites información personal real ni inventes evidencia de validación comercial.
- Simula las operaciones que no requieran un servicio real y representa honestamente esa simulación. Muestra una confirmación clara al completar el flujo, indicando que no se ha ejecutado una operación real si corresponde.
- Incluye una acción sencilla «Reiniciar demostración» para borrar el estado temporal y volver al inicio. Actualizar la página también debe regresar al estado inicial.
- Evita funcionalidades secundarias no solicitadas. No añadas perfiles, reseñas, fidelización, notificaciones, pagos u otras funciones que no formen parte del camino feliz indicado.

### Límites técnicos

- No integres APIs externas ni servicios reales.
- No utilices Firebase, Firestore ni ninguna otra base de datos.
- No implementes backend ni autenticación real; no requieras cuentas externas para usar la aplicación generada.
- Omite el login. Solo represéntalo si fuera absolutamente indispensable para comprender el flujo descrito; en ese caso debe ser una simulación sin credenciales reales.
- No solicites ni implementes despliegue.
- No uses `localStorage`, `sessionStorage`, cookies, IndexedDB, almacenamiento en servidor ni otros mecanismos de persistencia entre sesiones. Mantén únicamente el estado temporal necesario en memoria de la aplicación; no serialices ese estado para recuperarlo tras una recarga.
- La actualización de la página debe borrar las selecciones y volver al estado inicial.

### Adaptación al tipo de proyecto

Si la solución es un producto físico, representa la interacción de la persona con la oferta (presentación, selección, personalización, solicitud o interés) según el camino feliz indicado. No finjas reproducir el funcionamiento físico ni propiedades técnicas no implementadas.

Si la solución requiere lógica avanzada, como visión artificial, simula su resultado con datos ficticios claramente identificados. No presentes una respuesta prefijada como una inferencia real ni afirmes precisión, eficacia o validación inexistentes.

Antes de terminar, recorre los pasos en orden y comprueba que el usuario puede completar el objetivo, ver una confirmación y reiniciar. Mantén todo dentro del alcance definido.

---

Después de generar, cada integrante recorre su versión. Luego el equipo compara los resultados y selecciona la versión más clara y fiel a su funcionalidad principal y camino feliz.
