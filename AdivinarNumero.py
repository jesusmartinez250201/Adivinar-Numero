import random

intentos = 0
adivinarNumero = random.randint(1, 100)

while intentos <= 5:
    numeroIntroducido = int(input("Intenta adivinar el numero (entre 1 y 100: )"))
    intentos = intentos + 1
    if numeroIntroducido < adivinarNumero:
        print("El numero es mayor")
    if numeroIntroducido > adivinarNumero:
        print("El numero es menor")
    if numeroIntroducido == adivinarNumero:
        break

if numeroIntroducido == adivinarNumero:
    print("ADIVINASTE!!, el numero es" + str(adivinarNumero))
if numeroIntroducido != adivinarNumero:
    print("PERDISTE!!, el numero era " + str(adivinarNumero))