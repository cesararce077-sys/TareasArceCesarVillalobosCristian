
# Cuenta la cantidad de vocales en una palabra.
# Compatible con flake8.


def contar_vocales(palabra):
    # Cuenta las vocales en una cadena de texto.

    # :param palabra: texto a evaluar
    # :return: número de vocales
    
    vocales = "aeiouAEIOU"
    contador = 0

    for letra in palabra:
        if letra in vocales:
            contador += 1

    return contador

def main():
    
    # Función principal.
    palabra = "Ingenieria"
    cantidad = contar_vocales(palabra)

    print(f"Número de vocales: {cantidad}")


if __name__ == "__main__":
    main()
