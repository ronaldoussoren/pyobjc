from distutils.core import setup, Extension
import py2app

# Plugin
setup(
    plugin = ["IDNSnitchPlugin.py"],
)

setup(
    app = ["IDNSnitch.py"],
    data_files = ["dist/IDNSnitchPlugin.plugin", "English.lproj"],
)
