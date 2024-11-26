from elements_page import ElementsPage


class MainPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://demoqa.com/", timeout=100000)

    def open_elements(self):
        self.page.get_by_role("heading", name="Elements").click()
        return ElementsPage(self.page)
