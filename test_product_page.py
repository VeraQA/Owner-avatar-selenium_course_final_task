from .pages.main_page import MainPage
from .pages.product_page import ProductPage
# import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    ProductPage.add_product(page)
    ProductPage.should_have_right_name(page)
    ProductPage.should_have_one_price_basket_and_price(page)
