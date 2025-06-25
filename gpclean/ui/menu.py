# ui/menu.py

def create_menu():
    import maya.cmds as cmds
    from gpclean.main import launch_login_ui
    if cmds.menu("GPCleanMenu", exists=True):
        cmds.deleteUI("GPCleanMenu", menu=True)

    cmds.menu("GPCleanMenu", label="GP Clean", parent="MayaWindow", tearOff=True)
    cmds.menuItem(label="Open GP-Clean UI", parent="GPCleanMenu", command=lambda *_: launch_login_ui())
