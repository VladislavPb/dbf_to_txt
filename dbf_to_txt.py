my_layer = iface.activeLayer()

my_str = ''
my_list = []

#проходим построчно по таблице (без сортировки)
#составляем список из кортежей
for i in my_layer.getFeatures():
    KW = str(i['KW'])
    KCN = str(i['КЦН'])
    VYD = str(i['VD'])
    #если у подвыдела есть целое значение, добавляем его после точки к выделу
    if str(i['PVD']) != 'NULL':
        VYD += '.' + str(i['PVD'])
    KATZEM = str(i['КАТЗЕМ'])
    OZU = str(i['ОЗУ'])
    
    my_list.append((KW, KCN, VYD, KATZEM, OZU))

#делаем двойную сортировку списка по элементам кортежей списка
my_list_1 = sorted(sorted(my_list, key = lambda x: x[2]), key= lambda y: y[0])

#записываем данные из кортежей отсортированного списка в строку
for j in my_list_1:
    my_str += '00)' + j[0] + ',' + j[1] + '\n'
    my_str += '01)' + j[2] + ',,' + j[3] + ',,' + j[4] + '\n'
    my_str +=  '@@\n'

#извлекаем путь до файла (директория + название файла без расширения)
my_path = my_layer.dataProvider().dataSourceUri().split('.')[0]

#записываем строку в файл в одной директории с DBF файлом
with open(f'{my_path}.txt', 'w') as text_file:
    text_file.write(my_str)
    