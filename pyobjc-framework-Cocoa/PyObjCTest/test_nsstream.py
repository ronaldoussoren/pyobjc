import unittest
import objc

import Foundation

class TestNSStreamUsage(unittest.TestCase):

    def testUsage(self):
        # Test the usage of methods that require extra work

        if not hasattr(Foundation, 'NSStream'):
            return

        # Try to create a connection to the IPP port on the local host
        inputStream, outputStream = Foundation.NSStream.getStreamsToHost_port_inputStream_outputStream_(
                Foundation.NSHost.hostWithAddress_(u"127.0.0.1"), 
                631, # IPP port
                None,
                None
        )

        self.assert_(isinstance(inputStream, Foundation.NSInputStream))
        self.assert_(isinstance(outputStream, Foundation.NSOutputStream))

        inputStream.close()
        outputStream.close()

if __name__ == '__main__':
    unittest.main( )
