from bundlebuilder import buildapp

buildapp(
	mainprogram = "PythonBrowser.py",
	resources = ["MainMenu.nib", "PythonBrowser.nib", "PythonBrowserModel.py"],
	nibname = "MainMenu",
)
