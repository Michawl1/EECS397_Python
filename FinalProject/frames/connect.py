import serial
import serial.tools.list_ports
import tkinter
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk
import resources.constants
import struct


class Connect(object):
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
        self._frame.configure(text='Connect')
        self._frame.grid(row=self._row,
                         column=self._column,
                         sticky='we',
                         padx=2,
                         pady=2,
                         ipadx=5,
                         ipady=5)
        self._button = tkinter.Button(self._frame, text="Connect", command=self._connect)
        self._button.grid(row=0, column=0, sticky='we', padx=2, pady=2)

        self._baudrate_control()
        self._com_port_selector()

        self._update()

    def _update(self):
        if self._serial.isOpen():
            self.disable()
        else:
            self.enable()

    def _connect(self):
        """
        This sends the connect message to the logic analyzer
        """
        self._open_com_port()

        # for now all we'll do is send a command, later there will be a response
        self._serial.write(struct.pack("<BBBB",
                                       resources.constants.BYTE1,
                                       resources.constants.BYTE2,
                                       resources.constants.BYTE3,
                                       resources.constants.BYTE4)
                           )

    def _open_com_port(self):
        """
        Opens the com port from the selected port/baudrate
        """
        com_port = self._com_port_var.get()
        baudrate = self._baudrate_var.get()

        self._serial.port = com_port
        self._serial.baudrate = baudrate
        self._serial.timeout = resources.constants.COM_PORT_TIMEOUT

        try:
            self._serial.open()
        except Exception:
            text = "Could not open COM Port {}".format(com_port)
            messagebox.showinfo(resources.constants.APPLICATION_STRING,
                                text,
                                icon='warning')

    def _baudrate_control(self):
        """
        Sets up the drop down menu for the baudrates
        """
        baudrate_list = self._serial.BAUDRATES

        self._baudrate_var = tkinter.StringVar(self._frame)
        self._baudrate_var.set(baudrate_list[-1])

        baudrate_label = ttk.Label(self._frame)
        baudrate_label.configure(text="Baudrate: ")
        baudrate_label.grid(row=3, column=0, sticky='we', padx=2, pady=2)

        self._baudrate_combobox = ttk.Combobox(self._frame)
        self._baudrate_combobox.configure(textvariable=self._baudrate_var)
        self._baudrate_combobox.configure(values=baudrate_list)
        self._baudrate_combobox.grid(row=3, column=1, sticky='we',
                                     padx=2, pady=2)

    def _com_port_selector(self):
        """
        Sets up the drop down menu for the available com ports
        """
        com_ports = []
        com_port_list = serial.tools.list_ports.comports()
        for port in com_port_list:
            com_ports.append(port[0])

        self._com_port_var = tkinter.StringVar(self._frame)
        self._com_port_var.set(com_ports[0])

        com_port_label = ttk.Label(self._frame)
        com_port_label.configure(text="COM Port: ")
        com_port_label.grid(row=1, column=0, sticky='we', padx=2, pady=2)

        self._com_port_combobox = ttk.Combobox(self._frame)
        self._com_port_combobox.configure(textvariable=self._com_port_var)
        self._com_port_combobox.configure(values=com_ports)
        self._com_port_combobox.grid(row=1, column=1, sticky='we',
                                     padx=2, pady=2)

    def disable(self):
        """
        Disables the connect button
        """
        self._button.configure(text='Disconnect')
        self._com_port_combobox.configure(state=tkinter.DISABLED)
        self._baudrate_combobox.configure(state=tkinter.DISABLED)

    def enable(self):
        """
        Enables the connect button
        """
        self._button.configure(text="Connect")
        self._com_port_combobox.configure(state=tkinter.NORMAL)
        self._baudrate_combobox.configure(state=tkinter.NORMAL)
