#!/bin/bash

{
    imgurl=$(dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get string:'org.mpris.MediaPlayer2.Player' string:'Metadata' | egrep -A 1 "artUrl" | egrep -v "artUrl"| cut -b 44- | cut -d '"' -f 1)
    exec wget -q -O $HOME/.config/conky/dango_conky/assets/cover.jpg $imgurl
} || {
    imgurl=$(dbus-send --print-reply --dest=org.mpris.MediaPlayer2.audacious /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get string:'org.mpris.MediaPlayer2.Player' string:'Metadata' | egrep -A 1 "artUrl" | egrep -v "artUrl"| cut -b 44- | cut -d '"' -f 1)
    exec curl --output "$HOME/.config/conky/dango_conky/assets/cover.jpg" $imgurl
}
#EOF
