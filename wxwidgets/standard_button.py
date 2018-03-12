from wx import Button, EVT_BUTTON


class StandardButton(Button):
    def __init__(self, parent, text, callback, style=None):
        super().__init__(parent, label=text)
        self.Bind(EVT_BUTTON, callback)
