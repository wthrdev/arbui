from textual.app import ComposeResult
from textual.containers import CenterMiddle, HorizontalGroup, Container
from textual.widget import Widget
from textual.widgets import Static, Button

class WelcomePage(Widget):
    def compose(self) -> ComposeResult:
        with CenterMiddle():
            #with Container( ):
            with HorizontalGroup(classes="centered-container"):
                yield Button("Hello! 1", variant="primary")
                yield Button("Hello! 2", variant="success")
            yield Button("Hello! 3", variant="success")
            