from pages.main_page import MainPage


def test_search(browser):
    url = 'https://ya.ru/'

    page = MainPage(browser, url)
    page.open()

    page.should_be_search_input()
    page.write_text_in_search_input('ozon')
    page.should_be_suggest()
    page.press_button_of_search_input()
    page.should_be_search_result()
