# используется для сортировки
from operator import itemgetter


class Driver:
    """Водитель"""

    def __init__(self, id, fio, sal, Avtopark_id):
        self.id = id
        self.fio = fio
        self.sal = sal
        self.Avtopark_id = Avtopark_id


class Avtopark:
    """Автопарк"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class DriverAvtopark:
    """Связи многие-ко-многим"""

    def __init__(self, Avtopark_id, Driver_id):
        self.Avtopark_id = Avtopark_id
        self.Driver_id = Driver_id


# Автопарк
Avtoparks = [
    Avtopark(1, 'Автопарк Лада'),
    Avtopark(2, 'Автопарк Ford'),
    Avtopark(3, 'Автопарк BMW'),
]

# Водитель
Drivers = [
    Driver(1, 'Андреев', 60000, 3),
    Driver(2, 'Пахомкин', 35000, 1),
    Driver(3, 'Толпаров', 45000, 2),
    Driver(4, 'Шевчук', 35000, 1),
    Driver(5, 'Рогозин', 45000, 2),
]

Drivers_Avtoparks = [
    DriverAvtopark(1, 2),
    DriverAvtopark(2, 3),
    DriverAvtopark(1, 4),
    DriverAvtopark(2, 5),
    DriverAvtopark(3, 1),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(e.fio, e.sal, d.name)
                   for d in Avtoparks
                   for e in Drivers
                   if e.Avtopark_id == d.id]

    # Соединение данных многие-ко-многим
    many_to_many_tDriver = [(d.name, ed.Avtopark_id, ed.Driver_id)
                         for d in Avtoparks
                         for ed in Drivers_Avtoparks
                         if d.id == ed.Avtopark_id]

    many_to_many = [(e.fio, e.sal, Avtopark_name)
                    for Avtopark_name, Avtopark_id, Driver_id in many_to_many_tDriver
                    for e in Drivers if e.id == Driver_id]

    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)

    print('\nЗадание А2')
    res_12_unsorted = []
    for d in Avtoparks:
        d_Drivers = list(filter(lambda i: i[2] == d.name, one_to_many))
        if len(d_Drivers) > 0:
            d_sals = [sal for _, sal, _ in d_Drivers]
            d_sals_sum = sum(d_sals)
            res_12_unsorted.append((d.name, d_sals_sum))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание А3')
    res_13 = {}
    for d in Avtoparks:
        if 'Автопарк' in d.name:
            d_Drivers = list(filter(lambda i: i[2] == d.name, many_to_many))
            d_Drivers_names = [x for x, _, _ in d_Drivers]
            res_13[d.name] = d_Drivers_names

    print(res_13)


if __name__ == '__main__':
    main()

