# Tanda — ejemplo completo para la demostración

Caso ficticio del taller. No representa una barbería real ni registra citas. Datos coherentes con `assets/content/tanda/screen-01.png` … `screen-05.png`.

## Datos del equipo

**Nombre del proyecto:** Tanda

**Integrantes:** no aplica; caso de demostración del facilitador.

## Problema

Una persona que quiere reservar una cita en una barbería por WhatsApp puede tener que esperar respuestas y coordinar repetidamente los horarios disponibles. Este problema es el supuesto de nuestro caso ficticio, no evidencia de demanda comercial.

## Solución

Una aplicación web donde el cliente elige un servicio, selecciona un horario y reserva su cita.

## Funcionalidad principal

Reservar una cita en una barbería sin tener que coordinar manualmente por mensajes.

## Camino feliz

1. Seleccionar servicio.
2. Elegir fecha y horario.
3. Ingresar datos de reserva.
4. Revisar y confirmar la reserva.
5. Ver la confirmación de la cita.

## Color principal

Verde `#174C40`; fondo crema `#F7F6F0`, tinta `#152C27`, superficies blancas. Mantener una sola familia sans serif y contraste legible.

## Datos ficticios del recorrido de demostración

- Servicios: Corte clásico, 30 min, S/ 35; Barba, 20 min, S/ 25; Corte + barba, 50 min, S/ 55.
- Servicio elegido: Corte clásico.
- Fechas de ejemplo: jueves 19, viernes 20 y sábado 21 de noviembre de 2026.
- Horarios disponibles: 10:00, 11:00, 16:00 y 17:00.
- Selección: viernes 20 de noviembre de 2026, 16:00.
- Cliente ficticio: Alex Rivera; correo `alex@example.com`.
- Ningún correo se envía ni se registra una cita en una barbería real.

## Prompt final para Google AI Studio

Copiar el bloque siguiente en el entorno de construcción de aplicaciones web. Los controles deben funcionar en la aplicación generada; las cinco capturas del taller solo son referencias del mismo flujo, no una app funcional.

---

Construye un prototipo de aplicación web responsive llamado **Tanda**, para reservar citas en una barbería ficticia. Debe permitir completar la funcionalidad principal de principio a fin. Prioriza móvil sin descuidar escritorio. Usa interfaz en español, una sola familia sans serif y diseño minimalista consistente.

**Problema:** reservar una cita por WhatsApp puede requerir esperar respuestas y coordinar repetidamente horarios disponibles.

**Solución:** una web donde el cliente elige un servicio, selecciona un horario y reserva su cita.

**Funcionalidad principal:** reservar una cita en una barbería sin tener que coordinar manualmente por mensajes.

**Camino feliz obligatorio, con cinco pantallas en este orden:**

1. **Seleccionar servicio.** Mostrar Corte clásico (30 min, S/ 35), Barba (20 min, S/ 25) y Corte + barba (50 min, S/ 55). Permitir seleccionar uno y continuar. En la demostración se elegirá Corte clásico.
2. **Elegir fecha y horario.** Mostrar las fechas 19, 20 y 21 de noviembre de 2026, y las horas 10:00, 11:00, 16:00 y 17:00. Permitir seleccionar fecha y hora. En la demostración se elegirá viernes 20 de noviembre a las 16:00.
3. **Ingresar datos de reserva.** Formulario simple de nombre y correo. Para la demostración se introducirán Alex Rivera y alex@example.com. No requerir datos reales ni ningún dato adicional.
4. **Revisar y confirmar la reserva.** Mostrar el servicio, duración, precio, fecha, horario y datos introducidos. Permitir volver para corregir y una acción clara «Confirmar reserva».
5. **Ver la confirmación de la cita.** Mostrar «¡Reserva realizada!», los datos seleccionados y «Reserva de demostración. No se registró una cita real». Incluir «Reiniciar demostración» para volver al estado inicial.

**Estilo:** verde principal #174C40, fondo crema #F7F6F0, tinta #152C27 y superficies blancas. Nombre Tanda, sin logos de barberías reales. Mostrar un distintivo «DEMO» y que los datos son ficticios. Botones claros, texto legible, acciones cómodas en móvil y jerarquía visual limpia.

**Comportamiento:** construye pantallas navegables y acciones interactivas, no una imagen estática. Mantén las selecciones al avanzar o volver durante un recorrido. Usa únicamente estado temporal en memoria. Al pulsar reiniciar o actualizar la página, elimina todas las selecciones y vuelve a la primera pantalla. Muestra una confirmación clara solo después de confirmar. No envíes correos, no reserves un horario real y no presentes la simulación como una integración funcional con una barbería.

**Límites:** no APIs externas ni servicios reales; no Firebase, Firestore ni otras bases de datos; no backend; no autenticación, login, cuentas externas ni credenciales; no despliegue. No usar localStorage, sessionStorage, cookies, IndexedDB, almacenamiento en servidor ni otros mecanismos de persistencia. No añadir pagos, perfiles, reseñas, programas de fidelización ni notificaciones. Los importes son información ficticia del servicio, no un proceso de pago.

No presupongas que esta solución tiene demanda comercial validada. Comprueba que se pueden recorrer los cinco pasos, revisar los datos, confirmar la reserva simulada y reiniciar. La aplicación debe volver al inicio al actualizar la página.

---

## Uso en vivo — 38 minutos

1. 4 min: recuperar los cuatro insumos en el documento y mostrar cómo alimentan el prompt.
2. 8 min: generar y recorrer Tanda en Google AI Studio compartiendo pantalla.
3. 20 min: cada estudiante genera individualmente el prototipo de su equipo y recorre su camino feliz.
4. 6 min: comprobar la finalización, aclarar qué es simulado y regresar al deck.

Verificar el acceso a la herramienta antes del taller. No se ha creado ningún Google Docs ni enlace de Drive desde este repositorio. Una generación puede verse diferente de las capturas: evaluar la coherencia del flujo, no una reproducción píxel a píxel. No convertir la demo en una sesión de programación o despliegue.
