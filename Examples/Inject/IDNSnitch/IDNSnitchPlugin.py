from Foundation import *
from AppKit import *
import sys
import encodings.idna
import objc

import NSURLRequest_IDNSnitch
IDNSnitchBase = objc.lookUpClass('IDNSnitchBase')

HOSTS = {}

MESSAGE = u"""An URL using an IDN host has been detected.  URLs of this type may be misleading as there are many characters that look the same.

Display Host
  %s

Unicode Host
  %s

URL
  %s"""

class IDNSnitch(IDNSnitchBase):
    def checkURL_(cls, anURL):
        if anURL is None:
            return anURL
        host = anURL.host()
        if host is None:
            return anURL
        if encodings.idna.uace_prefix in host:
            uni = u'.'.join([encodings.idna.ToUnicode(part) for part in host.split(u'.')])
            shouldDeny = HOSTS.get(uni)
            if shouldDeny is None:
                res = NSRunAlertPanel(
                    u'IDN URL Detected',
                    MESSAGE % (uni, uni.encode('unicode_escape'), anURL),
                    u'Allow',
                    u'Deny',
                    None)
                shouldDeny = (res != NSAlertDefaultReturn)
                HOSTS[uni] = shouldDeny
            if shouldDeny:
                return NSURL.URLWithString_(u'about:blank')
        return anURL

      
IDNSnitch.startIDNSnitch_(None)
