import Vertical
import PodschetiPodUglom
import DiffrentFunctions


def poduglom():
    a = []
    action = DiffrentFunctions.Action("InputPodUglom.txt")
    if action == 1:
        AlphaStr = DiffrentFunctions.InPutLine(1, "InputPodUglom.txt")
        alpha = DiffrentFunctions.SearchPar(AlphaStr)
        Range_Str = DiffrentFunctions.InPutLine(2, "InputPodUglom.txt")
        range_ = DiffrentFunctions.SearchPar(Range_Str)
        HeightStr = DiffrentFunctions.InPutLine(3, "InputPodUglom.txt")
        height = DiffrentFunctions.SearchPar(HeightStr)
        SpeedStr = DiffrentFunctions.InPutLine(4, "InputPodUglom.txt")
        speed = DiffrentFunctions.SearchPar(SpeedStr)
        TimeStr = DiffrentFunctions.InPutLine(5, "InputPodUglom.txt")
        time = DiffrentFunctions.SearchPar(TimeStr)
    if action == 2:
        print('Укажите параметры, если что-то неизвестно укажите параметр равный "0"')
        alpha = int(input('Укажите угол с градусах: '))
        range_ = float(input('Укажите дальность полета в "м": '))
        height = float(input('Укажите высоту полета в "м": '))
        speed = float(input('Укажите начальную скорость в "м/c": '))
        time = float(input('Укажите время полета в "c": '))
    if ((range_ != 0 or height != 0) and (time != 0 or time == 0) and alpha == 0 and speed == 0):
        print('Error: По заданым параметрам посчитать нельзя')
        return None
    if height < 0 or speed < 0 or time < 0 or alpha < 0 or alpha > 90:
        print('Error: Укажите неотрицательные значения')
        return None
    a.append(height)
    a.append(range_)
    a.append(alpha)
    a.append(speed)
    a.append(time)
    t = Vertical.ZeroCount(a)
    if t > 3:
        print('Error: Проверьте ввод данных, известных параметров должно быть 1 и более: ')
        return None
    else:
        PodUglomPoz(a)


def PodUglomPoz(mass):
    height = mass[0]
    range_ = mass[1]
    alpha = mass[2]
    speed = mass[3]
    time = mass[4]
    PodschetiPodUglom.PodUglom(height, range_, alpha, speed, time)