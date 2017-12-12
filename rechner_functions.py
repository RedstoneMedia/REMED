def mathToList(calc):
    #Variablen Initializieren
    numbers = []
    operators = []
    numbercount = 0

    for i in range(len(calc)):
        if calc[i].isdigit():
            try:
                numbers[numbercount] = numbers[numbercount]+calc[i]
            except(IndexError):
                numbers.append(calc[i])
        else:
            numbercount += 1
            operators.append(calc[i])
    calc = []
    for i in range(len(numbers)):
        calc.append(numbers[i])
        try:
            calc.append(operators[i])
        except:
            print('', end='')
    return calc

print(mathToList(input()))
