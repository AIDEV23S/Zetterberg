abow = list(range(1,10))
#print(abow)
plus = 0
tt = ""
sext = ""
for i in abow:
    knas = list(range(1,10))
    text = []
    for b in knas:
        plus = i * b
       # print(plus)
        text.append(plus)
    ##print(text)
    for q in text:
       # print(text[1])
       sext += f"{q}\t"
       
    print(f"{sext}")
    sext=""