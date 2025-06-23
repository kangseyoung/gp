"""
- 사용자와 상호작용하는 인터페이스 제공
- 폼, 입력창, 버튼 등 구성
- Controller에서 UI 요소 접근 가능하도록 getter 함수 제공
"""

import sys
import PySide6
from PySide6.QtWidgets import QWidget,QApplication,QLabel
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtGui import QPixmap
from main.model import SubmissionDataModel


class Submitter(QWidget,SubmissionDataModel):
    def __init__(self):
        super().__init__()
        self.setup_ui()
    def setup_ui(self):
        ui_file_path="ui\\main\\main.ui"
        ui_file=QFile(ui_file_path)
        loader=QUiLoader()
        self.ui=loader.load(ui_file)#ui 불러온거다.
        self.ui.show()#ui띄우기.
        ui_file.close()
        self.veiw_info()
        """
        - [ ]  current path 띄우는 함수
        - [ ]  output path 띄누는 함수
        - [ ]  pc group 띄우는 함수
        - [ ]  DCC png 띄우는 함수
        - [ ]  profile icon pixmap 띄우는 함수
        - [ ]  name 띄우는 함수
        - [ ]  student ID 띄우는 함수
        - [ ]  file name 띄우는 함수
        - [ ]  send to deadline 버튼 누르면 연결되는 함수
        """
    ###################################################################
        """
        current_path

        output_path

        pcgroup

        filename

        DCC_png

        usericon

        name

        studentID

        send_to_deadline
        
        """

    def set_current_path(self):
        """
        현재 파일의 경로 가져와서 ui에 띄우기
        """
        text="text"
        self.ui.current_path.setText(text)
        pass
    def set_ouput_path(self):
        """
        output path 띄우는 함수
        """
        text="text"
        self.ui.output_path.setText(text)
        pass
    def set_pc_group(self):
        """
        pc group 띄우는 함수 이거는이제 DB에서 가져와야될 것들이고 그건
        다른 클래스에서 정보 가져오는거 여기선 띄우기만 
        """
        text="text"
        self.ui.pcgroup.setText(text)
        pass
    def set_DCC_png(self):
        """
        DCC png 띄우는 함수 현재 ui를 띄운 DCC툴이 뭔지를 파악하는 함수가 다른 클래스에
        있고 그 함수가 DCC툴 뭔지 알려주면
        ui폴더 안에 있는 png 사진들중에 일치하는거 대조해서
        얘가 가져옴 그래서 그거 띄우는거임
        """
        png="..\\image\\menu1.png"
        pixmap=QPixmap(png)
        self.ui.DCC_png.setPixmap(pixmap)

        pass
    def set_profile_icon(self):
        """
        profile icon pixmap 띄우는 함수 이거는 그냥 ui 파일 안에 
        png파일 넣어두고
        거기서 땡겨오게
        """
        png="..\\image\\usericon.jpg"
        pixmap=QPixmap(png)
        self.ui.usericon.setPixmap(pixmap)

        pass
    def set_studentID(self):
        """
        이거는이제 DB에서 정보 가져오는 함수의 정보를가지고
        ui에 띄우는
        """
        text="studentID"
        self.ui.current_path.setText(text)
        pass
    def set_file_name(self):
        """
        file name 은 DCC툴에서 current file 조회하느 api가 있을거임 그거쓴 함수로
        얘가 정보받아와서 ui에 띄우는거고

        """
        text="text"
        self.ui.filename.setText(text)
        pass
    def click_send_to_deadline(self):
        """
        이제 얠 클릭하면 버튼클릭 함수 실행되는거고 그건 controller 모듈에 있어야하는거고
        얘는 클릭 이벤트 후에 함수 어떤거 실행할지만 정해주는 함수임
        """
        self.ui.send_to_deadline.clicked.connect(self.test)
        pass
    def test(self):
        print("######sendtodeadline##########")
    #####################################################################
    def veiw_info(self):
        self.set_current_path()
        self.set_ouput_path()
        self.set_pc_group()
        self.set_DCC_png()
        self.set_profile_icon()
        self.set_studentID()
        self.set_file_name()
        self.click_send_to_deadline()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Submitter()
    window.show()
    sys.exit(app.exec())