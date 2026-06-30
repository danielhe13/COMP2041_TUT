#!/bin/dash

case $# in
    0)
        echo "Usage: $0 <file> [<file> ...]" >&2
        exit 1
    ;;
esac

for archive in "$@"; do
    if [ ! -f "$archive" ]; then
        echo "$0: Error: '$archive' is not a file" >&2
        exit 1
    fi

    case "$archive" in
        *.tar.bz2)      tar xjf     "$archive" ;;
        *.tar.gz )      tar xzf     "$archive" ;;
        *.tar.xz )      tar xJf     "$archive" ;;
        *.bz2    )      bunzip2     "$archive" ;;
        *.rar    )      rar x       "$archive" ;;   
        *.gz     )      gunzip      "$archive" ;;   
        *.tar    )      tar xf      "$archive" ;;   
        *.tbz2   )      tar xjf     "$archive" ;;   
        *.tgz    )      tar xzf     "$archive" ;;   
        *.zip    )      unzip       "$archive" ;;   
        *.jar    )      unzip       "$archive" ;;   
        *.Z      )      uncompress  "$archive" ;;
        *.7z     )      7z x        "$archive" ;;
        *)
            echo "$0: Error: '$archive' cannot be extracted" >&2
            exit 1
        ;;
    esac
done
