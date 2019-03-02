from utility.path_str import get_clean_path
from wx import ID_CANCEL, DirDialog

from wxwidgets._input_widget import InputWidget


class DirectoryInput(InputWidget):
    def __init__(self, parent, text, callback, file_type, text_open_file_title, text_open_file, initial="", reset=False):
        super().__init__(parent, text, callback, initial, reset)
        self._file_type = file_type

        self._text_open_file_title = text_open_file_title
        self._text_open_file = text_open_file

    def button_callback(self, event):
        with DirDialog(parent=self, message=self._text_open_file_title, defaultPath="") as dialog:
            if dialog.ShowModal() == ID_CANCEL:
                return  # the user changed their mind
            path = get_clean_path(dialog.Path)

        if self._reset:
            self._text_input.SetValue("")
        else:
            self._text_input.SetValue(path)
        self._callback(path=path)
