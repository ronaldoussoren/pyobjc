import di_test

extra_options = {}
extra_cmdclass = {}
for v in globals().values():
    extra_cmdclass.update(getattr(v, 'cmdclass', {}))
    extra_options.update(getattr(v, 'options', {}))
