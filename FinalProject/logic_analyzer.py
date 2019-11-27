import serial.tools.list_ports
import serial
import tkinter as tk
import tkinter.ttk as ttk
import resources.constants
import frames.connect
import frames.data

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

        self._control_frame()
        self._display_frame()

    def _exit(self):
        self._root.destroy()

    def _control_frame(self):
        control_frame = ttk.Frame(self._root)
        control_frame.pack(expand=False,
                           fill='both',
                           side='left',
                           anchor='nw',
                           padx=2,
                           pady=2)

        self._connect = frames.connect.Connect(control_frame, 0, 0, self._ser)

    def _display_frame(self):
        display_frame = ttk.Frame(self._root)
        display_frame.pack(expand=True,
                           fill='both',
                           side='right',
                           padx=2,
                           pady=2)

        display_tab_control = ttk.Notebook(display_frame)
        display_tab_control.pack(expand=1, fill='both')

        self._data = frames.data.Data(display_tab_control)

    def start(self):
        """
        Starts the GUI main event loop
        """
        self._root.mainloop()

if __name__ == '__main__':
    gui = LogicAnalyzerGui()
    gui.start()