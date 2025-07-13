from textual.app import ComposeResult
from textual.containers import Center, HorizontalGroup, Container
from textual.widget import Widget
from textual.widgets import Static, Button, TextArea

class LoginWidget(Widget):
    def compose(self) -> ComposeResult:
        with Container():
            #with Container( ):
            with HorizontalGroup():
                yield TextArea("Password",tooltip="Enter your Password", classes="input-field")
            with Center():
                yield Button("Hello! 3", variant="default")
            