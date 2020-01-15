# Задание
# Создать список из генератора квадратов чисел
# Создать метод-генератор квадратов чисел
# Сверить генераторы м/у собой
# Обратиться к списку сгенерированных чисел через индекс

from generator import Generator


def test_generator(generator, size):
    # value возвращает объект-генератор
    value = generator(size=size).value()

    # array - список квадратов чисел на выходе генератора
    array = [x**2 for x in range(0, size)]

    for index, element in enumerate(array):
        #  в sqr_number следующее число из метода-генератора
        sqr_number = next(value)

        # Обращаемся к элементу списка через index
        print(f'compare: {array[index]:^4} and {sqr_number:^4}')
        assert element == sqr_number
    return True


assert test_generator(generator=Generator, size=10)
print('result: ok')
