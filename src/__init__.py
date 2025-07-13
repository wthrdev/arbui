from core.translations import i18n
# from core.resticProfile import ResticProfile 
from ui.window import ThisApp
langs = i18n()
langs.loadLanguageFile("/lang/pt-br.ini")

def main():
    # myUser = ResticProfile()
    # myUser.login("")
    pass;
    ui = ThisApp()
    ui.run()


if __name__ == "__main__":
    main()