from textual import on
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import ModalScreen
from textual.widgets import Label, Button


class ConfirmModal(ModalScreen[bool]):
    CSS = """
    Horizontal {
        margin-top: 2;
        height: auto;
        background: red;
    }
    
    Button{
        border: none;
        min-width: 1;
        height: 1;
    }
    
    .cancel{
        dock: right;
    }
    """

    def __init__(self, label):
        super().__init__()
        self.label = label

    def compose(self) -> ComposeResult:
        with Vertical(id="dialog"):
            yield Label(self.label)

            with Horizontal():
                yield Button("Confirm", variant="success", id="confirm")
                yield Button("Cancel", variant="default", id="cancel", classes="cancel")

    @on(Button.Pressed, '#confirm')
    def on_confirm(self):
        self.dismiss(True)

    @on(Button.Pressed, '#cancel')
    def on_cancel(self):
        self.dismiss(False)
