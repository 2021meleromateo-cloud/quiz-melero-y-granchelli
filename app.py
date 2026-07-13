from flask import Flask, render_template, request
import random

app = Flask(__name__)

preguntas = [
    {
        "pregunta": "¿Cuántos jugadores tiene un equipo en la cancha al comenzar un partido?",
        "opciones": ["9", "10", "11", "12"],
        "correcta": "11"
    },
    {
        "pregunta": "¿Qué selección ganó el Mundial de Qatar 2022?",
        "opciones": ["Argentina", "Francia", "Brasil", "Croacia"],
        "correcta": "Argentina"
    },
    {
        "pregunta": "¿Cuántos minutos dura un partido de fútbol?",
        "opciones": ["80", "90", "100", "120"],
        "correcta": "90"
    },
    {
        "pregunta": "¿Qué jugador es conocido como 'La Pulga'?",
        "opciones": ["Cristiano Ronaldo", "Lionel Messi", "Neymar", "Mbappé"],
        "correcta": "Lionel Messi"
    },
    {
        "pregunta": "¿Qué tarjeta expulsa a un jugador?",
        "opciones": ["Amarilla", "Azul", "Roja", "Verde"],
        "correcta": "Roja"
    }
]

@app.route("/", methods=["GET", "POST"])
def index():

    preguntas_mezcladas = []

    for p in preguntas:
        opciones = p["opciones"][:]
        random.shuffle(opciones)

        preguntas_mezcladas.append({
            "pregunta": p["pregunta"],
            "opciones": opciones,
            "correcta": p["correcta"]
        })

    if request.method == "POST":

        puntaje = 0

        for i, p in enumerate(preguntas):
            respuesta = request.form.get(f"pregunta{i}")

            if respuesta == p["correcta"]:
                puntaje += 1

        return render_template(
            "resultado.html",
            puntaje=puntaje,
            total=len(preguntas)
        )

    return render_template(
        "index.html",
        preguntas=preguntas_mezcladas
    )

if __name__ == "__main__":
    app.run(debug=True)
