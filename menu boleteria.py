opcion= 0
cantmenor= 0
total= 0
cantadulto= 0
cantmayor= 0
while opcion!=2:
    try:
        print("Comprar boletos")
        print("1.- Ingresar compra")
        print("2.- Salir")
        opcion= int(input("Elija una opcion: "))
        if opcion==1:
            print("Tarifas de entrada")
            print("1.- Menor(s) $4000 ")
            print("2.- Adulto o adolescente $7000 ")
            print("3.- Adulto mayor $3000 ")
            opcitarifa=  int(input("Que opcion desea: "))
            if opcitarifa==1:
                cantidad= int(input("Cuantos desea: "))
                cantmenor += cantidad
                total+=(cantidad*4000)
            elif opcitarifa==2:
                cantidad= int(input("Cuantos desea: "))
                cantadulto += cantidad
                total+=(cantidad*7000)
            elif opcitarifa==3:
                cantidad= int(input("Cuantos desea: "))
                cantmayor += cantidad
                total+=(cantidad*3000)
            else:
                print("Opcion fuera de rango")
        elif opcion==2:
             print("compra")
             print("-------------------------------------")
             if cantmenor>0:
                 print(f"{cantmenor}Menor \t\t\t ${cantmenor*4000}")
             if cantadulto>0:
                 print(f"{cantadulto}Menor \t\t\t ${cantadulto*4000}")
             if cantmayor>0:
                 print(f"{cantmayor}Menor \t\t\t ${cantmayor*4000}")
             print("-------------------------------------")
             print(f"Total \t\t\t ${total} ")


    except ValueError:
        print("Debe ingresar un numero")
    except:
        print("Error en el sistema")
        