plånbok = 0
i = 0
cash = 0.01
while True:
    cash = float(cash * 2)
    plånbok = float(cash+plånbok)
    print(f"Du tjänar {cash:.2f}kr per dag. Din plånbok är {plånbok:.2f}kr \n Det har gått {i} dagarclear")
    i = i+1
    if plånbok >=1000000:
        break