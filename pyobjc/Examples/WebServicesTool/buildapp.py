from bundlebuilder import buildapp

buildapp(
	name = "Web Services Tool",
	mainprogram = "Main.py",
	resources = ["English.lproj", "Preferences.png", "Reload.png", "WST.png"],
	nibname = "MainMenu",
	iconfile = "WST.icns",
)
