# ~/.profile: executed by the command interpreter for login shells.
# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login exists.

# the default umask is set in /etc/profile; for setting the umask
# for ssh logins, install and configure the libpam-umask package.
#umask 022

# Helper functions for safe, deduplicated PATH manipulation
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

# Default editor and pager environment
export EDITOR='fresh'
export VISUAL='fresh'
export FILE='ranger'
export PAGER='less'
export MANPAGER='most'
export VIEWER='zathura'

# Go environment
export GOPATH="${GOPATH:-$HOME/go}"

# Construct clean $PATH in priority order (last prepended = highest priority)
path_prepend "/usr/local/go/bin"
path_prepend "$GOPATH/bin"
path_prepend "$HOME/.emacs.d/bin"
path_prepend "$HOME/.spicetify"
path_prepend "$HOME/perl5/bin"
path_prepend "$HOME/.cargo/bin"
path_prepend "$HOME/bin"
path_prepend "$HOME/.local/bin"
export PATH

# Perl5 environment
if [ -d "$HOME/perl5" ]; then
    PERL5LIB="$HOME/perl5/lib/perl5${PERL5LIB:+:${PERL5LIB}}" ; export PERL5LIB;
    PERL_LOCAL_LIB_ROOT="$HOME/perl5${PERL_LOCAL_LIB_ROOT:+:${PERL_LOCAL_LIB_ROOT}}" ; export PERL_LOCAL_LIB_ROOT;
    PERL_MB_OPT="--install_base \"$HOME/perl5\"" ; export PERL_MB_OPT;
    PERL_MM_OPT="INSTALL_BASE=$HOME/perl5" ; export PERL_MM_OPT;
fi

# If running bash, include .bashrc if it exists
if [ -n "$BASH_VERSION" ] && [ -f "$HOME/.bashrc" ]; then
    . "$HOME/.bashrc"
fi
