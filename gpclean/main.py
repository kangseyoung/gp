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

def launch_login_ui():
    print("🚀 launch_login_ui() 진입")

    app = QApplication.instance()
    if not app:
        print("🆕 QApplication 인스턴스 새로 생성")
        app = QApplication(sys.argv)
    else:
        print("🔁 기존 QApplication 인스턴스 사용")

    print("🪟 LoginView 인스턴스 생성")
    login_window = LoginView()

    print("🔌 Receiver 인스턴스 생성 및 시그널 연결")
    receiver = Receiver(login_window)
    login_window.login_dictionary.connect(receiver.return_info)

    print("📦 SubmissionDataModel 인스턴스 생성 및 시그널 연결")
    main_model = SubmissionDataModel()
    login_window.login_dictionary.connect(main_model.get_dictionary)

    print("👀 login_window.show() 호출")
    login_window.show()

    print("🌀 QApplication 실행 시작")
    try:
        sys.exit(app.exec())
    except AttributeError:
        print("⚠️ exec() 없음 → exec_()로 실행")
        sys.exit(app.exec_())
