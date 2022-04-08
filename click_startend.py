'''
右クリックを押すと表示されるコンテキストメニュー内に
タイムラインの開始位置と終了位置を指定するコマンドを追加する
ref: https://blender.stackexchange.com/questions/150101/python-how-to-add-items-in-context-menu-in-2-8
'''

import bpy                                          # bpy : Blender module
from bpy.types import Operator                      # for process

# addon information
bl_info = {
    "name": "ContextStartEnd",                                                              # addon name
    "author": "textcunma",                                                                  # addon author
    "version": (1, 0),                                                                      # addon version
    "blender": (3, 0, 0),                                                                   # Blender version
    "description": "decide start and end point at time sequence on context menu",           # addon description
    "warning": "",                                                                          # addon warning
    "support": "TESTING",                                                                   # addon classification
    "wiki_url": "https://github.com/textcunma/MyBlenderAddon",                              # addon description (GitHub URL etc...)
    "tracker_url": "https://github.com/textcunma/MyBlenderAddon",                           # addon support (GitHub URL etc...)
    "category": "User Interface"                                                            # addon category
}

class AddonStartTimeNow(Operator):
    bl_idname = "timeline.convert_startframe"                                               # ID for Blender process (!prohibit using capital letter!)
    bl_label = "現在のフレームを開始フレームにする"                                            # label on menu
    bl_description = "Set the current frame as the start frame"                             # description on menu when hover mouse
    bl_options = {'REGISTER', 'UNDO'}                                                       # process attribute

    #実行時に呼び出されるメイン処理
    # main process when run program
    def execute(self,context):
        bpy.context.scene.frame_start=bpy.context.scene.frame_current
        return {'FINISHED'}

class AddonEndTimeNow(Operator):
    bl_idname = "timeline.convert_endframe"                                               # ID for Blender process (!prohibit using capital letter!)
    bl_label = "現在のフレームを終了フレームにする"                                            # label on menu
    bl_description = "Set the current frame as the end frame"                             # description on menu when hover mouse
    bl_options = {'REGISTER', 'UNDO'}                                                       # process attribute

    #実行時に呼び出されるメイン処理
    # main process when run program
    def execute(self,context):
        bpy.context.scene.frame_end=bpy.context.scene.frame_current
        return {'FINISHED'}

def draw_menu(self, context):
    layout = self.layout
    layout.separator()
    layout.operator(AddonStartTimeNow.bl_idname, text="現在のフレームを開始フレームにする")
    layout.operator(AddonEndTimeNow.bl_idname, text="現在のフレームを終了フレームにする")

classes = [
    AddonStartTimeNow,
    AddonEndTimeNow,
]

# アドオン有効時の処理
# process when activate this addon
def register():
    for c in classes:                               # register class
        bpy.utils.register_class(c) 
    bpy.types.DOPESHEET_MT_context_menu.append(draw_menu)

# アドオン無効時の処理
# process when disable this addon
def unregister():
    for c in classes:                               # register class
        bpy.utils.register_class(c) 
    bpy.types.DOPESHEET_MT_context_menu.remove(draw_menu)

if __name__ == "__main__":
    register()