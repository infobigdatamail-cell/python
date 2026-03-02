'''

4. tieneLlave (Lógico):
Si Verdadero → “La puerta se abre”.
Si no → “Está cerrada”.

'''
# Muestra mensaje por consola y guarda lo que escribe por teclado en una variable
tieneLlave = input("¿Que nivel tienes? ")


# Estructura if y else para procesar los datos
if tieneLlave.lower() == "true":
    print ('La puerta se abre')
else:
    print ('Está cerrada')
