from utility.path_str import get_clean_path
from wx import FileDialog, FD_OPEN, \
    FD_FILE_MUST_EXIST, FD_MULTIPLE, ID_CANCEL


from wxwidgets.input_widget import InputWidget


class FileInput(InputWidget):
    def __init__(self, parent, text, callback, file_type, text_open_file_title, text_open_file, initial="", reset=False):
        super().__init__(parent, text, callback, initial, reset)
        self._file_type = file_type

        self._text_open_file_title = text_open_file_title
        self._text_open_file = text_open_file

    def button_callback(self, event):
        with FileDialog(self, self._text_open_file_title, "", "",
                        wildcard=self._text_open_file + '(' + self._file_type + ')|' + self._file_type,
                        style=FD_OPEN | FD_FILE_MUST_EXIST | FD_MULTIPLE) as dialog:
            if dialog.ShowModal() == ID_CANCEL:
                return  # the user changed their mind
            path = get_clean_path(dialog.Directory)
            files = dialog.Filenames

        if self._reset:
            self._text_input.SetValue("")
        else:
            self._text_input.SetValue(path)
        self._callback(path=path, files=files)
