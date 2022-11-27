import pytest
from player import Player

# Системные ошибки: данные
player_exceptions = [
    (3, TypeError)
]

class TestPlayer:
    # Базовые ошибки: тесты
    def test_points_null(self):
        number = Player('name')
        assert number.add_points(0) == 0, 'Число равно нулю'

    def test_type_error(self):
        with pytest.raises(TypeError):
            name = Player(player_exceptions)