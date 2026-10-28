# Alias definitions
# Keeping them in a separate file for portability across shells

# exa replacement for ls
alias ls='exa -al --icons --color=always --group-directories-first'  # preferred
alias la='exa -a --icons --color=always --group-directories-first'   # all files & dirs
alias ll='exa -l --icons --color=always --group-directories-first'   # long list
alias lt='exa -aT --icons --color=always --group-directories-first'  # tree list
alias l.='exa -a | egrep "^\."'                                      # only dots
alias lr='exa -al -s newest --icons --color=always'                  # reverse by modified

# Shell reload aliases
alias breload='. ~/.bashrc'
alias zreload='. ~/.zshrc'

# Misc stuff
alias cm='cm.sh'   # cmatrix with random color
alias df='df -h'
alias free='free -h'
alias myip="curl http://ipecho.net/plain; echo"
alias mkdir='mkdir --parents --verbose'

# Quick weather forecasts
alias qf='curl wttr.in/60504?u'
alias qford='curl wttr.in/ORD?u'
alias qfmdw='curl wttr.in/MDW?u'
alias qmoon='curl wttr.in/moon'

# Doppler radar loops - ILX=Central IL, LOT=Chicago
alias dopconus='curl -s -o /tmp/doppler.gif https://radar.weather.gov/ridge/standard/CONUS_loop.gif && ffplay -loglevel quiet -loop 0 /tmp/doppler.gif'
alias dopilx='curl -s -o /tmp/doppler.gif https://radar.weather.gov/ridge/standard/KILX_loop.gif && ffplay -loglevel quiet -loop 0 /tmp/doppler.gif'
alias doplot='curl -s -o /tmp/doppler.gif https://radar.weather.gov/ridge/standard/KLOT_loop.gif && ffplay -loglevel quiet -loop 0 /tmp/doppler.gif'
alias doppah='curl -s -o /tmp/doppler.gif https://radar.weather.gov/ridge/standard/KPAH_loop.gif && ffplay -loglevel quiet -loop 0 /tmp/doppler.gif'

# Emacs quick commands
alias emacs="emacsclient -c -a 'emacs'&"

# Add a fortune to the clear command
alias clear='clear ; fortune | cowsay -w -n'

# Gemini shortcuts
alias gb='~/gemblog.sh'
alias gf='~/gemfull.sh'

# Update Horizon website
alias hrzup='~/horizon-update.sh'

# Play TheEL.US Radio Station
alias radio='mpv --quiet "https://streaming.live365.com/a71722"'

# Get tmux status for session/windows/panes
alias tmuxst='tmux ls && tmux lsw -a && tmux lsp -a'

# Check Unicode support in terminal
alias unisup='curl https://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-demo.txt'

# enable/disable Pop Shop
alias popshopoff='
sed -i "s/X-GNOME-Autostart-enabled=true/X-GNOME-Autostart-enabled=false/" /home/$USER/.config/autostart/io.elementary.appcenter-daemon.desktop
echo "Pop Shop disabled"
killall io.elementary.appcenter'

# Package management aliases
alias saupdate='sudo apt update'
alias saupgrade='sudo apt upgrade'
alias aptup='sudo apt update && sudo apt upgrade'
alias aptlistup='apt list --upgradeable'
alias mydots='/usr/bin/git --git-dir=/home/bobossler/.dotfiles --work-tree=/home/bobossler'
