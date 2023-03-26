import random

Gruen = [0]
Rot = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
Schwarz = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
Startguthaben = 250
Starteinsatz = 1

final_balances = []
for j in range(10000):
    Guthaben = Startguthaben
    Einsatz = Starteinsatz
    for i in range (20):
        Feld_mit_Kugel = random.randint(0,36)

        if Feld_mit_Kugel in Rot:
            Guthaben += Einsatz
            Einsatz = Starteinsatz

        elif Feld_mit_Kugel in Schwarz:
            Guthaben -= Einsatz
            Einsatz *= 2

        elif Feld_mit_Kugel in Gruen:
            Guthaben -= Einsatz
            Einsatz *= 2

        if Guthaben - Einsatz < 0:
            break
    
    final_balances.append(Guthaben)

average_balance = sum(final_balances) / 10000 -250
print("The average balance after playing 10k rounds is", average_balance, "CHF.")

# Mit diesem Programm kann man z.B. den Erwartungswert nach 20 Runden mit der Martingale Strategie überprüfen
