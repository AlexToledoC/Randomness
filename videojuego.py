import random


def run():
    print("Bienvenid@ al programa para adivinar el número que la computadora pensó.")
    numero_aleatorio = random.randint(1, 1000)
    numero_elegido = int(input("Escribe un número del 1 al 1000: "))
    while numero_aleatorio != numero_elegido:
        if numero_elegido < numero_aleatorio:
            numero_elegido = int(input("Intenta con un número más grande: "))
        else:
            numero_elegido = int(input("Intenta con un número más pequeño: "))
    print("Felicidades. ¡Has acertado!")
    

if __name__ == '__main__':
    run()