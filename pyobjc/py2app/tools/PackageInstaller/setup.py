from distutils.core import setup
import py2app

setup(
    app = ["PackageInstaller.py"],
    options = dict(py2app=dict(
        excludes=['py2app', 'bdist_mpkg'],
        argv_emulation=True,
        semi_standalone=True,
        site_packages=True,
    ))
)
