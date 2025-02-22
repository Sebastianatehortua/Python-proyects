mayor = None
menor = None

while True:
    num = int(input("Ingrese un número (negativo para salir): "))
    
    if num < 0:
        break  # Sale del ciclo si el número es negativo
    
    if mayor is None or num > mayor:
        mayor = num
    
    if menor is None or num < menor:
        menor = num

if mayor is not None and menor is not None:
    print(f"Número mayor ingresado: {mayor}")
    print(f"Número menor ingresado: {menor}")
else:
    print("No se ingresaron números válidos.")

