def moves(request, shop, store):
    """ Проверяем количество товара и количество свободного места

    """
    # Получаем запрос от пользователя
    move_from = request.get_data().get('from')
    move_to = request.get_data().get('to')
    product = request.get_data().get('product')
    amount = request.get_data().get('amount')

    # Определяем откуа и куда будем доставлять
    if move_from == 'shop':
        temp_from = shop
        temp_to = store
    else:
        temp_from = store
        temp_to = shop

    if product not in temp_from.get_items().keys():
        print("Нет такого продукта")
    else:
        if temp_to.get_free_space() >= amount:
            if temp_from.remove(product, amount):
                temp_to.add(product, amount)
                print(f'\nНужное количество есть на/в {temp_from}'
                      f'\nКурьер забрал {amount} {product} со/из {temp_from}'
                      f'\nКурьер везет {amount} {product} со/из {temp_from} в/на {temp_to}'
                      f'\nКурьер доставил {amount} {product} в в/на {temp_to}\n')
            else:
                print(f'Не достаточно количества в месте отправки')
        else:
            print(f'Не достаточно места в месте доставки')

    print_all(shop, store)


def print_all(shop, store):
    """Печать статистики по складу и магазину"""
    print(f'В Магазине: ')
    if shop.get_unique_items_count() == 0:
        print('нет товаров')
    for key, value in shop.get_items().items():
        print(f'{key} - {value}')

    print(f'\nНа складе: ')
    if store.get_unique_items_count() == 0:
        print('нет товаров')
    for key, value in store.get_items().items():
        print(f'{key} - {value}')
