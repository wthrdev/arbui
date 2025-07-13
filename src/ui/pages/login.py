from textual.app import ComposeResult
from textual.containers import CenterMiddle, HorizontalGroup, Container
from textual.widget import Widget
from textual.widgets import Static, Button, TextArea
from src.ui.components.login_dialog import LoginWidget

class LoginPage(Widget):
    
    DEFAULT_CSS = """
.debug {
    background: red;
}
"""
    def compose(self) -> ComposeResult:
        with CenterMiddle():
            yield LoginWidget()