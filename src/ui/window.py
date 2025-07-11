from textual.app import App, ComposeResult
from textual.widgets import Footer, Header
from pages.welcome import WelcomePage


    
class StopwatchApp(App): # type: ignore
    """A Textual app to manage stopwatches."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    # def __init__(self):
        # self.super.__init__()
    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield WelcomePage()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == "__main__":
    app = StopwatchApp()
    app.run()