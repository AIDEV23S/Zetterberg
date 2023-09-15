print(''.join([c + 'o' + c if c.isalpha() and c not in 'AEIOUaeiou' else c for c in input("Skriv in en text: ")]))
