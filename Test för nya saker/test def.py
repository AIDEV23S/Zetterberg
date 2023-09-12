import keyboard


def abo():
    x = 0
    z = 0
    x = input("Hej vi har tre abonomang att erbjuda! \n Hur många minuter brukar du ringa varje månad?: ")
    z = int(x)
    if z <= 33:
        print(f"För att du använder {z} minuter så erbjuder vi kontant abonomang")
    elif z > 33 and z <= 66:
        print(f"För att du använder {z} minuter så erbjuder vi normal abonomang")
    else:
        print(f"För att du använder {z} minuter så erbjuder vi premium")
    
    return

def femett():
    text = input("Skriv en mening bestående av minst 2 ord: ")
    text = text.strip()
    ord = text.split()

    antal = len(ord)
    ord1 = ord[0]
    ord2 = ord[-1]

    print(f"Antal ord {antal}. Första ordet: {ord1}. Sista ordet: {ord2}.")
    return
def femtva():
    fuck = input("Skriv ditt personnummer 10 siffror med - sträck :/ ")
    x = fuck[2:6]
    if x == "0907":
        print("grattis åsna!")

    return
def femtre():
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
    return
def t():
    print("\nESC TO EXIT\nHej välj en av följande program\n1: Abonomang\n2: Mening\n3: Födelsedag\n4: Man eller mus\nC:/ ")
    print("\n-------------------------------------------------")
i = 1
print("\nESC TO EXIT\nHej välj en av följande program\n1: Abonomang\n2: Mening\n3: Födelsedag\n4: Man eller mus\nC:/ ")
print("\n-------------------------------------------------")
while i == 1:
        if keyboard.is_pressed('1'):
            abo()
            t()
        elif keyboard.is_pressed('2'):
            femett()
            t()
        elif keyboard.is_pressed('3'):
            femtva()
            t()
        elif keyboard.is_pressed('4'):
            femtre()
            t()
        elif keyboard.is_pressed('esc'):
                i = 0
    
                


