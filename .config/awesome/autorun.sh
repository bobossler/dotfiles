#!/usr/bin/env bash

function run {
  if ! pgrep -f $1 ;
  then
    $@&
  fi
}

#run /usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1
run nm-applet
#run parcellite
#run clipmenud
#run volctl
#run ~/.config/conky/start_conky ~/.config/conky/MX-CoreBlue/conkyrc2core 
#run remmina -i
run picom --experimental-backends --config $HOME/.config/picom/picom.conf
run ibus-daemon -drx
if ! pgrep -f deja-dup-mon; then flatpak run --command=/app/libexec/deja-dup/deja-dup-monitor org.gnome.DejaDup; fi
#run mpv --no-video ~/.config/awesome/fishlive/sounds/startup-snd-1.mp3
