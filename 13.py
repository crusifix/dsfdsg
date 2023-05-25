#Algoritmo que lea dos números y nos diga cuál de ellos es mayor o bien si son iguales 
#(recuerda usar la estructura condicional SI)

A= int(input("Ingresa su primer numero: "))
B= int(input("Ingresa su segundo numero: "))

if A>B:
    print(f"{A} es mayor a {B}")
elif A<B:
    print(f"{A} es menor a {B}")
elif A==B:
    print("Son iguales")


