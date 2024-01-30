import time

from selenium.webdriver.common.by import By
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    page = BasePage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    login_page = page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
    # login_page.should_be_login_page()


# Проверить, что есть ссылка, которая ведет на логин
def test_guest_should_see_login_link(browser):
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasePage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.open_basket_page()
    BasketPage.should_be_empty_basket(page)
    BasketPage.should_be_empty_basket_text(page)
