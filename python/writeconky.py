#asd
import os
import subprocess
from conky_settings import *

HOME = os.environ['HOME']
SCRIPTS = "/.config/conky/dango_conky/scripts/"
CORES = int(subprocess.run(["grep", "-c", "^processor", "/proc/cpuinfo"], capture_output=True).stdout)
PROCESSES = 5
STYLE_TEXT = "${font Roboto:bold:size=8}${goto 95}${color1}"
STYLE_PLAYER_TITLE = "${font Roboto:bold:size=8}${goto 170}${color1}"


def gen_header(name):
    return "${font Roboto:bold:size=10}${color0}" + name + "${color1}  ${hr 2}\n"


def system_info():
    header = gen_header("SYSTEM INFO")
    info = STYLE_TEXT + "${voffset 10}OS: ${color2}$sysname $kernel\n"
    cpu = STYLE_TEXT + "CPU: ${color2}Intel i7-7600U\n"
    gpu = STYLE_TEXT + "GPU: ${color2}None\n"
    utime = STYLE_TEXT + "Uptime: ${color2}${uptime_short}\n"
    return header + info + cpu + gpu + utime + "##\n"


def cpu_info():
    header = gen_header("CPU")
    graph = STYLE_TEXT + "${cpugraph 0 20,300 515151 ff3333 -t}\n"
    cores = "${voffset 10}"
    prosesses = ""

    for i in range(1, CORES+1):
        cores += STYLE_TEXT + "Core " + str(i) + ": ${goto 140}${color2}${freq_g " + str(i) + "}Ghz ${goto 190}${color1}${cpubar cpu" + str(i) + "}\n"
    for i in range(1, PROCESSES+1):
        prosesses += STYLE_TEXT + "${top name " + str(i) + "}${color2}${goto 220}${top mem_res " + str(i) + "}${goto 260}${top cpu " + str(i) + "}\n"
    return header + cores + graph + prosesses + "##\n"


def memory_info():
    header = gen_header("MEMORY")
    bar_ram = STYLE_TEXT + """${voffset 10}${color1}RAM ${goto 220}${color2}$mem ${color1}/ ${color2}$memmax $alignr $memperc%
${goto 95}${color1}$membar\n"""
    bar_swap = STYLE_TEXT + """swap ${goto 220}${color2}$swap ${color1}/ ${color2}$swapmax $alignr $swapperc%
${goto 95}${color1}$swapbar\n"""
    prosesses = "${voffset 10}"

    for i in range(1, PROCESSES+1):
        prosesses += STYLE_TEXT + "${top_mem name " + str(i) + "}${color2}${goto 220}${top_mem mem_res " + str(i) + "}${goto 260}${top_mem cpu " + str(i) + "}\n"
    return header + bar_ram + bar_swap + prosesses + "##\n"

def storage_info():
    header = gen_header("STORAGE")
    root_bar = STYLE_TEXT + """${voffset 10}root ${goto 220}${color2}${fs_used /} ${color1}/ ${color2}${fs_size /} $alignr ${fs_free_perc /}%
${goto 95}${color1}${fs_bar /}\n"""
    home_bar = STYLE_TEXT + """home ${goto 220}${color2}${fs_used /home/camilla} ${color1}/ ${color2}${fs_size /home/camilla} $alignr ${fs_free_perc /home/camilla}%
${goto 95}${color1}${fs_bar /home/camilla}\n"""
    return header + root_bar + home_bar + "##\n"


def time_info():
    header = gen_header("TIME")
    time = r"""${font Roboto:size=30}${goto 130}${voffset 20}${color0}${time %H:%M:%S }
${font Roboto:bold:size=10}${goto 150}${voffset -20}${color2}${time %e %B %Y}
${font Roboto:bold:size=8}${goto 180}${color2}${time %A}
# ${color1} ${execpi 60 DJS=`date +%_d`; cal | sed s/"\(^\|[^0-9]\)$DJS"'\b'/'\1${color0}'"$DJS"'$color1'/}
"""
    return header + time + "##\n"


def weather_info():
    header = gen_header("WEATHER")
    weather = "${font Roboto:bold:size=8}${color1}${voffset 20}${execpi 900  python " + HOME + "/.config/conky/dango_conky/python/weather.py}"
    image = "${image " + HOME + "/.config/conky/dango_conky/assets/weather_icon.png -p 260,550}"
    return header + weather + image + "\n##\n"


def now_playing_info():
    header = gen_header("NOW PLAYING")
    get_image = "${exec " + HOME + SCRIPTS + "get_cover.sh}"
    get_album = "${exec " + HOME + SCRIPTS +"get_album.sh}"
    get_artist = "${exec " + HOME + SCRIPTS +"get_artist.sh}"
    get_track = "${exec " + HOME + SCRIPTS + "get_track.sh}"
    #get_status = "${exec " + HOME + SCRIPTS + "get_status.sh}"

    image = "${image " + HOME + "/.config/conky/dango_conky/assets/cover.jpg -p 10,30 -s 150x150}\n"
    #track = STYLE_PLAYER_TITLE + "${voffset -20}Title: \n${font Roboto:bold:size=12}${goto 170}${color0}${execpi 10 " + HOME + SCRIPTS + "get_track.sh >&1 " + HOME + SCRIPTS + "print_track.sh}"

    track = STYLE_PLAYER_TITLE + "${voffset -20}Title: \n${font Roboto:bold:size=12}${goto 170}${color0}${scroll 60 3 " + get_track +  "}\n"
    artist = STYLE_PLAYER_TITLE + "Artist: \n${font Roboto:bold:size=10}${goto 170}${color1}" + get_artist + "\n"
    album = STYLE_PLAYER_TITLE + "Album: \n${font Roboto:bold:size=8}${goto 170}${color2}" + get_album + "\n"
    return "\n" + header + get_image + "\n" + image  + track + artist + album +"##\n"


def skinfo_info():
    header = "${voffset 100}" + gen_header("SKINFO")
    lists = "${execpi 3600 python " + HOME + "/.config/conky/dango_conky/python/skinfo.py}"
    return header + lists


def build_conky(parts):
    conky_dict = {"settings_gen": general_settings(),
                  "settings_pl": nowplaying_settings(),
                  "sys": system_info(),
                  "cpu": cpu_info(),
                  "ram": memory_info(),
                  "storage": storage_info(),
                  "time": time_info(),
                  "weather": weather_info(),
                  "player": now_playing_info(),
                  "skinfo": skinfo_info()}

    conky = ""
    for part in parts:
        conky += conky_dict[part]

    return conky


def write_conky(conky_file, parts):
    path = HOME + "/.config/conky/dango_conky/conky/" + conky_file
    with open(path, 'w') as file:
        file.write(build_conky(parts))


def main():
    main_conky = ["settings_gen", "sys", "cpu", "ram", "storage", "time"]
    player_conky = ["settings_pl", "player"]
    write_conky("conkyrc_test", main_conky)
    write_conky("conkyrc_player", player_conky)


if __name__ == "__main__":
    main()
