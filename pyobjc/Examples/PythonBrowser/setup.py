from distutils.core import setup
import py2app

setup(
    app = ["PythonBrowser.py"],
    data_files = ["MainMenu.nib", "PythonBrowser.nib"],
)
