# ============================================================================
# SISTEMA DE GESTIÓN DE MENÚ DE RESTAURANTE CON PROMOCIONES
# ============================================================================
# Este programa permite administrar un menú de restaurante aplicando
# descuentos promocionales basados en categorías y umbrales de precio.
# TRABAJO REALIZADO POR ARNOL
# ============================================================================

def mostrar_menu_principal():
    """
    Función que muestra el menú principal del sistema.
    """
    print("\n" + "=" * 70)
    print(" 🍽️  SISTEMA DE GESTIÓN DE MENÚ DE RESTAURANTE")
    print("=" * 70)
    print("1. Ingresar productos al menú")
    print("2. Ver menú completo")
    print("3. Configurar promoción")
    print("4. Aplicar promoción y mostrar precios finales")
    print("5. Salir del programa")
    print("=" * 70)


def calcular_precio_final(precio_base, categoria, categoria_objetivo, umbral_precio, descuento_aplicado):
    """
    Función que calcula el precio final de un producto aplicando promoción.

    Parámetros:
        precio_base (float): Precio original del producto
        categoria (str): Categoría del producto actual
        categoria_objetivo (str): Categoría que aplica para la promoción
        umbral_precio (float): Precio mínimo para aplicar descuento
        descuento_aplicado (float): Porcentaje de descuento (15% = 0.15)

    Retorna:
        float: Precio final después de aplicar promoción

    Lógica de negocio:
        - Si el producto cumple con la categoría objetivo Y su precio base
          es mayor al umbral: se aplica el descuento del 15%
        - Si no cumple las condiciones: mantiene el precio base
    """
    # Verificamos si se cumplen las dos condiciones para aplicar descuento
    if categoria.lower() == categoria_objetivo.lower() and precio_base > umbral_precio:
        # Calculamos el descuento (15% del precio base)
        descuento = precio_base * descuento_aplicado
        # Precio final = precio base - descuento
        precio_final = precio_base - descuento
        return precio_final
    else:
        # No se cumplen las condiciones, mantiene precio original
        return precio_base


def ingresar_productos():
    """
    Función que solicita al usuario ingresar productos del menú.
    Crea y retorna una matriz con la información de los productos.

    Retorna:
        list: Matriz con los productos. Cada producto es una lista:
              [nombre, categoria, precio_base]
    """
    menu = []

    print("\n--- INGRESO DE PRODUCTOS AL MENÚ ---")

    # Solicitamos cuántos productos desea ingresar (mínimo 6)
    while True:
        try:
            cantidad_productos = int(input("\n¿Cuántos productos desea ingresar? (mínimo 6): "))
            if cantidad_productos >= 6:
                break
            else:
                print("⚠️  Debe ingresar al menos 6 productos.")
        except ValueError:
            print("⚠️  Por favor ingrese un número válido.")

    # Ciclo para ingresar cada producto
    for i in range(cantidad_productos):
        print(f"\n--- Producto {i + 1} de {cantidad_productos} ---")

        nombre = input("Nombre del producto: ").strip()
        categoria = input("Categoría (ej: Entrada, Plato Fuerte, Postre, Bebida): ").strip()

        # Validamos que el precio sea un número válido
        while True:
            try:
                precio_base = float(input("Precio base: $"))
                if precio_base > 0:
                    break
                else:
                    print("⚠️  El precio debe ser mayor a cero.")
            except ValueError:
                print("⚠️  Por favor ingrese un precio válido.")

        # Creamos una lista con los datos del producto
        producto = [nombre, categoria, precio_base]

        # Agregamos el producto a la matriz del menú
        menu.append(producto)

    print(f"\n✓ Se han ingresado {cantidad_productos} productos correctamente.")
    return menu


def mostrar_menu(menu):
    """
    Función que muestra todos los productos del menú en formato tabla.

    Parámetros:
        menu (list): Matriz con los productos del menú
    """
    if len(menu) == 0:
        print("\n⚠️  El menú está vacío. Primero debe ingresar productos.")
        return

    print("\n" + "=" * 90)
    print(" MENÚ DEL RESTAURANTE")
    print("=" * 90)
    print(f"{'Nombre':<30} {'Categoría':<20} {'Precio Base':<15}")
    print("-" * 90)

    # Ciclo para recorrer cada producto de la matriz
    for producto in menu:
        nombre = producto[0]
        categoria = producto[1]
        precio_base = producto[2]

        print(f"{nombre:<30} {categoria:<20} ${precio_base:<14.2f}")

    print("=" * 90)


def configurar_promocion():
    """
    Función que permite al usuario configurar los parámetros de la promoción.

    Retorna:
        tuple: (categoria_objetivo, umbral_precio, descuento) configurados
    """
    print("\n--- CONFIGURACIÓN DE PROMOCIÓN ---")
    print("La promoción aplicará un 15% de descuento a productos que cumplan:")
    print("1. Pertenezcan a una categoría específica")
    print("2. Tengan un precio base mayor a un umbral definido\n")

    categoria_objetivo = input("Ingrese la categoría objetivo para la promoción: ").strip()

    while True:
        try:
            umbral_precio = float(input("Ingrese el umbral de precio mínimo: $"))
            if umbral_precio > 0:
                break
            else:
                print("⚠️  El umbral debe ser mayor a cero.")
        except ValueError:
            print("⚠️  Por favor ingrese un precio válido.")

    # Descuento fijo del 15%
    descuento = 0.15

    print(f"\n✓ Promoción configurada:")
    print(f"  - Categoría: {categoria_objetivo}")
    print(f"  - Umbral de precio: ${umbral_precio:.2f}")
    print(f"  - Descuento: {descuento * 100:.0f}%")

    return categoria_objetivo, umbral_precio, descuento


def aplicar_promocion(menu, categoria_objetivo, umbral_precio, descuento):
    """
    Función que aplica la promoción al menú y muestra los resultados.
    Utiliza calcular_precio_final() para cada producto.

    Parámetros:
        menu (list): Matriz con los productos del menú
        categoria_objetivo (str): Categoría que aplica para promoción
        umbral_precio (float): Precio mínimo para descuento
        descuento (float): Porcentaje de descuento (0.15 = 15%)
    """
    if len(menu) == 0:
        print("\n⚠️  El menú está vacío. Primero debe ingresar productos.")
        return

    print("\n" + "=" * 100)
    print(" MENÚ CON PROMOCIÓN APLICADA")
    print("=" * 100)
    print(f"Promoción: {descuento * 100:.0f}% de descuento en '{categoria_objetivo}' con precio > ${umbral_precio:.2f}")
    print("-" * 100)
    print(f"{'Nombre':<25} {'Categoría':<18} {'Precio Base':<15} {'Precio Final':<15} {'Estado':<20}")
    print("-" * 100)

    # Contadores para estadísticas
    productos_con_descuento = 0
    total_ahorrado = 0

    # Ciclo para procesar cada producto del menú
    for producto in menu:
        nombre = producto[0]
        categoria = producto[1]
        precio_base = producto[2]

        # Llamamos a la función que calcula el precio final
        precio_final = calcular_precio_final(precio_base, categoria,
                                             categoria_objetivo, umbral_precio, descuento)

        # Determinamos si se aplicó descuento
        if precio_final < precio_base:
            estado = f"✓ -{descuento * 100:.0f}% DESCUENTO"
            productos_con_descuento += 1
            ahorro = precio_base - precio_final
            total_ahorrado += ahorro
        else:
            estado = "Sin promoción"

        # Mostramos la información del producto
        print(f"{nombre:<25} {categoria:<18} ${precio_base:<14.2f} ${precio_final:<14.2f} {estado:<20}")

    print("=" * 100)
    print(f"\n📊 RESUMEN DE PROMOCIÓN:")
    print(f"   • Total de productos: {len(menu)}")
    print(f"   • Productos con descuento: {productos_con_descuento}")
    print(f"   • Productos sin descuento: {len(menu) - productos_con_descuento}")
    print(f"   • Ahorro total para clientes: ${total_ahorrado:.2f}")


# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

def main():
    """
    Función principal que ejecuta el programa.
    Controla el flujo del menú y las opciones del usuario.
    """
    # Variables principales del programa
    menu = []
    promocion_configurada = False
    categoria_objetivo = ""
    umbral_precio = 0.0
    descuento = 0.15  # 15% fijo

    # Ciclo principal del programa
    while True:
        mostrar_menu_principal()

        opcion = input("\nSeleccione una opción (1-5): ").strip()

        # Estructura condicional para manejar las opciones
        if opcion == "1":
            # Opción 1: Ingresar productos
            menu = ingresar_productos()

        elif opcion == "2":
            # Opción 2: Ver menú completo
            mostrar_menu(menu)

        elif opcion == "3":
            # Opción 3: Configurar promoción
            categoria_objetivo, umbral_precio, descuento = configurar_promocion()
            promocion_configurada = True

        elif opcion == "4":
            # Opción 4: Aplicar promoción
            if not promocion_configurada:
                print("\n⚠️  Primero debe configurar la promoción (opción 3).")
            else:
                aplicar_promocion(menu, categoria_objetivo, umbral_precio, descuento)

        elif opcion == "5":
            # Opción 5: Salir
            print("\n" + "=" * 70)
            print(" Gracias por usar el Sistema de Gestión de Menú")
            print(" ¡Hasta pronto! 🍽️")
            print("=" * 70)
            break

        else:
            # Opción inválida
            print("\n⚠️  Opción no válida. Por favor seleccione entre 1 y 5.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()