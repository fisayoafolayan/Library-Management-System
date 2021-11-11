"""
Entry point of the app. It builds the GUI of the app
"""
from View.main_view import MainView


class AppView:
    def __init__(self):
        self.main = MainView()
        self.main.build_library()


if __name__ == "__main__":
    app = AppView()
