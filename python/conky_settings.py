def general_settings():
    return r"""# Conky settings #
background yes
update_interval 1

cpu_avg_samples 6
net_avg_samples 2

override_utf8_locale yes

double_buffer yes
no_buffers yes

text_buffer_size 2048
imlib_cache_size 0

temperature_unit celsius

# Window specifications #
own_window yes
own_window_class Conky
own_window_type override
own_window_transparent yes
own_window_hints undecorated,sticky,skip_taskbar,skip_pager,below

border_inner_margin 0
border_outer_margin 0

minimum_size 400 1024

alignment top_left
gap_y 21
gap_x 20

# Graphics settings #
draw_shades no
draw_outline no
draw_borders no
draw_graph_borders no

# Text settings #
use_xft yes
override_utf8_locale yes
xftfont Roboto:bold:size=6
xftalpha 0.8
uppercase no

temperature_unit celsius

default_color 333333
color0 ff3333
color1 515151
color2 666666

own_window_argb_value 0
own_window_argb_visual no
own_window_colour 000000

TEXT
"""


def nowplaying_settings():
    return r"""# Conky settings #
background yes
update_interval 1

cpu_avg_samples 6
net_avg_samples 2

override_utf8_locale yes

double_buffer yes
no_buffers yes

text_buffer_size 2048
imlib_cache_size 0

temperature_unit celsius

# Window specifications #
own_window yes
own_window_class Conky
own_window_type override
own_window_hints undecorated,sticky,skip_taskbar,skip_pager,below
own_window_transparent yes
own_window_argb_visual no
own_window_argb_value 0
own_window_colour 000000

border_inner_margin 0
border_outer_margin 0

minimum_size 400 200

alignment top_left
gap_y 11
gap_x 500

# Graphics settings #
draw_shades no
draw_outline no
draw_borders no
draw_graph_borders no

# Text settings #
use_xft yes
override_utf8_locale yes
xftfont Roboto:bold:size=6
xftalpha 0.8
uppercase no

temperature_unit celsius

default_color 333333
color0 ff3333
color1 515151
color2 666666

TEXT
"""
