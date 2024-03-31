from parsing import parser
import json

while True:
    location = input("Введите адрес (q -выход, r - создание нового файла): ").capitalize()
    if location.lower() == 'q':
        break

    if location.lower() == 'r':
        parser(input("Введите название файла:"))
        print("Файл создан успешно")
        continue

    points = []
    adress = location.replace(',', ' ').split()
    with open('output_adress', 'r', encoding='utf-8') as inp:
        for line in inp:
            t = line.split(';')
            if adress[0] and adress[1] in t[0]:
                points.extend([i.strip() for i in t[1:]])
                break

    coords = []
    with open('output_id', 'r', encoding='utf-8') as inp_id:
        for i in points:
            for line in inp_id:
                if i in line:
                    coords.append(line.split()[1:3])
                    break

    if coords:
        x = sum(float(i[0]) for i in coords) / len(coords)
        y = sum(float(i[1]) for i in coords) / len(coords)

        output_data = {
            "location": location,
            "average_coordinates": {"x": x, "y": y},
            "coordinates": coords
        }

        print(json.dumps(output_data, indent=4, ensure_ascii=False))
    else:
        print("Адрес не найден. Попробуйте другой адрес.")