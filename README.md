# Haz tu propio puente — Producto Final (Fase 4)

Asistente conversacional 100 % por texto y chat diseñado para orientar paso a paso a estudiantes, familias y personas en situación de desventaja, adultos mayores, migrantes o usuarios con barreras de idioma, lectura técnica o conectividad limitada sobre **becas, trámites escolares, servicios de salud y apoyos públicos**.

- **Hackatón:** Hackatón Nacional de Innovación con IA Aplicada · Ingenio Incluyente — UVM 2026
- **Equipo:** Linces-BJ (`UVM Campus San Rafael`)
- **Integrantes:** Carlos Sebastián Martínez Torres (Líder), Gabriel Eduardo Ornelas Vargas, Julio César Martínez Solís
- **Reto:** Reto 1 · Puentes de oportunidad — Reducción de la brecha de acceso (**ODS 10** y **ODS 11**)
- **Repositorio en GitHub:** `https://github.com/a010210541-source/Linces-BJ`
- **Carpeta de documentación y bocetos:** `https://github.com/a010210541-source/Linces-BJ/tree/main/docs`
- **Proyecto en Google Stitch:** `https://stitch.google.com/projects/15289391016942737046`
- **Video del pitch (5 min):** *(Pega aquí el enlace de YouTube o Drive del pitch final)*

---

## App demostrable y validación

- **URL de demo desplegada:** *(Agrega aquí el enlace público de tu app si está alojada en línea)*
- **Entorno local validado:** `http://127.0.0.1:5000` (configurable a `host="0.0.0.0"` para pruebas en red local)

---

## Enfoque y funcionalidades finales

- **Asistente 100 % por chat de texto:** Interfaz clara y accesible enfocada en texto y chat, sin funciones ni íconos de voz, priorizando control del usuario, privacidad (sin solicitar contraseñas ni datos bancarios) y simplicidad en conexiones limitadas.
- **Selector de idioma:** Cambio dinámico entre **Español** y **English**.
- **Selector de nivel de lectura:** Alterna entre **Lenguaje sencillo / cotidiano** y **Explicación detallada**.
- **Orientación paso a paso y checklists:** Realiza preguntas breves para ubicar la necesidad del usuario, explica pasos generales de trámites o convocatorias y entrega listas accionables de documentos básicos.

---

## Arquitectura técnica y resiliencia

El backend está desarrollado en **Python (Flask)** conectado al SDK oficial **`google-genai`**, cargando variables de entorno desde `.env` (excluido por `.gitignore`, con `.env.example` como plantilla):

1. **Límite de tiempo de espera (`timeout`):** Cliente configurado con `timeout=12000` (12 segundos) por solicitud para evitar esperas prolongadas.
2. **Cascada de modelos:** Intenta primero **`gemini-3.8-flash`** y, ante fallos o indisponibilidad, pasa automáticamente a **`gemini-3.5-flash-lite`**.
3. **Manejo de errores (`503`, `504`, `404`):** Captura respuestas de alta demanda (`503 UNAVAILABLE`), tiempo agotado (`504 DEADLINE_EXCEEDED`) o modelo no encontrado (`404 NOT_FOUND`) sin interrumpir el servicio.
4. **Guía estática de respaldo:** Ante indisponibilidad total de los modelos, devuelve una guía estructurada de respaldo con pasos generales y documentos sugeridos manteniendo respuesta `HTTP 200`.

---

## Estructura del repositorio

```text
Linces-BJ/
├── .env.example
├── .gitignore
├── README.md
├── docs/
└── src/
    ├── app.py
    ├── prompts.py
    └── requirements.txt
