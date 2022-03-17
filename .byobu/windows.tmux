new-session -s Terminals -n Home -c /home/bobossler ;
split-window -h -c /home/bobossler ;
new-window -n Win2 -c /home/bobossler/mpv-test ;
send-keys ls Space -l Enter ;
split-window -v -c /home/bobossler ;
send-keys man Space byobu Enter ;
select-window -t Home ;
select-pane -t 0
