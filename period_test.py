import pytest
from period import get_period

# Системные ошибки: данные
period_exceptions = [
    (-3, ValueError),
    (25, ValueError)
]

# Базовые ошибки: тесты
class TestPeriod:
    def test_get_period_seven(self):
        hour = get_period(7)
        assert hour == "ночь", "Аргумент не равен семи"

    def test_get_period_ten(self):
        hour = get_period(10)
        assert hour == "утро", "Аргумент не равен <= 12"

    def test_get_period_twenty_tree(self):
        hour = get_period(23)
        assert hour == "вечер", "Аргумент не попал ни в одну ветку цикла"

    def test_get_period_four(self):
        hour = get_period(4)
        assert hour == "ночь", "Аргумент не <= 7"

    def test_get_period_seventeen(self):
        hour = get_period(17)
        assert hour == "день", "Аргумент не <= 18"

    def test_get_period_nineteen(self):
        hour = get_period(19)
        assert hour == "вечер", "Аргумент не попал ни в одну ветку цикла"


# Системные ошибки: тесты
@pytest.mark.parametrize('hour, exception', period_exceptions)
def test_value_error(hour, exception):
    with pytest.raises(exception):
        get_period(hour)