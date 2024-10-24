#Cadena de paréntesis
Cadena1 = "()(())" #True
Cadena2 = "())" #False

def EsCadena(Cadena):
    trim = Cadena.replace("", "")
    resto = len(trim) % 2
    if resto != 0:
        print('Falso')
    else:
        print('Verdadero')

print(EsCadena(Cadena1))
print(EsCadena(Cadena2))
