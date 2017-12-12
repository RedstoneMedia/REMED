def mathToList(calc):
    numbers = []
    operators = []
    numbercount = 0
    trash = ''
    for i in range(len(calc)):
        if calc[i].isdigit():
            try:
                numbers[numbercount] = numbers[numbercount]+calc[i]
            except(IndexError):
                numbers.append(calc[i])
        else:
            numbercount += 1
            operators.append(calc[i])
    return [numbers,operators]
print(mathToList(input()))