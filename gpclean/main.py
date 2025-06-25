
from gpclean.logging_setup import logger
try:
    from PySide6.QtWidgets import QApplication
    USING_QT = "PySide6"
    logger.info("6됨")
except ImportError:
    from PySide2.QtWidgets import QApplication
    USING_QT = "PySide2"
    logger.info("2됨")

logger.info(f" Loaded {USING_QT}")


import sys
from gpclean.ui.login.login_view import LoginView
from gpclean.ui.login.login_controller import Receiver
from gpclean.ui.main.model import SubmissionDataModel

login_window = None  # 전역 변수로 유지

def launch_login_ui():
    global login_window
    logger.info(" launch_login_ui 진입")

    app = QApplication.instance()
    if not app:
        logger.info("⚠️ QApplication 인스턴스가 없음 → 생성 필요")
        app = QApplication(sys.argv)

    logger.info(" LoginView 인스턴스 생성")
    login_window = LoginView()

    logger.info(" Receiver 연결")
    receiver = Receiver(login_window)
    login_window.login_dictionary.connect(receiver.return_info)

    logger.info(" Model 연결")
    main_model = SubmissionDataModel()
    login_window.login_dictionary.connect(main_model.get_dictionary)

    logger.info(" login_window.show() 호출")
    login_window.show()

    # 마야 내에서는 필요 없음
    # sys.exit(app.exec())
