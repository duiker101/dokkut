from rich import print
from rich.console import Console
from rich.panel import Panel
# console = Console()
# Panel.fit("[bold yellow]Hi, I'm a Panel", border_style="red")
# # print("[italic red]Hello[/italic red] World!")
# console.rule("[bold red]Chapter 2")

from textual.reactive import var
from textual.widget import Widget, AwaitMount
from textual.widgets import DirectoryTree, Footer, Header, Static, ListItem, ListView, Label, Button
from textual.app import App, ComposeResult

from textual.containers import Container, VerticalScroll, Horizontal, Vertical

from command import cmd
from commands.apps import cmd_apps_list, cmd_app_report
from ui.AppsScreen import AppsScreen, AppsList


class Dokkut(App):
    CSS_PATH = "main.tcss"

    def on_mount(self):
        self.push_screen(AppsScreen())


if __name__ == "__main__":
    Dokkut().run()
