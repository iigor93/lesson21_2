from classes.store_class import Store
from classes.shop_class import Shop
from classes.request_class import Request
from make_moves import moves, print_all

# Создаем экземпляры классов Магазин и Склад
store = Store()
shop = Shop()

print("Формат запроса 'Доставить 1 яблоко со склада в магазин'")

# Печать всего что на складе и в магазине
print_all(shop, store)

# Основной цикл работы, пользователь вводит комманду, программа испоняет
while 1:
    user_input = input('Введите запрос (exit для выхода) ')
    if user_input == 'exit':
        break

    try:
        # создаем объект Request с проверкой корректности ввода
        request = Request(user_input)
    except Exception as e:
        print('Wrong request', e)
    else:
        # Основная логика программы
        moves(request, shop, store)
