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

# 메뉴 생성 함수
def create_menu():
    try:
        import maya.cmds as cmds
        from gpclean.main import launch_login_ui

        if cmds.menu("GPCleanMenu", exists=True):
            cmds.deleteUI("GPCleanMenu", menu=True)
            logger.info("기존 GPCleanMenu 삭제함")

        cmds.menu("GPCleanMenu", label="PRFS", parent="MayaWindow", tearOff=True)
        cmds.menuItem(label="submit to deadline", parent="GPCleanMenu", command=lambda *_: launch_login_ui())

        logger.info("GPCleanMenu 생성 완료")

    except Exception as e:
        logger.exception(e)
