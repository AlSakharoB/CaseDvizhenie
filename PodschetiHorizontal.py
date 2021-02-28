import matplotlib.pyplot as plt
from math import sqrt
from matplotlib import pylab
import MailSent


def PodHorizontal(h, r, s, t):
    if h == 0:
        if r == 0:
            if s == 0:
                print('Error: По заданым параметрам построить график нельзя')
                return None
            elif s != 0 and t != 0:
                r = s * t
                h = 9.8 * t ** 2 / 2
            else:
                print('Error: По заданым параметрам построить график нельзя')
                return None
        else:
            if s != 0:
                t = r / s
                h = 9.8 * t ** 2 / 2
            elif t != 0:
                s = r / t
                h = 9.8 * t ** 2 / 2
    else:
        if r == 0:
            if s == 0:
                print('Error: По заданым параметрам построить график нельзя')
                return None
            else:
                t = sqrt(2 * h / 9.8)
                r = s * t
        else:
                t = sqrt(2 * h / 9.8)
                s = r / t
                r = s * t
    HorOutPut(h, r, s, t)


def HorOutPut(h, r, s, t):
    a = []
    b = []
    x = 0
    y = 0
    t1 = 0
    while y >= 0 and x < r and t1 <= t:
        y = h - (9.8 * t1 ** 2 / 2)
        x = s * t1
        t1 += 0.01
        a.append(x)
        b.append(y)
    plt.figure(figsize=(6, 6))
    plt.plot(a, b)
    max = r
    if r < h:
        max = h
    pylab.xlim(0, max + max // 10)
    pylab.ylim(0, max + max // 10)
    print('{}: {} {}'.format('Максимальная высота', round(h, 2), "м"))
    print('{}: {} {}'.format('Дальность полета', round(r, 2), "м"))
    print('{}: {} {}'.format('Длительность полета', round(t, 2), "c"))
    print('{}: {} {}'.format('Начальная скорость', round(s, 2), "м/с"))
    WriteHor(h, r, t, s)
    plt.show()


def WriteHor(h, r, t, s):
    fout = open("Output.txt", "w", encoding="UTF-8")
    fin = open("InputHorizontal.txt", "w", encoding="UTF-8")
    fin.write('Тема: Движение горизонтально, если параметр не известен замените его на "0" \n')
    fin.write('\t{}\n\t{}\n\t{}\n\t{}\n'.format("Укажите дальность полета в 'м': ", "Максимальная высота в 'м': ",
                                                "Начальная скорость в 'м/с'", "Длительность полета в 'с': "))
    fin.close()
    fout.write('{}: {}\n'.format('Тема', 'Движение вертикально вверх'))
    fout.write('\t{}: {} {}\n'.format('Максимальная высота', round(h, 2), "м"))
    fout.write('\t{}: {} {}\n'.format('Дальность полета', round(r, 2), "м"))
    fout.write('\t{}: {} {}\n'.format('Длительность полета', round(t * 2, 2), "c"))
    fout.write('\t{}: {} {}\n'.format('Начальная скорость', round(s, 2), "м/с"))
    fout.close()
    email = input('Хотите получить результаты по почте?Если нет, то просто нажмите на Enter: ')
    message = ('{}: {}\n'.format('Тема', 'Движение вертикально вверх')) \
              + ('\t{}: {} {}\n'.format('Максимальная высота', round(h, 2), "м")) \
              + ('\t{}: {} {}\n'.format('Дальность полета', round(r, 2), "м")) \
              + ('\t{}: {} {}\n'.format('Длительность полета', round(t * 2, 2), "c")) \
              + ('\t{}: {} {}\n'.format('Начальная скорость', round(s, 2), "м/с"))
    MailSent.MailCheck(email, message)
