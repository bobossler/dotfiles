# Alias definitions
# I am keeping them separate from my main .bashrc file for portability

# some more ls aliases
# alias ll='ls -AlFh --color=auto'
# alias la='ls -A --color=auto'
# alias l='ls -CF --color=auto'

# trying out exa as a replacement for ls
alias ls='exa -al --color=always --group-directories-first'  # preferred
alias la='exa -a --color=always --group-directories-first'   # all files & dirs
alias ll='exa -l --color=always --group-directories-first'   # long list
alias lt='exa -aT --color=always --group-directories-first'  # tree list
alias l.='exa -a | egrep "^\."'                              # only dots
alias lr='exa -alr --sort=modified --color=always'           # reverse by modified

# Misc stuff
alias cm='cm.sh'   #cmatrix with random color
alias df='df -h'
alias free='free -h'
alias myip="curl http://ipecho.net/plain; echo"
alias neo='neofetch'

# Quick weather forecasts
alias qf='curl wttr.in/60504?u'
alias qford='curl wttr.in/ORD?u'
alias qfmdw='curl wttr.in/MDW?u'
alias qmoon='curl wttr.in/moon'

# Doppler radar loops - ILX=Central IL, LOT=Chicago
alias dopilx='curl -s https://radar.weather.gov/ridge/lite/KILX_loop.gif >! /tmp/doppler.gif && ffplay -loglevel quiet -loop 0 /tmp/doppler.gif'
alias doplot='curl -s https://radar.weather.gov/ridge/lite/KLOT_loop.gif >! /tmp/doppler.gif && ffplay -loglevel quiet -loop 0 /tmp/doppler.gif'

# Nordvpn quick commands
alias vpnc='nordvpn connect'
alias vpnd='nordvpn disconnect'
alias vpns='nordvpn status'
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

# Check Unicode support in terminal
alias unisup='curl https://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-demo.txt'

# A few package aliases
alias saupdate='sudo apt update'
alias saupgrade='sudo apt upgrade'
alias aptlistup='apt list --upgradeable'
alias mydots='/usr/bin/git --git-dir=/home/bobossler/.dotfiles --work-tree=/home/bobossler'
alias nalaupd='sudo nala update && nala list --upgradeable'
alias nalaupg='sudo nala upgrade'
alias nalaar='sudo nala autoremove'
