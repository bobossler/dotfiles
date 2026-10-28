# Ensure unique PATH entries
typeset -U PATH path

# History options
setopt histignorealldups sharehistory
HISTSIZE=15000
SAVEHIST=15000
HISTFILE=~/.zsh_history
setopt HIST_IGNORE_SPACE
setopt HIST_REDUCE_BLANKS
setopt HIST_VERIFY
setopt EXTENDED_HISTORY

# Use modern completion system
fpath+=~/.zsh
autoload -Uz compinit
compinit

# Prompts for confirmation after 'rm *' etc
setopt RM_STAR_WAIT

# Don't write over existing files with >, use >! or >| instead
setopt NOCLOBBER

# Enable color support and grep aliases
if [[ "$TERM" != "dumb" ]]; then
    if (( $+commands[dircolors] )); then
        eval "$(dircolors -b)"
        alias 'grep=grep --color=auto'
        alias 'fgrep=fgrep --color=auto'
        alias 'egrep=egrep --color=auto'
    fi
fi

# Setup static named directories (shortcuts to long path names)
hash -d acmedir=~/Projects/hugosite/acme-corporation
hash -d grampsdir=~/Projects/gramps

# Alias definitions (kept in separate file for portability)
if [ -f ~/.zsh_aliases ]; then
    . ~/.zsh_aliases
fi

# Completion configuration
zstyle ':completion:*' auto-description 'specify: %d'
zstyle ':completion:*' completer _expand _complete _correct _approximate
zstyle ':completion:*' format 'Completing %d'
zstyle ':completion:*' group-name ''
zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"
zstyle ':completion:*' list-prompt %SAt %p: Hit TAB for more, or the character to insert%s
zstyle ':completion:*' matcher-list '' 'm:{a-z}={A-Z}' 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=* l:|=*'
zstyle ':completion:*' menu select=long
zstyle ':completion:*' select-prompt %SScrolling active: current selection at %p%s
zstyle ':completion:*' use-compctl false
zstyle ':completion:*' verbose true

zstyle ':completion:*:*:kill:*:processes' list-colors '=(#b) #([0-9]#)*=0=01;31'
zstyle ':completion:*:kill:*' command 'ps -u $USER -o pid,%cpu,tty,cputime,cmd'

# Functions for zellij
function zr () { zellij run --name "$*" -- zsh -ic "$*";}
function zrf () { zellij run --name "$*" --floating -- zsh -ic "$*";}
function ze () { zellij edit "$*";}
function zef () { zellij edit --floating "$*";}

# Source zsh auto suggestions, syntax highlighting, and fzf
source /usr/share/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

# display a Fortune upon opening a new terminal session
# also using cowsay/cowthink for fun
fortune | cowthink -w -n

# display a random colorscript
#colorscript random

# Initialize Starship prompt
eval "$(starship init zsh)"

# NVM (Node Version Manager) setup
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
