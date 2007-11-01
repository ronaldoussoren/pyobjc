import sys

def check(cmd, mf):
    """
    In python2.5 modules in the email package were renamed to be
    PEP8 compliant. The older names still work through some backward
    compatibility code. Modulefinder doesn't deal with that code
    directory, therefore include all of email for now.
    """
    if sys.version_info[:2] < (2, 5):
        return None

    m = mf.findNode('email')
    if m is None or m.filename is None:
        return None
    return dict(
        packages = ['email'],
    )
