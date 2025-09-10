class Perro:

    def __init__(self, edad, nombre, color_ojos, animado):
        self.edad = edad
        self.nombre = nombre
        self.color_ojos = color_ojos
        self.animado = animado

    def ladrar(self):
        print("GUAUGUAU")

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}")

    def feliz(self):
        print("YEII, QUE FELICIDAD DIGO GUAUGUAU")


Thara = Perro(5, "Thara", "rojo", "animado")


Thara.ladrar()
Thara.saludar()
Thara.feliz()
