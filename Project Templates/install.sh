#!/bin/sh

TARGET=$1/Developer/ProjectBuilder\ Extras/Project\ Templates/Application

mkdir -p "$TARGET"

gnutar -c -f - -v -p --exclude=CVS Cocoa-Python\ Application | \
    ( cd "$TARGET" ; gnutar xfvp - )
