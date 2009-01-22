#!/usr/bin/python

from ScriptingBridge import *

iTunes = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")

print iTunes.currentTrack().name()
