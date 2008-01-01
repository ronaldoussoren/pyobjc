import pydoc

__all__ = ['gethtmldoc']

def gethtmldoc(thing, forceload=0):
    obj, name = pydoc.resolve(thing, forceload)
    page = pydoc.html.page(
        pydoc.describe(obj),
        pydoc.html.document(obj, name)
    )
    return page
