def _argv_emulation():
    import sys
    # only use if started by LaunchServices
    for arg in sys.argv[1:]:
        if arg.startswith('-psn'):
            import argvemulator
            argvemulator.ArgvCollector().mainloop()
            break
_argv_emulation()
