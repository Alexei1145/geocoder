def parser(file_input):
    inp = open(file_input, 'r', encoding='utf-8')
    output_id = open('output_id', 'w', encoding='utf-8')
    output_adress = open('output_adress', 'w', encoding='utf-8')
    # пропускаем лишние строки
    for _ in range(5):
        inp.readline()
    # форматируем максимальные и минимальные координаты
    output_id.write(''.join(filter(lambda x: x.isdigit() or x == '.' or x == ' ', inp.readline())) + '\n')
    # переводим точки к значению id x y
    while True:
        a = inp.readline()
        if '<way id=' in a:
            break
        if 'tag' not in a:
            filtered_string = ''.join(filter(lambda x: x.isdigit() or x == '.' or x == ' ', a[:a.find('version')]))
            if filtered_string.strip():
                output_id.write(filtered_string + '\n')
    # собираем данные об адресах
    d = []
    while True:
        b = []
        number = ''
        street = ''
        # считываем объект
        while True:
            a = inp.readline()
            if a == '':
                break
            if '</way>' in a:
                break
            b.append(a)
        if a == '':
            break
        c = '<tag'
        # фильтруем здания
        while '<tag' in c:
            for i in reversed(b):
                c = i
                if 'addr:street' in i:
                    start_index = i.find('v="') + 3
                    end_index = i.find('"', start_index)
                    street = i[start_index:end_index]
                if 'addr:housenumber' in i:
                    start_index = i.find('v="') + 3
                    end_index = i.find('"', start_index)
                    number = i[start_index:end_index]
        # записываем адрес, если это здание, иначе пропускаем
        if street and number:
            q = []
            d.append(street+' '+number)
            c = '<nd ref='
            while '<nd ref=' in c:
                for i in b:
                    c = i
                    if '<nd ref=' in i:
                        start_quote = i.find('"')
                        end_quote = i.rfind('"')
                        id = i[start_quote + 1:end_quote]
                        q.append(id)
            output_adress.write(f"{street}, {number}; {'; '.join(q)}" + '\n')
        else:
            continue
    inp.close()
    output_id.close()
    output_adress.close()