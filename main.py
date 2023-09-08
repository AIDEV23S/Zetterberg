while True:
  print("Hej! Vi har tre abonnemang som kan passa dig!\n")
  ofta = float(input("Hur många minuter ringer du varje månad?"))
  if ofta < 33:
      print(f"Du skall köpa vårt kontant erbjudande {ofta}")
  elif ofta > 33 and ofta <= 66:
      print(f"Du måste köpa normala erbjudandet som ligger på 6000kr för du använder {ofta} minuter i månaden")
  else:
      print(f"KÖP PLUS {ofta}")
  a = input("Vill du köra igen? Y/N:    ").lower()
  if a == "n":
      break
