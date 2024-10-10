print('------------Detector de Palíndromos------------')

ElInput = input('Ingresar string: ')
ConTrim = ElInput.replace(" ", "")
palabra = ConTrim.lower()

def invertir(palabra):
    return palabra[::-1]

mi_palabra = invertir(palabra)

if palabra.lower() == invertir(palabra):
    print('El string ingresado es palíndromo.')
else:
    print('El string ingresado no es palíndromo.')