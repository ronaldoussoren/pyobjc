from compiler import parseFile
from compiler.ast import Module, Stmt, Assign, AssName, Const

__version__ = '1.0'

def findVersion(fn):
    ast = parseFile(fn)
    if not isinstance(ast, Module):
        raise ValueError, "expecting Module"
    statements = ast.getChildNodes()
    if not (len(statements) == 1 and isinstance(statements[0], Stmt)):
        raise ValueError, "expecting one Stmt"
    for node in statements[0].getChildNodes():
        if not isinstance(node, Assign):
            continue
        if not len(node.nodes) == 1:
            continue
        assName = node.nodes[0]
        if not (
                isinstance(assName, AssName) and
                isinstance(node.expr, Const) and
                assName.flags == 'OP_ASSIGN' and 
                assName.name == '__version__'
                ):
            continue
        return node.expr.value
    else:
        raise ValueError, "Version not found"
    
if __name__ == '__main__':
    import sys
    for arg in (sys.argv[1:] or [__file__]):
        print arg, findVersion(arg)
