#!/bin/bash

player=$(dbus-send --session --dest=org.freedesktop.DBus \
        --type=method_call --print-reply /org/freedesktop/DBus \
        org.freedesktop.DBus.ListNames | grep org.mpris.MediaPlayer2 |
        awk -F\" '{print $2}' | cut -d '.' -f4- | sort )
read -a strarr <<< "$player"
echo $strarr
