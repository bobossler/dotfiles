"
"    ____        __
"   / __ )____  / /_
"  / __  / __ \/ __ \
" / /_/ / /_/ / /_/ /
"/_____/\____/_.___/
"

""""""""""""""""""""""""""""""""""""""""""""""""
"  Using vim-plugged for managing plugins      "
""""""""""""""""""""""""""""""""""""""""""""""""

set nocompatible                        " use all vim features
filetype off                            " required for some plugins ???

call plug#begin('~/.vim/plugged')       " call plugin manager; plugins start below

Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'morhetz/gruvbox'
Plug 'airblade/vim-gitgutter'
Plug 'tpope/vim-fugitive'
Plug 'tpope/vim-commentary'
Plug 'tpope/vim-surround'
Plug 'preservim/nerdtree'
Plug 'Xuyuanp/nerdtree-git-plugin'
" Plugins for writing
Plug 'junegunn/goyo.vim'
Plug 'dhruvasagar/vim-table-mode'
Plug 'robertbasic/vim-hugo-helper'
Plug 'reedes/vim-pencil'
Plug 'xuhdev/vim-latex-live-preview', { 'for': 'tex' } " live preview for LaTeX
Plug 'tmsvg/pear-tree'
Plug 'ap/vim-css-color'
Plug 'rust-lang/rust.vim'
" Plugins for terminal usage
Plug 'voldikss/vim-floaterm'
" Unused Plugins (for the moment)
"    Color schemes
" Plug 'kristijanhusak/vim-hybrid-material'
" Plug 'NLKNguyen/papercolor-theme'
" Plug 'ajh17/Spacegray.vim'
"    Writing
" Plug 'vimwiki/vimwiki'
" Plug 'tools-life/taskwiki'
" Plug 'godlygeek/tabular'
" Plug 'plasticboy/vim-markdown'
"    Formatting
" Plug 'alvan/vim-closetag'
" Plug 'jiangmiao/auto-pairs'

call plug#end()                         " end pligin section; all plugins are above

filetype plugin indent on               " required

""""""""""""""""""""""""""""""""""""""""""""""""
"  Airline settings                            "
""""""""""""""""""""""""""""""""""""""""""""""""
"let g:airline_theme='<theme>'
let g:airline_powerline_fonts = 1

""""""""""""""""""""""""""""""""""""""""""""""""
"  Hugo Helper settings                        "
""""""""""""""""""""""""""""""""""""""""""""""""
let g:hugohelper_spell_check_lang = 'en_us'

""""""""""""""""""""""""""""""""""""""""""""""""
"  Set pdf previewer                           "
""""""""""""""""""""""""""""""""""""""""""""""""
let g:livepreview_previewer = 'zathura'

""""""""""""""""""""""""""""""""""""""""""""""""
"  NERDTree settings                           "
""""""""""""""""""""""""""""""""""""""""""""""""
let g:NERDTreeWinSize = 40
let NERDTreeNaturalSort = 1
let NERDTreeRespectWildIgnore = 1
let NERDTreeMinimalUI = 1

"""""""""""""""""""""""""""""""""""""""""""""""
"  VimWiki settings                           "
"""""""""""""""""""""""""""""""""""""""""""""""
" let g:vimwiki_list = [{'path': '~/vimwiki/', 'syntax': 'markdown', 'ext': '.md'}]
" let g:vimwiki_ext2syntax = {'md': 'markdown', '.markdown': 'markdown', '.mdown': 'markdown'}
" Makes vimwiki markdown links as [text](text.md) instead of [text](text)
" let g:vimwiki_markdown_link_ext = 1

"""""""""""""""""""""""""""""""""""""""""""""""
"  TaskWiki settings                          "
"""""""""""""""""""""""""""""""""""""""""""""""
" let g:taskwiki_markup_syntax = 'markdown'
" let g:markdown_folding = 1

"""""""""""""""""""""""""""""""""""""""""""""""
"  Floaterm settings                          "
"""""""""""""""""""""""""""""""""""""""""""""""
let g:floaterm_keymap_toggle = '<F10>'
let g:floaterm_keymap_kill = '<Leader>fk'

syntax enable

set encoding=utf-8
set noerrorbells
set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab
set smartindent
set nu rnu
set nowrap
set smartcase
set noswapfile
set nobackup
set undodir=~/.vim/undodir
set undofile
set incsearch
set scrolloff=8
set splitbelow splitright
set autoread
set wildmenu
set nohlsearch
set spelllang=en_us
set termguicolors
" set spell
" set confirm

" Enable Folding
set foldmethod=indent
set foldlevel=99

" Give more space for displaying messages.
set cmdheight=2
set signcolumn=yes
set colorcolumn=80
highlight colorcolumn ctermbg=0 guibg=lightgrey

if exists('+termguicolors')
    let &t_8f="\<Esc>[38;2;%lu;%lu;%lum"
    let &t_8b="\<Esc>[48;2;%lu;%lu;%lum"
endif

" Color Scheme
colorscheme gruvbox
set background=dark

" Set .rasi filetype
au BufNewFile,BufRead /*.rasi setf css

" Trim white space
fun! TrimWhiteSpace()
    let l:save = winsaveview()
    keeppatterns %s/\s\+$//e
    call winrestview(l:save)
endfun

" Flag Unneccessary Whitespace
highlight BadWhitespace ctermbg=9 guibg=red
augroup badwhitespace
    au!
    au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/
augroup end

" Remove Whitespace
augroup RemoveWSP
    autocmd!
    autocmd BufWritePre *.py,*.pyw,*.c,*.h :call TrimWhiteSpace()
augroup end

" Special Indents
augroup pyindents
    au!
    au BufNewFile,BufRead *.py set ts=4 sts=4 sw=4
        \ textwidth=79
        \ expandtab
        \ autoindent
        \ fileformat=unix
augroup end

augroup webindents
    au!
    au BufNewFile,BufRead *.js,*.html,*.css set ts=2 sts=2 sw=2
augroup end

" Set line number mode based on vim mode
augroup numbertoggle
  autocmd!
  autocmd BufEnter,FocusGained,InsertLeave * set relativenumber
  autocmd BufLeave,FocusLost,InsertEnter * set norelativenumber
augroup end

" Keyboard mapping
imap <F5> <ESC>:w<CR>:! clear; python3 %<CR>
nmap <F5> <ESC>:w<CR>:! clear; python3 %<CR>
nmap <Leader>ft :FloatermNew --name=python --wintype=vsplit python3<CR>
vmap <F9> :FloatermSend --name=python<CR><F10>
