import pytest
from grade import get_grade

# Системные ошибки: данные
grade_exceptions = [
    (0, ValueError),
    (-24, ValueError),
    (-300, ValueError),
    (-101, ValueError)
]

# Базовые ошибки: тесты
class TestGrade:
    def test_get_grade_two(self):
        # Сохраняем вызов в переменную
        grade = get_grade(20)
        # Записываем, что  функция с данной переменной должна выводить 20,
        # ну а если False, то выведем текст с подробностями об ошибке
        assert grade == 2, "Аргумент должен не подходит для 2"

    def test_get_grade_tree(self):
        grade = get_grade(37)
        assert grade == 3, "Аргумент должен не подходит для 3"

    def test_get_grade_four(self):
        grade = get_grade(75)
        assert grade == 4, "Аргумент должен не подходит для 4"

    def test_get_grade_five(self):
        grade = get_grade(98)
        assert grade == 5, "Аргумент должен не подходит для 5"


# Системные ошибки: тесты
@pytest.mark.parametrize('points, exception', grade_exceptions)
def test_grade(points, exception):
    with pytest.raises(exception):
        # теперь просто вызываем нужную нам функцию
        get_grade(points)

