from bundlebuilder import buildapp

buildapp(
	name = "DotView",
	mainprogram = "DotView.py",
	resources = ["English.lproj"],
	nibname = "MainMenu",
)
