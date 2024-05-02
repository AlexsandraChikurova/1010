import json
def jsn():
    filename = '1.json'
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

        for product in data['products']:
            print(f"Название: {product['name']} Цена: {product['price']}")
            print(f"Вес: {product['weight']}")
            if product['available']:
                print("В наличии")
            else:
                print("Нет в наличии!")
            print()
import json


import json

def add_product_to_json():
    fili = '10.json'
    name = input("Введите название продукта: ")
    price = int(input("Введите цену продукта: "))
    weight = int(input("Введите вес продукта: "))
    available = input("Продукт в наличии? (да/нет): ").lower() == 'да'

    with open(fili, 'r', encoding='utf-8') as file:
        data = json.load(file)
        data['products'].append({
            "name": name,
            "price": price,
            "weight": weight,
            "available": available
        })

    with open(fili, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
def z3():
    with open('en-ru.txt', 'r', encoding='utf-8') as file:
        rows = file.readlines()
        ru_en = {}

        for row in rows:
            words = row.strip().split(' - ')
            if len(words) == 2:
                en_word = words[0]
                ru_words = words[1].split(', ')
                for word in ru_words:
                    ru_en[word] = en_word

        # Выводим отладочную информацию
    print("Отсортированный словарь:")
    for ru, en in ru_en.items():
        print(f"{ru} - {en}")

    with open('ru-en.txt', 'w', encoding='utf-8') as file:
        sort = dict(sorted(ru_en.items()))
        for ru, en in sort.items():
            file.write(f"{ru} - {en}\n")


while True:
    print('1. список')
    print('2. добавка')
    print('3. русангл')
    print('4. Выход')
    a = int(input('Выберите действие: '))
    if a == 1:
        jsn()
    elif a == 2:
        add_product_to_json()
    elif a == 3:
        z3()
    elif a == 4:
        break
    else:
        print('Неверное действие')
