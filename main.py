from PySide6.QtWidgets import QApplication
import sys
from ui.login.login_view import LoginView
from ui.login.login_controller import Receiver
from ui.main.model import SubmissionDataModel


if __name__ == "__main__":
    app = QApplication(sys.argv)

    login_window = LoginView()
    receiver = Receiver(login_window)  # ← 여기서 생성하고
    login_window.login_dictionary.connect(receiver.return_info)
    main_model = SubmissionDataModel()
    login_window.login_dictionary.connect(main_model.get_dictionary)

    login_window.show()
    sys.exit(app.exec())
