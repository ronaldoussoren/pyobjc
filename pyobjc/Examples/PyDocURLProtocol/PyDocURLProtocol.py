from Foundation import *
import objc
from pydochelper import gethtmldoc

PYDOCSCHEME = u'pydoc'

class PyDocURLProtocol(NSURLProtocol):

    def canInitWithRequest_(klass, request):
        print "canInitWithRequest_"
        if request.URL().scheme() == PYDOCSCHEME:
            return True
        return False
        
    canInitWithRequest_ = objc.selector(
        canInitWithRequest_,
        signature=NSURLProtocol.canInitWithRequest_.signature,
        isClassMethod=True,
    )

    def canonicalRequestForRequest_(klass, request):
        print "canonical", request.URL().standardizedURL().path()
        return request
        
    canonicalRequestForRequest_= objc.selector(
        canonicalRequestForRequest_,
        signature=NSURLProtocol.canonicalRequestForRequest_.signature,
        isClassMethod=True,
    )

    def startLoading(self):
        print "start"
        client = self.client()
        request = self.request()
        urlpath = request.URL().standardizedURL().path()
        print 'urlpath', urlpath
        modpath = urlpath.replace(u'/', u'.'
            ).lstrip(u'.'
            ).replace(u'.html', u'')
            
        print 'modpath', modpath
        try:
            data = gethtmldoc(modpath.encode('utf-8'))
        except Exception, e:
            print repr(e), str(e)
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
                NSData.dataWithBytes_length_(data, len(data)),
            )
            client.URLProtocolDidFinishLoading_(self)

    def stopLoading(self):
        print "stop"

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
