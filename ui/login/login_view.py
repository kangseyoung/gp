

import sys
sys.path.append("C:\\Users\\User\\Downloads\\_phoenix_\\lib\\asdasd\\")
sys.path.append("C:\\Users\\User\\OneDrive\\Desktop\\gp_clean\\")
import PySide6
from PySide6.QtWidgets import QWidget,QApplication,QLabel
from PySide6.QtCore import QObject, Signal
from PySide6.QtCore import Slot
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtGui import QPixmap
from datetime import datetime
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from login.login_controller import Receiver
 
"""
student_id
password
signinS
"""

class LoginView(QWidget):
    login_dictionary = Signal(dict)

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        ui_file_path="ui\\login\\login.ui"
        ui_file=QFile(ui_file_path)
        loader=QUiLoader()
        self.ui=loader.load(ui_file)#ui 불러온거다.
        self.ui.show()#ui띄우기.
        ui_file.close()
        self.ui.signin.clicked.connect(self.signin_button)

    def get_student_id(self):
        student_id = self.ui.student_id.text()
        return student_id
    
    def get_password(self):
        password = self.ui.password.text()
        return password
    
    def signin_button(self):
        student_id = self.get_student_id()
        password = self.get_password()
        date_time = datetime.now()
        formatted = date_time.isoformat()
        login_info_dict = {"student_id":student_id,
                                "password":password,
                                "date_time": formatted}
        self.login_dictionary.emit(login_info_dict)
        self.ui.close()
        

"""App=QApplication()
win=LoginView()

receiver = Receiver(LoginView)
win.login_dictionary.connect(receiver.return_info)

win.show()
sys.exit(App.exec())
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginView()
    receiver = Receiver(LoginView)
    window.login_dictionary.connect(receiver.return_info)
    window.show()
    sys.exit(app.exec())