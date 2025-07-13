from configparser import ConfigParser
from typing import Any

class i18n:
    obj: ConfigParser;
    currentLanguage: str = "en";

    def __init__(self):
        obj = ConfigParser()
        self.obj = obj
        pass

    # I don't think we should preload every language file. 
    def loadLanguageText(self, FILE_TEXT: str):
        self.obj.read_string(FILE_TEXT)
        pass;
    
    def loadLanguageFile(self, filepath: str):
        
        self.obj.read(filepath)

    def setLanguage(self):
        pass;

    def getString(self, section: str, key: str, *args: Any, **kwargs: Any):
        return self.obj.get(section, key, *args, **kwargs)