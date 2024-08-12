import numpy as np
import pytesseract
from PIL.Image import Image
from PIL import Image
from matplotlib import pyplot as plt
from pyautogui import screenshot

from rectangle import Rectangle
from settings import get_settings

pytesseract.pytesseract.tesseract_cmd = get_settings('tesseract_cmd', 'str')


class Screenshot:
    def __init__(self, rectangle: Rectangle | None = None) -> None:
        self.array: np.array | None = None
        if rectangle is None:
            self.rectangle: Rectangle = Rectangle()
        else:
            self.rectangle: Rectangle = rectangle

    @staticmethod
    def crop_picture(picture: Image, rectangle: Rectangle) -> Image:
        cropped_screenshot: Image = picture.crop((rectangle.x_min,
                                                  rectangle.y_min,
                                                  rectangle.x_max,
                                                  rectangle.y_max))
        return cropped_screenshot

    def new_screenshot(self) -> None:
        picture: Image = Screenshot.crop_picture(screenshot(), self.rectangle)
        self.array = np.array(picture)

    def simplify(self) -> None:
        white_upper: np.array = np.array([255, 255, 255])
        white_lower: np.array = np.array([120, 120, 120])
        mask_upper: np.array = self.array >= white_lower
        mask_lower: np.array = self.array <= white_upper
        mask: np.array = np.all(mask_lower & mask_upper, axis=-1)
        self.array[mask] = np.array([255, 255, 255])  # White
        self.array[~mask] = np.array([0, 0, 0])  # Black

    def renew(self) -> None:
        self.new_screenshot()
        self.simplify()

    def text(self) -> str:
        picture: Image = Image.fromarray(self.array)
        text: str = pytesseract.image_to_string(picture)
        return text

    def full(self) -> str:
        self.renew()
        string: str = self.text()
        return string

    def show(self) -> None:
        plt.imshow(self.array)
        plt.axis('off')
        plt.savefig('New', dpi=1000)
        plt.show()
