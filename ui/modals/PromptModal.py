from textual import on
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import ModalScreen
from textual.widgets import Label, Button, Input

from commands.domains import cmd_domains_add


class PromptModal(ModalScreen[bool]):
    CSS = """
    Horizontal {
        width: auto;
        height: auto;
    }
    """

    def __init__(self, app_name):
        super().__init__()
        self.app_name = app_name

    def compose(self) -> ComposeResult:
        with Vertical(id="dialog"):
            yield Label("Are you sure you want to quit?", id="question")
            yield Input(placeholder='Domain', id='domain')

            with Horizontal():
                yield Button("Add", variant="success", id="add")
                yield Button("Cancel", variant="default", id="cancel")

    @on(Button.Pressed, '#add')
    def on_add(self):
        value = self.query_one('#domain', Input).value
        cmd_domains_add(self.app_name, value)
        self.dismiss(True)

    @on(Button.Pressed, '#cancel')
    def on_cancel(self):
        self.dismiss(False)
