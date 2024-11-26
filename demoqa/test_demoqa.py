from playwright.sync_api import Page, expect
from main_page import MainPage
import allure


@allure.title("Test Text Box Functionality")
def test_text_box(page: Page):
    main_page = MainPage(page)
    main_page.open()
