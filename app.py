import funciones
import objeto

while True:
    opcion=int(input("Que desea hacer?\n 1.Sumar\n 2.Restar \n 3.Multiplicar \n 4.Dividir \n5.Salir \n>"))
    if opcion==1:
        valor1=int(input("Valor para sumar: "))
        valor2=int(input("Valor para ser sumado: "))
        print(funciones.suma(valor1,valor2))
    elif opcion==2:
        valor1=int(input("Valor para restar: "))
        valor2=int(input("Valor para ser restado: "))
        print(funciones.resta(valor1,valor2))
    elif opcion==3:
        valor1=int(input("Valor para multiplicar: "))
        valor2=int(input("Valor para ser multiplicado: "))
        print(funciones.multiplicar(valor1,valor2))
    elif opcion==4:
        valor1=int(input("Valor para dividir: "))
        valor2=int(input("Valor para ser dividido: "))
        print(funciones.dividir(valor1,valor2))
    elif opcion==5:
        break