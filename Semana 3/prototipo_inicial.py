# ============================================================
# SISTEMA DE VENTAS - RUCAM
# Prototipo inicial en Python
# ============================================================

# Nombre del negocio
nombre_negocio = "RUCAM"

# Catálogo de productos y precios
productos = [
    "Maruchan",
    "Queso Oaxaca",
    "Huevo por kilo",
    "Sabritas",
    "Rollo de papel suelto",
    "Cigarros sueltos"
]

precios = [20, 25, 46, 22, 14, 8]

# Variables para llevar el control de las ventas
total_dia = 0
contador_ventas = 0

# Menú principal
while True:

    print("\n===================================")
    print("       SISTEMA DE VENTAS RUCAM")
    print("===================================")
    print("1. Registrar venta")
    print("2. Consultar resumen de ventas")
    print("3. Salir")
    print("===================================")

    # Solicitar opción del usuario
    try:
        opcion = int(input("Selecciona una opción: "))
    except ValueError:
        print("Error: debes ingresar un número.")
        continue

    # Opción 1: Registrar una venta
    if opcion == 1:

        print("\n========== REGISTRAR VENTA ==========")

        total_compra = 0
        cantidades = [0] * len(productos)

        # Mostrar productos y solicitar cantidades
        for i in range(len(productos)):

            print("\nProducto:", productos[i])
            print("Precio: $", precios[i])

            while True:
                try:
                    cantidad = int(input("Cantidad que desea comprar: "))

                    if cantidad >= 0:
                        cantidades[i] = cantidad
                        break
                    else:
                        print("La cantidad no puede ser negativa.")

                except ValueError:
                    print("Error: ingresa una cantidad válida.")

            # Calcular el importe del producto
            importe = precios[i] * cantidades[i]
            total_compra = total_compra + importe

        # Verificar que exista una compra
        if total_compra > 0:

            print("\n===================================")
            print("         RESUMEN DE COMPRA")
            print("===================================")

            for i in range(len(productos)):

                if cantidades[i] > 0:
                    importe = precios[i] * cantidades[i]

                    print(
                        productos[i],
                        "x",
                        cantidades[i],
                        "= $",
                        importe
                    )

            print("-----------------------------------")
            print("Total a pagar: $", total_compra)

            # Seleccionar forma de pago
            while True:

                print("\nForma de pago:")
                print("1. Efectivo")
                print("2. Tarjeta bancaria")

                try:
                    opcion_pago = int(input("Selecciona una opción: "))

                    if opcion_pago == 1:
                        forma_pago = "Efectivo"
                        break

                    elif opcion_pago == 2:
                        forma_pago = "Tarjeta bancaria"
                        break

                    else:
                        print("Opción no válida.")

                except ValueError:
                    print("Error: ingresa un número válido.")

            # Actualizar el registro de ventas
            total_dia = total_dia + total_compra
            contador_ventas = contador_ventas + 1

            print("\n===================================")
            print("          VENTA REGISTRADA")
            print("===================================")
            print("Negocio:", nombre_negocio)
            print("Total pagado: $", total_compra)
            print("Forma de pago:", forma_pago)
            print("===================================")

        else:
            print("\nNo se registró la venta porque no se seleccionaron productos.")

    # Opción 2: Consultar resumen de ventas
    elif opcion == 2:

        print("\n===================================")
        print("       RESUMEN DE VENTAS RUCAM")
        print("===================================")

        print("Número de ventas realizadas:", contador_ventas)
        print("Total acumulado: $", total_dia)

        if contador_ventas > 0:

            promedio = total_dia / contador_ventas

            print("Promedio por venta: $", round(promedio, 2))

        else:
            print("Todavía no se han registrado ventas.")

        print("===================================")

    # Opción 3: Salir del programa
    elif opcion == 3:

        print("\nGracias por utilizar el sistema de RUCAM.")
        print("Hasta pronto.")
        break

    # Validar opciones incorrectas
    else:
        print("\nOpción no válida. Intenta nuevamente.")