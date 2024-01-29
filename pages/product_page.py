from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product(self):
        self.click_button(*ProductPageLocators.BASKET_BUTTON)
        self.solve_quiz_and_get_code()

    def should_have_right_name(self):
        prod_name = self.get_value(*ProductPageLocators.PRODUCT_NAME)
        prod_name_mes = self.get_value(*ProductPageLocators.PRODUCT_NAME_MES)
        assert prod_name == prod_name_mes, f"The product name in the post does not match the product you added . {prod_name}  <> {prod_name_mes}"

    def should_have_one_price_basket_and_price(self):
        assert self.get_value(*ProductPageLocators.PRODUCT_PRICE) == self.get_value(
            *ProductPageLocators.PRODUCT_PRICE_MES), "The price of the cart does not match the price of the product."
