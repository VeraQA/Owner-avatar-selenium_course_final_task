from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import pytest
import time
# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail) ,
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

@pytest.mark.parametrize('link',["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"])

def test_guest_can_add_product_to_basket(browser,link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    ProductPage.add_product(page)
    ProductPage.should_have_right_name(page)
    ProductPage.should_have_one_price_basket_and_price(page)
@pytest.mark.parametrize('link',["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"])
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser,link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    ProductPage.add_product(page)
    ProductPage.should_not_be_success_message(page)

@pytest.mark.parametrize('link',["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"])

def test_guest_cant_see_success_message(browser,link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    ProductPage.should_not_be_success_message(page)
@pytest.mark.parametrize('link',["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"])
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser,link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    ProductPage.add_product(page)
    ProductPage.should_dissappeare(page)
