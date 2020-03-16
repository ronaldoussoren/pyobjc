import sys

from Cocoa import (
    NSURL,
    NSData,
    NSError,
    NSString,
    NSURLCacheStorageNotAllowed,
    NSURLErrorDomain,
    NSURLErrorResourceUnavailable,
    NSURLProtocol,
    NSURLResponse,
)
from pydochelper import gethtmldoc

PY3K = sys.version_info[0] == 3

PYDOCSCHEME = "pydoc"


class PyDocURLProtocol(NSURLProtocol):
    def canInitWithRequest_(klass, request):
        if request.URL().scheme() == PYDOCSCHEME:
            return True
        return False

    def canonicalRequestForRequest_(klass, request):
        return request

    def startLoading(self):
        client = self.client()
        request = self.request()
        urlpath = request.URL().standardizedURL().path()
        modpath = urlpath.replace("/", ".").lstrip(".").replace(".html", "")

        if not PY3K:
            modpath = modpath.encode("utf-8")

        try:
            data = gethtmldoc(modpath)
            if PY3K:
                data = data.encode("utf-8")
        except Exception:
            client.URLProtocol_didFailWithError_(
                self,
                NSError.errorWithDomain_code_userInfo_(
                    NSURLErrorDomain, NSURLErrorResourceUnavailable, None
                ),
            )
        else:
            response = NSURLResponse.alloc().initWithURL_MIMEType_expectedContentLength_textEncodingName_(  # noqa: B950
                request.URL(), "text/html", len(data), "utf-8"
            )
            client.URLProtocol_didReceiveResponse_cacheStoragePolicy_(
                self, response, NSURLCacheStorageNotAllowed
            )
            client.URLProtocol_didLoadData_(
                self, NSData.dataWithBytes_length_(data, len(data))
            )
            client.URLProtocolDidFinishLoading_(self)

    def stopLoading(self):
        pass


def setup():
    NSURLProtocol.registerClass_(PyDocURLProtocol)


def teardown():
    NSURLProtocol.unregisterClass_(PyDocURLProtocol)


def main(*args):
    if not args:
        args = ("dict",)

    setup()
    try:
        for arg in args:
            url = NSURL.URLWithString_("pydoc:///%s" % (arg,))
            print(NSString.stringWithContentsOfURL_(url))
    finally:
        teardown()


if __name__ == "__main__":
    main(*sys.argv[1:])
