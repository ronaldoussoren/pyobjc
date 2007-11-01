class _ArgvCollector:
    """argvemulator - create sys.argv from an 'aevtodoc' Apple event.
    Used by applets that want unix-style arguments.
    """
    
    def __init__(self):
        import sys
        import Carbon.AppleEvents as k
        from Carbon import AE
        
        # Remove the funny -psn_xxx_xxx argument
        if len(sys.argv) > 1 and sys.argv[1].startswith('-psn'):
            del sys.argv[1]
        AE.AEInstallEventHandler(k.kCoreEventClass, k.kAEOpenApplication,
            self.__runapp)
        AE.AEInstallEventHandler(k.kCoreEventClass, k.kAEOpenDocuments,
            self.__openfiles)
    
    def __runapp(self, requestevent, replyevent):
        self._quit()
    
    def __openfiles(self, requestevent, replyevent):
        import sys
        import Carbon.AppleEvents as k
        from Carbon import File

        try:
            listdesc = requestevent.AEGetParamDesc(k.keyDirectObject,
                k.typeAEList)
            for i in range(listdesc.AECountItems()):
                aliasdesc = listdesc.AEGetNthDesc(i + 1, k.typeAlias)[1]
                alias = File.Alias(rawdata=aliasdesc.data)
                fsref = alias.FSResolveAlias(None)[0]
                pathname = fsref.as_pathname()
                sys.argv.append(pathname)
        except Exception, e:
            print "argvemulator.py warning: can't unpack an open documents event:"
            import traceback
            traceback.print_exc()
        self._quit()
    
    def mainloop(self, *args, **kargs):
        from Carbon import CarbonEvt
        CarbonEvt.RunApplicationEventLoop()
    
    def _quit(self):
        from Carbon import CarbonEvt
        CarbonEvt.QuitApplicationEventLoop()


def _argv_emulation():
    import sys
    # only use if started by LaunchServices
    for arg in sys.argv[1:]:
        if arg.startswith('-psn'):
            _ArgvCollector().mainloop()
            break
_argv_emulation()
