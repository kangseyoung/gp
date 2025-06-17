"""
- 사용자 입력 값이나 시스템에서 얻은 정보를 구조화
- Deadline에서 요구하는 Job/Plugin 설정 구조 관리
- 저장/불러오기 또는 JSON 변환 처리 등
Model: 데이터 정의 및 처리 담당
데이터 파밍도하고 , 외부 툴이랑 연동해서
컨트롤러에서 만들어진 데이터를 여기서 딕셔너리로정리하는곳.
"""

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

from datetime import datetime

class SubmissionDataModel():
    def check_DCC(self):
        try:
            import maya.cmds as cmds
            return "maya"
        except ImportError:
            try:
                import bpy
                return "blender"
            except ImportError:
                try:
                    import nuke
                    return "nuke"
                except ImportError:
                    return "unknown"

    def get_current_path(self):
        """
        현재 파일의 경로 가져오기 


        """
        
        dcc = self.check_DCC()

        # 현재 열려있는 파일의 경로를 가져옵니다.
        if dcc == "maya":
            current_file = cmds.file(q=True, sceneName=True)
            print(current_file)
            #C:/Projects/shot01/scene_v002.mb

            return current_file
        elif dcc == "blender":
            current_file = bpy.data.filepath
            #D:/BlenderProjects/scene.blend

            return current_file
        elif dcc == "nuke":
            current_file = nuke.root().name()
            #E:/NukeProjects/composite_v01.nk

        elif dcc == "unknown":
            print("Unknown DCC tools..ㅗ")
            return dcc
        
    def get_ouput_path(self):
        """
        output path 띄우는 함수
        학번/날짜/여기부턴 설정값대로 
        
        """
        studentID = self.get_studentID()
        today = datetime.date()
        output_dir = f"render_output\\{studentID}\\{today}\\"

        pass
    def get_pc_group(self):
        """
        pc group 띄우는 함수 이거는이제 DB에서 가져와야될 것들이고 그건
        다른 클래스에서 정보 가져오는거 여기선 띄우기만 
        """
        
        pass

    def get_name(self):
        """
        이거는이제 DB에서 정보 가져오는 함수의 정보를가지고
        DB에서 가져와야되는 부분분
        """
        
        pass
    def get_studentID(self):
        """
        이거는이제 DB에서 정보 가져오는 함수의 정보를가지고
        ui에 띄우는
        """

        pass
    def get_file_name(self):
        """
        file name 은 DCC툴에서 current file 조회하느 api가 있을거임 그거쓴 함수로
        얘가 정보받아와서 ui에 띄우는거고
        get_current_path랑 합쳐도될거같고,,아님 그 path에서 스플릿해서[-1]  
        """

        pass
