import random , time , crypto


def clear():
    for i in range(3):
        print("                                                                                                                  ")

def zufällig_einheit(hoch2):
    if hoch2 == 1:
        einheit = random.randint(1,7)
        if einheit == 1:
            einheit = "mm^2"
        if einheit == 2:
            einheit = "cm^2"
        if einheit == 3:
            einheit = "dm^2"
        if einheit == 4:
            einheit = "m^2"
        if einheit == 5:
            einheit = "a"
        if einheit == 6:
            einheit = "ha"
        if einheit == 7:
            einheit = "km^2"
        return str(einheit)
    elif hoch2 == 2:
        einheit = random.randint(1, 5)
        if einheit == 1:
            einheit = "mm"
        if einheit == 2:
            einheit = "cm"
        if einheit == 3:
            einheit = "dm"
        if einheit == 4:
            einheit = "m"
        if einheit == 5:
            einheit = "km"
        return str(einheit)


delete = open("testfile.txt",mode="w")
delete.write("")
delete.close()

länge = input("wie vile Zufällige Rechnungen sollen Genneriert werden ? : ")



for i in range(int(länge)):
    hoch2 = random.randint(1, 2)
    floatodernicht = random.randint(1, 2)
    if floatodernicht == 1:
        Wert1 = random.uniform(1.1, 10000)
    else:
        Wert1 = random.randint(1,10000)
    einheit1 = zufällig_einheit(hoch2)
    einheit2 = zufällig_einheit(hoch2)
    while einheit1 == einheit2:
        einheit1 = zufällig_einheit(hoch2)
        einheit2 = zufällig_einheit(hoch2)

    print("  -----------------------------------------------------------  ")
    print(str(i) + "/" + str(länge))
    print("  -----------------------------------------------------------  ")
    clear()




    testfile = open("testfile.txt",mode="a")
    testfile.write(str(Wert1) + "," + einheit1 + "," + einheit2 + "\n")
    testfile.close()
