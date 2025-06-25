import logging
import os
import maya.cmds as cmds
import maya.mel as mel
import maya.utils

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
    try:
        from gpclean.main import launch_login_ui
        if cmds.menu("PRFS", exists=True):
            cmds.deleteUI("PRFS", menu=True)
            logger.info("기존 메뉴 PRFS 삭제함")

        # 부모를 'MayaWindow'로 하면 정상적으로 생성됨 (Python 방식)
        cmds.setParent("MayaWindow")
        cmds.menu("PRFS", label="PRFS", tearOff=True)
        cmds.menuItem(label="Submit to Deadline", parent="PRFS", command=lambda *_: launch_login_ui())

        logger.info("PRFS 메뉴 생성 완료")

    except Exception as e:
        logger.exception("메뉴 생성 중 에러 발생: %s", e)

    except Exception as e:
        logger.exception(e)