#!/usr/bin/env python

#
# Copyright 2002 CodeFab, Inc.  -- bbum@codefab.com
#
# All Rights Reserved.
#
# Consider this under the MIT license.  Full text
# easily obtained via Google.
#

import sys
import xmlrpclib
import pprint
import types
import string

def usage(msg, exitCode=1):
    if msg:
        sys.stderr.write('\nerror: %s\n\n' % msg)
    sys.stderr.write('''usage: dump-methods.py http://host/path/to/xml-rpc/interface [prefix]

    examples:

    dump-methods.py http://localhost:5335/RPC2
    
    dump-methods.py http://www.oreillynet.com/meerkat/xml-rpc/server.php system
    
''')
    sys.exit(exitCode)

def main():
    if not ( (len(sys.argv) == 2) or (len(sys.argv) == 3) ):
        usage('''Need 1 or 2 arguments.''')

    if len(sys.argv) == 3:
        prefix = sys.argv[2]
        if len(prefix):
            if prefix[-1:] != ".":
                prefix = "%s." % prefix
    else:
        prefix = ""

    listMethodsMethodName = prefix + "listMethods"
    methodSignatureMethodName = prefix + "methodSignature"
    methodHelpMethodName = prefix + "methodHelp"
         
    server = xmlrpclib.ServerProxy(sys.argv[1])

    print "Checking server capabilities via method '%s' on server %s...." % (listMethodsMethodName, sys.argv[1])
    try:
        methodList = getattr(server, listMethodsMethodName)()
    except xmlrpclib.Fault, reason:
        usage('''An XML-RPC fault occurred.  The fault is as follows:

        %s
        
        Ensure that the URL to the RPC handler is correct.
        If it is, it is likely that the server does not
        implement the listMethods() command.''' % reason)

    if not (len(methodList) > 0):
        usage('''listMethods returned nothing.  No methods available or server problem?''')

    hasMethodSignature = 1
    try:
        getattr(server, methodSignatureMethodName)(methodList[0])
    except:
        hasMethodSignature = 0
        print """WARNING: It appears that the server does not implement methodSignature().
It is also possible that listMethods() did not return an array of just the method names as it should have."""
        print

    hasMethodHelp = 1
    try:
        getattr(server, methodHelpMethodName)(methodList[0])
    except:
        hasMethodHelp = 0
        print """WARNING: It appears that the server does not implement methodHelp().
It is also possible that listMethods() did not return an array of just the method names as it should have."""
        print

    if (not hasMethodHelp) and (not hasMethodSignature):
        print """It appears that the server does not implement either methodHelp() or methodSignature().
It is also possible that listMethods() did not return an array of just the method names as it should have.

In any case, the script is punting on trying to retrieve method descriptions in the recommended fashion and
will simply dump whatever was returned by listMethods() in its raw form."""
        print

        print "Dumping raw for %d methods." % len(methodList)
        pprint.pprint(methodList)
    else:
        print "Dumping information for %d methods." % len(methodList)
        for aMethod in methodList:
            print "---------------------"
            print "Method: %s" % aMethod
            if hasMethodSignature:
                try:
                    print "Signature:"
                    signature = getattr(server, methodSignatureMethodName)(aMethod)
                    if type(signature) == types.ListType:
                        count = 0
                        for aSignature in signature:
                            if (type(aSignature) == types.ListType) and (len(aSignature) > 0):
                                print "\t%s %s(%s)" % (aSignature[0], aMethod, string.join(aSignature[1:], ", "))
                            else:
                                print "\t%s" % (aSignature)
                            count = count + 1
                    else:
                        pprint.pprint(signature)
                    print
                except xmlrpclib.Fault, reason:
                    print "Fault while trying to retrieve signature for '%s' (%s)" % (aMethod, reason)

            if hasMethodHelp:
                try:
                    print "Help:\n\n%s" % getattr(server, methodHelpMethodName)(aMethod)
                except xmlrpclib.Fault, reason:
                    print "Fault while trying to retrieve help for '%s' (%s)" % (aMethod, reason)
            print

    sys.exit(0)
    
if __name__ == "__main__":
    main()
