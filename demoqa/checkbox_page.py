import re

from playwright.sync_api import Page, expect


class CheckBoxPage:
    def __init__(self, page):
        self.page = page

    def verify_page_is_open(self):
        expect(self.page.get_by_role("heading", name="Check Box")).to_be_visible()

    def verify_checkbox_work(self):
        self.page.get_by_label("Toggle").first.click()

        expect(self.page.locator("label").filter(has_text="Home").get_by_role("img").first).not_to_be_checked()
        self.page.locator("label").filter(has_text="Home").get_by_role("img").first.click()
        expect(self.page.locator("label").filter(has_text="Home").get_by_role("img").first).to_be_checked()

        self.page.locator("li").filter(has_text=re.compile(r"^Downloads$")).get_by_label("Toggle").click()
        expect(self.page.locator("label").filter(has_text="Excel File.doc").locator("path").first).to_be_checked()

        self.page.locator("label").filter(has_text="Word File.doc").get_by_role("img").first.click()
        expect(self.page.locator("label").filter(has_text="Word File.doc").get_by_role("img").first)\
            .not_to_be_checked()
        expect(self.page.locator("label").filter(has_text="Home").get_by_role("img").first)\
            .to_have_class("rct-icon rct-icon-half-check")
        expect(self.page.locator("label").filter(has_text="Downloads").get_by_role("img").first)\
            .to_have_class("rct-icon rct-icon-half-check")
