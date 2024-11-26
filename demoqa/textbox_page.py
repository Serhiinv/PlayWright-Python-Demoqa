from playwright.sync_api import Page, expect


class TextBoxPage:
    def __init__(self, page):
        self.page = page

    def verify_page_is_open(self):
        expect(self.page.get_by_role("heading", name="Text Box")).to_be_visible()

    def verify_submit_button_visible(self):
        expect(self.page.get_by_role("button", name="Submit")).to_be_visible()

    def verify_name_field_visible(self):
        expect(self.page.get_by_text("Full Name")).to_be_visible()

    def verify_email_field_visible(self):
        expect(self.page.get_by_text("Email")).to_be_visible()

    def file_name(self, full_name):
        self.page.get_by_placeholder("Full Name").click()
        self.page.get_by_placeholder("Full Name").fill(full_name)  # "TestName"
        self.page.get_by_placeholder("Full Name").press("Enter")
        self.page.screenshot(path="../screenshots/name_filed.png")

    def file_email(self, email):
        self.page.get_by_placeholder("name@example.com").click()
        self.page.get_by_placeholder("name@example.com").fill(email)  # "test@g.com"
        self.page.get_by_placeholder("name@example.com").press("Enter")
        self.page.screenshot(path="../screenshots/email_filed.png")

    def submit_form(self):
        self.page.get_by_role("button", name="Submit").click()

    def verify_form_submitted(self, full_name, email):
        expect(self.page.get_by_text("Name:" + full_name)).to_be_visible()
        expect(self.page.get_by_text("Email:" + email)).to_be_visible()
        self.page.screenshot(path="../screenshots/submit_verified.png")
