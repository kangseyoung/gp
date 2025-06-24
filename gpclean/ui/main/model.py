from gpclean.backend.authDB.db import reservation_collection

try:
    from PySide6.QtCore import QObject, Slot
    USING_QT_CORE = "PySide6"
except ImportError:
    from PySide2.QtCore import QObject, Slot
    USING_QT_CORE = "PySide2"

print(f"✅ Loaded {USING_QT_CORE} for QObject and Slot")

class SubmissionDataModel(QObject):

    @Slot(dict)
    def __init__(self):
        super().__init__()
        print("✅ SubmissionDataModel: __init__() 실행됨")

    def get_dictionary(self, dict):
        self.dictionary = dict
        print(f"📌 dictionary 저장됨: {dict}")

    def check_DCC(self):
        try:
            import maya.cmds as cmds
            print("📌 DCC 감지: Maya")
            return "maya"
        except ImportError:
            try:
                import bpy
                print("📌 DCC 감지: Blender")
                return "blender"
            except ImportError:
                try:
                    import nuke
                    print("📌 DCC 감지: Nuke")
                    return "nuke"
                except ImportError:
                    print("⚠️ DCC 감지 실패: Unknown")
                    return "unknown"

    def get_current_path(self):
        dcc = self.check_DCC()

        if dcc == "maya":
            import maya.cmds as cmds
            current_file = cmds.file(q=True, sceneName=True)
            print(f"📂 Maya 파일 경로: {current_file}")
            return current_file
        elif dcc == "blender":
            import bpy
            current_file = bpy.data.filepath
            print(f"📂 Blender 파일 경로: {current_file}")
            return current_file
        elif dcc == "nuke":
            import nuke
            current_file = nuke.root().name()
            print(f"📂 Nuke 파일 경로: {current_file}")
            return current_file
        else:
            print("❌ 현재 경로 가져오기 실패 (Unknown DCC)")
            return "unknown"

    def get_ouput_path(self):
        studentID = self.get_studentID()
        today = self.dictionary.get("date_time")
        output_dir = f"render_output\\{studentID}\\{today}\\"
        print(f"📁 Output 디렉토리: {output_dir}")
        return output_dir

    def get_pc_group(self):
        print("📌 PC 그룹 요청됨 (아직 구현 안됨)")
        pass

    def get_studentID(self):
        studentID = self.dictionary.get('student_id')
        print(f"🪪 Student ID: {studentID}")
        return studentID

    def get_file_name(self):
        current_path = self.get_current_path()
        file_name = current_path.split("\\")[-1]
        print(f"📄 파일 이름: {file_name}")
        return file_name

    def get_signed_time(self):
        time = self.dictionary.get("date_time")
        print(f"⏰ 로그인 시간: {time}")
        return time

    def get_reservation_list_for_student_id(self):
        print("📥 예약 시간 조회 중...")
        reservation_dict = reservation_collection.find_one({"student_id": self.dictionary["student_id"]})
        print(f"📦 DB 반환 값: {reservation_dict}")
        reservation_time = reservation_dict.get("days") if reservation_dict else []
        print(f"📅 예약 시간 리스트: {reservation_time}")
        return reservation_time
