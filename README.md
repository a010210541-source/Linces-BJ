# Haz tu propio puente — Hackatón Nacional de Innovación con IA Aplicada 2026 (UVM)

**Equipo:** Linces-BJ | **Campus:** San Rafael | **Integrantes:** 3 (Carlos Sebastián Martínez Torres, Julio Cesar Martinez Solis, Gabriel Eduardo Ornelas Vargas)

---

## 1. Resumen Ejecutivo
**Haz tu propio puente** es una aplicación móvil inclusiva diseñada para acercar becas, trámites escolares, servicios de salud y apoyos gubernamentales a personas en situación de desventaja, estudiantes de primera generación, adultos mayores, migrantes o usuarios con barreras de idioma, conectividad o lenguaje técnico. Mediante un asistente guiado por chat y voz adaptado al nivel de lectura del usuario, la app traduce procesos complejos en pasos claros y accionables. Su innovación radica en combinar accesibilidad multimodal (lectura clara, voz e idioma adaptable) con guías personalizadas impulsadas por Gemini para reducir la exclusión por desinformación.

## 2. Boceto y Concepto
* **Reto:** Reto 1 · Puentes de oportunidad — Reducción de la brecha de acceso.
* **Problemática (ODS 10 y ODS 11):** La información oficial sobre becas, trámites y servicios suele estar dispersa, ser extensa y utilizar lenguaje técnico o burocrático difícil de comprender, lo que excluye a poblaciones vulnerables (ODS 10) y dificulta el acceso equitativo a servicios, trámites y recursos comunitarios (ODS 11).
* **Usuario objetivo:** Estudiantes de primera generación, jóvenes y adultos en situación de desventaja, adultos mayores y personas con barreras de comprensión lectora, idioma o baja conectividad.
* **Propuesta de solución:** Una aplicación móvil con asistente conversacional y de voz que adapta el nivel de lectura e idioma, explica requisitos en términos sencillos y genera una guía paso a paso para completar el proceso.
* **Enlace al boceto / diseño (Fase 2):** Por agregar al completar el diseño en Google Stitch.

## 3. Documentación Funcional
* **Selector de accesibilidad:** Configuración de idioma preferido y nivel de lectura (básico/cotidiano o detallado).
* **Asistente guiado (chat y voz):** Interacción mediante preguntas breves y orientación paso a paso para verificar elegibilidad básica.
* **Simplificador de convocatorias y trámites:** Reescritura de textos complejos o requisitos pegados/seleccionados en lenguaje claro y cotidiano.
* **Checklist personalizado:** Generación de listas de verificación accionables de documentos y pasos a seguir.
* **Lectura en voz alta:** Respuestas redactadas de forma clara y optimizadas para accesibilidad auditiva.

## 4. Documentación Técnica
* **Arquitectura general:** Flujo de interfaz móvil conectada a la API de Google Gemini para procesamiento de lenguaje, simplificación por perfil/nivel de lectura y generación de guías/checklists, manteniendo las credenciales en entorno local seguro (`.env` ignorado por Git).
* **Stack tecnológico:** Google Gemini (API/SDK), Google AI Studio, Google Stitch, Python, GitHub, Google Workspace.
* **Integración de Gemini:** Gemini actúa como motor conversacional, traductor y adaptador cognitivo: simplifica requisitos o convocatorias según el nivel de lectura e idioma del usuario, guía la conversación para verificar elegibilidad básica y genera checklists paso a paso y respuestas aptas para lectura en voz alta.
* **Enlace a la app demostrable / demo (Fase 3):** Por agregar al tener listo el prototipo funcional.

## 5. Manual de Usuario
Guía paso a paso para usar **Haz tu propio puente**:
1. Abre la aplicación y selecciona tu idioma y nivel de lectura o modo de accesibilidad.
2. Elige un trámite, beca o servicio, o pega el texto de una convocatoria/requisito que quieras entender.
3. Responde las preguntas breves del asistente para revisar tu elegibilidad básica.
4. Revisa la explicación en lenguaje sencillo, escucha la lectura en voz alta si lo necesitas y sigue tu checklist de pasos y documentos.

## 6. Accesibilidad e Impacto
* **Características de inclusión y accesibilidad:** Lenguaje sencillo adaptable al nivel de lectura, soporte de idioma, interacción por chat y voz, respuestas optimizadas para lectura en voz alta y estructura pensada para baja familiaridad digital o conectividad limitada.
* **Impacto social esperado (ODS 10 y ODS 11):** Reduce las barreras burocráticas y de información para que más personas accedan a becas, apoyos y servicios a los que califican (ODS 10), y facilita el aprovechamiento de servicios públicos y trámites locales evitando traslados innecesarios o confusiones (ODS 11).

---

## Declaración de Uso de Inteligencia Artificial Generativa
En cumplimiento con las Bases Generales del Hackatón Nacional de Innovación con IA Aplicada 2026, declaramos de forma transparente las herramientas de IA utilizadas durante el desarrollo:

| Etapa / Componente | Herramienta de IA Utilizada | Descripción del uso / asistencia |
| :--- | :--- | :--- |
| Ideación y arquitectura | Google Gemini | Definición de la propuesta *Haz tu propio puente* para el Reto 1, estructura de carpetas del repositorio y plan de trabajo por fases. |
| Bocetado de interfaz (UI/UX) | Google Stitch | Diseño de pantallas y flujos visuales de la aplicación (en progreso para Fase 2). |
| Prototipado y lógica central de IA | Google AI Studio / API de Gemini | Configuración de clave de API en entorno local y pruebas/lógica de simplificación, elegibilidad y checklists. |
| Generación y depuración de código | Google Gemini | Apoyo en estructuración, escritura y ajuste de código del prototipo. |
| Documentación técnica y manual | Google Gemini | Redacción y organización del `README.md`, propuesta inicial y documentación del proyecto. |

---

## Enlaces de Entrega
* **Repositorio GitHub:** https://github.com/a010210541-source/Linces-BJ
* **Boceto / Documentación con IA (Fase 2):** Por agregar.
* **Prototipo funcional / Demo (Fase 3):** Por agregar.
* **Video Pitch (5 min — Fase 4):** Por agregar.
