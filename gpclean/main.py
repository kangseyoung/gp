try:
    from PySide6.QtWidgets import QApplication
    USING_QT = "PySide6"
    print("6됨")
except ImportError:
    from PySide2.QtWidgets import QApplication
    USING_QT = "PySide2"
    print("2됨")

print(f"✅ Loaded {USING_QT}")

import sys
from gpclean.ui.login.login_view import LoginView
from gpclean.ui.login.login_controller import Receiver
from gpclean.ui.main.model import SubmissionDataModel

print("hello")
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
    try:
        app.exec()
    except AttributeError:
        app.exec_()

if __name__ == "__main__":
    launch_login_ui()