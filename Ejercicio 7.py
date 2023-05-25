#identifica tipo de triangulo: isosceles equilatero o rectangulo

lado1= int(input("Ingrese primer lado: "))
lado2= int(input("Ingrese segundo lado: "))
lado3= int(input("Ingrese tercer lado: "))

if lado1==lado2 and lado1!=lado3 or lado1==lado3 and lado1!=lado2 or lado2==lado1 and lado2!=lado3 or lado2==lado3 and lado2!=lado1 or lado3==lado1 and lado3!=lado2 or lado3==lado2 and lado3!=lado1:
    print("Es isosceles")
elif lado1==lado2==lado3:
    print("Es equilatero")
elif lado1!=lado2!=lado3 or lado1!=lado3!=lado2:
    print("Es rectangulo")