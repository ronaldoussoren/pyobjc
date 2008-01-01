from distutils.core import setup
import py2app

setup(
    app = ['../python/myapp.py'],
    data_files = ['../data']
)
