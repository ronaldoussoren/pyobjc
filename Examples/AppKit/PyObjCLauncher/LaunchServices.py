# Just enough LaunchServices to get what we want.
def _load(g=globals()):
    import objc
    from Foundation import NSBundle
    OSErr = objc._C_SHT
    def S(*args):
        return ''.join(args)

    FUNCTIONS = [
        (u'LSGetApplicationForInfo', 'sII@Io^{FSRef=[80C]}o^@'),
    ]

    bndl = NSBundle.bundleWithPath_(objc.pathForFramework('/System/Library/Frameworks/ApplicationServices.framework'))
    objc.loadBundleFunctions(bndl, g, FUNCTIONS)
globals().pop('_load')()

kLSUnknownType = 0
kLSUnknownCreator = 0
kLSRolesViewer = 2

if __name__ == '__main__':
    err, outRef, outURL = LSGetApplicationForInfo(kLSUnknownType, kLSUnknownCreator, u'txt', kLSRolesViewer)
    print err, outRef.as_pathname(), outURL
