from textual.widgets import DirectoryTree, Footer, Header, Static, ListItem, ListView, Label, Button
from textual.app import App, ComposeResult
from textual.screen import Screen

from textual.containers import Container, VerticalScroll, Horizontal, Vertical

from commands.apps import cmd_apps_list
from ui.DomainsScreen import DomainsScreen


class AppsScreen(Screen):
    BINDINGS = [
        ("s", "ssh", "SSH"),
        ("d", "domains", "Domains"),
        ("e", "events", "Events"),
        ("q", "app.quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        yield AppsList()


class AppsList(Static):
    def on_mount(self) -> None:
        apps = cmd_apps_list()

        self.query_one("#list").mount_all([ListItem(Label(a)) for a in apps])

    def on_button_pressed(self, event):
        if event.button.id == 'domains':
            self.app.push_screen(DomainsScreen('test'))

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield ListView(id="list", classes='list col')
            with Vertical(classes='side'):
                yield Button('Stats', id='stats')
                yield Button('Configs', id='configs')
                yield Button('Storage', id='storage')
                yield Button('Deployments')
                yield Button('Logs')
                yield Button('Domains', id='domains')
                yield Button('Report')
                yield Button('Clone')
                yield Button('Rename')

        yield Footer()
