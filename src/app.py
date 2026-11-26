cat << 'EOF' > src/app.py
import os
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template_string, request
from google import genai
from google.genai import types
from prompts import SYSTEM_INSTRUCTION

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("No se encontró GEMINI_API_KEY. Agrégala a tu archivo .env local.")

client = genai.Client(api_key=api_key)
app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Haz tu propio puente — MVP (Linces-BJ)</title>
  <style>
    body {
      font-family: system-ui, -apple-system, sans-serif;
      background: #faf8ff;
      color: #131b2e;
      margin: 0;
      padding: 16px;
    }
    .app {
      max-width: 720px;
      margin: 0 auto;
      background: #ffffff;
      border: 2px solid #e2e8f0;
      border-radius: 20px;
      padding: 20px;
    }
    h1 {
      margin: 0 0 4px;
      font-size: 1.35rem;
      color: #00288e;
    }
    .sub {
      color: #444653;
      font-size: 0.9rem;
      margin-bottom: 14px;
    }
    .controls {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-bottom: 14px;
    }
    label {
      font-size: 0.9rem;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    select, textarea, button {
      font-family: inherit;
      font-size: 1rem;
      border-radius: 12px;
    }
    select {
      padding: 8px 10px;
      border: 2px solid #cbd5e1;
      background: #f2f3ff;
    }
    .chat {
      min-height: 280px;
      max-height: 430px;
      overflow-y: auto;
      background: #f8fafc;
      border: 2px solid #e2e8f0;
      border-radius: 16px;
      padding: 14px;
      margin-bottom: 14px;
      white-space: pre-wrap;
      line-height: 1.5;
    }
    .msg-user {
      background: #00288e;
      color: #ffffff;
      padding: 10px 14px;
      border-radius: 14px;
      margin-bottom: 10px;
    }
    .msg-bot {
      background: #ffffff;
      border: 2px solid #cbd5e1;
      padding: 12px 14px;
      border-radius: 14px;
      margin-bottom: 12px;
    }
    form {
      display: flex;
      gap: 10px;
    }
    textarea {
      flex: 1;
      min-height: 56px;
      padding: 12px;
      border: 2px solid #94a3b8;
      resize: vertical;
    }
    button {
      min-height: 56px;
      padding: 0 20px;
      background: #00288e;
      color: #ffffff;
      border: none;
      font-weight: 700;
      cursor: pointer;
    }
    button:hover {
      background: #1e40af;
    }
  </style>
</head>
<body>
  <div class="app">
    <h1>Haz tu propio puente</h1>
    <div class="sub">Asistente por chat (solo texto) · MVP Fase 3 · Equipo Linces-BJ</div>

    <div class="controls">
      <label>
        Idioma:
        <select id="idioma">
          <option value="Español">Español</option>
          <option value="English">English</option>
        </select>
      </label>
      <label>
        Lectura:
        <select id="nivel">
          <option value="sencillo">Lenguaje sencillo / cotidiano</option>
          <option value="detallado">Explicación detallada</option>
        </select>
      </label>
    </div>

    <div id="chat" class="chat">
      <div class="msg-bot"><strong>Asistente:</strong> Hola. Escríbeme sobre qué beca, trámite o apoyo necesitas ayuda y te guío paso a paso.</div>
    </div>

    <form id="chat-form">
      <textarea id="mensaje" placeholder="Escribe tu consulta aquí..." required></textarea>
      <button type="submit">Enviar</button>
    </form>
  </div>

  <script>
    const form = document.getElementById("chat-form");
    const input = document.getElementById("mensaje");
    const chat = document.getElementById("chat");

    function escapeHtml(text) {
      return text.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    }

    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      const mensaje = input.value.trim();
      if (!mensaje) return;

      const idioma = document.getElementById("idioma").value;
      const nivel = document.getElementById("nivel").value;

      chat.innerHTML += `<div class="msg-user"><strong>Tú:</strong> ${escapeHtml(mensaje)}</div>`;
      input.value = "";
      chat.scrollTop = chat.scrollHeight;

      try {
        const res = await fetch("/api/chat", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ mensaje, idioma, nivel })
        });
        const data = await res.json();
        const texto = data.respuesta || data.error || "No se recibió respuesta.";
        chat.innerHTML += `<div class="msg-bot"><strong>Asistente:</strong>\n${escapeHtml(texto)}</div>`;
      } catch (err) {
        chat.innerHTML += `<div class="msg-bot"><strong>Asistente:</strong> Hubo un error de conexión al consultar el servicio.</div>`;
      }
      chat.scrollTop = chat.scrollHeight;
    });
  </script>
</body>
</html>
"""


@app.get("/")
def home():
    return render_template_string(HTML_TEMPLATE)


@app.post("/api/chat")
def chat_endpoint():
    payload = request.get_json(silent=True) or {}
    mensaje = (payload.get("mensaje") or "").strip()
    idioma = (payload.get("idioma") or "Español").strip()
    nivel = (payload.get("nivel") or "sencillo").strip()

    if not mensaje:
        return jsonify({"error": "Por favor escribe una pregunta."}), 400

    prompt = (
        f"Idioma de respuesta: {idioma}\n"
        f"Nivel de lectura: {nivel}\n"
        f"Consulta del usuario: {mensaje}"
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=0.35,
        ),
    )

    return jsonify({"respuesta": (response.text or "").strip()})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
EOF
