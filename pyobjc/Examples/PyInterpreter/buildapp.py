from bundlebuilder import buildapp

buildapp(
	mainprogram = "PyInterpreter.py",
	resources = ["PyInterpreter.nib"],
	nibname = "PyInterpreter",
    includePackages = ['encodings'],
)
