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
    EXPORT=r'(?:(?:(?:[A-Z-a-z_]\w*?_)?EXPORT|extern))',
    STATIC_INLINE=r'(?:(?:(?:[A-Z-a-z_]\w*?_)?INLINE|static inline|static __inline__))',
    INDIRECTION=r'(?:\s*\*)',
    BOL=r'(?:\s*^\s*)',
    EOL=r'(?:\s*$\n?)',
    SEMI=r';\s*',
)

def deadspace(string, begin, end):
    return 'NO MATCH FOR [%d:%d] %r' % (begin, end, string[begin:end])

def pattern(s):
    return dedent(s).strip() % SUBPATTERNS

def example(s):
    return dedent(s).strip()

class BlockComment(Token):
    pattern = pattern(r'\s*/\*(?P<comment>(?:[^*]|\*[^/])*)\*/\s*')
    example = example(r'/* this is a block comment */')

class SingleLineComment(Token):
    pattern = pattern(r'\s*//(?P<comment>[^\n]*)(\n|$)')
    example = example(r'// this is a single line comment')

class InsignificantWhitespace(IgnoreToken):
    pattern = pattern(r'''\s+''')
    example = example('  \t\n\r   ')

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
    ''')
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
    ''')
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
    ''')
    example = example('#import <Foo/Bar.h>')

class StringImport(Token):
    pattern = pattern(r'''
    %(BOL)s
    \#\s*(?P<import_type>import|include)
        \s+"(?P<import_file>[^"]*)"
    %(EOL)s
    ''')
    example = example('#import "Foo/Bar.h"')

class SimpleDefine(Token):
    # XXX foo << bar
    # XXX foo | bar | baz
    # XXX ((type)foo)
    pattern = pattern(r'''
    %(BOL)s
    \#\s*define\s*
        (?P<name>%(IDENTIFIER)s)\s+
        \(?(?P<value>
            (?!%(KEYWORD)s)%(IDENTIFIER)s
            | %(HEX)s
            | %(INTEGER)s
            | %(DECIMAL)s
            | %(CHARS)s
            | %(STRING)s
            | %(CFSTRING)s
            | %(SIZEOF)s
        )\)?
    %(EOL)s
    ''')
    example = example(r'''
    #define foo bar
    #define foo 0x200
    #define foo 2.0
    #define foo 'foo!'
    #define foo "foo"
    #define foo CFSTR("foo")
    #define foo sizeof(bar)
    #define foo (8)
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
    pattern = pattern(r'@class (?P<name>[^;]+);')
    example = example(r'@class Foo;')

class EnumBareMember(Token):
    pattern = pattern(r'''
    \s*(?P<name>%(IDENTIFIER)s)
    \s*,?
    ''')
    example = example(r'''
    Foo,
    Foo
    ''')

class EnumValueMember(Token):
    pattern = pattern(r'''
    \s*(?P<name>%(IDENTIFIER)s)
    \s*=
    \s*(?P<value>%(INTEGER)s)
    \s*,?
    ''')
    example = example(r'''
    Foo = 12,
    Foo = 2
    ''')

class NamedEnumEnd(Token):
    pattern = pattern(r'''
    \s*}
    \s*(?P<name>%(IDENTIFIER)s)
    \s*%(SEMI)s
    ''')
    example = example(r'''
    } FooBarBazWible;
    ''')

class NamedEnum(ScanningToken):
    pattern = pattern(r'''
    %(BOL)s
    typedef
    \s+enum
    \s*{\s*
    ''')
    endtoken = NamedEnumEnd
    lexicon = [
        InsignificantWhitespace,
        BlockComment,
        SingleLineComment,
        EnumValueMember,
        EnumBareMember,
    ]
    example = example(r'''
    typedef enum {
        FooBar = 1, // This is the best value for FooBar
        Baz = 2,
        Wibble
    } FooBarBazWibble;
    typedef enum {
        FooBar, /* But this FooBar has no value! */
        Baz,
        Wibble
    } FooBarBazWibble;
    ''')

class EnumEnd(Token):
    pattern = pattern(r'''
    \s*}
    \s*%(SEMI)s
    ''')
    example = example(r'''
    };
    ''')

class Struct(Token):
    # XXX handle comments? need its own internal parser?
    pattern = pattern(r'''
    %(BOL)s
    struct
    \s*(?P<structname>%(IDENTIFIER)s)?
    \s*{
        (?P<content>[^}]*)
    \s*}
    \s*%(SEMI)s
    ''')
    example = example(r'''
    struct {
        signed foo name;
        int bar;
    };
    struct _FooBarStruct {
        signed foo name;
        int bar;
    };
    ''')

class NamedStruct(Token):
    # XXX handle comments, needs its own internal parser
    pattern = pattern(r'''
    %(BOL)s
    typedef
    \s+struct
    \s*(?P<structname>%(IDENTIFIER)s)?
    \s*{
        (?P<content>[^}]*)
    \s*}
    \s*(?P<name>%(IDENTIFIER)s)
    \s*%(SEMI)s
    ''')
    example = example(r'''
    typedef struct {
        signed foo name;
        int bar;
    } FooBarStruct;
    typedef struct _FooBarStruct {
        signed foo name;
        int bar;
    } FooBarStruct;
    ''')
 
class Enum(ScanningToken):
    pattern = pattern(r'''
    %(BOL)s
    \s*enum
    \s*{\s*
    ''')
    endtoken = EnumEnd
    lexicon = [
        InsignificantWhitespace,
        BlockComment,
        SingleLineComment,
        EnumValueMember,
        EnumBareMember,
    ]
    example = example(r'''
    enum {
        FooBar = 1, // This is the best value for FooBar
        Baz = 2,
        Wibble
    };
    enum {
        FooBar, /* But this FooBar has no value! */
        Baz,
        Wibble
    };
    ''')

class FunctionEnd(Token):
    pattern = pattern(r'''
    \)
    \s*%(SEMI)s
    ''')
    example = example(r'''
    );
    )  ;
    ''')

class FunctionParameter(Token):
    pattern = pattern(r'''
    (%(IDENTIFIER)s\s*)+
    \s*%(INDIRECTION)s
    \s*%(IDENTIFIER)s?
    \s*,?\s*
    ''')
    example = example(r'''
    NSString *foo, NSString *bar
    ''')

#class ExportFunction(ScanningToken):
#    pattern = pattern(r'''
#    %(BOL)s
#    %(EXPORT)s
#    \s*(?P<returns>%(IDENTIFIER)s%(INDIRECTION)s*)
#    \s*%(IDENTIFIER)s
#    \s*\(
#    ''')
#    endtoken = FunctionEnd
#    lexicon = [
#        InsignificantWhitespace,
#        FunctionParameter,
#    ]
#    example = example(r'''
#    FOUNDATION_EXPORT SomeResult **SomeName(const Foo *, const Foo *Bar);
#    FOUNDATION_EXPORT SomeResult SomeName(int,float);
#    ''')

class ExportFunction(Token):
    pattern = pattern(r'''
    %(BOL)s
    %(EXPORT)s
    \s*(?P<returns>%(IDENTIFIER)s%(INDIRECTION)s*)
    \s*(?P<name>%(IDENTIFIER)s)
    \s*\(
    \s*[^)]*
    \s*\)
    \s*%(SEMI)s
    ''')
    example = example(r'''
    FOUNDATION_EXPORT SomeResult **SomeName(const Foo *, const Foo *Bar);
    FOUNDATION_EXPORT SomeResult SomeName(int,float);
    ''')

class StaticInlineFunction(Token):
    # XXX need to figure out how to find a close brace
    pattern = pattern(r'''
    %(BOL)s
    %(STATIC_INLINE)s
    \s*(?P<returns>%(IDENTIFIER)s%(INDIRECTION)s*)
    \s*(?P<name>%(IDENTIFIER)s)
    \s*\(
    \s*[^)]*
    \s*\)
    \s*{
    \s*[^}]*
    \s*}
    ''')
    example = example(r'''
    FOUNDATION_STATIC_INLINE BOOL NSDecimalIsNotANumber(const NSDecimal *dcm)
      { return ((dcm->_length == 0) && dcm->_isNegative); }
    ''')


LEXICON = [
    InsignificantWhitespace,
    BlockComment,
    SingleLineComment,
    Interface,
    Protocol,
    AngleImport,
    SimpleDefine,
    GlobalString,
    GlobalCharArray,
    ForwardClassReference,
    NamedEnum,
    Enum,
    NamedStruct,
    Struct,
    ExportFunction,
    StaticInlineFunction,
]

if __name__ == '__main__':
    from pdb import pm
    import re
    import sys
    fn = '/System/Library/Frameworks/Foundation.framework/Headers/NSDecimal.h'
    fn = (sys.argv[1:] or [fn])[0]
    scan = Scanner(LEXICON)
    for token in scan.iterscan(file(fn).read(), dead=deadspace):
        if token is not None:
            print token
