lista = []
x = 0
while x < 10:
    skriv = int(input("Skriv heltal som läggs in i lista: "))
    if skriv not in lista:
        lista.append(skriv)
        x += 1
    else:
        print("Heltalet finns redan i listan. Försök igen.")
    print(lista)
print("Unika heltal i listan:", lista)
