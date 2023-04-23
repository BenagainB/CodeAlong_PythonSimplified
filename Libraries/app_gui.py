from dearpygui.core import *
from dearpygui.simple import *

# window object settings
set_main_window_size(540, 720)
set_global_font_scale(1.25)
set_theme("Gold")
set_style_window_padding(30, 30)

with window("Simple SMS Spam Filter", width=520, height=677):
    print("GUI is running...")
    set_window_pos("Simple SMS Spam Filter", 0, 0)
    add_drawing("logo", width=520, height=290)
    add_separator()
    add_spacing(count=12)

draw_image("logo", "logo_spamFilter.png", [0,240])

start_dearpygui()
