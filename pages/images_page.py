from .base_page import BasePage
from .locators import ImagesPageLocators
from PIL import Image, ImageChops
import math, operator
from functools import reduce


class ImagesPage(BasePage):

    name_of_first_category = ''

    def open_first_category(self):
        self.name_of_first_category = self.get_text_of_element(*ImagesPageLocators.NAME_OF_FIRST_CATEGORY)
        self.press_button(*ImagesPageLocators.FIRST_CATEGORY)

    def check_first_category_is_opened(self):
        text_in_input_field = self.get_text_of_input_field(*ImagesPageLocators.TEXT_IN_INPUT_FIELD)

        assert self.name_of_first_category == text_in_input_field, \
            f'The text in input field is not equal the name of first category'

    def open_first_image(self):
        images = self.browser.find_elements(*ImagesPageLocators.FIRST_IMAGE)
        images[0].click()

    def compare_images(self):
        self.take_screenshot('screenshots/screen_one.png', *ImagesPageLocators.OPENED_IMAGE)
        self.press_button(*ImagesPageLocators.NEXT_BUTTON)
        self.take_screenshot('screenshots/screen_two.png', *ImagesPageLocators.OPENED_IMAGE)
        self.press_button(*ImagesPageLocators.PREVIOUS_BUTTON)
        self.take_screenshot('screenshots/screen_three.png', *ImagesPageLocators.OPENED_IMAGE)

        h1 = Image.open('screenshots/screen_one.png').histogram()
        h2 = Image.open('screenshots/screen_two.png').histogram()

        rms1 = math.sqrt(reduce(operator.add,
                                map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))

        assert rms1 > 0, f'The first image should be different from the second'

        h3 = Image.open('screenshots/screen_three.png').histogram()
        rms2 = math.sqrt(reduce(operator.add,
                                map(lambda a, b: (a - b) ** 2, h1, h3)) / len(h1))

        assert rms2 < 1, f'Images should be the same'

        print(rms1, rms2)
