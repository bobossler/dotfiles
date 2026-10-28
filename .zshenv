# ~/.zshenv: Executed for all zsh shells (scripts, interactive, login).

# Ensure unique entries in PATH automatically
typeset -U PATH path

# Portable path_prepend function
path_remove() {
    PATH=":$PATH:"
    while case "$PATH" in *":$1:"*) true ;; *) false ;; esac; do
        PATH="${PATH%%:$1:*}:${PATH#*:$1:}"
    done
    PATH="${PATH#:}"
    PATH="${PATH%:}"
}

path_prepend() {
    [ -d "$1" ] || return 0
    path_remove "$1"
    PATH="$1${PATH:+:$PATH}"
}

# Environment variables
export EDITOR='fresh'
export VISUAL='fresh'
export FILE='ranger'
export PAGER='less'
export MANPAGER='most'
export VIEWER='zathura'

# Go environment
export GOPATH="${GOPATH:-$HOME/go}"

# Prepend user directories in order of priority (last prepended = highest priority)
path_prepend "/usr/local/go/bin"
path_prepend "$GOPATH/bin"
path_prepend "$HOME/.emacs.d/bin"
path_prepend "$HOME/.spicetify"
path_prepend "$HOME/perl5/bin"
path_prepend "$HOME/.cargo/bin"
path_prepend "$HOME/bin"
path_prepend "$HOME/.local/bin"
export PATH

# Set $PATH and vars for Perl5 cleanly
if [ -d "$HOME/perl5" ]; then
    PERL5LIB="$HOME/perl5/lib/perl5${PERL5LIB:+:${PERL5LIB}}" ; export PERL5LIB;
    PERL_LOCAL_LIB_ROOT="$HOME/perl5${PERL_LOCAL_LIB_ROOT:+:${PERL_LOCAL_LIB_ROOT}}" ; export PERL_LOCAL_LIB_ROOT;
    PERL_MB_OPT="--install_base \"$HOME/perl5\"" ; export PERL_MB_OPT;
    PERL_MM_OPT="INSTALL_BASE=$HOME/perl5" ; export PERL_MM_OPT;
fi
