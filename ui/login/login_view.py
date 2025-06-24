from datetime import datetime
import sys
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import Signal
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


class LoginView(QWidget):
    login_dictionary = Signal(dict)

    def __init__(self):
        super().__init__()
        print("✅ LoginView: __init__() 호출됨")
        self.setup_ui()

    def setup_ui(self):
        print("✅ LoginView: setup_ui() 시작")
        ui_file_path = "ui\\login\\login.ui"
        ui_file = QFile(ui_file_path)
        loader = QUiLoader()

        self.ui = loader.load(ui_file)
        self.ui.show()
        ui_file.close()
        print("✅ LoginView: UI 로딩 완료")

        self.ui.signin.clicked.connect(self.signin_button)
        print("✅ LoginView: 로그인 버튼 연결 완료")

    def get_student_id(self):
        student_id = self.ui.student_id.text()
        print(f"📌 student_id 입력값: {student_id}")
        return student_id

    def get_password(self):
        password = self.ui.password.text()
        print(f"📌 password 입력값: {password}")
        return password

    def signin_button(self):
        print("🟡 signin_button() 클릭됨")
        student_id = self.get_student_id()
        password = self.get_password()
        today = datetime.now()
        date_str = today.strftime("%Y_%m_%d")

        login_info_dict = {
            "student_id": student_id,
            "password": password,
            "date_time": date_str
        }

        self.login_dictionary.emit(login_info_dict)
        print(f"📤 emit login_dictionary: {login_info_dict}")

        self.ui.close()
        print("✅ 로그인 시도 후 UI 닫기")