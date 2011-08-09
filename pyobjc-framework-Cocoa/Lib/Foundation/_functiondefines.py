"""
Port of "function defines".
"""
from Foundation import NSBundle, NSProcessInfo

def NSLocalizedString(key, comment):
    return NSBundle.mainBundle().localizedStringForKey_value_table_(key, '', None)

def NSLocalizedStringFromTable(key, tbl, comment):
    return NSBundle.mainBundle().localizedStringForKey_value_table_(key, '', tbl)

def NSLocalizedStringFromTableInBundle(key, tbl, bundle, comment):
    return bundle.localizedStringForKey_value_table_(key, '', tbl)

def NSLocalizedStringWithDefaultValue(key, tbl, bundle, val, comment):
    return bundle.localizedStringForKey_value_table_(key, val, tbl)


def MIN(a, b):
    if a < b:
        return a
    else:
        return b

def MAX(a, b):
    if a < b:
        return b
    else:
        return a

ABS = abs

class _OC_DisabledSuddenTermination (object):
    """
    Helper class to implement NSDisabledSuddenTermination

    Usage::

        with NSDisabledSuddenTermination:
            pass

    Inside the with block sudden termination is disabled.

    This only has an effect on OSX 10.6 or later.
    """
    if hasattr(NSProcessInfo, 'disableSuddenTermination'):
        def __enter__(self):
            NSProcessInfo.processInfo().disableSuddenTermination()

        def __exit__(self, type, value, tb):
            NSProcessInfo.processInfo().enableSuddenTermination()

    else:
        def __enter__(self):
            pass

        def __exit__(self, type, value, tb):
            pass


NSDisabledSuddenTermination = _OC_DisabledSuddenTermination()

if hasattr(NSProcessInfo, 'disableSuddenTermination_'):
    class NSDisabledAutomaticTermination (object):
        """
        Helper class to implement NSDisabledAutomaticTermination

        Usage::

            with NSDisabledAutomaticTermination:
                pass

        Inside the with block sudden termination is disabled.

        This only has an effect on OSX 10.6 or later.
        """
        def __init__(self, reason):
            self._reason = reason

        def __enter__(self):
            NSProcessInfo.processInfo().disableAutomaticTermination_(self._reason)

        def __exit__(self, type, value, tb):
            NSProcessInfo.processInfo().enableAutomaticTermination_(self._reason)
