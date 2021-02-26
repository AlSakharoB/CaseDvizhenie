def InPutLine(index, file):
    fin = open(file, encoding="UTF-8")
    lines = fin.readlines()
    fin.close()
    return lines[index]


def Action(file):
    print('\t1.Считать данные из файла', file)
    print('\t2.Ввести данные с клавиатуры')
    act = int(input('Метод: '))
    if act < 1 or act > 2:
        print('Error: Упс...Укажите число от 1 до 2')
        act = int(input('Метод: '))
    return act


def SearchPar(str_):
    par = ''
    for i in str_:
        if i.isdigit() or i == '.':
            par += i
    return float(par)
