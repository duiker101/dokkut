from textual import events
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.screen import Screen
from textual.widgets import Footer, Header, Static, ListItem, ListView, Label

from commands.domains import cmd_domains_report, cmd_domains_remove
from ui.modals.ConfirmModal import ConfirmModal
from ui.modals.PromptModal import PromptModal


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
    }
    
    #global_container{
        dock: right;
        width: 50%;
    }
    """

    def __init__(self, app_name: str) -> None:
        self.app_name = app_name
        self.app.title = f'Dokkut - {app_name} Domains'
        self.domains = []
        self.global_domains = []
        super().__init__()

    def action_add_domain(self):
        def close(success: bool):
            if success:
                self.update_domains()

        self.app.push_screen(PromptModal(self.app_name), close)

    def action_remove_domain(self):
        domain = self.domains[self.query_one('#domains_list', ListView).index]

        def close(success: bool):
            if success:
                cmd_domains_remove(self.app_name, domain)
                self.update_domains()

        self.app.push_screen(ConfirmModal(f'Remove {domain} domain from {self.app_name}?'), close)

    def on_mount(self, event: events.Mount) -> None:
        self.query_one('#container').border_title = f'{self.app_name} - VHost Domains'
        # self.query_one('#global_container').border_title = f'Global Domains'
        self.update_domains()

    def update_domains(self):
        self.query_one('#domains_list', ListView).clear()
        # self.query_one('#global_domains_list', ListView).clear()
        domains = cmd_domains_report(self.app_name)
        self.domains = domains['vhost_domains']
        self.global_domains = domains['global_domains']

        self.query_one('#domains_list', ListView).mount_all([ListItem(Label(d)) for d in domains['vhost_domains']])
        # self.query_one('#global_domains_list', ListView).mount_all(
        #     [ListItem(Label(d)) for d in domains['global_domains']])

    def on_list_view_selected(self, event: events.Event) -> None:
        pass
        # if event.control.id == 'domains_list':
        #     self.query_one('#global_domains_list', ListView).index = None
        # if event.control.id == 'global_domains_list':
        #     self.query_one('#domains_list', ListView).index = None

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            with Static(id='container', classes='panel'):
                yield ListView(id='domains_list')
            # with Static(id='global_container', classes='panel'):
            #     yield ListView(id='global_domains_list')
        yield Footer()
