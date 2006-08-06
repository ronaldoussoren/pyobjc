import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, Extension

LONG_DESCRIPTION="""
Wrappers for the notify library on Mac OS X 10.3 or later. This library allows
processes to exchange stateless notification events.

Notifications are associated with names in a namespace shared by all
clients of the system.  Clients may post notifications for names, and
may monitor names for posted notifications.  Clients may request
notification delivery by a number of different methods.
"""

CLASSIFIERS = filter(None,
"""
Development Status :: 5 - Production/Stable
Environment :: Console
Environment :: MacOS X
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Natural Language :: English
Operating System :: MacOS :: MacOS X
Programming Language :: Python
Topic :: Software Development :: Libraries :: Python Modules
""".splitlines())


def grep_version():
    fp = open("Lib/notify/__init__.py", "r")
    for ln in fp:
        if ln.startswith("__version__"):
            return ln.split('=')[-1].strip()[1:-1]


setup(
    name="macosx-notify",
    version=grep_version(),
    description="Wrapper for the notify library in MacOSX 10.3 or later",
    long_description=LONG_DESCRIPTION,
    author="Ronald Oussoren",
    author_email="ronaldoussoren@mac.com",
    # url=
    platforms=[ "MacOS X" ],
    ext_modules=[
        Extension("notify._notify", [ 'Modules/_notify.c']),
    ],
    packages = ['notify'],
    package_dir = { '': 'Lib' },
    classifiers = CLASSIFIERS,
    license = "MIT License",
    # download_url=
)



