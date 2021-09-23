import random

for i in range(random.randint(1, 10)):
    print()
    print()
    letters = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'Tren']
    letter = letters[random.randint(0, len(letters) - 1)]
    number = random.randint(1, 8)
    players = ["Racso", "Santo", "Shazana"]
    playersMelee = random.randint(0, len(players))
    print("Cuantos melee:", playersMelee, "Cuantos armas:", (len(players) - playersMelee))

    for i in range(playersMelee):
        num = random.randint(0, len(players) - 1)
        print("Melee", players.pop(num))

    print("Quedarse:", "si" if random.randint(0, 1) == 1 else "no")
    print("Posicion mapa:", letter, number if letter != 'Tren' else "")
