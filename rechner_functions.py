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

#meine varriante xD
def get_Values(Values):
    temp = list(Values)
    temp2 = []
    temp3 = []
    temp4 = []
    temp5 = []
    klammern = []
    k = False
    for i in temp:
            if not k == True:
                try:
                    int(i)
                    temp3.append(str(i))
                except:
                    if i == "(" or i == ")":
                        k = True
                    else:
                        temp2.append("".join(temp3))
                        temp3 = []
                        temp2.append(i)
            else:
                if i == ")":
                    k = False
                i = str(i).replace(")","")
                i = str(i).replace("(", "")

                try:
                    int(i)
                    temp4.append(i)
                except:
                    klammern.append("".join(temp4))
                    temp4 = []
                    if not str(i) == "":
                        klammern.append(str(i))

    temp2.append("".join(temp3))

    #gibt bei klammern "" zurück damit mann später augerechnete zahl einsetzen kann !
    return (temp2,klammern)


def is_single_item_list(list_to_check):
    #Checkt ob Liste leer ist
    try:
        _ = list_to_check[0]
    except IndexError:
        return False
    #chekt ob nur eins drinne ist
    try:
        _ = list_to_check[1]
    except IndexError:
        return True

    return False

def is_emty(List):
    try:
        _ = List[0]
    except IndexError:
        return True
