
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSMovie (TestCase):

    @onlyOn32Bit
    def testMethods(self):
        self.fail("- (id) initWithMovie:(void* /*Movie*/)movie; ")
        self.fail("- (void*/*Movie*/)QTMovie;")

if __name__ == "__main__":
    main()
