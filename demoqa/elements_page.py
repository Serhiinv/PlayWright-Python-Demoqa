from playwright.sync_api import Page, expect

from checkbox_page import CheckBoxPage
from textbox_page import TextBoxPage


class ElementsPage:
    def __init__(self, page):
        self.page = page

    def verify_page_is_open(self):
        expect(self.page.get_by_text("Text Box")).to_be_visible()

    def open_text_box_page(self):
        self.page.get_by_text("Text Box").click()
        return TextBoxPage(self.page)

    def open_check_box_page(self):
        self.page.get_by_text("Check Box").click()
        return CheckBoxPage(self.page)
