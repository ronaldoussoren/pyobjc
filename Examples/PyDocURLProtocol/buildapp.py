from bundlebuilder import buildapp

buildapp(
        mainprogram = "PyDocBrowser.py",
        resources = ["PyDocBrowser.nib", 
                     "PyDocURLProtocol.py", "pydochelper.py"],
        nibname = "PyDocBrowser",
)
