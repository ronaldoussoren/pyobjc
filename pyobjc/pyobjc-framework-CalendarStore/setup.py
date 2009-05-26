''' 
Wrappers for the "CalendarStore" on MacOSX 10.5 and later. The CalendarStore
frameworks provides access to the iCal data. It's possible to fetch iCal
records, such as calendars and tasks, as well as modify them and get 
notifications when records change in iCal.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup
try:
    from PyObjCMetaData.commands import extra_cmdclass, extra_options
except ImportError:
    extra_cmdclass = {}
    extra_options = lambda name: {}

setup(
    name='pyobjc-framework-CalendarStore',
    version='2.2b3',
    description = "Wrappers for the framework CalendarStore on Mac OS X",
    long_description = __doc__,
    author='Ronald Oussoren',
    author_email='pyobjc-dev@lists.sourceforge.net',
    url='http://pyobjc.sourceforge.net',
    platforms = [ "MacOS X" ],
    packages = [ "CalendarStore" ],
    package_dir = { '': 'Lib' },
    install_requires = [ 
        'pyobjc-core>=2.2b1',
        'pyobjc-framework-Cocoa>=2.2b1',
    ],
    package_data = { 
        '': ['*.bridgesupport'] 
    },
    test_suite='PyObjCTest',
    cmdclass = extra_cmdclass,
    options = extra_options('CalendarStore'),
    zip_safe = True,
)
