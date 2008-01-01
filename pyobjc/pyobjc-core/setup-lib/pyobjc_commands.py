import build_html
import di_sdist
import di_test
try:
    import pyobjc_mpkg
    import bdist_dmg
except ImportError:
    pass

extra_options = {}
extra_cmdclass = {}
for v in globals().values():
    extra_cmdclass.update(getattr(v, 'cmdclass', {}))
    extra_options.update(getattr(v, 'options', {}))
