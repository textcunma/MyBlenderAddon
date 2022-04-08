'''
nフレーム前後に移動(n=1,2,3,4)
translation forward and backward : n frame (n=1,2,3,4)
'''

import bpy                                          # bpy : Blender module
from bpy.types import Operator                      # for process

# addon information
bl_info = {
    "name": "translation n frame",                                      # addon name
    "author": "textcunma",                                              # addon author
    "version": (1, 0),                                                  # addon version
    "blender": (3, 0, 0),                                               # Blender version
    "description": "translation n frame forward or backward",           # addon description
    "warning": "",                                                      # addon warning
    "support": "TESTING",                                               # addon classification
    "wiki_url": "https://github.com/textcunma/MyBlenderAddon",       # addon description (GitHub URL etc...)
    "tracker_url": "https://github.com/textcunma/MyBlenderAddon",    # addon support (GitHub URL etc...)
    "category": "TIMELINE"                                                  # addon category
}

# 1フレームを移動する
# move forward 1 frame (Operator class inheritance)
class AddonTranslationFrameNum1_Forward(Operator):
    bl_idname = "timeline.trans1_forward"                                   # ID for Blender process (!prohibit using capital letter!)
    bl_label = "forward 1 frame"                                            # label on menu
    bl_description = "forward 1 frame on timeline"                          # description on menu when hover mouse
    bl_options = {'REGISTER', 'UNDO'}                                       # process attribute

    #実行時に呼び出されるメイン処理
    # main process when run program
    def execute(self,context):
        bpy.context.scene.frame_current+=1
        return {'FINISHED'}

# 2フレームを移動する
# move forward 2 frame (Operator class inheritance)
class AddonTranslationFrameNum2_Forward(Operator):
    bl_idname = "timeline.trans2_forward"                                   # ID for Blender process (!prohibit using capital letter!)
    bl_label = "forward 2 frame"                                            # label on menu
    bl_description = "forward 2 frame on timeline"                          # description on menu when hover mouse
    bl_options = {'REGISTER', 'UNDO'}                                       # process attribute

    #実行時に呼び出されるメイン処理
    # main process when run program
    def execute(self,context):
        bpy.context.scene.frame_current+=2
        return {'FINISHED'}

# 3フレームを移動する
# move forward 3 frame (Operator class inheritance)
class AddonTranslationFrameNum3_Forward(Operator):
    bl_idname = "timeline.trans3_forward"                                   # ID for Blender process (!prohibit using capital letter!)
    bl_label = "forward 3 frame"                                            # label on menu
    bl_description = "forward 3 frame on timeline"                          # description on menu when hover mouse
    bl_options = {'REGISTER', 'UNDO'}                                       # process attribute

    #実行時に呼び出されるメイン処理
    # main process when run program
    def execute(self,context):
        bpy.context.scene.frame_current+=3
        return {'FINISHED'}

# 4フレームを移動する
# move forward 4 frame (Operator class inheritance)
class AddonTranslationFrameNum4_Forward(Operator):
    bl_idname = "timeline.trans4_forward"                                   # ID for Blender process (!prohibit using capital letter!)
    bl_label = "forward 4 frame"                                            # label on menu
    bl_description = "forward 4 frame on timeline"                          # description on menu when hover mouse
    bl_options = {'REGISTER', 'UNDO'}                                       # process attribute

    #実行時に呼び出されるメイン処理
    # main process when run program
    def execute(self,context):
        bpy.context.scene.frame_current+=4
        return {'FINISHED'}

# 1フレーム前に戻る
# move backard 1 frame (Operator class inheritance)
class AddonTranslationFrameNum1_Backward(Operator):
    bl_idname = "timeline.trans1_backward"                                   # ID for Blender process (!prohibit using capital letter!)
    bl_label = "backward 1 frame"                                            # label on menu
    bl_description = "backward 1 frame on timeline"                          # description on menu when hover mouse
    bl_options = {'REGISTER', 'UNDO'}                                       # process attribute

    #実行時に呼び出されるメイン処理
    # main process when run program
    def execute(self,context):
        bpy.context.scene.frame_current-=1
        return {'FINISHED'}

# 2フレーム前に戻る
# move backard 2 frame (Operator class inheritance)
class AddonTranslationFrameNum2_Backward(Operator):
    bl_idname = "timeline.trans2_backward"                                   # ID for Blender process (!prohibit using capital letter!)
    bl_label = "backward 2 frame"                                            # label on menu
    bl_description = "backward 2 frame on timeline"                          # description on menu when hover mouse
    bl_options = {'REGISTER', 'UNDO'}                                       # process attribute

    #実行時に呼び出されるメイン処理
    # main process when run program
    def execute(self,context):
        bpy.context.scene.frame_current-=2
        return {'FINISHED'}

# 3フレーム前に戻る
# move backard 2 frame (Operator class inheritance)
class AddonTranslationFrameNum3_Backward(Operator):
    bl_idname = "timeline.trans3_backward"                                   # ID for Blender process (!prohibit using capital letter!)
    bl_label = "backward 3 frame"                                            # label on menu
    bl_description = "backward 3 frame on timeline"                          # description on menu when hover mouse
    bl_options = {'REGISTER', 'UNDO'}                                       # process attribute

    #実行時に呼び出されるメイン処理
    # main process when run program
    def execute(self,context):
        bpy.context.scene.frame_current-=3
        return {'FINISHED'}

# 4フレーム前に戻る
# move backard 2 frame (Operator class inheritance)
class AddonTranslationFrameNum4_Backward(Operator):
    bl_idname = "timeline.trans4_backward"                                   # ID for Blender process (!prohibit using capital letter!)
    bl_label = "backward 4 frame"                                            # label on menu
    bl_description = "backward 4 frame on timeline"                          # description on menu when hover mouse
    bl_options = {'REGISTER', 'UNDO'}                                       # process attribute

    #実行時に呼び出されるメイン処理
    # main process when run program
    def execute(self,context):
        bpy.context.scene.frame_current-=4
        return {'FINISHED'}

# classes for registering Blender
classes = [
    AddonTranslationFrameNum1_Forward,
    AddonTranslationFrameNum2_Forward,
    AddonTranslationFrameNum3_Forward,
    AddonTranslationFrameNum4_Forward,
    AddonTranslationFrameNum1_Backward,
    AddonTranslationFrameNum2_Backward,
    AddonTranslationFrameNum3_Backward,
    AddonTranslationFrameNum4_Backward,
]

# List for shortcut key
addon_keymaps = []

# register shortcut key
def registershortcut():
    kc = bpy.context.window_manager.keyconfigs.addon         # info about all keymap
    if kc:
        kc = bpy.context.window_manager.keyconfigs.addon         # info about all keymap
        editor_l = [
            ('Dopesheet', 'DOPESHEET_EDITOR'),
            ('Graph Editor', 'GRAPH_EDITOR'),
            ("NLA Editor", "NLA_EDITOR"),
            ("Sequencer", "SEQUENCE_EDITOR")
        ]

        for editor, space in editor_l:
            km = kc.keymaps.new(name=editor, space_type=space)
            kmi = km.keymap_items.new(
                idname=AddonTranslationFrameNum1_Forward.bl_idname,     # press numeric keypad 1 -> +1 frame
                type='NUMPAD_1', value='PRESS')
            addon_keymaps.append((km, kmi))

            kmi2 = km.keymap_items.new(
                idname=AddonTranslationFrameNum2_Forward.bl_idname,     # press numeric keypad 2 -> +2 frame
                type='NUMPAD_2', value='PRESS')
            addon_keymaps.append((km, kmi2))

            kmi3 = km.keymap_items.new(
                idname=AddonTranslationFrameNum3_Forward.bl_idname,     # press numeric keypad 3 -> +3 frame
                type='NUMPAD_3', value='PRESS')
            addon_keymaps.append((km, kmi3))

            kmi4 = km.keymap_items.new(
                idname=AddonTranslationFrameNum4_Forward.bl_idname,     # press numeric keypad 4 -> +4 frame
                type='NUMPAD_4', value='PRESS')
            addon_keymaps.append((km, kmi4))

            kmi5 = km.keymap_items.new(
                idname=AddonTranslationFrameNum1_Backward.bl_idname,    # press Ctrl + numeric keypad 1 -> -1 frame
                type='NUMPAD_1', ctrl=True, value='PRESS')
            addon_keymaps.append((km, kmi5))

            kmi6 = km.keymap_items.new(
                idname=AddonTranslationFrameNum4_Backward.bl_idname,    # press Ctrl + numeric keypad 2 -> -2 frame
                type='NUMPAD_2', ctrl=True, value='PRESS')
            addon_keymaps.append((km, kmi6))

            kmi7 = km.keymap_items.new(
                idname=AddonTranslationFrameNum4_Backward.bl_idname,    # press Ctrl + numeric keypad 3 -> -3 frame
                type='NUMPAD_3', ctrl=True, value='PRESS')
            addon_keymaps.append((km, kmi7))

            kmi8 = km.keymap_items.new(
                idname=AddonTranslationFrameNum4_Backward.bl_idname,    # press Ctrl + numeric keypad 4 -> -4 frame
                type='NUMPAD_4', ctrl=True, value='PRESS')
            addon_keymaps.append((km, kmi8))

# unregister shortcut key
def unregistershortcut():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()


def draw_menu(self,context):
    layout = self.layout
    layout.separator()
    layout.operator(AddonTranslationFrameNum2_Forward.bl_idname, text="+2")
    layout.operator(AddonTranslationFrameNum3_Forward.bl_idname, text="+3")
    layout.operator(AddonTranslationFrameNum3_Backward.bl_idname, text="-2")
    layout.operator(AddonTranslationFrameNum3_Backward.bl_idname, text="-3")

# アドオン有効時の処理
# process when activate this addon
def register():
    for c in classes:                               # register class
        bpy.utils.register_class(c)
    bpy.types.TIME_MT_editor_menus.append(draw_menu)
    bpy.types.DOPESHEET_MT_editor_menus.append(draw_menu)
    registershortcut()                              # register shortcut key

# アドオン無効時の処理
# process when disable this addon
def unregister():
    unregistershortcut()                            # register shortcut key
    for c in classes:                               # unregister class
        bpy.utils.unregister_class(c)
    bpy.types.TIME_MT_editor_menus.remove(draw_menu)
    bpy.types.DOPESHEET_MT_editor_menus.remove(draw_menu)

if __name__ == "__main__":
    register()