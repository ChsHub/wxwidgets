from wx import Panel, TextCtrl, Button, HORIZONTAL, BoxSizer, EVT_BUTTON, TOP, EVT_TEXT_ENTER, TE_PROCESS_ENTER

class InputWidget(Panel):
    _text_input = None
    _callback = None
    _reset = False

    def __init__(self, parent, text, callback, initial="", reset=False):
        super().__init__(parent)
        self._reset = reset
        self._callback = callback

        sizer = BoxSizer(HORIZONTAL)
        self._text_input = TextCtrl(self, size=(400, 20), style=TE_PROCESS_ENTER)
        self._text_input.SetValue(initial)
        self._text_input.Bind(EVT_TEXT_ENTER, self.button_callback)
        sizer.Add(self._text_input, 1, flag=TOP, border=1)

        button = Button(self, size=(200, 22), label=text)
        button.Bind(EVT_BUTTON, self.button_callback)

        sizer.Add(button)
        self.SetSizer(sizer)

    def button_callback(self, event):
        self._callback(self._text_input.GetValue())
        if self._reset:
            self._text_input.SetValue("")
