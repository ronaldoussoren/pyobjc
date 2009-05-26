''' 
Wrappers for the framework "LatentSemanticMapping" on MacOSX 10.5 or later.

The Latent Semantic Mapping framework supports the classification of text and other token-based content into developer-defined categories.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks.  

NOTE: Apple's documentation for this framework is very minimal at the moment,
making it very hard to actually use the framework.
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
    name='pyobjc-framework-LatentSemanticMapping',
    version='2.2b3',
    description = "Wrappers for the framework LatentSemanticMapping on Mac OS X",
    long_description = __doc__,
    author='Ronald Oussoren',
    author_email='pyobjc-dev@lists.sourceforge.net',
    url='http://pyobjc.sourceforge.net',
    platforms = [ "MacOS X" ],
    packages = [ "LatentSemanticMapping" ],
    package_dir = { '': 'Lib' },
    install_requires = [ 
        'pyobjc-core>=2.2b3',
        'pyobjc-framework-Cocoa>=2.2b3',
    ],
    package_data = { 
        '': ['*.bridgesupport'] 
    },
    test_suite='PyObjCTest',
    cmdclass = extra_cmdclass,
    options = extra_options('LatentSemanticMapping'),
    zip_safe = True,
)
