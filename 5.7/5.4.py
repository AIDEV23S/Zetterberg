def oversatt_till_rovarspraket(text):
    vokaler = "AEIOUaeiou"
    oversatt_text = ""

    for tecken in text:
        if tecken.isalpha() and tecken not in vokaler:
            oversatt_text += tecken + 'o' + tecken
        else:
            oversatt_text += tecken

    return oversatt_text

text = input("Skriv in en text: ")
oversatt = oversatt_till_rovarspraket(text)
print(f"Översatt till rövarspråket: {oversatt}")
