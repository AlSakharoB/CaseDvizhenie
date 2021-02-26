import Vertical
import Horizontal
import PodUglom
import webbrowser


print('Выберите тип движения:' + '\n', '  1.Движение вертикально вверх' + '\n', '  2.Движение под углом к горизонту')
print('   3.Движение горизонтально')
print('   4.Ознакомится с материалами по темам')
action = int(input('Тип: '))
while action < 1 or action > 4:
    print('Error: Упс...Укажите число от 1 до 4')
    action = int(input('Тип: '))
if action == 4:
    webbrowser.open_new_tab('http://fizmat.by/kursy/kinematika/parabolicheskoe')
    action = int(input('Тип: '))
    while action < 1 or action > 4:
        print('Error: Упс...Укажите число от 1 до 4')
        action = int(input('Тип: '))
if action == 1:
    Vertical.vertical()
if action == 2:
    PodUglom.poduglom()
if action == 3:
    Horizontal.horizontal()

