#
# This module tries to scan header files using a regexp-based parser.
#
from scanner import *
from textwrap import dedent
import re

TYP_PTR = re.compile(r'\s+\*')
SPACE_NORMALIZE = re.compile(r'\s+')

#type mapping 'const unsigned char *   ConstStringPtr' -> 'unsigned char* ConstStringPtr'
#type mapping 'unsigned char           Str255[256]' -> 'unsigned char Str255[256]'
#type mapping 'const unsigned char *   ConstStr255Param' -> 'unsigned char* ConstStr255Param'
def normalize_type(typ, _memoize={}):
    if typ is None:
        return None
    try:
        return _memoize[typ]
    except KeyError:
        pass
    orig = typ
    # XXX: Technically const could be turned into objc._C_CONST but
    #      I can't imagine how that would make a difference.
    for skip in ('const',):
        if typ.startswith(skip + ' '):
            typ = typ[len(skip)+1:]
        typ = typ.replace(' ' + skip + ' ', ' ')
    typ = TYP_PTR.sub('*', typ)
    typ = SPACE_NORMALIZE.sub(' ', typ)
    typ = typ.strip()
    #if orig != typ:
    #    print 'type mapping %r -> %r' % (orig, typ)
    _memoize[orig] = typ
    return typ

SUBPATTERNS = dict(
    AVAILABLE=r'(((AVAIL|DEPRE)[A-Z0-9_]+)|(LK_DEPRECATED)|(CA_DEPRECATED)|(MD_AVAIL_[A-Z0-9_]+)|(NSMQA[0-9]+)|MD_AVAIL)',
    PROTOCOLS=r'(<[^>]+>)',
    TYPE_KEYWORD=r'((unsigned|long|char|volatile|inline|__(\w+?)__|const|__strong|__weak))',
    KEYWORD=r'((double|float|int|unsigned|long|char|extern|volatile|void|inline|__(\w+?)__|const|typedef|static|__weak|__strong))',
    IDENTIFIER=r'((?!const|volatile)[A-Za-z_]\w*)',
    SIZEOF=r'(sizeof\(([^)]+)\))',
    DECIMAL=r'([+\-]?((\.\d+)|(\d+(\.\d*)?))([eE]\d+)?[fF]?)',
    INTEGER=r'([+\-]?\d+[uU]?[lL]?[lL]?)',
    CHARS=r"('([^\\'\n]|\\')*')",
    STRING=r'("([^\\"\n]|\\")*")',
    CFSTRING=r'(CFSTR\("([^\\"\n]|\\")*"\))',
    NSSTRING=r'@("([^\\"\n]|\\")*")',
    HEX=r'(0[xX][0-9a-fA-F]+[uU]?[lL]?)',
    EXTERN=r'((([A-Z-a-z_]\w*?_)?(EXTERN|EXPORT)|extern|(extern\s+"C")))',
    EXPORT=r'((([A-Z-a-z_]\w*?_)?(EXPORT|EXTERN)|extern|(extern\s+"C")))',
    STATIC_INLINE=r'((([A-Z-a-z_]\w*?_)?INLINE|static\s+inline|static\s+__inline__))',
    BRACES=r'(([^\n}]*|([^}][^\n]*\n)*))',
    INDIRECTION=r'(\s*\*)',
    BOL=r'(\s*^\s*)',
    EOL=r'(\s*$\n?)',
    OPERATORS=r'(\||\+|-|\*|&|>>|<<|\^)',
)

WEIRD_INTEGER = re.compile(r'(0[xX][0-9a-fA-F]+|[0-9]+)[uUlL]+')
def cleanup_text(s):
    return WEIRD_INTEGER.sub(r'\1L', s.replace('\t', '        '))

def deadspace(string, begin, end):
    return 'NO MATCH FOR [%d:%d] %r' % (begin, end, string[begin:end])

def pattern(s):
    return dedent(s).strip() % SUBPATTERNS

def example(s):
    return dedent(s).strip()

class AttributeCrap (Token):
    pattern = pattern(r'''
        __attribute__\(\([^)]*\)(,\([^)]*\))*\)
        ''')

    example('''
        __attribute__((__objc_exception__))
        __attribute__((__unused__), (__fobar_))
    ''')

class CPPDecls(Token):
    pattern = pattern(r'''
    (__BEGIN_DECLS|__END_DECLS|[A-Z]+_EXTERN_C_BEGIN|[A-Z]+_EXTERN_C_END|[A-Z]+_BEGIN_C_DECLS|[A-Z]+_END_C_DECLS)
    ''')

class CPPCrap(Token):
    pattern = pattern(r'''
    \#\s*(
        if\s*defined\s*\(\s*__cplusplus\s*\)
        | ifdef\s*__cplusplus
    )
    (?P<body>
        [^#]*
        (
            \#if[^#]*
            (
                (?!\#\s*endif)
                \#
                [^#]*
            )*
            \#\s*endif[^#]*
          |
            (?!\#\s*endif)
            \#
            [^#]*
        )*
    )
    \#\s*endif
    ''')
    example = example('''
    #if defined(__cplusplus)
    extern "C" {
    #endif
    #if defined(__cplusplus)
    }
    #endif
    #ifdef __cplusplus
    sucktastic
    #define foo
    #endif
    ''')

class BlockComment(Token):
    # Note: we use non-greedy matching instead of spelling out that the
    # contents of a comment cannot contain '*/' because we ran into 
    # limitation of the regexp-engine when parsing files with very big
    # comments, such as in SystemConfiguration.framework
    pattern = pattern(r'''
    \/\*
    (?P<comment>.*?)
    \*\/
    ''')
    example = example('''
    /*************\t\tThis is an annoying one\t\t**********/
    /* this is a block comment */
    ''')
    # The really nasty one is this:
    # /* foo \*/ bar */
    # Don't worry about it until we see this in real headers

class SingleLineComment(Token):
    pattern = pattern(r'//(?P<comment>[^\n]*)(\n|$)')
    example = example(r'// this is a single line comment')

class OpaqueNamedStruct (Token):
    pattern = pattern(r'''
    typedef\s+(?P<const>const\s+)?struct\s+
    (?P<label>%(IDENTIFIER)s)\s*
    (?P<indirection>(\s|\*)+)
    \s*
    (?P<name>%(IDENTIFIER)s)\s*
    ;
    ''')
    
    example = example('''
    typedef struct _Foo Foo;
    typedef struct _Bar *BarRef;
    typedef const struct __CFString * CFStringRef;
    ''')

class UninterestingTypedef(Token):
    pattern = pattern(r'''
    typedef
    \s*(?P<body>[^;]*)
    ;
    ''')
    example = example('''
    typedef baz wibble fun* SomethingGreat;
    ''')

class CompilerDirective(Token):
    pattern = pattern(r'''
    \#\s*(?P<name>undef|if|ifdef|ifndef|endif|else|elif|pragma|error|warn|define)
    [ \t]*(?P<body>([^\\\n]|\\(\n|$))*)
    ''')
    example = example(r'''
    #if defined(foo)
    #if \
        insane
    #endif
    #else stuff
    #define NS_DURING { \
        GARBAGE!  blah blah {
    ''')



class AngleImport(Token):
    pattern = pattern(r'''
    \#\s*(?P<import_type>import|include)
        \s+<(?P<import_file>[^>]*)>
    ''')
    example = example('#import <Foo/Bar.h>')

class StringImport(Token):
    pattern = pattern(r'''
    \#\s*(?P<import_type>import|include)
        \s+"(?P<import_file>[^"]*)"
    ''')
    example = example('#import "Foo/Bar.h"')

class SimpleDefine(Token):
    #XXX ((type)foo)
    pattern = pattern(r'''
    \#\s*define\s*
        (?P<name>%(IDENTIFIER)s)\s+
        \(?
            (\(%(TYPE_KEYWORD)s\s*%(KEYWORD)s\)\s*)?
            (\(%(IDENTIFIER)s\)\s*)?
            \(?
            (?P<value>
                (?!%(KEYWORD)s)
                (
                    %(CFSTRING)s
                    | %(NSSTRING)s
                    | %(CHARS)s
                    | %(STRING)s
                    | %(SIZEOF)s
                    | %(DECIMAL)s
                    | [~]?(
                        %(HEX)s
                        | %(INTEGER)s
                        | %(IDENTIFIER)s
                        | %(OPERATORS)s
                        | [ \t]+
                      )+
                )
            )
            \)?
        \)?
        (?!
            [ \t]*[^/\n \t]
        )
    ''')
    example = example(r'''
    #define IB_BIG_SIZE (10000)
    #define foo bar | baz
    #define foo bar << 1234
    #define foo (bar | baz)
    #define foo (bar | 0xFFF)
    #define foo 'foo!'
    #define foo bar
    #define foo 0x200
    #define foo 2.0
    #define foo "foo"
    #define foo CFSTR("foo")
    #define foo sizeof(bar)
    #define foo (8)
    #define foo @"bar"
    #define foo ((long long)-1)
    #define foo ((HRESULT)100L)
    #define foo ((kCGAnyInputEventType)(~0))
    #define kCGNotifyEventTapAdded          "com.apple.coregraphics.eventTapAdded"
    ''')
    
class FunctionCallDefine(Token):
    pattern = pattern(r'''
    \#\s*define\s*
        (?P<name>%(IDENTIFIER)s)
        [ \t]+(?:\\\n[ \t]*)?
        (?P<body>
            %(IDENTIFIER)s
            [ \t]*
            \(
                (?:(?:\([^)]*\))|[^)])*
            \)
            [ \t]*
        )
    (\n|$)
    ''')
    example = example(r'''
    #define IUnknownUUID \
            CFUUIDGetConstantUUIDWithBytes(NULL, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xC0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x46)
    #define kSCResvLink \
            SC_SCHEMA_KV(kSCResvLink    \
                ,"__LINK__"             \
                ,CFString   )
    #define kSCPropNetOverridePrimary                  \
              SC_SCHEMA_KV(kSCPropNetOverridePrimary   \
                          ,"OverridePrimary"           \
                          ,CFNumber (0 or 1)           )

    ''')

class MacroDefine(Token):
    pattern = pattern(r'''
    \#\s*define\s*
        (?P<name>%(IDENTIFIER)s)
        \(
            (?P<args>
                (\s*%(IDENTIFIER)s\s*,)*
                (\s*%(IDENTIFIER)s\s*)?
            )
        \)
    \s*(?P<body>([^\\\n]|\\(\n|$))*)
    ''')
    example = example(r'''
    #define NSLocalizedString(key, comment) \
        [[NSBundle mainBundle] localizedStringForKey:(key) value:@"" table:nil]
    #define GetNSApp() [NSApplication sharedApplication]
    #define DoStuff(a, b, c) do { \
        blah blah blah \
        blah blah blah \
    } while (0);
    ''')

class GlobalThing(Token):
    pattern = pattern(r'''
    (?:%(EXTERN)s|%(EXPORT)s)\s+
    (const\s+)?
    (?P<type>%(IDENTIFIER)s%(INDIRECTION)s*)
    \s*(const\s+)?
    (?P<name>
        %(IDENTIFIER)s
        (
            \s*,\s*
            %(INDIRECTION)s*
            \s*(const\s+)?
            %(IDENTIFIER)s
        )*
    )
    (?:\s*\[\s*\]\s*|\b)
    (
        (\s*/\*(?P<comment2>.*?)\*/)?
        (\s*//(?P<comment>[^\n]*)(\n|$))?
        (?:\s+%(AVAILABLE)s)
    )*
    ;
    ''')
    example = example(r'''
    extern const double FooBar;
    extern const NSString *foo;
    extern NSString *foo;
    extern NSString* const foo;
    APPKIT_EXTERN NSString* const foo;
    RONALD_EXTERN NSString* const foo /* comment */ AVAILABLE_NEVER;
    APPKIT_EXTERN NSString* const foo // argh a comment
        AVAILABLE_SOMEWHERE;
    FOUNDATION_EXPORT NSString * const Foo;
    extern CFStringRef cfFoo AVAILABLE_MAC_OSX_10_8;
    APPKIT_EXTERN const char foosball[] AVAILABLE_NEVER;
    FOUNDATION_EXPORT BOOL NSKeepAllocationStatistics;
    APPKIT_EXTERN const char foosball[] AVAILABLE_NEVER CA_DEPRECATED;
    ''')

class ForwardClassReference(Token):
    pattern = pattern(r'@class\s*(?P<name>[^;]+);')
    example = example(r'@class Foo;')

class ForwardProtocolReference(Token):
    pattern = pattern(r'@protocol\s*(?P<name>%(IDENTIFIER)s\s*(,\s*%(IDENTIFIER)s\s*)*);')
    example = example(r'''
    @protocol Foo, Bar;
    @protocol Handle;
    ''')

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
    \s*(?P<value>(
        (\([A-Za-z_][A-Za-z0-9_]*\)\s*)?
        \(?
        (
            %(CHARS)s
            | (
                (?: %(HEX)s )
                | (?: %(INTEGER)s )
                | (?: %(IDENTIFIER)s )
                | (?: %(OPERATORS)s )
                | (?: \s+ )
             )*
        )
        \)?
        ))
    \s*,?
    ''')
    example = example(r'''
    NSXMLNodePreserveQuotes = (NSXMLNodeUseSingleQuotes | NSXMLNodeUseDoubleQuotes),
    NSXMLNodePreserveCharacterReferences = 1 << 27,
    Foo = 12,
    Foo = 2,
    Bar = 0x00
    ''')

class NamedEnumEnd(Token):
    pattern = pattern(r'''
    \s*}
    \s*(?P<name>%(IDENTIFIER)s)
    \s*;
    ''')
    example = example(r'''
    } FooBarBazWible;
    ''')

class NamedEnum(ScanningToken):
    pattern = pattern(r'''
    typedef
    \s+enum\s*(\/\*.*?\*\/\s*)?
    (?P<name>%(IDENTIFIER)s)?
    \s*(\/\*.*?\*\/\s*)?
    {\s*
    ''')
    endtoken = NamedEnumEnd
    lexicon = [
        CompilerDirective,
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
    typedef enum _bla {
        v = 3,
        x = 4
    } bla;
    typedef enum Foo /* Hello world */
    {
        v = 3,
    } bar;
    ''')

class EnumEnd(Token):
    pattern = pattern(r'''
    \s*}
    \s*(?:%(IDENTIFIER)s\s*)?;
    ''')
    example = example(r'''
    };
    } DEPRECATED_IN_10_8;
    ''')

class UninterestingStruct(Token):
    # XXX handle comments? need its own internal parser?
    pattern = pattern(r'''
    struct[^{;]+;
    ''')
    example = example(r'''
    struct Foo;
    struct Foo Bar;
    ''')

 
class Struct(Token):
    # XXX handle comments? need its own internal parser?
    pattern = pattern(r'''
    (struct|union)
    \s*(?P<structname>%(IDENTIFIER)s)?
    \s*{
        (?P<content>%(BRACES)s)
    }
    (\s*%(AVAILABLE)s)*
    \s*;
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
    struct {
        struct {
            int foo;
        };
        int bar;
    };

    ''')

class NamedStructEnd(Token):
    pattern = pattern(r'''
    \s*}
    \s*(?P<name>%(IDENTIFIER)s)
    (\s*%(AVAILABLE)s)*
    (?:\s*,\s*(?P<altname>\*?\s*%(IDENTIFIER)s))?
    \s*;
    ''')
    example = example(r'''
        } FooBarBazWible;
        } FooBar AVAILABLE_MAC_OS_X_10_3_AND_LATER;
        } FooBar DEPRECATED_IN_MAC_OS_X_VERSION_10_5_AND_LATER;
        } FooBar, *FooBarPointer;
        } FooBar AVAILABLE_MAC_OS_X_10_3_AND_LATER CA_DEPRECATED;
    ''')


class FunctionStructMember(Token):
    pattern = pattern(r'''
    \s*(?P<returns>%(IDENTIFIER)s%(INDIRECTION)s*)
    \s*\(\s*\*\s*%(IDENTIFIER)s\s*\)
    \(
        (?P<args>\s*[^)]*)
    \);
    ''')
    example = example(r'''
        void* (*pfunc)(int, float);
    ''')

class NestedStructMember(Token):
    pattern = pattern(r'''
    \s*(union|struct)\s+(?P<structname>%(IDENTIFIER)s)?
    \s*{\s*
        (?P<body>[^}]*)
    }\s+(?P<name>%(IDENTIFIER)s)\s*(?:\s+%(AVAILABLE)s)*\s*;
    ''')
    example=example('''
    union {
        int a;
        int b;
    } c;
    union foo {
        int my;
        int thy;
    } foo;
    struct {
        int foo;
        int bar;
    } bar;
    struct {
        int foo;
        int bar;
    } bar DEPRECATED_IN_MAC_OS_X_VERSION_10_5_AND_LATER;
    ''')

class StructMember(Token):
    pattern = pattern(r'''
    (const\s+)?
    (?P<type>%(IDENTIFIER)s%(INDIRECTION)s*)
    \s*(const\s+)?
    (?P<name>
        %(IDENTIFIER)s
        (
            \s*,\s*
            %(INDIRECTION)s*
            \s*(const\s+)?
            %(IDENTIFIER)s
        )*
    )
    (?:\s*\[\s*\]\s*|\b)
    (
        (\s*//(?P<comment>[^\n]*)(\n|$))?
        (?:\s+%(AVAILABLE)s)
    )*
    ;
    ''')
    example = example(r'''
    const double FooBar;
    const NSString *foo;
    NSString *foo;
    NSString* const foo;
    NSString* const foo // argh a comment
        AVAILABLE_SOMEWHERE;
    NSString * const Foo;
    CFStringRef cfFoo AVAILABLE_MAC_OSX_10_8;
    const char foosball[] AVAILABLE_NEVER;
    ''')

class StructOpaqueDefine (Token):
    pattern = pattern(r'''
        \s*[A-Z][A-Z0-9_]*\s*;
    ''')

    example = example(r'''
        IUNKNOWN_C_GUTS;
    ''')

class NamedStruct(ScanningToken):
    # XXX handle comments? need its own internal parser?
    pattern = pattern(r'''
    typedef
    \s+(?P<structtype>(struct|union))
    \s*(?P<structname>%(IDENTIFIER)s)?
    \s*{\s*
    ''')
    endtoken = NamedStructEnd
    lexicon = [
        CompilerDirective,
        NestedStructMember,
        FunctionStructMember,
        StructMember,
        StructOpaqueDefine,
    ]
    example = example(r'''
    typedef struct { } NSEmptyStruct;
    typedef struct {unsigned long v;} NSSwappedFloat;
    typedef struct { int bar; } FooBar;
    typedef struct {
        signed foo name;
        int bar;
    } FooBarStruct;
    typedef struct _FooBarStruct {
        signed foo name;
        int bar;
    } FooBarStruct;
    typedef struct _FooBarStruct {
        signed foo name;
        union {
            int stuff;
        } foo;
        int bar;
    } FooBarStruct;
    typedef struct {
        int (*pfunc)(void);
    } FunctionStruct;
    typedef struct {
        IUNKNOWN_C_GUTS;
        OSStatus    (*GenerateThumbnailForURL)(void *thisInterface, QLThumbnailRequestRef thumbnail, CFURLRef url, CFStringRef contentTypeUTI, CFDictionaryRef options, CGSize maxSize);
        void        (*CancelThumbnailGeneration)(void *thisInterface, QLThumbnailRequestRef thumbnail);
        OSStatus    (*GeneratePreviewForURL)(void *thisInterface, QLPreviewRequestRef preview, CFURLRef url, CFStringRef contentTypeUTI, CFDictionaryRef options);
        void        (*CancelPreviewGeneration)(void *thisInterface, QLPreviewRequestRef preview);
    } QLGeneratorInterfaceStruct;

    ''')
 
class Enum(ScanningToken):
    pattern = pattern(r'''
    \s*enum\s*(\/\*.*?\*\/\s*)?
    \s*(?P<name>%(IDENTIFIER)s)?
    \s*(\/\*.*?\*\/\s*)?
    {\s*
    ''')
    endtoken = EnumEnd
    lexicon = [
        CompilerDirective,
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
    enum {
        foo = 'a',
        bar = 'b',
    #if MAC_OS_X_VERSION_10_2 <= MAC_OS_X_VERSION_MAX_ALLOWED
        baz = 'c',
    #end
        last = 'd'
    } DEPRECATED_IN_MAC_OS_X_VERSION_10_5_AND_LATER;
    enum hoopla /* No such thing */
    {
        a,
        b,
        c
    };

    ''')

class FunctionEnd(Token):
    pattern = pattern(r'''
    \s*\)
    (\s*\/\*[^*]*\*\/)?
    (\s*(?P<available>%(AVAILABLE)s))*
    \s*;
    ''')
    example = example(r'''
    );
    )  ;
    ) AVAILABLE_SOMEHOW;
    ) /* Foo */ AVAILABLE_X;
    ) /* Foo */;
    ''')

class FunctionParameter(Token):

    # The pattern isn't correct arguments like 'long param', those will be
    # parsed into type=='long param', name=None.
    pattern = pattern(r'''
    \s*(?P<type>
        ((%(TYPE_KEYWORD)s|struct)\s+)*
        %(IDENTIFIER)s\s*
        (%(INDIRECTION)s|%(KEYWORD)s|\s)*
        \s*
    )\s*
    (\/\*[^*]*\*\/)?\s*
    (?<=(\s|\*))(?P<name>%(IDENTIFIER)s\s*)?\s*(?P<array>\[\d*\])?,?
    ''')
    example = example(r'''
    NSString* foo
    NSString *foo, NSString *bar
    CFDataRef ref
    const struct FSRef* fsRef
    const unsigned char * const data[5],
    ''')

class FunctionElipsisParameter (Token):
    pattern = pattern(r'''\s*\.\.\.\s*''')
    example = example(r'''...''')

class ExportVoidFunction (Token):
    pattern = pattern(r'''
    %(EXPORT)s?
    \s*(?P<returns>
        (%(TYPE_KEYWORD)s(\s+%(TYPE_KEYWORD)s)*)??
        \s*%(IDENTIFIER)s
        ((\s|\*)(\s*(\*|%(KEYWORD)s))*\s*(?<=\s|\*))?
    )
    (\s*(?P<protocols>%(PROTOCOLS)s)\s*)?
    \s*(\/\*[^*]*\*\/)?\s*
    (\s%(IDENTIFIER)s\s)?
    \s*(?P<name>%(IDENTIFIER)s)
    \s*\(\s*void\s*\)
    (\s*(?P<available>%(AVAILABLE)s))*;''')

class SC_SCHEMA_DECLARATION (Token):
    pattern = pattern(r'''
    SC_SCHEMA_DECLARATION\(\s*(?P<name>%(IDENTIFIER)s),\s*%(IDENTIFIER)s\)
    ''')
    example = example(r'''
    SC_SCHEMA_DECLARATION(kSCResvLink, AVAILABLE_MAC_OS_X_VERSION_10_1_AND_LATER)
    ''')

class StaticInlineEnd(Token):
    pattern = pattern(r'''
    \s*\)
    \s*{
        (?P<body>%(BRACES)s)
    }
    ''')
    example = example('''
        ) { return 22; }

        ) {
            union fconv {
                float number;
                NSSwappedFloat sf;
            };
            return ((union fconv *)&x)->sf;
        }

    ''')

class StaticInlineFunction(ScanningToken):
    # XXX need to figure out how to find a close brace
    #     will probably need something stateful I guess
    pattern = pattern(r'''
    %(STATIC_INLINE)s
    \s*(?P<returns>
        (%(KEYWORD)s\s*)*
        %(IDENTIFIER)s
        (%(INDIRECTION)s|\s+%(KEYWORD)s)*
    )
    \s*(?<=(\s|\*))(?P<name>%(IDENTIFIER)s)
    \s*\(
    ''')
    endtoken = StaticInlineEnd
    lexicon = [
        BlockComment,
        InsignificantWhitespace,
        FunctionElipsisParameter,
        FunctionParameter,
    ]
    example = example(r'''
    static inline unsigned int NSEventMaskFromType(NSEventType type) { return (1 << type); }
    FOUNDATION_STATIC_INLINE BOOL NSDecimalIsNotANumber(const NSDecimal *dcm)
      { return ((dcm->_length == 0) && dcm->_isNegative); }
    FOUNDATION_STATIC_INLINE unsigned short NSSwapShort(unsigned short inv) {
        return CFSwapInt16(inv);
    }
    FOUNDATION_STATIC_INLINE NSSwappedFloat NSConvertHostFloatToSwapped(float x) {
        union fconv {
        float number;
        NSSwappedFloat sf;
        };
        return ((union fconv *)&x)->sf;
    }
    ''')

class ExportFunction(ScanningToken):
    pattern = pattern(r'''
    %(EXPORT)s?
    \s*(?P<returns>
        (%(TYPE_KEYWORD)s(\s+%(TYPE_KEYWORD)s)*)??
        \s*%(IDENTIFIER)s
        ((\s|\*)(\s*(\*|%(KEYWORD)s))*\s*(?<=\s|\*))?
    )
    (\s*(?P<protocols>%(PROTOCOLS)s)\s*)?
    \s*(\/\*[^*]*\*\/)?\s*
    (\s%(IDENTIFIER)s\s)?
    \s*(?P<name>%(IDENTIFIER)s)
    \s*\(\s*
    ''')
    endtoken = FunctionEnd
    lexicon = [
        BlockComment,
        InsignificantWhitespace,
        FunctionElipsisParameter,
        FunctionParameter,
    ]
    example = example(r'''
    extern void*const MyFunc(void);
    extern void*__strong MyFunc(void);
    extern NSString *ABLocalizedPropertyOrLabel(NSString *propertyOrLabel);
    APPKIT_EXTERN NSString *NSSomething(NSString *arg, NSString *arg)
        AVAILABLE_SOMEWHERE;
    FOUNDATION_EXPORT void *NSSomething(unsigned long arg, unsigned long arg) AVAILABLE_SOMEWHERE;
    FOUNDATION_EXPORT SomeResult <NSObject> SomeName(const Foo *, const Foo *Bar);
    FOUNDATION_EXPORT SomeResult **SomeName(const Foo *, const Foo *Bar);
    FOUNDATION_EXPORT SomeResult SomeName(int,float);
    CFArrayRef /* of SCFoo's */ SCNetworkInterfaceCopyAll    (void) AVALABLE_FOO;
    CF_EXPORT
    const UInt8 *CFDataGetBytePtr(CFDataRef theData);
    NPError NP_LOADSS   NP_New(void);
    Boolean CFCalendarComposeAbsoluteTime(CFCalendarRef calendar, /* out */ CFAbsoluteTime *at, const unsigned char *componentDesc, ...) AVAILABLE_MAC_OS_X_VERSION_10_4_AND_LATER;
    extern CFIndex ABBeginLoadingImageDataForClient(ABPersonRef person, ABImageClientCallback callback, void* refcon);
    extern "C" NSString *STComposeString(NSString *, ...);
    CFArrayRef /* of SCNetworkServiceRef's */ SCNetworkServiceCopyAll                         (SCPreferencesRef               prefs)          AVAILABLE_MAC_OS_X_VERSION_10_4_AND_LATER;

    ''')

#!# class ExportFunction(Token):
#!#     # XXX handle comments? need its own internal parser?
#!#     pattern = pattern(r'''
#!#     %(EXPORT)s?
#!#     \s*(?P<returns>
#!#         (%(KEYWORD)s\s*)*
#!#         %(IDENTIFIER)s
#!#         (%(INDIRECTION)s|\s+%(KEYWORD)s)*
#!#     )
#!#     (\s*(?P<protocols>%(PROTOCOLS)s))?
#!#     \s*(?P<name>%(IDENTIFIER)s)
#!#     \s*\(
#!#         (?P<args>\s*[^)]*)
#!#     \s*\)
#!#     (\s*(?P<available>%(AVAILABLE)s))?
#!#     \s*;
#!#     ''')
#!#     example = example(r'''
#!#     APPKIT_EXTERN NSString *NSSomething(NSString *arg, NSString *arg)
#!#         AVAILABLE_SOMEWHERE;
#!#     FOUNDATION_EXPORT void *NSSomething(unsigned long arg, unsigned long arg) AVAILABLE_SOMEWHERE;
#!#     FOUNDATION_EXPORT SomeResult <NSObject> SomeName(const Foo *, const Foo *Bar);
#!#     FOUNDATION_EXPORT SomeResult **SomeName(const Foo *, const Foo *Bar);
#!#     FOUNDATION_EXPORT SomeResult SomeName(int,float);
#!#     ''')

class StaticInlineFunctionPrototype(Token):
    pattern = pattern(r'''
    %(STATIC_INLINE)s
    \s*(?P<returns>
        (%(KEYWORD)s\s*)*
        %(IDENTIFIER)s
        (%(INDIRECTION)s|\s+%(KEYWORD)s)*
    )
    \s*(?P<name>%(IDENTIFIER)s)
    \s*\(
        (?P<args>\s*[^)]*)
    \s*\)
    \s*;
    ''')
    example = example(r'''
    static inline unsigned int NSEventMaskFromType(NSEventType type);
    CG_INLINE CGSize CGSizeMake(CGFloat width, CGFloat height);
    ''')



class SimpleMethodDef(Token):
    pattern = pattern(r'''
       (?P<kind>[-+])
       \s*
       (\((?P<returntype>[^)]*)\))?
       \s*
       (?P<name>%(IDENTIFIER)s);
       ''')

    example = example(r'''
    - (id)foo;
    + bar;
    - (NSArray /* NSString */ *)supportedEntityNames;
    ''')

class MethodSegment (Token):
    pattern = pattern(r'''
    (?P<name>%(IDENTIFIER)s:)\s*(\((?P<type>[^)]*)\))?\s*%(IDENTIFIER)s
    ''')
    example = example(r'''
    foo:(float)bar
    foo:bar
    ''')

class SegmentedMethodEnd(Token):
    pattern = pattern(r';')
    example = example(r';')

class SegmentedMethodDef(ScanningToken):
    pattern = pattern(r'''
       (?P<kind>[-+])
       \s*
       (\((?P<returntype>[^)]*)\))?
       ''')
    lexicon = [
        MethodSegment,
        BlockComment,
        FunctionElipsisParameter,
    ]
    endtoken = SegmentedMethodEnd

    example = example(r'''
    - (id)foo:(int)k;
    + bar:j foo:(float)b;
    - (NSString *)stringByAppendingFormat:(NSString *)format, ...;
    - (BOOL)syncWithClient:(ISyncClient *)client inBackground:(BOOL)flag handler:(id <NSPersistentStoreCoordinatorSyncing>)syncHandler error:(NSError **)rError;
    ''')


class InterfaceEnd(Token):
    pattern = pattern(r'''@end''')
    example = example(r'''
    @end
    ''')

class PropertyName (Token):
    pattern = pattern(r'''
        (?P<name>
            %(IDENTIFIER)s
            (
                \s*,\s*
                %(INDIRECTION)s*
                \s*(const\s+)?
                %(IDENTIFIER)s
            )*
        )
        (?:\s*\[\s*\]\s*|\b)
        ,?\s*
        ''')
    example = example('''
        foo,
        *foo,
        * foo,
        bar
        ''')

class PropertySeperator (Token):
    pattern = pattern('''\s*,\s*''')
    example = example(''',''')

class PropertyEnd (Token):
    pattern = pattern('''\s*;''')
    example = example(''';''')


class PropertyDefinition(ScanningToken):
    pattern = pattern(r'''
        @property
        \s*(?P<options>\([^)]*\))?
        (const\s+)?
        (?P<type>%(IDENTIFIER)s%(INDIRECTION)s*)
        \s*(const\s+)?
        ''')
    endtoken = PropertyEnd
    lexicon = [
            PropertyName,
            PropertySeperator,
            BlockComment,
            SingleLineComment,
    ]

class Interface(ScanningToken):
    pattern = pattern(r'''
    (?:%(AVAILABLE)s\s*)*@interface
        \s+(?P<name>%(IDENTIFIER)s)
        \s*(?:\(\s*(?P<category>%(IDENTIFIER)s)\s*\))?
        \s*(?::\s*(?P<super>%(IDENTIFIER)s))?
        \s*(?:<(?P<protocols>[^>]*)>)?
        \s*(?:{(?P<ivars>%(BRACES)s)})?
    ''')
    endtoken = InterfaceEnd
    lexicon = [
        SimpleMethodDef,
        SegmentedMethodDef,
        CompilerDirective,
        InsignificantWhitespace,
        BlockComment,
        SingleLineComment,
        NamedEnum,
        Enum,
        GlobalThing,
        PropertyDefinition,
    ]
    example = example(r'''
    @interface Foo(Bar): Baz <protocols> {
    @private
        NSArray *crazy;
    }

    + (Foo *)newFoo;
    - init;
    @end

    @interface Foo ( bar )
    {
    }
    - init;
    @end

    AVAILABLE_MAC_OS_X_VERSION_10_0_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_5
    @interface NSMailDelivery : NSObject
    {
    }
    @end

    ''')

class ProtocolEnd(Token):
    pattern = pattern(r'''@end''')
    example = example(r'''
    @end
    ''')

class Protocol(ScanningToken):
    pattern = pattern(r'''
    @protocol
        \s+(?P<name>%(IDENTIFIER)s)
        \s*(?:<(?P<super>%(IDENTIFIER)s)>)?
    ''')
    endtoken = ProtocolEnd
    lexicon = [
        SimpleMethodDef,
        SegmentedMethodDef,
        CompilerDirective,
        InsignificantWhitespace,
        BlockComment,
        SingleLineComment,
        NamedEnum,
        Enum,
        GlobalThing,
    ]
    example = example(r'''
    @protocol FooProtocol <Foo>
    + (Foo *)protoFoo;
    @end

    @protocol BarProtocol
      /* Hello world @end */
    @end
    ''')

LEXICON = [
    InsignificantWhitespace,
    BlockComment,
    SingleLineComment,
    ForwardProtocolReference,
    AttributeCrap,
    Interface,
    Protocol,
    AngleImport,
    StringImport,
    FunctionCallDefine,
    SimpleDefine,
    GlobalThing,
    ForwardClassReference,
    NamedEnum,
    Enum,
    NamedStruct,
    Struct,
    MacroDefine,
    CPPDecls,
    CPPCrap,
    CompilerDirective,
    OpaqueNamedStruct,
    UninterestingTypedef,
    StaticInlineFunctionPrototype,
    StaticInlineFunction,
    ExportVoidFunction,
    SC_SCHEMA_DECLARATION,
    ExportFunction,
    UninterestingStruct,
]

if __name__ == '__main__':
    from pdb import pm
    import re
    import sys
    frameworks = """
    SystemConfiguration
    AddressBook
    AppKit
    ExceptionHandling
    Foundation
    InterfaceBuilder
    Message
    PreferencePanes
    ScreenSaver
    SecurityInterface
    WebKit
    CoreFoundation
    AppKitScripting
    ApplicationServices
    Cocoa
    DirectoryService
    DiscRecording
    DiscRecordingUI
    LDAP
    Scripting
    SecurityFoundation
    SecurityInterface
    System
    SystemConfiguration
    Security
    Carbon
    CoreServices
    """.split()
    files = sys.argv[1:]
    if not files:
        import glob
        for framework in frameworks:
            if framework.startswith('#'):
                continue
            files.extend(glob.glob('/System/Library/Frameworks/%s.framework/Headers/*.h' % (framework,)))
    fn = None
    def deadraise(string, i, j):
        print '-' * len(fn)
        print fn
        print '-' * len(fn)
        s = string[i:].split('\n',1)[0]
        print s
        print
        import pdb
        pdb.Pdb().set_trace()
    scan = Scanner(LEXICON)
    for fn in files:
        print '-' * len(fn)
        print fn
        print '-' * len(fn)
        for token in scan.iterscan(file(fn).read(), dead=deadraise):
            if token is not None:
                print token
