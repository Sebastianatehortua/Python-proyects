numero=float(input('Digite un numero: '))
residuo= numero % 5
residuo2=numero % 11
if residuo==0 and residuo2==0:
    print('el numero es divisible por 5 y 11')
else:
    print('No es divisible por 5 y 11')