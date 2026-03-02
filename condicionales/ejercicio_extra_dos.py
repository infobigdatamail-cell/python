'''

Si monedas ≥ 50 → “Puedes abrir el cofre” y se restan 50.
Si no → “Faltan X monedas”

'''
monedas = input("¿Cuantas monedas tienes? ")

monedas = int(monedas)
if monedas >= 50:
    print ('Puedes abrir el cofre')
    monedas -= 50
    print (f'Ahora tienes {monedas} monedas')
else:
    monedas = 50 - monedas
    print (f'Falta {monedas} monedas')
