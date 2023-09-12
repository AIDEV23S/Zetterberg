import random
import os

class Player:
    def __init__(self, name, lastname, place=1, life=100, cash=0, hunger=100, honor = 0):
        self.name = name
        self.lastname = lastname
        self.place = place
        self.life = life
        self.cash = cash
        self.hunger = hunger
        self.honor = honor

def save_game(player):
    with open("saved_game.txt", "w") as file:
        file.write(f"{player.name}\n")
        file.write(f"{player.lastname}\n")
        file.write(f"{player.place}\n")
        file.write(f"{player.life}\n")
        file.write(f"{player.cash}\n")
        file.write(f"{player.hunger}\n")
        file.write(f"{player.honor}\n")
        

def load_game():
    if os.path.exists("saved_game.txt"):
        with open("saved_game.txt", "r") as file:
            name = file.readline().strip()
            lastname = file.readline().strip()
            place = int(file.readline().strip())
            life = int(file.readline().strip())
            cash = int(file.readline().strip())
            hunger = int(file.readline().strip())
            honor = int(file.readline().strip())
            return Player(name, lastname, place, life, cash, hunger, honor)
    else:
        return None

# Check if a saved game exists
loaded_player = load_game()

if loaded_player:
    print("Loaded saved game.")
    player = loaded_player
else:
    playername = input("What is your first name: ")
    playerlast = input("What is your last name: ")
    player = Player(playername, playerlast, 1)


def village():
    event = random.choice(["friendly_villagers", "bandits"])
    name_place = "Village"
    
    if event == "friendly_villagers":
        print("\n\nYou arrive at a peaceful village. The villagers welcome you warmly.")
        input("You spend some time in the village...\n\n")
        print("You've gained 10 honor.")
        player.honor += 10
        input("Press enter to continue your journey.")
    
    elif event == "bandits":
        print("\n\nAs you approach the village, you notice a group of bandits blocking the way.")
        choice = input("\n1: Fight the bandits\n2: Try to sneak around them: ").lower()
        if choice == "1":
            print("\nYou engage in a fierce battle with the bandits.")
            if random.randint(0, 1):
                print("You defeated the bandits! You've gained 20 cash and 5 honor.")
                player.cash += 20
                player.honor += 5
            else:
                print("The bandits overpower you. You lose 30 cash.")
                player.cash -= 30
            input("Press enter to continue your journey.")
        else:
            print(f"\nYou manage to sneak around the bandits and continue your journey.")
            input("Press enter to continue your journey.")
    player.place = 3


def forrest():
    event = random.choice(["lost", "death", "stranger",])
    name_place = "Deep forrest"
    if event == "lost":
        print("\n\nYou are lost in a forrest. Surrounded by mud. You get going")
        input("You continue in the forrest...\n\n")
    
    elif event == "death":
        print("\n\nYou wake up in a forrest after bloody fight. All around you are dead bodies.")
        choice = input("\n\n1: Loot the corpses\n2: Get going: ").lower()
        if choice == "1":
            player.cash += 10
            player.honor -= 1
            print(f"\nYou gained some cash, now you have {player.cash} denar. You've lost honor now at: {player.honor}\n\n")
            input("Press enter to walk east")
        else:
            input("\nPress enter to walk east")
    elif event == "stranger" :
        print("\n\nYou wake up by a stranger in the middle of the forrest. No idea how you got here.\nStranger: Hey mate what you doi'n her?")
        choice = input("\n1: Strangle the fucker\n2: Talk to him: ").lower()
        if choice == "1":
            print("\n\nWithout hesitation you take your arm around his neck and choke him. \nNow that you started it you feel you must kill him and you hold for a bit too long\n\nYou looted 35 denars and lost 15 honor\n\n")
            player.cash +=35
            player.honor -= 15
            input("Press enter to walk east")
        else:
            print(f"\n{player.name}: Hey what happend, where are we?\nStranger: We are in {name_place}. Well dont get to friendly some people died not to far away west of here. Either way you should go, Now.\n")
            input("Press enter to walk east")
    player.place = 2

##Fortssätttt
def city_entrance():
    name_place = "City Gates"
    print("\nYou see in the distance a city. It smells horrid. But with no food and nothing to your name you decide to walk over to the gate...")
    events = random.choice(["Guard", "Peasant", "Walk"])
    if events == "Walk":
        input("The gates seem to be open. \nYou decide to walk in...")
    elif events == "Guard":
        print("\nYou walk towards the gate. \nGuard: You not takin nothor step, give us ye gold.")
        choice = input("\n\n1: Give the guards all your gold to enter the city\n2: Kill the guard").lower()
        if choice == "1":
            player.cash = 0
            input("You enter the city...")
        else:
            print("You try to get a armlock against his neck. \n\nThe other guard stab you with a spear in the belly.\nYou bleed and soon all is black....")
            player.life -= 10000

allplaces = {
    1: forrest,
    2: village,
    3: city_entrance
}
while player.life > 0:
    nowplace=allplaces.get(player.place)
    if nowplace:
        nowplace()
    else:
        player.place = 1
        print("ERRRORRR PLAYER PLACE")
    save_game(player)

# Game loop ends when player's life reaches 0
print("Game over. Your life is 0.")
os.remove("saved_game.txt")