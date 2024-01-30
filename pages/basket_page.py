from .base_page import BasePage
from .locators import BasketPageLoators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLoators.BASKET_PRICE_NOTIFICATION), \
            "Basket is not empty, but it should be"

    def should_be_empty_basket_text(self):
        a=self.get_value(*BasketPageLoators.BASKET_EMPTY_TEXT)
        print(a)
        assert  self.is_element_present(*BasketPageLoators.BASKET_EMPTY_TEXT) , \
            "Text about empty basket is not present, but it should be "