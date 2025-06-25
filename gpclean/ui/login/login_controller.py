try:
    from PySide6.QtCore import QObject, Slot
    from PySide6.QtWidgets import QMessageBox
    USING_QT = "PySide6"
except ImportError:
    from PySide2.QtCore import QObject, Slot
    from PySide2.QtWidgets import QMessageBox
    USING_QT = "PySide2"
from gpclean.logging_setup import logger

logger.info(f"ReplaceA Loaded {USING_QT}")

from gpclean.backend.authDB.db import auth_collection
import hashlib


logger.info(" Receiver 모듈 로드됨")

class Receiver(QObject):
    logger.info(" Receiver 클래스 정의됨")

    @Slot(dict)
    def __init__(self,veiw):
        super().__init__()
        logger.info("ReplaceA Receiver: __init__() 실행됨")
        self.view = veiw

    #######################################################
    def return_info(self, dictionary):
        logger.info(" Receiver.return_info() 호출됨")
        self.dictionary = dictionary
        logger.info(f" 받은 딕셔너리: {self.dictionary}")
        self.db_dictionary = auth_collection
        self.get_info_if_exists()

    #######################################################
    def hash_password(self):
        password = self.dictionary["password"]
        hashed = hashlib.sha256(password.encode()).hexdigest()
        logger.info(f" 비밀번호 해시값: {hashed}")
        return hashed

    def get_info_if_exists(self):
        logger.info(" get_info_if_exists(): DB에서 사용자 조회 중...")

        docs = auth_collection.find_one({"student_id": self.dictionary["student_id"]})
        logger.info(f" 조회 결과: {docs}")

        if docs:
            logger.info("ReplaceA 학번 존재함, 비밀번호 확인 중...")
            if docs["password_hash"] == self.hash_password():
                logger.info("ReplaceA 비밀번호 일치! 메인 UI로 이동!")
                self.open_main_win()
            else:
                logger.info(" 비밀번호 틀림")
                QMessageBox.warning(self.view.ui, "로그인 실패", "비밀번호가 틀렸습니다.")
        else:
            logger.info(" 학번 없음")
            QMessageBox.warning(self.view.ui, "로그인 실패", "학번이 틀렸습니다.")

    def open_main_win(self):
        logger.info(" open_main_win() 호출됨")
        try:
            from gpclean.ui.main.view import Submitter
            from gpclean.ui.main.model import SubmissionDataModel

            logger.info(" Submitter import 성공")

            # ReplaceA SubmissionDataModel을 먼저 만들고 dictionary 전달
            self.model = SubmissionDataModel()
            self.model.get_dictionary(self.dictionary)

            # ReplaceA Submitter에 model을 전달
            self.render_ui = Submitter(self.model)
            self.render_ui.show()

            logger.info("메인 UI 띄움")
        except Exception as e:
            logger.info(f" 메인 UI 열기 실패: {e}")