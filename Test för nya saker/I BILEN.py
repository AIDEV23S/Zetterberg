import random
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100

name = input("\nYou are wake up in the middle of the forrest. \nWhere you are is lost in space. You find yourself wondering what name you have: ")
lastname = input("-----------------\nWhile thinking to yourself. You remember that most people have a last name.\nWhat's yours: ")
life = 100
cash = 0
day = 0
hunger = 100
place = "Quiet Forrest"
def main():
    print("\n\n\n\n")
    print(f"\t\tMain Menu\nDay:{day}\nName: {name} {lastname}\nCash:{cash}\nHealth:{life}HP\nHunger:{hunger}\n\nYou are at {place}.\n\nYou have two options\n1: Stay here\n2: Get going\n")
    option = input(f"{name}: ")
    if option == "1":
        stay()
    elif option == "2":
        going()
    return
main()

def stay():
    global cash
    global day
    global life
    global place
    global hunger
    print("You have decided to stay. You decide to start making a shelter and sleep for the night")
    day +=1
    hunger
    event = random.choice([])