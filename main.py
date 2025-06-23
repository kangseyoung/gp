from PySide6.QtWidgets import QApplication
import sys
from ui.login.login_view import LoginView

if __name__ == "__main__":
    app = QApplication(sys.argv)       # ✅ 1. 무조건 제일 먼저 생성
    window = LoginView()               # ✅ 2. 그 다음에 UI 생성
    window.show()
    sys.exit(app.exec())               # ✅ 3. 이벤트 루프 실행
