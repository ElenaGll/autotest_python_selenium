from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    def should_be_search_input(self):
        self.is_element_present(*MainPageLocators.SEARCH_INPUT)

    def write_text_in_search_input(self, text):
        self.input(text, *MainPageLocators.SEARCH_INPUT)

    def should_be_suggest(self):
        self.is_element_present(*MainPageLocators.SUGGEST)

    def press_button_of_search_input(self):
        self.press_button(*MainPageLocators.BUTTON_OF_SEARCH_INPUT)

    def should_be_search_result(self):
        self.is_element_present(*MainPageLocators.SEARCH_RESULT)

    def open_necessary_services(self, *service):
        self.press_button(*MainPageLocators.SEARCH_INPUT)
        self.press_button(*MainPageLocators.SUGGEST_MORE_ICONS)
        self.press_button(*service)
