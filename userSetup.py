import sys
import logging
site_packages = "D:/new_maya/Maya2023/2023/scripts"
if site_packages not in sys.path:
    sys.path.append(site_packages)
    logging.info("appendsdfsdfsdfsdfsdfsdfdsfsdf")
try:
    from gpclean.ui.menu import create_menu
    if __name__ == "__main__":
        import maya.utils
        maya.utils.executeDeferred(create_menu)

except Exception as e:
    print(e)  # 전체 트레이스백 기록