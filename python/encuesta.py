class Encuesta:
    def __init__(self, tiempo_disponible  , nombre , edad , respuesta_proyecto):
        self.nombre = nombre
        self.edad = edad
        self.respuesta_proyecto = respuesta_proyecto
        self.tiempo_disponible= tiempo_disponible
        
    def mostrar(self):
        print("| nombre:", self.nombre, 
              "| edad:", self.edad, 
              "| respuesta de proyecto:",  self.respuesta_proyecto,
              "| Que cantidad de hooras tienes disponibles para el proyecto", self.tiempo_disponible)

Ecuestas = []
for i in range(10):  
    print("\nEncuestas", i+1)
    nombre = str(input("|Dime tu nombre por favor|"))
    edad = int(input("|dime tu edad|"))
    respuesta_proyecto = str(input("|cual es tu idea de proyecto? |"))
    tiempo_disponible = int(input("cuantas horas tienes disponible para el proyecto"))
    E = Encuesta( nombre , edad , respuesta_proyecto, tiempo_disponible)
    Ecuestas.append(E)

    print("\ listado de encuesta")
    for i in range(len(Ecuestas)):
         Ecuestas[i].mostrar()
