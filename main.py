from textual.app import App

from ui.screens.AppsScreen import AppsScreen


class Dokkut(App):
    CSS_PATH = "main.tcss"

    def on_mount(self):
        self.push_screen(AppsScreen())


if __name__ == "__main__":
    Dokkut().run()
