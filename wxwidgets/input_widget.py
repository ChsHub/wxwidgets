from wx import Panel, TextCtrl, Button, HORIZONTAL, BoxSizer, EVT_BUTTON


class InputWidget(Panel):
    _text_input = None
    _callback = None
    _reset = False

    def __init__(self, parent, text, callback, initial="", reset=False):
        super().__init__(parent)
        self._reset = reset
        self._callback = callback

        sizer = BoxSizer(HORIZONTAL)
        self._text_input = TextCtrl(self, size=(400, 20))
        self._text_input.SetValue(initial)
        sizer.Add(self._text_input)

        button = Button(self, -1, size=(200, 22), label=text)
        button.Bind(EVT_BUTTON, self.button_callback)
        sizer.Add(button)
        self.SetSizer(sizer)

    def button_callback(self, event):
        self._callback(self._text_input.GetValue())
        if self._reset:
            self._text_input.SetValue("")
