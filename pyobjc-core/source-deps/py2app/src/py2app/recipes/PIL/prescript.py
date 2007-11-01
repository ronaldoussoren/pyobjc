def _recipes_pil_prescript(plugins):
    import Image
    import sys
    def init():
        if Image._initialized >= 2:
            return
        for plugin in plugins:
            try:
                __import__(plugin, globals(), locals(), [])
            except ImportError:
                if Image.DEBUG:
                    print 'Image: failed to import'
                    print f, ':', sys.exc_info()[1]
        if Image.OPEN or Image.SAVE:
            Image._initialized = 2
    Image.init = init
