# Haz tu propio puente — Fase 3 (MVP)

Asistente conversacional 100 % por texto y chat diseñado para orientar paso a paso a estudiantes, familias y personas en situación de vulnerabilidad o con barreras de acceso sobre **becas, trámites escolares, servicios de salud y apoyos públicos**.

- **Hackatón:** Hackatón Nacional de Innovación con IA Aplicada · Ingenio Incluyente — UVM 2026
- **Equipo:** Linces-BJ (`UVM Campus San Rafael`)
- **Integrantes:** Carlos Sebastián Martínez Torres (Líder), Gabriel Eduardo Ornelas Vargas, Julio César Martínez Solís
- **Reto:** Reto 1 · Puentes de oportunidad — Reducción de la brecha de acceso (ODS 10 y ODS 11)
- **Repositorio:** `https://github.com/a010210541-source/Linces-BJ`
- **Referencia visual (Fase 2 — Google Stitch):** `https://stitch.google.com/projects/15289391016942737046`

---

## App demostrable

- **URL de demo desplegada:** *(Agrega aquí el enlace público de tu app si ya está alojada en línea, o indica que la demostración se ejecuta en local)*
- **Entorno local por defecto:** `http://127.0.0.1:5000` (configurable a `0.0.0.0` para pruebas en red local)

---

## Funcionalidades del MVP (Fase 3)

- **Asistente 100 % por chat de texto:** Interfaz web sencilla enfocada en claridad, privacidad y control del usuario, sin depender de funciones de voz.
- **Selector de idioma:** Cambio dinámico entre **Español** y **English**.
- **Selector de nivel de lectura:** Alterna entre **Lenguaje sencillo / cotidiano** y **Explicación detallada** según lo que necesite la persona.
- **Guía paso a paso y checklists:** Ayuda a identificar requisitos básicos, pasos generales de un trámite y documentos frecuentes.

---

## Arquitectura y Resiliencia

El backend está desarrollado en **Python (Flask)** utilizando el SDK oficial **`google-genai`** y variables de entorno cargadas desde `.env` (protegido por `.gitignore`, con `.env.example` como plantilla):

1. **Límite de tiempo de espera (`timeout`):** El cliente se configura con `timeout=12000` (12 segundos) para evitar esperas indefinidas.
2. **Cascada de modelos:** Intenta primero **`gemini-3.8-flash`** y, ante fallos o indisponibilidad, pasa a **`gemini-3.5-flash-lite`**.
3. **Manejo de errores HTTP (`503`, `504`, `404`):** Captura errores de alta demanda (`503 UNAVAILABLE`), tiempo agotado (`504 DEADLINE_EXCEEDED`) o modelo no encontrado (`404 NOT_FOUND`) sin tumbar el servidor.
4. **Guía estática de respaldo:** Si los modelos no responden, entrega una guía estructurada de respaldo manteniendo continuidad en la conversación.

---

## Estructura del proyecto

```text
Linces-BJ/
├── .env.example
├── .gitignore
├── README.md
└── src/
    ├── app.py
    ├── prompts.py
    └── requirements.txt
