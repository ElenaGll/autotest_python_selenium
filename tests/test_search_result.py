from pages.search_result_page import SearchResultPage


def test_search_result(browser):
    url = 'https://ya.ru/search/?text=ozon&lr=62&search_source=yaru_desktop_common&search_domain=yaru'

    search_result_page = SearchResultPage(browser, url)
    search_result_page.open()
    search_result_page.should_be_necessary_link('ozon.ru', 5)
