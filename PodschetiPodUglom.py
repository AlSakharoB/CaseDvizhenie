import matplotlib.pyplot as plt
from math import sqrt, cos, sin
from matplotlib import pylab
from numpy import arcsin
import MailSent


def PodUglom(h, r, a, s, t):
    if h == 0:
        Height0(r, a, s, t, h)
    else:
        Height1(r, a, s, t, h)


def Height0(r, a, s, t, h):
    if r == 0:
        if t != 0 and s != 0:
            sinus = (9.8 * t) / (2 * s)
            a = round(arcsin(sinus) / 0.0173)
            h = s ** 2 * sin(a / 180 * 3.14) ** 2 / 19.6
            r = s ** 2 * sin(a / 180 * 3.14 * 2) / 9.8
        elif s == 0:
            s = 9.8 * t / 2 * sin(a / 180 * 3.14)
            h = s ** 2 * sin(a / 180 * 3.14) ** 2 / 19.6
            r = s ** 2 * sin(a / 180 * 3.14 * 2) / 9.8
        elif t == 0:
            t = 2 * s * sin(a / 180 * 3.14) / 9.8
            h = s ** 2 * sin(a / 180 * 3.14) ** 2 / 19.6
            r = s ** 2 * sin(a / 180 * 3.14 * 2) / 9.8
    else:
        if s != 0:
            dsinus = (9.8 * r) / (s ** 2)
            if dsinus > 1:
                dsinus = 1
            a = round((arcsin(dsinus) / 0.0173) / 2)
            t = 2 * s * sin(a / 180 * 3.14) / 9.8
            h = s ** 2 * sin(a / 180 * 3.14) ** 2 / 19.6
        else:
            s = sqrt(9.8 * r / sin(a * 2 / 180 * 3.14))
            h = s ** 2 * sin(a / 180 * 3.14) ** 2 / 19.6
            t = 2 * s * sin(a / 180 * 3.14) / 9.8
    UglOutPut(r, a, s, t, h)


def Height1(r, a, s, t, h):
    if r == 0:
        if a != 0:
            s = sqrt(2 * h * 9.8 / sin(a / 180 * 3.14) ** 2)
            t = 2 * s * sin(a / 180 * 3.14) / 9.8
            r = s ** 2 * sin(a / 180 * 3.14 * 2) / 9.8
        elif s != 0:
            sinus = sqrt(2 * h * 9.8 / s ** 2)
            a = round(arcsin(sinus) / 0.0173)
            t = 2 * s * sin(a / 180 * 3.14) / 9.8
            r = s ** 2 * sin(a / 180 * 3.14 * 2) / 9.8
    else:
        if a != 0:
            s = sqrt(2 * h * 9.8 / sin(a / 180 * 3.14) ** 2)
            t = 2 * s * sin(a / 180 * 3.14) / 9.8
        elif s != 0:
            sinus = sqrt(2 * h * 9.8 / s ** 2)
            a = round(arcsin(sinus) / 0.0173)
            t = 2 * s * sin(a / 180 * 3.14) / 9.8
            r = s ** 2 * sin(a / 180 * 3.14 * 2) / 9.8
    UglOutPut(r, a, s, t, h)


def UglOutPut(r, a, s, t, h):
    a1 = []
    b = []
    x = 0
    y = 0
    t1 = 0
    while y >= 0 and x < r and t1 <= t:
        y = s * sin(a / 180 * 3.14) * t1 - (9.8 * t1 ** 2 / 2)
        x = s * cos(a / 180 * 3.14) * t1
        t1 += 0.01
        if y >= 0:
            a1.append(x)
            b.append(y)
    a1.append(r)
    b.append(0)
    plt.plot(a1, b)
    max = r
    if r < h:
        max = h
    pylab.xlim(0, max + max // 10)
    pylab.ylim(0, max + max // 10)
    print('{}: {} {}'.format('Максимальная высота', round(h, 2), "м"))
    print('{}: {} {}'.format('Дальность полета', round(r, 2), "м"))
    print('{}: {}{}'.format('Угол броска', a, "°"))
    print('{}: {} {}'.format('Длительность полета', round(t, 2), "c"))
    print('{}: {} {}'.format('Начальная скорость', round(s, 2), "м/с"))
    WritePodUglom(h, r, a, t, s)
    plt.show()


def WritePodUglom(h, r, a, t, s):
    fout = open("Output.txt", "w", encoding="UTF-8")
    fin = open("InputPodUglom.txt", "w", encoding="UTF-8")
    fin.write('Тема: Движение под углом к горизонту, если параметр не известен замените его на "0" \n')
    fin.write('\t{}\n\t{}\n\t{}\n\t{}\n\t{}\n'.format("Укажите угол с градусах: ", "Укажите дальность полета в 'м': ",
                                                      "Максимальная высота в 'м': ", "Начальная скорость в 'м/с': ",
                                                      "Длительность полета в 'с': "))
    fin.close()
    fout.write('{}: {}\n'.format('Тема', 'Движение вертикально вверх'))
    fout.write('\t{}: {} {}\n'.format('Максимальная высота', round(h, 2), "м"))
    fout.write('\t{}: {} {}\n'.format('Дальность полета', round(r, 2), "м"))
    fout.write('\t{}: {}{}\n'.format('Угол броска', a, "°"))
    fout.write('\t{}: {} {}\n'.format('Длительность полета', round(t * 2, 2), "c"))
    fout.write('\t{}: {} {}\n'.format('Начальная скорость', round(s, 2), "м/с"))
    fout.close()
    email = input('Хотите получить результаты по почте?Если нет, то просто нажмите на Enter: ')
    message = ('{}: {}\n'.format('Тема', 'Движение вертикально вверх')) \
              + ('\t{}: {} {}\n'.format('Максимальная высота', round(h, 2), "м")) \
              + ('\t{}: {} {}\n'.format('Дальность полета', round(r, 2), "м")) \
              + ('\t{}: {}{}\n'.format('Угол броска', a, "°")) \
              + ('\t{}: {} {}\n'.format('Длительность полета', round(t * 2, 2), "c")) \
              + ('\t{}: {} {}\n'.format('Начальная скорость', round(s, 2), "м/с"))
    MailSent.MailCheck(email, message)