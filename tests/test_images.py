from pages.main_page import MainPage
from pages.locators import MainPageLocators
from pages.images_page import ImagesPage
import time


def test_images_page(browser):
    url = 'https://ya.ru/'

    page = MainPage(browser, url)
    page.open()
    page.open_necessary_services(*MainPageLocators.OPEN_IMAGES)
    page.switch_to_new_window()

    images_page = ImagesPage(browser, browser.current_url)
    images_page.check_current_url('https://ya.ru/images/')

    images_page.open_first_category()
    images_page.check_first_category_is_opened()

    images_page.open_first_image()
    images_page.compare_images()

    time.sleep(2)
