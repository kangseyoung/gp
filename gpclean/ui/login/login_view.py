from datetime import datetime
import os
try:
    from PySide6.QtWidgets import QWidget, QApplication
    from PySide6.QtCore import Signal, QFile
    from PySide6.QtUiTools import QUiLoader
    USING_QT = "PySide6"
except ImportError:
    from PySide2.QtWidgets import QWidget, QApplication
    from PySide2.QtCore import Signal, QFile
    from PySide2.QtUiTools import QUiLoader
    USING_QT = "PySide2"

print(f"✅ Loaded {USING_QT}")


class LoginView(QWidget):
    login_dictionary = Signal(dict)

    def __init__(self):
        super().__init__()
        print("✅ LoginView: __init__() 호출됨")
        self.setup_ui()

    def setup_ui(self):
        print("✅ LoginView: setup_ui() 시작")
        ui_file_path = os.path.join(os.path.dirname(__file__), "login.ui")  # 상대 경로 문제 해결
        print(f"📁 UI 파일 경로: {ui_file_path}")

        ui_file = QFile(ui_file_path)
        if not ui_file.exists():
            print("❌ UI 파일이 존재하지 않습니다!")
            return

        if not ui_file.open(QFile.ReadOnly):
            print("❌ UI 파일을 열 수 없습니다!")
            return

        loader = QUiLoader()
        self.ui = loader.load(ui_file)
        ui_file.close()

        if self.ui is None:
            print("❌ UI 로딩 실패")
            return

        self.ui.show()
        print("✅ UI 로딩 및 show() 완료")
        self.ui.signin.clicked.connect(self.signin_button)
        
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