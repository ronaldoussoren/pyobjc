from distutils.core import setup, Extension
import py2app

# Plugin
setup(
    ext_modules = [
        Extension('NSURLRequest_IDNSnitch', ['NSURLRequest_IDNSnitch.m'],
            extra_link_args=['-framework', 'Foundation']),
    ],
    plugin = ["IDNSnitchPlugin.py"],
)

setup(
    app = ["IDNSnitch.py"],
    data_files = ["dist/IDNSnitchPlugin.plugin", "English.lproj"],
)
