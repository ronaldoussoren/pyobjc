from scanner import *
from textwrap import dedent


SUBPATTERNS = dict(
    AVAILABLE=r'(?:AVAILABLE_\w+)',
    KEYWORD=r'((?:double|float|int|unsigned|long|char|extern|volatile|void|inline|__(?:\w+?)__|const|typedef|static|const))',
    IDENTIFIER=r'([A-Za-z_]\w*)',
    SIZEOF=r'(?:sizeof\(([^)]+)\))',
    DECIMAL=r'(?:[+\-]?\d*(?:\.\d*)?(?:[eE]\d+)?[fF]?)',
    INTEGER=r'(?:[+\-]?\d*[uU]?[lL]?)',
    CHARS=r"(?:'(?:[^\\'\n]|\\')*')",
    STRING=r'(?:"(?:[^\\"\n]|\\")*")',
    CFSTRING=r'(?:CFSTR\("(?:[^\\"\n]|\\")*"\))',
    HEX=r'(?:0[xX][0-9a-fA-F]+[lL]?)',
    EXTERN=r'(?:(?:(?:[A-Z-a-z_]\w*?_)?EXTERN|extern))',
    BOL=r'(?:^\s*)',
    EOL=r'(?:\s*$\n?)',
    SEMI=r';\s*',
)

def pattern(s):
    return dedent(s).strip() % SUBPATTERNS

def example(s):
    return dedent(s).strip()

class BlockComment(Token):
    pattern = pattern(r'/\*(?P<comment>(?:[^*]|\*[^/])*)\*/')
    example = example(r'/* this is a block comment */')

class SingleLineComment(Token):
    pattern = pattern(r'//(?P<comment>[^\n]*)(\n|$)')
    example = example(r'// this is a single line comment')

class Interface(Token):
    pattern = pattern(r'''
    %(BOL)s
    @interface
        \s+(?P<name>%(IDENTIFIER)s)
        \s*(?:\((?P<category>%(IDENTIFIER)s)\))?
        \s*(?::\s*(?P<super>%(IDENTIFIER)s))?
        \s*(?:<(?P<protocols>[^>]*)>)?
        \s*(?:{(?P<ivars>[^}])})?
        \s*(?P<interface_body>.*?)
    %(BOL)s
    @end
    %(EOL)s
    ''' % SUBPATTERNS)
    example = example(r'''
    @interface Foo(Bar): Baz <protocols> {
    @private
        NSArray *crazy;
    }

    + (Foo *)newFoo;
    - init;
    @end
    ''')

class Protocol(Token):
    pattern = pattern(r'''
    %(BOL)s
    @protocol
        \s+(?P<name>%(IDENTIFIER)s)
        \s*(?:<(?P<super>%(IDENTIFIER)s)>)?
        \s*(?P<protocol_body>.*?)
    %(BOL)s
    @end
    %(EOL)s
    ''' % SUBPATTERNS)
    example = example(r'''
    @protocol FooProtocol <Foo>
    + (Foo *)protoFoo;
    @end
    ''')

class AngleImport(Token):
    pattern = pattern(r'''
    %(BOL)s
    \#\s*(?P<import_type>import|include)
        \s+<(?P<import_file>[^>]*)>
    %(EOL)s
    ''' % SUBPATTERNS)
    example = example('#import <Foo/Bar.h>')

class StringImport(Token):
    pattern = pattern(r'''
    %(BOL)s
    \#\s*(?P<import_type>import|include)
        \s+"(?P<import_file>[^"]*)"
    %(EOL)s
    ''' % SUBPATTERNS)
    example = example('#import "Foo/Bar.h"')

class SimpleDefine(Token):
    # XXX foo << bar
    # XXX foo | bar | baz
    # XXX ((type)foo)
    pattern = pattern(r'''
    %(BOL)s
    \#\s*define\s*
        (?P<name>%(IDENTIFIER)s)\s+
        (?P<value>
            (?!%(KEYWORD)s)%(IDENTIFIER)s
            | %(HEX)s
            | %(INTEGER)s
            | %(DECIMAL)s
            | %(CHARS)s
            | %(STRING)s
            | %(CFSTRING)s
            | %(SIZEOF)s
        )
    %(EOL)s
    ''' % SUBPATTERNS)
    example = example(r'''
    #define foo bar
    #define foo 0x200
    #define foo 2.0
    #define foo 'foo!'
    #define foo "foo"
    #define foo CFSTR("foo")
    #define foo sizeof(bar)
    ''')
    

class GlobalString(Token):
    pattern = pattern(r'''
    %(BOL)s
    %(EXTERN)s\s*
    (const\s+)?
    (CFStringRef|(NSString|char)\s*\*)
    \s*(const\s+)?
    (?P<name>%(IDENTIFIER)s)\b
    \s*%(AVAILABLE)s?\s*
    %(SEMI)s
    ''')
    example = example(r'''
    extern const NSString *foo;
    extern NSString *foo;
    APPKIT_EXTERN NSString* const foo;
    extern CFStringRef cfFoo AVAILABLE_MAC_OSX_10_8;
    ''')

class GlobalCharArray(Token):
    pattern = pattern(r'''
    %(BOL)s
    %(EXTERN)s
    \s*(const\s+)?
    char
    \s*(const\s+)?
    (?P<name>%(IDENTIFIER)s)\s*\[\s*\]\s*
    \s*%(AVAILABLE)s?\s*
    %(SEMI)s
    ''')
    example = example(r'''
    APPKIT_EXTERN const char foosball[] AVAILABLE_NEVER;
    ''')
    

class ForwardClassReference(Token):
    pattern = pattern(r'@class[^;]+;')
    example = example(r'@class Foo;')
    
LEXICON = [
    BlockComment,
    SingleLineComment,
    Interface,
    Protocol,
    AngleImport,
    SimpleDefine,
    GlobalString,
    GlobalCharArray,
    ForwardClassReference,
]

if __name__ == '__main__':
    from pdb import pm
    import re
    fn = '/System/Library/Frameworks/Foundation.framework/Headers/NSDecimal.h'
    scan = Scanner(LEXICON)
    for token in scan.iterscan(file(fn).read()):
        print token
