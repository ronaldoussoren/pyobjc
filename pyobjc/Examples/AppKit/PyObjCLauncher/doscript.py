import os

def doscript(cmd):
    OSASCRIPT = '/usr/bin/osascript'
    # not ideal, of course
    scriptcmd = [OSASCRIPT,
        '-e', 'tell application "Terminal"',
        '-e', 'run',
        '-e', 'do script "%s"' % cmd.replace('\\', '\\\\').replace('"', '\\"'),
        '-e', 'end tell']
    return os.spawnv(os.P_WAIT, scriptcmd[0], scriptcmd)
