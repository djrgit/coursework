" General configuration options:
set nocompatible			" Use Vim settings, rather than Vi settings.
set history=10000			" Set history of executed commands.
set showcmd					" Show incomplete commands at the bottom.
set showmode				" Show current mode at the bottom.

" User interface options:
set laststatus=2			" Always display the status bar.
set ruler					" Always show cursor position.
set wildmenu				" Display command line's tab complete options as a menu.
colorscheme desert			" Change color scheme.
set cursorline				" Highlight the line currently under cursor.
set number					" Show line numbers on the sidebar.
set relativenumber			" Show line number on the current line and relative numbers on all other lines.
set title					" Set the window's title, reflecting the file currently being edited.

" Indentation options:
set autoindent				" New lines inherit the indentation of previous lines.
filetype plugin indent on	" Smart auto indentation (instead of old smartindent option).	
set tabstop=4				" Show existing tab with 4 spaces width.
set shiftwidth=2			" When indenting with '>', use 2 spaces width.
set expandtab				" On pressing tab, insert 4 spaces.

" Search options:
set incsearch				" Find the next match as we type the search.
set hlsearch				" Highlight searches by default.
set ignorecase				" Ignore case when searching ...
set smartcase				" ... unless you type a capital.

" Text rendering options:
set encoding=utf-8			" Use an encoding that supports Unicode.
set linebreak				" Wrap lines at convenient points, avoid wrapping a line in the middle of a word.
set scrolloff=3				" The number of screen lines to keep above and below the cursor.
set sidescrolloff=5			" The number of screen columns to keep to the left and right of the cursor.
syntax enable				" Enable syntax highlighting

" Miscellaneous options:
set confirm					" Display a confirmation dialog when closing an unsaved file.
set shell					" The shell used to execute commands.
set spell					" Enable spell checking (English language default).

" Status line:
set statusline=%t			" tail of the filename
set statusline+=%{&ff}		" file format
set statusline+=%h			" help file flag
set statusline+=%m			" modified flag
set statusline+=%r			" read only flag
set statusline+=%y			" filetype
set statusline+=%c,			" cursor column
set statusline+=%l/%L		" cursor line/total lines
set statusline+=\ %P		" percent through file

" Swap files organization:
set directory=$HOME/.vim/swp//


filetype indent on			" Enable indenting for files
set nobackup				" Disable backup files
