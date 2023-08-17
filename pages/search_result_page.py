from .base_page import BasePage
from .locators import SearchResultPageLocators


class SearchResultPage(BasePage):

    def should_be_necessary_link(self, link, number):
        result = self.get_links_list_from_search_result(number, *SearchResultPageLocators.LINKS_FROM_SEARCH_RESULT)
        assert link in result, f'The necessary link is not in search result'
