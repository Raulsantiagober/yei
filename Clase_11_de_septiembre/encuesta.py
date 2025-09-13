class Estudiante:
    def __init__(self, nombre, edad, respuesta_proyecto, tiempo_disponible):
        self.nombre = nombre
        self.edad = edad
        self.respuesta_proyecto = respuesta_proyecto
        self.tiempo_disponible = tiempo_disponible

    def __str__(self):
        return (f"Nombre: {self.nombre} | Edad: {self.edad} | "
                f"Proyecto: {self.respuesta_proyecto} | "
                f"Horas disponibles: {self.tiempo_disponible}")



class Encuesta:
    def __init__(self, preguntas):
        self.preguntas = preguntas
        self.respuestas = [] 

    def agregar_respuesta(self, estudiante):
       
        respuesta_est = {
            "nombre": estudiante.nombre,
            "edad": estudiante.edad,
            "respuesta_proyecto": estudiante.respuesta_proyecto,
            "tiempo_disponible": estudiante.tiempo_disponible
        }
        self.respuestas.append(respuesta_est)

    def mostrar_resultados(self):
        print("\n_*_*_*RESULTADOS DE LA ENCUESTA_*_*_*_")
        for i, r in enumerate(self.respuestas, start=1):
            print(f"\n--- Encuesta {i} ---")
            print(f"--Nombre: {r['nombre']}")
            print(f"--Edad: {r['edad']} años")
            print(f"--Idea de proyecto: {r['respuesta_proyecto']}")
            print(f"--Horas disponibles: {r['tiempo_disponible']}")

    def resumen(self):
        print("\n___RESUMEN___")
        
        horas_dict = {}
        for r in self.respuestas:
            horas = r["tiempo_disponible"]
            horas_dict[horas] = horas_dict.get(horas, 0) + 1

        for horas, cantidad in horas_dict.items():
            print(f"{cantidad} estudiante(s) tienen {horas} horas disponibles")



preguntas = [
    "---Dime tu nombre: ",
    "---Dime tu edad: ",
    "---¿Cuál es tu idea de proyecto?: ",
    "---¿Cuántas horas tienes disponible para el proyecto?: "
]

encuesta = Encuesta(preguntas)

for i in range(10):  
    print(f"\n---Encuesta {i+1}---")
    nombre = input(preguntas[0])
    edad = int(input(preguntas[1]))
    respuesta_proyecto = input(preguntas[2])
    tiempo_disponible = int(input(preguntas[3]))

    estudiante = Estudiante(nombre, edad, respuesta_proyecto, tiempo_disponible)
    encuesta.agregar_respuesta(estudiante)


encuesta.mostrar_resultados()

encuesta.resumen()
