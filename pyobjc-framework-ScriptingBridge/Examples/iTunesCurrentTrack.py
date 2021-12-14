#!/usr/bin/python

from ScriptingBridge import SBApplication

iTunes = SBApplication.applicationWithBundleIdentifier_("com.apple.Music")
print("currentTrack" in dir(iTunes))
print(iTunes.currentTrack)

print(iTunes.currentTrack().name())
