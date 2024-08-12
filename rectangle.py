from time import sleep
from pyautogui import position
from keyboard import is_pressed

from settings import get_settings


class Rectangle:
    def __init__(self, pair: tuple[tuple[int, int], tuple[int, int]] | None = None):
        if pair is None:
            pair: tuple[tuple[int, int], tuple[int, int]] = self.setup()
        self.x_min: int = pair[0][0]
        self.x_max: int = pair[1][0]
        self.y_min: int = pair[0][1]
        self.y_max: int = pair[1][1]

    @staticmethod
    def get_corner() -> tuple[int, int]:
        while True:
            sleep(0.05)  # Prevent Lag
            if is_pressed(get_settings('setup_key', 'str')):
                corner: tuple[int, int] = (int(position().x), int(position().y))
                break
        sleep(1)
        return corner

    @staticmethod
    def setup() -> tuple[tuple[int, int], tuple[int, int]]:
        print("Upper left Corner")
        corner1: tuple[int, int] = Rectangle.get_corner()
        print("Lower right Corner")
        corner2: tuple[int, int] = Rectangle.get_corner()
        pair: tuple[tuple[int, int], tuple[int, int]] = (corner1, corner2)
        return pair

    def __str__(self) -> str:
        string: str = ('( ('
                       + str(self.x_min)
                       + ', '
                       + str(self.y_min)
                       + '), ('
                       + str(self.x_max)
                       + ', '
                       + str(self.y_max)
                       + ') )')
        return string
