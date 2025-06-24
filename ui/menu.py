# ui/menu.py
import maya.cmds as cmds
from main import launch_login_ui

def create_menu():
    if cmds.menu("GPCleanMenu", exists=True):
        cmds.deleteUI("GPCleanMenu", menu=True)

    cmds.menu("GPCleanMenu", label="GP Clean", parent="MayaWindow", tearOff=True)
    cmds.menuItem(label="Open GP-Clean UI", parent="GPCleanMenu", command=lambda *_: launch_login_ui())
