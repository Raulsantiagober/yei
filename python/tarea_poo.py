#31

import math

class CuerpoCeleste:
    G = 6.67430e-11  # Constante gravitacional

    def __init__(self, id_unico, nombre, masa, densidad, diametro, distancia_sol):
        self.id_unico = id_unico
        self.nombre = nombre
        self.masa = masa
        self.densidad = densidad
        self.diametro = diametro
        self.distancia_sol = distancia_sol

    def atraccion(self, otro):
        # Fórmula de atracción gravitatoria
        distancia = abs(self.distancia_sol - otro.distancia_sol)
        if distancia == 0:
            return 0
        return (CuerpoCeleste.G * self.masa * otro.masa) / (distancia ** 2)


# Ejemplo de uso
tierra = CuerpoCeleste(1, "Tierra", 5.97e24, 5510, 12742e3, 1.496e11)
marte = CuerpoCeleste(2, "Marte", 6.39e23, 3933, 6779e3, 2.279e11)

print("Atracción Tierra-Marte:", tierra.atraccion(marte))


#32
print("Este código siempre se ejecuta")

if __name__ == "__main__":
    print("Este es el punto de entrada del programa")

#33

import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                # Intercambiar
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

def quicksort(arr):
    # Versión muy básica
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    menores = []
    mayores = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            menores.append(arr[i])
        else:
            mayores.append(arr[i])
    return quicksort(menores) + [pivot] + quicksort(mayores)

# ----------------------------
# Programa principal
# ----------------------------
n = int(input("Tamaño del array: "))
arr = []

# Generar números aleatorios
for i in range(n):
    arr.append(random.randint(0, 100))

print("Array generado:", arr)

opcion = input("Ordenar con (B)urbuja o (Q)uicksort?: ").upper()

if opcion == "B":
    arr = bubble_sort(arr)
elif opcion == "Q":
    arr = quicksort(arr)

print("Array ordenado:", arr)


#34

class Vehiculo:
    def __init__(self, pasajeros, tripulacion, ruedas, matricula, medio):
        self.pasajeros = pasajeros
        self.tripulacion = tripulacion
        self.ruedas = ruedas
        self.matricula = matricula
        self.medio = medio

    def mostrar(self):
        print("Vehículo -> Pasajeros:", self.pasajeros,
              "| Tripulación:", "Sí" if self.tripulacion else "No",
              "| Ruedas:", self.ruedas,
              "| Matrícula:", self.matricula,
              "| Medio:", self.medio)


# Programa
vehiculos = []
for i in range(10):  # ahora son 10
    print("\nVehículo", i+1)
    pasajeros = int(input("Número de pasajeros: "))
    trip = input("¿Tiene tripulación? (s/n): ").lower() == "s"
    ruedas = int(input("Número de ruedas: "))
    matricula = input("Fecha de matriculación (YYYY-MM-DD): ")
    medio = input("Medio de desplazamiento: ")
    v = Vehiculo(pasajeros, trip, ruedas, matricula, medio)
    vehiculos.append(v)

print("\nListado de vehículos:")
for i in range(len(vehiculos)):
    vehiculos[i].mostrar()
