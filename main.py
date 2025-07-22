from suma import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def menu():
    while True:
        print("\nCalculadora")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Suma Avanzada")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", sumar(a, b))
        elif opcion == "2":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", restar(a, b))
        elif opcion == "3":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", multiplicar(a, b))
        elif opcion == "4":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", dividir(a, b))
        elif opcion == "5":
            nums = input("Escribe los números separados por coma: ")
            lista = [float(n) for n in nums.split(",")]
            print("Resultado:", suma_avanzada(lista))
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")

menu()