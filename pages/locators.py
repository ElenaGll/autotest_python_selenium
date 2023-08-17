from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, 'div.search3__input-wrapper input.search3__input')
    SUGGEST = (By.CSS_SELECTOR, 'div.mini-suggest__popup ul.mini-suggest__popup-content')
    BUTTON_OF_SEARCH_INPUT = (By.CSS_SELECTOR, 'div.search3__inner button.search3__button')
    SEARCH_RESULT = (By.ID, 'search-result')
    SUGGEST_MORE_ICONS = (By.CSS_SELECTOR, 'div.services-suggest__icons-more')
    OPEN_IMAGES = (By.XPATH, '//a[@aria-label="Картинки"]')


class SearchResultPageLocators:
    LINKS_FROM_SEARCH_RESULT = (By.CSS_SELECTOR, 'div.Path.Organic-Path > a > b')


class ImagesPageLocators:
    FIRST_CATEGORY = (By.CSS_SELECTOR, 'div.PopularRequestList div.PopularRequestList-Item_pos_0')
    NAME_OF_FIRST_CATEGORY = (By.CSS_SELECTOR, 'div.PopularRequestList div.PopularRequestList-Item_pos_0 div.PopularRequestList-SearchText')
    TEXT_IN_INPUT_FIELD = (By.CSS_SELECTOR, 'span.input__box input.input__control.mini-suggest__input')
    FIRST_IMAGE = (By.CSS_SELECTOR, 'img.serp-item__thumb')
    OPENED_IMAGE = (By.CSS_SELECTOR, 'div.MMImageContainer')
    NEXT_BUTTON = (By.CSS_SELECTOR, 'div.CircleButton_type_next')
    PREVIOUS_BUTTON = (By.CSS_SELECTOR, 'div.CircleButton_type_prev')
