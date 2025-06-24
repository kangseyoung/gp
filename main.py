from PySide6.QtWidgets import QApplication
import sys
from ui.login.login_view import LoginView
from ui.login.login_controller import Receiver
from ui.main.model import SubmissionDataModel


def launch_login_ui():
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    login_window = LoginView()
    receiver = Receiver(login_window)
    login_window.login_dictionary.connect(receiver.return_info)

    main_model = SubmissionDataModel()
    login_window.login_dictionary.connect(main_model.get_dictionary)

    login_window.show()
    app.exec()

if __name__ == "__main__":
    launch_login_ui()