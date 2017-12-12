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
            pass
    return calc

#z.B. List = ['2', '+', '56']
#z.B. index = 1
#Als index immer das rechenzeichen, es werden dann die zahl davor mit der zahl danach gerechnet.
def listCalculation(list, index):
    operator = list[index]
    result = 0
    a = int(list[index-1])
    b = int(list[index+1])
    if operator == '+':
        result = a+b
    if operator == '-':
        result = a-b
    if operator == '*':
        result = a*b
    if operator == '/':
        result = a/b
    return result
