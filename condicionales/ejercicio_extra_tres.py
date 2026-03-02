'''

Si nivel ≥ 10 → “Mapa avanzado desbloqueado”.
Si no → “Sigue subiendo nivel”.

'''
# Muestra mensaje por consola y guarda lo que escribe por teclado en una variable
nivelEntero = input("¿Que nivel tienes? ")

# Convierte la variable a tipo int
nivelEntero = int(nivelEntero)

# Estructura if y else para procesar los datos
if nivelEntero >= 10:
    print ('Mapa avanzado desbloqueado')
else:
    print ('Sigue subiendo nivel')
