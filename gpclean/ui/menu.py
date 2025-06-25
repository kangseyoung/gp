import logging
import os

# 로그 설정
log_dir = "D:/new_maya"
os.makedirs(log_dir, exist_ok=True)
log_path = os.path.join(log_dir, "gpclean.log")

logger = logging.getLogger("gpclean")
logger.setLevel(logging.DEBUG)

if not logger.handlers:
    file_handler = logging.FileHandler(log_path, encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

def create_menu():
    import maya.cmds as cmds
    import maya.mel as mel

    try:
        from gpclean.main import launch_login_ui

        # 메뉴 바 layout 이름 가져오기
        main_menu = mel.eval('$tmp=$gMainWindowMenuBar')

        if cmds.menu("GPCleanMenu", exists=True):
            cmds.deleteUI("GPCleanMenu", menu=True)
            logger.info("기존 GPCleanMenu 삭제함")

        cmds.menu("GPCleanMenu", label="PRFS", parent=main_menu, tearOff=True)
        cmds.menuItem(label="submit to deadline", parent="GPCleanMenu", command=lambda *_: launch_login_ui())

        logger.info("GPCleanMenu 생성 완료")

    except Exception as e:
        logger.exception(e)
