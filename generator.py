class Generator:
    def __init__(self, size):
        """Кол-во генерируемых элементов """
        self.size = size

    def value(self):
        """Метод-генератор"""
        for num in range(0, self.size):
            yield num**2

