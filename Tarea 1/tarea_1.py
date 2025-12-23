# Tarea 1

# Met 1. Toma dos ententeros y un str. Con el str "op" elige la operacion
# a realizar a num 1 con respecto a num 2
def operation_selector(num1, num2, op):

    # Sanity check
    if type(num1) is not int or type(num2) is not int:
        return ("Error 0: num1 and num2 must be Integer Object", None)

    if type(op) is not str:
        return ("Error 1: op must be a string Object", None)

    # selector de operacion
    match op:
        case "+":
            return ("Ex1", num1 + num2)
        case "-":
            return ("Ex2", num1 - num2)
        case "*":
            return ("Ex3", num1 * num2)
        case "&":
            return ("Ex4", num1 and num2)
        case _:
            return ("Error 2: op must be a valid string (+,-,*,&)", None)


# Met 2. Toma un objeto iterable de un tamaño menor a 10 y retorna
# el valor promedio de sus elementos
def calculo_promedio(lista_valores):

    # Sanity check
    if len(lista_valores) > 10:
        return ("Error 3: lista_valores size must not exceed 10", None)

    suma = 0
    # Itera cada elemento, primero Sanity check, y luego lo suma
    for elemento in lista_valores:
        if type(elemento) is not int:
            return ("Error 4: All values must be Integer Object", None)
        suma += elemento

    return ("Ex5", suma / len(lista_valores))
