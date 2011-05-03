from Foundation import *
import objc
from pydochelper import gethtmldoc

PYDOCSCHEME = u'pydoc'

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
        modpath = urlpath.replace(u'/', u'.'
            ).lstrip(u'.'
            ).replace(u'.html', u'')

        try:
            data = gethtmldoc(modpath.encode('utf-8'))
        except Exception, e:
            client.URLProtocol_didFailWithError_(
                self,
                NSError.errorWithDomain_code_userInfo_(
                    NSURLErrorDomain,
                    NSURLErrorResourceUnavailable,
                    None,
                ),
            )
        else:
            response = NSURLResponse.alloc().initWithURL_MIMEType_expectedContentLength_textEncodingName_(
                request.URL(),
                u'text/html',
                len(data),
                u'utf-8',
            )
            client.URLProtocol_didReceiveResponse_cacheStoragePolicy_(
                self,
                response,
                NSURLCacheStorageNotAllowed,
            )
            client.URLProtocol_didLoadData_(
                self,
                buffer(data),
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
        args = ('dict',)
    setup()
    for arg in args:
        url = NSURL.URLWithString_(u'pydoc:///%s' % (arg,))
        print NSString.stringWithContentsOfURL_(url)
    teardown()

import sys
if __name__ == '__main__': main(*sys.argv[1:])
