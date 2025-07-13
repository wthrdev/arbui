import subprocess
import time
import threading
from typing import Callable

class console_handler:
    """A console handler for managing all commands needs
    """    
    _execInit: float;
    _execEnd: float;

    _lastprc_: str = "";
    _stdout_stacked_: str = "";
    _stderr_stacked_: str = "";

    _procObj_: subprocess.Popen[str] | None = None;
    
    def _thread_callback_end_(self, 
            process: subprocess.Popen[str], 
            cmdLine: list[str], 
            callback: Callable[[subprocess.Popen[str], list[str]], None]
        ) -> None:

        out, err = process.communicate();
        
        self._stdout_stacked_ += out
        self._stderr_stacked_ += err

        callback(process, cmdLine)
        return

    def exec(self,
            cmdline: list[str],
            callback: Callable[[str], None]
        ):


        if (self._procObj_ is not None):
            if (self.isFinished() == False):
                return "", "";

        self._execInit = time.time()
        proc = subprocess.Popen(
            cmdline,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True,
        )
        
        threading.Thread(target=self._thread_callback_end_, args=(proc, cmdline, callback))
        # Supposes that app execution is instant
        # out, err = proc.communicate();


        self._procObj_ = proc

        return proc

    def isFinished(self) -> bool:
        if (self._procObj_ is None):
            return True;
        return (self._procObj_.poll() is not None);

    def halt(self) -> None:
        if (self._procObj_ is not None):
            self._procObj_.kill();


    def getAccOutput(self, isErr: bool):
        if (isErr):
           return self._stderr_stacked_
        return self._stdout_stacked_