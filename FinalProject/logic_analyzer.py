import serial.tools.list_ports
import serial
import tkinter as tk
import tkinter.ttk as ttk
import resources.constants

class LogicAnalyzerGui:
    def __init__(self):
        self._ser = serial.Serial()

        self._root = tk.Tk()
        self._root.title(resources.constants.APPLICATION_STRING)
        self._root.grid_rowconfigure(0, weight=1)
        self._root.grid_columnconfigure(0, weight=1)
        self._root.protocol("WM_DELETE_WINDOW",
                            lambda: self._exit())
        self._root.minsize(500, 500)
        self._root.resizable(2560, 1440)

    def _exit(self):
        self._root.destroy()

    def start(self):
        """
        Starts the GUI main event loop
        """
        self._root.mainloop()

if __name__ == '__main__':
    gui = LogicAnalyzerGui()
    gui.start()