import tkinter
import tkinter.ttk as ttk
import resources.constants
import struct


class RequestData(object):
    def __init__(self,
                 parent,
                 row,
                 column,
                 ser):
        self._parent = parent
        self._row = row
        self._column = column
        self._serial = ser

        self._frame = ttk.LabelFrame(self._parent)
        self._frame.configure(text='Request Data')
        self._frame.grid(row = self._row,
                         column = self._column,
                         sticky='we',
                         padx=2,
                         pady=2,
                         ipadx=5,
                         ipady=5)
        self._button = tkinter.Button(self._frame, text='Poll Data', command=self._poll)
        self._button.grid(row=0, column=0, sticky='we', padx=2, pady=2)

    def _poll(self):
        """
        This will be responsible for telling the logic analyzer to start recording data
        """
        if self._serial.isOpen():
            # for now all we'll do is send a command, later there will be a response
            self._serial.write(struct.pack("<BBBBI",
                                           resources.constants.BYTE1,
                                           resources.constants.BYTE2,
                                           resources.constants.BYTE3,
                                           resources.constants.BYTE4,
                                           resources.constants.DATA_REQUEST))
