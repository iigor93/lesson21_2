from classes.check_user_input import check_user_input


class Request:
    """Класс запрос пользователя
        Доставить 3 печеньки из склад в магазин
    """
    def __init__(self, user_request):
        self._data = check_user_input(user_request)
        self.amount = self._data.get('amount')
        self.product = self._data.get('product')
        self.from_ = self._data.get('from')
        self.to_ = self._data.get('to')

    def __repr__(self):
        return f'From - {self.from_}' \
               f'\nTo - {self.to_}' \
               f'\nProduct - {self.product}' \
               f'\nAmount - {self.amount}'

    def get_data(self):
        return {'amount': self.amount,
                'product': self.product,
                'from': self.from_,
                'to': self.to_
                }
