"""
Port of "function defines".
"""
from Foundation import NSBundle

def NSLocalizedString(key, comment):
    return NSBundle.mainBundle().localizedStringForKey_value_table_(key, '', None)

def NSLocalizedStringFromTable(key, tbl, comment):
    return NSBundle.mainBundle().localizedStringForKey_value_table_(key, '', tbl)

def NSLocalizedStringFromTableInBundle(key, tbl, bundle, comment):
    return bundle.localizedStringForKey_value_table_(key, '', tbl)

def NSLocalizedStringWithDefaultValue(key, tbl, bundle, val, comment):
    return bundle.localizedStringForKey_value_table_(key, val, tbl)
