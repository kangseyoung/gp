import logging
import os
import maya.cmds as cmds
import maya.mel as mel

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

        # 올바른 메뉴바 layout 불러오기
        menu_bar = mel.eval('$tmp = $gMainWindowMenuBar')

        if cmds.menu('PRFS', exists=True):
            cmds.deleteUI('PRFS', menu=True)
            logger.info("기존 PRFS 삭제함")

        custom_menu = cmds.menu('PRFS', parent=menu_bar, tearOff=True, label='PRFS')
        cmds.menuItem(label="submit to deadline", parent=custom_menu, command=lambda *_: launch_login_ui())

        logger.info("'PRFS' 생성 완료")

    except Exception as e:
        logger.exception(e)
