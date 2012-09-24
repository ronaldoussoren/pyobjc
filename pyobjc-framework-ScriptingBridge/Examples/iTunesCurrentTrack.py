#!/usr/bin/python

from ScriptingBridge import SBApplication

iTunes = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")

print iTunes.currentTrack().name()
