from distutils.core import setup
import py2app

setup(
    plugin = ["InjectInterpreterPlugin.py"],
)
