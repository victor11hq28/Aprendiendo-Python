import random
lista = ['piedra', 'papel', 'tijera']
computadora = random.choice(lista)
usuario = input("Elige piedra, papel o tijera: ").lower()
if usuario not in lista:
    print("Elección inválida. Por favor elige piedra, papel o tijera.")
else:
    print(f"La computadora eligió: {computadora}")
    if usuario == computadora:
        print("Empate!")
    elif (usuario == 'piedra' and computadora == 'tijera') or \
         (usuario == 'papel' and computadora == 'piedra') or \
         (usuario == 'tijera' and computadora == 'papel'):  
        print("¡Ganaste!")
    else:
        print("¡Perdiste!") 

        