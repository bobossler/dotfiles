#!/usr/bin/env bash

function runme {
  if ! pgrep -f $1 ;
  then
    $@&
  fi
}

#run /usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1
runme nm-applet
#run parcellite
#run clipmenud
#run volctl
#run ~/.config/conky/start_conky ~/.config/conky/MX-CoreBlue/conkyrc2core 
#run remmina -i
runme picom --experimental-backends --config $HOME/.config/picom/picom.conf
runme conky -c $HOME/.config/conky/awesome/dracula-01.conkyrc

#if ! pgrep -f deja-dup-mon; then flatpak run --command=/app/libexec/deja-dup/deja-dup-monitor org.gnome.DejaDup; fi
#if ! pgrep -f ibus-daemon; then ibus-daemon -drx; fi
# test a notification
notify-send "Startup" "System starting"
# trying to get a startup sound
mpv --no-video /usr/share/sounds/freedesktop/stereo/service-login.oga

