from textual import events
from textual.message import Message
from textual.widgets import DirectoryTree, Footer, Header, Static, ListItem, ListView, Label, Button
from textual.app import App, ComposeResult
from textual.screen import Screen

from textual.containers import Container, VerticalScroll, Horizontal, Vertical

from commands.domains import cmd_domains_report


class DomainsScreen(Screen):
    BINDINGS = [
        ("escape", "app.pop_screen", "Back"),
        ("a", "add_domain", "Add"),
        ("r", "remove_domain", "Remove"),
        ("e", "edit_domain", "Edit"),
        ("c", "clear_domain", "Clear"),
    ]

    CSS = """
    #container{
        dock: left;
        width: 50%;
    }
    
    #global_container{
        dock: right;
        width: 50%;
    }
    """

    def __init__(self, app_name: str) -> None:
        self.app_name = app_name
        self.app.title = f'Dokkut - {app_name} Domains'
        super().__init__()

    def on_mount(self, event: events.Mount) -> None:
        domains = cmd_domains_report(self.app_name)
        self.query_one('#container').border_title = f'{self.app_name} - VHost Domains'
        self.query_one('#global_container').border_title = f'Global Domains'
        self.query_one('#domains_list', ListView).mount_all([ListItem(Label(d)) for d in domains['vhost_domains']])
        self.query_one('#global_domains_list', ListView).mount_all([ListItem(Label(d)) for d in domains['global_domains']])

    def on_list_view_selected(self, event: events.Event) -> None:
        if event.control.id == 'domains_list':
            self.query_one('#global_domains_list', ListView).index = None
        if event.control.id == 'global_domains_list':
            self.query_one('#domains_list', ListView).index = None

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            with Static(id='container', classes='panel'):
                yield ListView(id='domains_list')
            with Static(id='global_container', classes='panel'):
                yield ListView(id='global_domains_list')
        yield Footer()
