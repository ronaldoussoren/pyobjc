import imp

def imp_find_module(name):
    """same as imp.find_module, but handles dotted names"""
    names = name.split('.')
    path = None
    for name in names:
        result = imp.find_module(name, path)
        path = [result[1]]
    return result

def test_imp_find_module():
    import encodings.aliases
    fn = imp_find_module('encodings.aliases')[1]
    assert encodings.aliases.__file__.startswith(fn)

if __name__ == '__main__':
    test_imp_find_module()
