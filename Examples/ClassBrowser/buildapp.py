from bundlebuilder import buildapp

buildapp(
        mainprogram = "ClassBrowser.py",
        resources = ["ClassBrowser.nib"],
        nibname = "ClassBrowser",
)
