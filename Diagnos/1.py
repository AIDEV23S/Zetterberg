def är_primtal(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primtal_mellan_2_och_n(n):
    primtal_lista = []
    for num in range(2, n + 1):
        if är_primtal(num):
            primtal_lista.append(num)
    return primtal_lista

n = int(input("Ange ett heltal mellan 1 och 9999999999: "))

if 1 <= n <= 999999999:
    resultat = primtal_mellan_2_och_n(n)
    print(f"Primtal mellan 2 och {n}: {resultat}")
else:
    print("Ange ett giltigt heltal mellan 1 och 99.")
