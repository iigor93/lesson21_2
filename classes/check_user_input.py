def check_user_input(user_request):
    """Проверка ввода пользователя
        что бы строка соответствовала нужному формату
    """

    temp = user_request.strip().split(' ')
    temp_from = ('из', 'со', 'с')
    temp_to = ('в', 'на')

    if str(temp[0].lower()) != 'доставить' \
            or str(temp[3].lower()) not in temp_from \
            or str(temp[5].lower()) not in temp_to:
        raise Exception("Не верный формат запроса")

    if len(temp) != 7:
        raise Exception("Кол-во слов не равно 7")

    # создание переменных amount, product
    if str(temp[1]).isdigit():
        amount = int(temp[1])
        product = temp[2].lower()
    elif str(temp[2]).isdigit():
        amount = int(temp[2])
        product = temp[1].lower()
    else:
        raise Exception("Не определено количество товара")

    temp_store = ('склада', 'склад')
    temp_shop = ('магазина', 'магазин')

    if temp[4].lower() in temp_store:
        from_ = 'store'
    elif temp[4].lower() in temp_shop:
        from_ = 'shop'
    else:
        raise Exception("Не верный пункт отправления")

    if temp[6].lower() in temp_store:
        to_ = 'store'
    elif temp[6].lower() in temp_shop:
        to_ = 'shop'
    else:
        raise Exception("Не верный пункт назначения")

    if from_ == to_:
        raise Exception("Пункт назначения совпадает с пунктом отправления")

    return {'amount': amount, 'product': product, 'from': from_, 'to': to_}
