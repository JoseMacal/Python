#Calculo de IMC
nombre = str(input("Ingresa tu nombre: "))
edad = int(input("Ingresa tu edad: "))
peso = float(input("Ingresa tu peso: "))
altura = float(input("Ingresa tu altura: "))
imc = peso /(altura ** 2)

print(type(nombre))
print(type(edad))
print(type(peso))
print(type(altura))

print("Hola, ", nombre, "tu edad es: ", edad, "y tu IMC es de: ", imc)