#mostrar la cantidad de numeros positivos multiplos de 2

numero = int(input('Ingrese un entero positivo: '))
cont=0

while numero%2==0:
    cont=cont+1
    numero = int(input('Ingrese un entero positivo: '))

print(f'La cantidad de multiplos de 2 es: {cont}')

