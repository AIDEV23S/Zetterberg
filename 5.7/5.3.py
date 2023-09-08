x = 1
y = 0
#Z avgör om man ska skippa hela programmet
z = 0
while x == 1:
    y += 1
    nummer = input("Vad är ditt personnummer? 10 siffror: ")
    
    #Om man kör 5 gånger med fel antal siffror så frågar den om man vill avsluta
    if y == 5:
        leey = input("Vill du sluta? [Y/N]: ")
        leey = leey.lower()
        if leey == "y":
            x = 0
            z = 1
        else:
            y = 0
    #Slutar loopen
    if len(nummer) == 10:
        x = 0

if z == 0:
    nummer1 = int(nummer[8])
    uträckna = nummer1 % 2
    if uträckna > 0:
        print("Du är en man")
    else:
        print("Du är en kvinna")