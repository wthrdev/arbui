from pathlib import Path
from dataclasses import dataclass

@dataclass
class ResticProfile:
    repositoryPath: str;
    unsafePwd: str;

    backupPath: list[str];

    def login(self, path: Path, pwd: str):
        pass;
    
    def validate(self):
        pass;
    
    def logoff(self):
        pass;

    def restoreByIndex(self, index: int, overwrite: bool, basepath: str):
        pass;

    def backupByIndex(self, index: int):
        pass;