from distutils.core import setup
import py2app

setup(
    app = ["DotView.py"],
    data_files = ["English.lproj"],
)
