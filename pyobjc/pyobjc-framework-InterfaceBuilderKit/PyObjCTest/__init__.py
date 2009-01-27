""" Unittests """
import os

if 'DYLD_FRAMEWORK_PATH' not in os.environ or \
    '/Developer/Library/PrivateFrameworks/' not in os.environ['DYLD_FRAMEWORK_PATH']: 
        # Check for:
        # DYLD_FRAMEWORK_PATH='/Developer/Library/PrivateFrameworks/'

        raise ImportError("Please define DYLD_FRAMEWORK_PATH, otherwise the tests will fail")
