from distutils.core import setup
import py2app

plist = dict(
    NSPrincipalClass='ProgressViewPalette',
)

setup(
    plugin = ['ProgressViewPalette.py'],
    data_files = ['English.lproj', 'palette.table'],
    options = dict(py2app=dict(
        extension='.palette',
        plist=plist,
    )),
)
