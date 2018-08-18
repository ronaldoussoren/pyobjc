from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import Network

    class TestNWObject (TestCase):
        def test_functions(self):
            self.assertFalse(hasattr(Network, 'nw_retain'))
            self.assertFalse(hasattr(Network, 'nw_release'))

if __name__ == "__main__":
    main()
