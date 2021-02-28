import matplotlib.pyplot as plt
from math import sqrt
from matplotlib import pylab
import MailSent


def PodVertical(h, s, t):
    if h == 0:
        if s == 0:
            s = t / 2 * 9.8
            h = s ** 2 / 19.6
            t /= 2
        else:
            h = s ** 2 / 19.6
            t = s / 9.8
    else:
        s = sqrt(19.6 * h)
        t = sqrt(2*h / 9.8)
    x = [h // 2, h // 2, h // 2]
    y1 = [0, h, 0]
    plt.figure(figsize=(6, 6))
    plt.plot(x, y1)
    pylab.xlim(0, h + h // 10)
    pylab.ylim(0, h + h // 10)
    print('{}: {} {}'.format('Максимальная высота', round(h, 2), "м"))
    print('{}: {} {}'.format('Длительность полета', round(t * 2, 2), "c"))
    print('{}: {} {}'.format('Начальная скорость', round(s, 2), "м/с"))
    WriteVer(h, s, t)
    plt.show()


def WriteVer(h, s, t):
    fout = open("Output.txt", "w", encoding="UTF-8")
    fin = open("InputVertical.txt", "w", encoding="UTF-8")
    fin.write('Тема: Движение вертикально вверх, если параметр не известен замените его на "0" \n')
    fin.write('\t{}\n\t{}\n\t{}\n'.format("Максимальная высота в 'м': ", "Начальная скорость в 'м/с'",
                                          "Длительность полета в 'с': "))
    fin.close()
    fout.write('{}: {}\n'.format('Тема', 'Движение вертикально вверх'))
    fout.write('\t{}: {} {}\n'.format('Максимальная высота', round(h, 2), "м"))
    fout.write('\t{}: {} {}\n'.format('Длительность полета', round(t * 2, 2), "c"))
    fout.write('\t{}: {} {}\n'.format('Начальная скорость', round(s, 2), "м/с"))
    fout.close()
    email = input('Хотите получить результаты по почте?Если нет, то просто нажмите на Enter: ')
    message = ('{}: {}\n'.format('Тема', 'Движение вертикально вверх')) \
              + ('\t{}: {} {}\n'.format('Максимальная высота', round(h, 2), "м")) \
              + ('\t{}: {} {}\n'.format('Длительность полета', round(t * 2, 2), "c")) \
              + ('\t{}: {} {}\n'.format('Начальная скорость', round(s, 2), "м/с"))
    MailSent.MailCheck(email, message)
