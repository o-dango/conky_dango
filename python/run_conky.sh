#!/bin/bash

killall conky
python writeconky.py
conky -c $HOME/.config/conky/dango_conky/conky/conkyrc_test &
conky -c $HOME/.config/conky/dango_conky/conky/conkyrc_player &
