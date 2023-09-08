text = input("Skriv en mening bestående av minst 2 ord: ")
text = text.strip()
ord = text.split()

antal = len(ord)
ord1 = ord[0]
ord2 = ord[-1]

print(f"Antal ord {antal}. Första ordet: {ord1}. Sista ordet: {ord2}.")