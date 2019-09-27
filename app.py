import funciones
import objeto




#Ejercicio
#Ingrese objeto:______________
#seleccione: multiplicar, sumar, restar
#while: ingrese valor:____________
#desea ingresar otro? si o No
# objeto
# resultado
# caracteristicas
# class objeto():
#     def operaciones():

objeto.objeto=input("Ingrese el objeto: \n>")
valores=[]
while True:
    opcion=int(input("Que desea hacer?\n1.Sumar\n2.Restar\n3.Multiplicar\n4.Dividir\n5.Salir\n>"))
    if opcion==1:
        valor1=int(input("Valor para sumar: "))
        valor2=int(input("Valor para ser sumado: "))
        print(funciones.suma(valor1,valor2))
        print("Objeto: ",objeto.objeto)
    elif opcion==2:
        valor1=int(input("Valor para restar: "))
        valor2=int(input("Valor para ser restado: "))
        print(funciones.resta(valor1,valor2))
        print("Objeto: ",objeto.objeto)
    elif opcion==3:
        valor1=int(input("Valor para multiplicar: "))
        valor2=int(input("Valor para ser multiplicado: "))
        resultado=funciones.multiplicar(valor1,valor2)
        while True:
            seleccion=int(input("Desea ingresar otro valor?\n1.Si\n2.No\n> "))
            if seleccion == 1:
                    valorX=int(input("Digite el nuevo valor: "))
                    resultado=funciones.multiplicar(resultado,valorX)
            elif seleccion==2:
                    print(resultado)
                    print("Objeto: ",objeto.objeto)
                    break     
    elif opcion==4:
        valor1=int(input("Valor para dividir: "))
        valor2=int(input("Valor para ser dividido: "))
        print(funciones.dividir(valor1,valor2))
        print("Objeto: ",objeto.objeto)
    elif opcion==5:
        break
   



# while True:
#     opcion=int(input("Que desea hacer?\n 1.Sumar\n 2.Restar \n 3.Multiplicar \n 4.Dividir \n5.Salir \n>"))
#     if opcion==1:
#         valor1=int(input("Valor para sumar: "))
#         valor2=int(input("Valor para ser sumado: "))
#         print(funciones.suma(valor1,valor2))
#     elif opcion==2:
#         valor1=int(input("Valor para restar: "))
#         valor2=int(input("Valor para ser restado: "))
#         print(funciones.resta(valor1,valor2))
#     elif opcion==3:
#         valor1=int(input("Valor para multiplicar: "))
#         valor2=int(input("Valor para ser multiplicado: "))
#         print(funciones.multiplicar(valor1,valor2))
#     elif opcion==4:
#         valor1=int(input("Valor para dividir: "))
#         valor2=int(input("Valor para ser dividido: "))
#         print(funciones.dividir(valor1,valor2))
#     elif opcion==5:
#         break