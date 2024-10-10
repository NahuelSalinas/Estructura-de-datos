print('-----------------CADENA DE PARENTESIS-----------------')
Cadena = input('Ingrese su cadena de (): ')

def EsCadena(Cadena):
    trim = Cadena.replace("", "")
    resto = len(trim) % 2
    if resto != 0:
        print('Falso')
    else:
        print('Facto')

print(EsCadena(Cadena))
