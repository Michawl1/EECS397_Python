import tkinter.ttk as ttk


class Data(object):
    def __init__(self, parent):
        self._parent = parent

        self._frame = ttk.Frame(self._parent, padding='15 15 10 10')
        self._parent.add(self._frame, text="Data")

        self._place_holder()

    def _place_holder(self):
        """
        Prints a giant label where the data is going to go
        """
        output = ttk.Label(self._frame)
        output.configure(text="DATA GOES HERE", font=("Helvetica", 40))
        output.grid(row=0, column=0, sticky='w', padx=2, pady=2)
