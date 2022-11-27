class Player:

    def __init__(self, name):
        self.name = name
        self.points = 0

        if type(name) != str:
            raise TypeError("Имя должно быть строковым значением")

    def change_name(self, new_name):
        """заменяет имя"""
        self.name = new_name

    def add_points(self, number):
        """добавляет баллы"""
        if number != 0:
            self.points += number
        else:
            return 'Число равно нулю'

    def get_points(self):
        """возвращает количество баллов"""
        return self.points
