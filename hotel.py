# # 1. Написать класс, хранящий информацию о длине лап разных животных,
# # и его название. Класс ничего не должен делать (даже инит!!!)

class Animals(dict):
    animals_dict = {
        'cat': 24,
        'dog': 57,
        'wolf': 73,
        'fox': 35,
        'duck': 7,
    }

    # 2. Добавить в класс метод, позволяющий указывать название животного
    #    и длину его лап

    def add_animals(self, animal, length):
        self.animals_dict[animal] = length
        return Animals.animals_dict

    # 4. Добавить способ печати животного на экран
    #    "Кошка, лапы 10 см"
    # Todo неполучилось вывести одно животное
    def __str__(self):
        result = ''
        for key, val in an.animals_dict.items():
            result += '{}, длина лам {} см.\n'.format(key, val)
        return result


an = Animals()

print(an.add_animals('giraffe', 97))

print(an)

# 3. Добавить способ сравнения классов на больше и меньше.
#    Продемонстрировать работу


giraffe = an.animals_dict['giraffe']
dog = an.animals_dict['dog']
print(giraffe < dog, '\n')


# 5. Создать класс, хранящий количества товаров на складе.
#    Если товара нет, класс должен возвращать 0 (не вываливаться)

class Products(dict):
    pr = {
        'Фен': 2,
        'Телефон': 5,
        'Ноутбук': 3,
        'Холодильник': 1,
        'Телевизор': 4,
    }

    def __missing__(self, key):
        return 0
# создание товара


p = Products({
    'Фен': 2,
    'Телефон': 5,
    'Ноутбук': 3,
    'Холодильник': 1,
    'Телевизор': 4,
})
print('Остаток на складе:', p['Телевизор'])
print('Остаток на складе:', p['Планшет'], '\n')


# 6. Создать класс Отель. Класс хранит цены на разные комнаты.
#    Класс хранит количество забронированных комнат разного типа.
#    Выдавать количество свободных комнат. Создать метод "забронировать"

class Hotel(dict):
    # Цены на разные комнаты
    num_price = {
        'Стандарт': 1500,
        'Комфорт': 2500,
        'Семейный': 3500,
        'Люкс': 5000,
    }
    # Количество забронированных комнат
    num = {
        'Стандарт': 3,
        'Комфорт': 2,
        'Семейный': 1,
        'Люкс': 1,
    }

    def free_room(self):
        result = {}
        for key, val in self.num.items():
            # Общее кол-во номер каждого класса - забронированные
            result[key] = 5 - val
        return result

    def reserve(self, room, amount):
        for key, val in self.num.items():
            if room in key:
                self.num[room] += amount
        return h.num


h = Hotel()
print(h.num_price)
print('Свободные номера', h.free_room())  # Количество свободных комнат
print('Бронь', h.reserve('Люкс', 1))  # Бронирование
print('Бронь', h.reserve('Стандарт', 1))  # Бронирование
print('Бронь', h.reserve('Комфорт', 1))  # Бронирование
print('Свободные номера', h.free_room())  # Количество свободных комнат
