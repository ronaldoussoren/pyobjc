from _tools import run_in_threads
import objc

NSObject = objc.lookUpClass("NSObject")
m = NSObject.description


def f(b):
    b.wait()
    d = m.__metadata__()
    assert isinstance(d, dict)
    assert d["arguments"][0] == {"type": b"@", "_template": True}
    assert d["retval"] == {"type": b"@", "_template": True}

    return


objc._updatingMetadata(True)
objc._updatingMetadata(False)
run_in_threads(f, ())
