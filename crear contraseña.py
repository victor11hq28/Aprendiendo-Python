import random
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>?/`~"
longitud = int(input("Ingrese la longitud de la contraseña: "))
random.choices = random.choices(caracteres, k=longitud)
contraseña = ''.join(random.choices)
print("Contraseña generada:", contraseña)