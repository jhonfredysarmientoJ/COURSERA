def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Error: División entre cero no está permitida.")

def calcular(operacion, a, b):
    if operacion == "+":
        return suma(a, b)
    elif operacion == "-":
        return resta(a, b)
    elif operacion == "*":
        return multiplicacion(a, b)
    elif operacion == "/":
        return division(a, b)
    else:
        raise ValueError("Error: Operador inválido.")

# Ejemplo de uso
try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    operador = input("Ingrese el operador (+, -, *, /): ")

    resultado = calcular(operador, num1, num2)
    print("El resultado es:", resultado)

except ValueError as e:
    print(str(e))
