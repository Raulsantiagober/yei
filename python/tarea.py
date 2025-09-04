#Raúl Santiago Bermúdez Camacho
#1072102047


#9
a=1

while a<10:
    print(a)
    a = a + 1

#10  
b=1
while b<=10000:
    print(b)
    b = b + 1 

#15

for i in range(1, 31):
    print(f"{i}^2 = {i**2}")

#16

producto = 1

for i in range(1, 21):
    producto *= i

print(f"El producto de los 20 primeros números naturales es: {producto}")

#26

a = int(input("Ingrese el primer número entero positivo: "))
b = int(input("Ingrese el segundo número entero positivo: "))
c = int(input("Ingrese el tercer número entero positivo: "))

mayor = max(a, b, c)
menor = min(a, b, c)

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")


#27

while True:
    f = float(input("Ingrese la temperatura en grados Fahrenheit (999 para salir): "))

    if f == 999:
        print("Programa finalizado.")
        break

    c = (5/9) * (f - 32)
    print(f"{f} °F = {c:.2f} °C")