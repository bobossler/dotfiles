#!/usr/bin/bash

# set the background
if [ -x "$(command -v feh)" ]; then
    feh --bg-scale --randomize ~/.wallpapers/*
fi

# start picom
picom --experimental-backends --config ~/.config/picom/picom.conf &

# start the emacs daemon
#/usr/bin/emacs --daemon &

# start conky
#conky -c ~/.config/conky/qtile/doom-one-01.conkyrc &

# start the network manager
nm-applet &

# start flameshot for screenshots
flameshot &

# start the DejaDup application
#flatpak run --command=/app/libexec/deja-dup/deja-dup-monitor org.gnome.DejaDup &

# start xfce-power-manager for screen power saving
xfce4-power-manager --daemon &

