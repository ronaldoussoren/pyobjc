#!/usr/bin/env python
"""
This script using NSNetServiceBrowser to look for local HTTP servers.
"""

import objc
from Foundation import NSDate, NSNetServiceBrowser, NSObject, NSRunLoop

objc.setVerbose(1)


class PrintingResolverDelegate(NSObject):
    def netServiceDidResolveAddress_(self, service):
        addresses = service.addresses()
        if len(addresses) == 0:
            return
        print(f"{service.name()}.{service.domain()}")
        for address in service.addresses():
            print(f"   {address}")
        print("")
        service.setDelegate_(None)

    def netService_didNotResolve_(self, service, didNotResolve):
        print("didNotResolve", didNotResolve)
        service.setDelegate_(None)


class PrintingBrowserDelegate(NSObject):
    def startLookup(self):
        self.delegates = []
        for aNetService in self.services:
            prd = PrintingResolverDelegate.new()
            aNetService.setDelegate_(prd)
            aNetService.resolve()
            self.delegates.append(prd)

    def netServiceBrowserWillSearch_(self, browser):
        print("Browsing for advertised services...")
        self.services = []

    def netServiceBrowserDidStopSearch_(self, browser):
        print("Browse complete")
        self.startLookup()

    def netServiceBrowser_didNotSearch_(self, browser, errorDict):
        print("Could not search.")

    def netServiceBrowser_didFindService_moreComing_(
        self, browser, aNetService, moreComing
    ):
        print(f"Found a service: {aNetService.name()} {aNetService.domain()}")
        self.services.append(aNetService)
        if not moreComing:
            browser.stop()

    def netServiceBrowser_didRemoveService_moreComing_(
        self, browser, aNetService, moreComing
    ):
        print(f"Service removed: {aNetService.name()}")
        if not moreComing:
            browser.stop()


def findDomains(serviceName, seconds=5.0):
    runloop = NSRunLoop.currentRunLoop()
    browser = NSNetServiceBrowser.new()
    pbd = PrintingBrowserDelegate.new()
    browser.setDelegate_(pbd)
    browser.searchForServicesOfType_inDomain_(serviceName, "")
    untilWhen = NSDate.dateWithTimeIntervalSinceNow_(seconds)
    runloop.runUntilDate_(untilWhen)


if __name__ == "__main__":
    # Use '_afpovertcp' instead of '_http' to look for fileservers.
    findDomains("_afpovertcp._tcp")
