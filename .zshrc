# Set up the prompt

#autoload -Uz promptinit
#promptinit
#prompt adam1 red yellow magenta

setopt histignorealldups sharehistory

# Use emacs keybindings even if our EDITOR is set to vi
bindkey -e

# Keep 15000 lines of history within the shell and save it to ~/.zsh_history:
HISTSIZE=15000
SAVEHIST=15000
HISTFILE=~/.zsh_history
setopt HIST_IGNORE_SPACE
setopt HIST_REDUCE_BLANKS
setopt HIST_VERIFY

# Use modern completion system
autoload -Uz compinit
compinit

# Prompts for confirmation after 'rm *' etc
# Helps avoid mistakes like 'rm * o' when 'rm *.o' was intended
setopt RM_STAR_WAIT

# Don't write over existing files with >, use  >! instead
setopt NOCLOBBER

#  Enable color support of 'ls' and add aliases
if [[ "$TERM" != "dumb" ]]; then
    if [[ -x `which dircolors 2> /dev/null` ]]; then
        eval `dircolors -b`
        alias 'ls=ls --color=auto'
        alias 'dir=dir --color=auto'
        alias 'vdir=vdir --color=auto'
        alias 'grep=grep --color=auto'
        alias 'fgrep=fgrep --color=auto'
        alias 'egrep=egrep --color=auto'
    fi
fi

# Setup some static named directories
# In effect, creating shortcuts to long path names
hash -d acmedir=~/Projects/hugosite/acme-corporation
hash -d grampsdir=~/Projects/gramps

# Alias definitions.
# I have my additional aliases in a separate file named
# ~/.zsh_aliases, instead of adding them here directly.
# This makes them more portable.
if [ -f ~/.zsh_aliases ]; then
    . ~/.zsh_aliases
fi

zstyle ':completion:*' auto-description 'specify: %d'
zstyle ':completion:*' completer _expand _complete _correct _approximate
zstyle ':completion:*' format 'Completing %d'
zstyle ':completion:*' group-name ''
zstyle ':completion:*' menu select=2

eval "$(dircolors -b)"
zstyle ':completion:*:default' list-colors ${(s.:.)LS_COLORS}
zstyle ':completion:*' list-colors ''

zstyle ':completion:*' list-prompt %SAt %p: Hit TAB for more, or the character to insert%s
zstyle ':completion:*' matcher-list '' 'm:{a-z}={A-Z}' 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=* l:|=*'
zstyle ':completion:*' menu select=long
zstyle ':completion:*' select-prompt %SScrolling active: current selection at %p%s
zstyle ':completion:*' use-compctl false
zstyle ':completion:*' verbose true

zstyle ':completion:*:*:kill:*:processes' list-colors '=(#b) #([0-9]#)*=0=01;31'
zstyle ':completion:*:kill:*' command 'ps -u $USER -o pid,%cpu,tty,cputime,cmd'

source /usr/share/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
#[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

# Neofetch is a cool tool for dislaying system info
# turning it off while i research an issue
# neofetch

# display a Fortune upon opening a new terminal session
# also using cowsay/cowthink for fun
fortune | cowthink -w -n

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/bobossler/anaconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/bobossler/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/bobossler/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/bobossler/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

# adding a line for the Starship prompt
# might want to disable the prompt stuff at the top of this file
eval "$(starship init zsh)"
