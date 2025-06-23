from PySide6.QtCore import QObject, Signal
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMessageBox
from backend.authDB.db import reservation_collection,auth_collection
import hashlib
from ui.main.view import Submitter
from login_view import LoginView
"""
{'_id': ObjectId('68514fcbb81ba211e54157d8'), 'student_id': 'C123000', 'password_hash': '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4'}
"""

"""
self.dictionary
{'student_id': 'SDFSDF', 
'password': 'SDFSDFAA', 
'date_time': '2025-06-21T16:43:23.679319'}
"""
class Receiver(QObject,LoginView):
    @Slot(dict)
    def __init__(self, login_view):
        self.view = login_view
    #######################################################
    def return_info(self,dictionary):
        self.dictionary = dictionary
        print(self.dictionary)
        self.db_dictionary = auth_collection
        self.get_info_if_exists()
    ######################################################
    def hash_password(self):
        password = self.dictionary["password"]

        return hashlib.sha256(password.encode()).hexdigest()
        #비밀번호해시화 하는 함수, 
    def get_info_if_exists(self):
        #ui에서 입력한 정보랑 디비에 있는 정보랑 대조하는 함수

        docs = auth_collection.find_one({"student_id": self.dictionary["student_id"]})
        if docs:
            if docs["password_hash"]==self.hash_password():
                self.open_main_win()
            else:
                QMessageBox.warning(self.view.ui, "로그인 실패", "비밀번호가 틀렸습니다.")
                print("uknown user") # ui에 띄우기?
        else:
            QMessageBox.warning(self.view.ui, "로그인 실패", "학번이 틀렸습니다.")

    def open_main_win(self):
        # 메인으로 넘겨주는 함수 만약에 대조해서 일치한다면. 
        self.render_ui = Submitter()
        self.render_ui.show()