import build_libffi
import build_html
import di_build_ext
import di_sdist
import di_test
import di_install
try:
    import pyobjc_mpkg
except ImportError:
    pass
try:
    import bdist_dmg
except ImportError:
    pass

extra_cmdclass = {}
for v in globals().values():
    extra_cmdclass.update(getattr(v, 'cmdclass', {}))
