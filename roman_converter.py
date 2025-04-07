def decimal_a_romano(num):
    valores = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
    }
    resultado = ""
    claves_ordenadas = sorted(valores.keys(), reverse=True)
    for valor in claves_ordenadas:
        simbolo = valores[valor]
        while num >= valor:
            resultado += simbolo
            num -= valor
    return resultado


def main():
    while True:
        num = int(input("Ingrese un numero cualquiera: "))
        if num > 3999:
            print("Ingrese un numero valido menor a 4000")
            continue
        romano = decimal_a_romano(num)
        print(f"El numero {num} en romano es: {romano}")
        continuar = (
            input("Desea continuar? Presione Y para seguir, cualquier otra tecla para salir del programa. ").strip().lower())
        if continuar != "y":
            break

if __name__ == "__main__":
    main()