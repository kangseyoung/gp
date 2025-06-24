bl_info = {
    "name": "GP Clean Blender Addon",
    "blender": (3, 0, 0),
    "version": (1, 0),
    "author": "Seyoung",
    "description": "Adds a menu item to launch GP Clean UI"
}

import bpy
import threading

def launch_tool():
    from main import launch_login_ui
    launch_login_ui()

class GP_OT_LaunchGPUI(bpy.types.Operator):
    bl_idname = "gp.launch_login_ui"
    bl_label = "PRFS"

    def execute(self, context):
        threading.Thread(target=launch_tool, daemon=True).start()
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(GP_OT_LaunchGPUI.bl_idname)

def register():
    bpy.utils.register_class(GP_OT_LaunchGPUI)
    bpy.types.TOPBAR_MT_editor_menus.append(menu_func)

def unregister():
    bpy.types.TOPBAR_MT_editor_menus.remove(menu_func)
    bpy.utils.unregister_class(GP_OT_LaunchGPUI)

if __name__ == "__main__":
    register()
