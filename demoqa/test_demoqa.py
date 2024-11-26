from playwright.sync_api import Page, expect
from main_page import MainPage
import allure


@allure.title("Test Text Box Functionality")
def test_text_box(page: Page):
    main_page = MainPage(page)
    main_page.open()
    elements_page = main_page.open_elements()
    elements_page.verify_page_is_open()
    text_box_page = elements_page.open_text_box_page()
    text_box_page.verify_page_is_open()

    text_box_page.verify_submit_button_visible()
    text_box_page.verify_name_field_visible()
    text_box_page.verify_email_field_visible()

    text_box_page.file_name("Test Name")
    text_box_page.file_email("test@g.com")
    text_box_page.submit_form()

    text_box_page.verify_form_submitted("Test Name", "test@g.com")


@allure.title("Test Check Box Functionality")
def test_check_box(page: Page):
    main_page = MainPage(page)
    main_page.open()
    elements_page = main_page\
        .open_elements()
    elements_page\
        .verify_page_is_open()

    check_box_page = elements_page\
        .open_check_box_page()
    check_box_page\
        .verify_page_is_open()
    check_box_page\
        .verify_checkbox_work()

