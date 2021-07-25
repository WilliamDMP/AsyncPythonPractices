#La funcion filter me permite retornar un valor que me indique una condicion
elementos = list(range(-5,6))
def filtrar(elementos):
    #mostrar todos los numeros positivos 
    return (elementos > 0)


funcfiltrar = list(filter(filtrar, elementos))
print(elementos)
print(funcfiltrar)
