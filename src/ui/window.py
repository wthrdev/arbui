from textual.app import App, ComposeResult
from textual.widgets import Footer, Header
from textual.containers import CenterMiddle
from ui.pages.login import LoginPage


    
class ThisApp(App): # type: ignore
    CSS_PATH = "styles.css"
    def compose(self) -> ComposeResult:
        yield Header()
        with CenterMiddle():
            yield LoginPage(classes="centered-container")
        yield Footer()


    #------------ Theme Handling ------------#
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == "__main__":
    app = ThisApp()
    app.run()