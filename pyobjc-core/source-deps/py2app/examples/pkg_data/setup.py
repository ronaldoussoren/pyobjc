from distutils.core import setup
import py2app

setup(
    app=['use_testpkg.py'],
    options=dict(py2app=dict(
        includes=['testpkg.*'],
        packages=['testpkg'],
    )),
)
