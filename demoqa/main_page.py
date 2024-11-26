
class MainPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://demoqa.com/", timeout=100000)



