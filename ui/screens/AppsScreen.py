from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Footer, Header, Static, ListItem, ListView, Label, Button

from commands.apps import cmd_apps_list
from ui.screens.DomainsScreen import DomainsScreen


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
                yield Button('Stats', classes='btn-sm', id='stats')
                yield Button('Configs', classes='btn-sm', id='configs')
                yield Button('Storage', classes='btn-sm', id='storage')
                # yield Button('Deployments')
                # yield Button('Logs')
                yield Button('Domains', classes='btn-sm', id='domains')
                # yield Button('Report')
                # yield Button('Clone')
                # yield Button('Rename')

        yield Footer()
