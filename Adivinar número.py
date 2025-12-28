import random

def generate_random_numbers(count, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(count)]

num = generate_random_numbers(1, 1, 20)
vida = 5

print("Adivina el numero entre 1 y 20:")

while True:
    try:

        print("♥" * vida)
        guess = int(input("Introduce tu suposición: "))

        if guess < 1 or guess > 20:
            print("Por favor, introduce un número entre 1 y 20.")
            continue 
        
        if guess < num[0]:
            print("Demasiado bajo. Intenta de nuevo.")
        elif guess > num[0]:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            print("¡Felicidades! Has adivinado el número.")
            break 
        vida -= 1
        if vida == 0:
            print("Has perdido. El número era " + str(num[0])+".")
            break

    except ValueError:
  
        print("Entrada inválida. Por favor, introduce un número entero.")