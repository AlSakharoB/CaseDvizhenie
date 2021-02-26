import Vertical
import PodschetiHorizontal
import DiffrentFunctions

def horizontal():
    a = []
    action = DiffrentFunctions.Action("InputHorizontal.txt")
    if action == 1:
        Range_Str = DiffrentFunctions.InPutLine(1, "InputHorizontal.txt")
        range_ = DiffrentFunctions.SearchPar(Range_Str)
        HeightStr = DiffrentFunctions.InPutLine(2, "InputHorizontal.txt")
        height = DiffrentFunctions.SearchPar(HeightStr)
        SpeedStr = DiffrentFunctions.InPutLine(3, "InputHorizontal.txt")
        speed = DiffrentFunctions.SearchPar(SpeedStr)
        TimeStr = DiffrentFunctions.InPutLine(4, "InputHorizontal.txt")
        time = DiffrentFunctions.SearchPar(TimeStr)
    if action == 2:
        print('Укажите параметры, если что-то неизвестно укажите параметр равный "0"')
        range_ = float(input('Укажите дальность полета в "м": '))
        height = float(input('Укажите высоту полета в "м": '))
        speed = float(input('Укажите начальную скорость в "м/c": '))
        time = float(input('Укажите время полета в "c": '))
    if height < 0 or speed < 0 or time < 0 or range_ < 0:
        print('Error: Укажите неотрицательные значения')
        return None
    a.append(range_)
    a.append(height)
    a.append(speed)
    a.append(time)
    t = Vertical.ZeroCount(a)
    if t > 3 or (t > 2 and range_ != 0):
        print('Error: Проверьте ввод данных, известных параметров должно быть 1 и более: ')
        return None
    else:
        HorizontalPoz(a)


def HorizontalPoz(mass):
    r = mass[0]
    h = mass[1]
    s = mass[2]
    t = mass[3]
    PodschetiHorizontal.PodHorizontal(h, r, s, t)