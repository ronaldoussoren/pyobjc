#!/bin/sh
set -x
PP=/Library/Frameworks/Python.framework/Versions/Current
pythonw ${PP}/Mac/scripts/BuildApplet.py -r -o TodoPY --extra English.lproj/MainMenu.nib main.py

CpMac -r English.lproj TodoPY.app/Contents/Resources
cp *.py TodoPY.app/Contents/Resources
cp Images/*.tiff TodoPY.app/Contents/Resources

cp Images/LeftArrow.tiff  TodoPY.app/Contents/Resources/DoneMark.tiff
cp Images/RightArrow.tiff  TodoPY.app/Contents/Resources/DeferredMark.tiff
cp Images/*.tiff TodoPY.app/Contents/Resources
cp Icons/*.icns TodoPY.app/Contents/Resources
cp Info.plist TodoPY.app/Contents
