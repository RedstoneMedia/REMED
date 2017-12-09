import math , time
from Rechner_Main import *


def clear():
    for i in range(30):
        print("                                                                                                                  ")


Command = input("bitte Command eingeben : ")


LIST = Command.split(" ")

LIST[0] = LIST[0].lower()

if LIST[0] == "umwandeln":
    ErGebnisse = []
    count = 0
    flächen = 0
    Längen = 0
    try:
        text = open(LIST[1],mode="r").readlines()
    except:
        print("Datei nicht Gefunden oder Angegeben")
        quit()
    for i in text:
        count += 1
        Werte2 = i.split(",")
        i = i.replace("\n","")
        Werte = i.split(",")
        if "^2" in Werte[1] or "^2" in Werte[2] or "a" in Werte[1] or "ha" in Werte[1] or "a" in Werte[2] or "ha" in Werte[2]:
            flächen += 1
            Werte[1] = Werte[1].replace("^2","")
            Werte[2] = Werte[2].replace("^2", "")
            s1 = 0
            s2 = 0

            #km
            if "km" in Werte[1] or "km" == Werte[1]:
                s1 = 7
            if "km" in Werte[2] or "km" == Werte[2]:
                s2 = 7

            #hektar
            if "ha" == Werte[1] or "ha" == Werte[1]:
                s1 = 6
            if "ha" == Werte[2] or "ha" == Werte[2]:
                s2 = 6

            #ar
            if "a" == Werte[1] or "a" == Werte[1]:
                s1 = 5
            if "a" == Werte[2] or "a" == Werte[2]:
                s2 = 5

            #meter
            if "m" == Werte[1] or "m" == Werte[1]:
                s1 = 4
            if "m" == Werte[2] or "m" == Werte[2]:
                s2 = 4

            #dezimeter
            if "dm" == Werte[1] or "dm" == Werte[1]:
                s1 = 3
            if "dm" == Werte[2] or "dm" == Werte[2]:
                s2 = 3

            #cm
            if "cm" == Werte[1] or "cm" == Werte[1]:
                s1 = 2
            if "cm" == Werte[2] or "cm" == Werte[2]:
                s2 = 2

            #mm
            if "mm" == Werte[1] or "mm" == Werte[1]:
                s1 = 1
            if "mm" == Werte[2] or "mm" == Werte[2]:
                s2 = 1

            schritte = s1 - s2

            if "-" in str(schritte):
                ergebnis = float(Werte[0])
                schritte = str(schritte).replace("-","")
                for b in range(int(schritte)):
                    ergebnis /= 100
                ErGebnisse.append("Nummer : " + str(count) + " , " + str(ergebnis) + Werte2[2])

            else:
                ergebnis = float(Werte[0])
                for b in range(int(schritte)):
                    ergebnis *= 100
                ErGebnisse.append("Nummer : " + str(count) + " , " + str(ergebnis) + Werte2[2])
            print("Ergebnis ist : " + str(ergebnis))
            clear()

        else:

            Längen += 1

            s1 = 0
            s2 = 0

            # km
            if "km" in Werte[1] or "km" == Werte[1]:
                s1 = 5
            if "km" in Werte[2] or "km" == Werte[2]:
                s2 = 5

            # meter
            if "m" == Werte[1] or "m" == Werte[1]:
                s1 = 4
            if "m" == Werte[2] or "m" == Werte[2]:
                s2 = 4

            # dezimeter
            if "dm" == Werte[1] or "dm" == Werte[1]:
                s1 = 3
            if "dm" == Werte[2] or "dm" == Werte[2]:
                s2 = 3

            # cm
            if "cm" == Werte[1] or "cm" == Werte[1]:
                s1 = 2
            if "cm" == Werte[2] or "cm" == Werte[2]:
                s2 = 2

            # mm
            if "mm" == Werte[1] or "mm" == Werte[1]:
                s1 = 1
            if "mm" == Werte[2] or "mm" == Werte[2]:
                s2 = 1

            schritte = s1 - s2

            if s2 == 5 and not s1 == 5:
                if schritte < 0:
                    schritte -= 2
                elif schritte > 0:
                    schritte += 2
                else:
                    schritte += 0




            if "-" in str(schritte):
                ergebnis = float(Werte[0])
                schritte = str(schritte).replace("-","")
                for b in range(int(schritte)):
                    ergebnis /= 10
                ErGebnisse.append("Nummer : " + str(count) + " , " + str(ergebnis) + Werte2[2])

            else:
                ergebnis = float(Werte[0])
                for b in range(int(schritte)):
                    ergebnis *= 10
                ErGebnisse.append("Nummer : " + str(count) + " , " + str(ergebnis) + Werte2[2])
            print("Ergebnis ist : " + str(ergebnis))
            clear()










    delete = open("Umgerechnete_Einheiten.txt", mode="w")
    delete.write("")
    delete.close()

    for i in ErGebnisse:
        output = open("Umgerechnete_Einheiten.txt", mode="a")
        output.write(str(i))
        output.close()

    clear()
    cdown = 6
    while not cdown == 0:
        print("  ------------------------------------------------------------------------------  ")
        print(str(count) + " Ergebnise wurden berechnent !")
        print(str(flächen) + " Flachen wurden berechnet !")
        print(str(Längen) + " Längen wurden berechnet !")
        print("Program endet in : " + str(cdown) + " Sekunden")
        print("  ------------------------------------------------------------------------------  ")
        time.sleep(1)
        cdown -= 1
        clear()
    quit()

else:
    Rechnen(List=LIST)
    print(Rechnen.selflist[0])






