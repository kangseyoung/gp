import sys
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtGui import QPixmap

class Submitter(QWidget):
    def __init__(self, model):
        super().__init__()
        try:
            print("✅ Submitter 생성자 진입")
            self.model = model  # ✅ 전달된 모델 저장
            self.setup_ui()
        except Exception as e:
            print(f"❌ Submitter 초기화 실패: {e}")

    def setup_ui(self):
        print("📌 Submitter: setup_ui() 진입")
        ui_file_path = "ui\\main\\main.ui"
        ui_file = QFile(ui_file_path)
        loader = QUiLoader()

        self.ui = loader.load(ui_file)
        print("✅ UI 로딩 완료")

        self.ui.show()
        ui_file.close()
        print("✅ UI 화면 show() 호출됨")

        self.veiw_info()

    ###################################################################
    def set_current_path(self):
        print("📌 set_current_path() 호출됨")
        text = self.model.get_current_path()
        self.ui.current_path.setText(text)

    def set_ouput_path(self):
        print("📌 set_ouput_path() 호출됨")
        text = self.model.get_ouput_path()
        self.ui.output_path.setText(text)

    def set_pc_group(self):
        print("📌 set_pc_group() 호출됨")
        text = "text" #얘는 ,,,잘 모르겠다 안쓰는걸 할당해줘야할지,, 예약할 때, 받아야할지.,,
        #아님 내가 임의로 정해서 줘도될지... 
        self.ui.pcgroup.setText(text)

    def set_DCC_png(self):
        print("📌 set_DCC_png() 호출됨")
        png = "ui\\image\\menu1.png"
        pixmap = QPixmap(png)
        self.ui.DCC_png.setPixmap(pixmap)

    def set_profile_icon(self):
        print("📌 set_profile_icon() 호출됨")
        png = "ui\\image\\usericon.jpg"
        pixmap = QPixmap(png)
        self.ui.usericon.setPixmap(pixmap)

    def set_studentID(self):
        print("📌 set_studentID() 호출됨")
        text = self.model.get_studentID()
        self.ui.studentID.setText(text)

    def set_file_name(self):
        print("📌 set_file_name() 호출됨")
        text = self.model.get_file_name()
        self.ui.filename.setText(text)

    def click_send_to_deadline(self):
        print("📌 click_send_to_deadline() 연결 시작")
        self.ui.send_to_deadline.clicked.connect(self.test)
        print("✅ send_to_deadline 버튼 연결 완료")

    def test(self):
        print("💥 버튼 클릭됨: sendtodeadline")

    #####################################################################
    def veiw_info(self):
        print("▶️ veiw_info() 시작")
        self.set_current_path()
        self.set_ouput_path()
        self.set_pc_group()
        self.set_DCC_png()
        self.set_profile_icon()
        self.set_studentID()
        self.set_file_name()
        self.click_send_to_deadline()
        print("✅ veiw_info() 완료")

if __name__ == "__main__":
    print("🚀 Submitter main 진입")
    app = QApplication(sys.argv)
    window = Submitter()
    window.show()
    print("✅ Submitter window.show() 완료")
    sys.exit(app.exec())
