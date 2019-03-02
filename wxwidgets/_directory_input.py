from utility.path_str import get_clean_path
from wx import ID_CANCEL, DirDialog

from wxwidgets._input_widget import InputWidget


class DirectoryInput(InputWidget):
    """
    Simple widget for opening a directory
    """
    def __init__(self, parent, callback, text_button, text_title, initial="", reset=False):
        """
        Builds the widget
        :param parent: Parent wx element
        :param callback: Function, that receives the directory
        :param text_button: Text is displayed on the "open-button"
        :param text_title: Text is displayed in the window title
        :param initial: Initial path
        :param reset: Don't show last opened directory
        """
        super().__init__(parent, text_button, callback, initial, reset)

        self._text_title = text_title

    def button_callback(self, event):
        """
        Receive selection event after directory is selected
        :param event: Event contains directory path
        :return: None
        """
        with DirDialog(parent=self, message=self._text_title, defaultPath="") as dialog:
            if dialog.ShowModal() == ID_CANCEL:
                return  # The user changed their mind
            path = get_clean_path(dialog.Path)

        # Display path
        if self._reset:
            self._text_input.SetValue("")
        else:
            self._text_input.SetValue(path)
        self._callback(path)
