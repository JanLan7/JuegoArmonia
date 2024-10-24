import random

preguntas_respuestas = {
    "¿Cuál es el acorde formado por las notas C, E y G?": "C mayor",
    "¿Qué acorde se forma con las notas A, C y E?": "A menor",
    "¿Cuál es el acorde formado por las notas G, B y D?": "G mayor",
    "¿Qué acorde se forma con las notas F#, A y C#?": "F# menor",
    "¿Cuál es el acorde formado por las notas D, F# y A?": "D mayor"
}

def jugar_juego():
    puntaje = 0
    preguntas = list(preguntas_respuestas.keys())
    random.shuffle(preguntas)

    for pregunta in preguntas:
        print(pregunta)
        respuesta = input("Respuesta: ")

        if respuesta.lower() == preguntas_respuestas[pregunta].lower():
            print("¡Respuesta correcta!")
            puntaje += 1
        else:
            print("Respuesta incorrecta.")
            print("La respuesta correcta es:", preguntas_respuestas[pregunta])

        print()  # Agrega una línea en blanco para separar las preguntas

    print("Juego terminado. Puntaje:", puntaje)

print("¡Bienvenido al juego de preguntas y respuestas de armonía moderna musical!")
print("Responde las preguntas correctamente para ganar puntos.")
jugar_juego()
