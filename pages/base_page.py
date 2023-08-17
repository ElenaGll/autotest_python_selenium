from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage:

    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, *element):
        assert self.browser.find_element(*element), \
            f'The element is not presented'

    def input(self, text, *element):
        input_field = self.browser.find_element(*element)
        input_field.send_keys(text)

    def press_button(self, *element):
        button = self.browser.find_element(*element)
        button.click()

    def get_links_list_from_search_result(self, number, *element):
        links = self.browser.find_elements(*element)
        list_of_links = []
        for i in links[:number]:
            list_of_links.append(i.text)
        return list_of_links

    def switch_to_new_window(self):
        WebDriverWait(self.browser, 10).until(EC.number_of_windows_to_be(2))
        self.browser.switch_to.window(self.browser.window_handles[1])

    def check_current_url(self, link):
        assert self.browser.current_url == link, \
            f'The link is not equal the current url'

    def get_text_of_element(self, *element):
        element = self.browser.find_element(*element)
        return element.text

    def get_text_of_input_field(self, *input_field):
        input_field = self.browser.find_element(*input_field)
        return input_field.get_attribute('value')

    def take_screenshot(self, screen_name, *element):
        image = self.browser.find_element(*element)
        time.sleep(1)
        image.screenshot(screen_name)


