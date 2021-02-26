import PodschetiVertical
import DiffrentFunctions

def vertical():
    a = []
    action = DiffrentFunctions.Action("InputVertical.txt")
    if action == 1:
        HeightStr = DiffrentFunctions.InPutLine(1, "InputVertical.txt")
        height = DiffrentFunctions.SearchPar(HeightStr)
        SpeedStr = DiffrentFunctions.InPutLine(2, "InputVertical.txt")
        speed = DiffrentFunctions.SearchPar(SpeedStr)
        TimeStr = DiffrentFunctions.InPutLine(3, "InputVertical.txt")
        time = DiffrentFunctions.SearchPar(TimeStr)
    if action == 2:
        print('Укажите параметры, если что-то неизвестно укажите параметр равный "0"')
        height = float(input('Укажите высоту полета в "м": '))
        speed = float(input('Укажите начальную скорость в "м/c": '))
        time = float(input('Укажите время полета в "c": '))
    if height < 0 or speed < 0 or time < 0:
        print('Error: Укажите неотрицательные значения')
        return None
    a.append(height)
    a.append(speed)
    a.append(time)
    t = ZeroCount(a)
    if t > 2:
        print('Error: Проверьте ввод данных, известных параметров должно быть 1 и более: ')
        return None
    else:
        VerticalPoz(a)


def ZeroCount(mass):
    count = 0
    for i in mass:
        if i == 0:
            count += 1
    return count


def VerticalPoz(mass):
    height = mass[0]
    speed = mass[1]
    time = mass[2]
    PodschetiVertical.PodVertical(height, speed, time)