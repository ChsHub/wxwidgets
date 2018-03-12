from wx import Panel, BoxSizer, HORIZONTAL, Button, StaticText, VERTICAL, EXPAND, ListCtrl, LC_REPORT, BORDER_SUNKEN
from wx.grid import Grid

from wxGUI.standard_button import StandardButton


class Table(ListCtrl):
    row_index = -1

    def __init__(self, parent, headers, size=(-1, 100)):
        super().__init__(parent, size=size, style=LC_REPORT | BORDER_SUNKEN)
        # sizer = Grid(self)#cols=len(headers))

        for i, text in enumerate(headers):
            # self.
            self.InsertColumn(i, text)
            # sizer.Add(header)
        # self.SetSizer(sizer)
        # self.SetBackgroundColour(color_blue)

    def add_line(self, data_list):
        self.row_index += 1
        self.InsertItem(self.row_index, data_list[0])
        for i, item in enumerate(data_list):
            self.SetItem(self.row_index, i, item)



    def update_cell(self, data, column):
        self.SetItem(self.row_index, column, data)


class Preview(Panel):
    _listbox = None

    def __init__(self, parent, headers, *buttons):
        super().__init__(parent)

        self._listbox = Table(self, headers=[str(x.value) for x in headers])  # , size=(600, 200))

        # CONTROL FRAMES
        button_frame = Panel(self)
        button_sizer = BoxSizer(HORIZONTAL)
        for callback, text in buttons:
            button_sizer.Add(StandardButton(button_frame, text=text, callback=callback))
        button_frame.SetSizer(button_sizer)
        # ALIGN
        sizer = BoxSizer(VERTICAL)
        sizer.Add(self._listbox, 1, EXPAND)
        sizer.Add(button_frame, 1, EXPAND)
        self.SetSizer(sizer)

    def update_view(self, data):
        for line in data:
            self._listbox.add_line(data)
