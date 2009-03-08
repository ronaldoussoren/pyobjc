''' 
Wrappers for framework 'CoreText'. 

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, Extension
try:
    from PyObjCMetaData.commands import extra_cmdclass, extra_options
except ImportError:
    extra_cmdclass = {}
    extra_options = lambda name: {}

setup(
    name='pyobjc-framework-CoreText',
    version='2.2b1',
    description = "Wrappers for the framework CoreText on Mac OS X",
    long_description = __doc__,
    author='Ronald Oussoren',
    author_email='pyobjc-dev@lists.sourceforge.net',
    url='http://pyobjc.sourceforge.net',
    platforms = [ "MacOS X" ],
    packages = [ "CoreText" ],
    package_dir = { '': 'Lib' },
    ext_modules = [
            Extension('CoreText._manual',
                [ 'Modules/_manual.m' ],
                extra_link_args=['-framework', 'CoreServices']),
    ],
    setup_requires = [ 
    ],
    install_requires = [ 
        'pyobjc-core>=2.2b1',
        'pyobjc-framework-Cocoa>=2.2b1',
        'pyobjc-framework-Quartz>=2.2b1',
    ],
    dependency_links = [],
    package_data = { 
        '': ['*.bridgesupport'] 
    },
    test_suite='PyObjCTest',
    cmdclass = extra_cmdclass,
    options = extra_options('CoreText'),
    zip_safe = True,
)
