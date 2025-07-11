from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.widget import Widget
from textual.widgets import Button

class WelcomePage(Widget):
    def __init__(self):

        super().__init__()

    def compose(self) -> ComposeResult:
        with VerticalScroll():
            for i in range(5000):
                yield Button(f"Hello! {i}", "primary")
        # return super().compose()
