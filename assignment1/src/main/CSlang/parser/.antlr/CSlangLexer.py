# Generated from d:\Program\XAMPP\htdocs\btl-nllt\assignment1\src\main\CSlang\parser\CSlang.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u016c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\3\2\3\2\3\3\6\3{\n\3\r\3\16\3|\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\4\7\4\u0085\n\4\f\4\16\4\u0088\13\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\7\5\u0093\n\5\f\5\16\5\u0096")
        buf.write("\13\5\3\5\3\5\3\6\3\6\7\6\u009c\n\6\f\6\16\6\u009f\13")
        buf.write("\6\3\7\3\7\6\7\u00a3\n\7\r\7\16\7\u00a4\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3\"")
        buf.write("\3#\3#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)")
        buf.write("\3)\3*\3*\3*\3+\3+\3+\3,\3,\3-\3-\3-\3-\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65")
        buf.write("\3\65\3\66\3\66\3\67\3\67\38\38\39\39\39\3:\3:\7:\u0162")
        buf.write("\n:\f:\16:\u0165\13:\3:\3:\3;\3;\3;\3;\3\u0086\2<\3\2")
        buf.write("\5\3\7\4\t\5\13\6\r\7\17\b\21\t\23\n\25\13\27\f\31\r\33")
        buf.write("\16\35\17\37\20!\21#\22%\23\'\24)\25+\26-\27/\30\61\31")
        buf.write("\63\32\65\33\67\349\35;\36=\37? A!C\"E#G$I%K&M\'O(Q)S")
        buf.write("*U+W,Y-[.]/_\60a\61c\62e\63g\64i\65k\66m\67o8q9s:u;\3")
        buf.write("\2\7\6\2\62;C\\aac|\5\2\n\f\16\17\"\"\4\2\f\f\17\17\5")
        buf.write("\2C\\aac|\n\2$$))^^ddhhppttvv\2\u0170\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\3w\3\2\2\2\5z\3\2\2\2\7\u0080\3\2\2\2\t\u008e\3\2\2")
        buf.write("\2\13\u0099\3\2\2\2\r\u00a0\3\2\2\2\17\u00a6\3\2\2\2\21")
        buf.write("\u00ac\3\2\2\2\23\u00b5\3\2\2\2\25\u00b8\3\2\2\2\27\u00bd")
        buf.write("\3\2\2\2\31\u00c1\3\2\2\2\33\u00c6\3\2\2\2\35\u00cc\3")
        buf.write("\2\2\2\37\u00d0\3\2\2\2!\u00d6\3\2\2\2#\u00db\3\2\2\2")
        buf.write("%\u00e2\3\2\2\2\'\u00e9\3\2\2\2)\u00ee\3\2\2\2+\u00f4")
        buf.write("\3\2\2\2-\u0100\3\2\2\2/\u0104\3\2\2\2\61\u0109\3\2\2")
        buf.write("\2\63\u010e\3\2\2\2\65\u0114\3\2\2\2\67\u0119\3\2\2\2")
        buf.write("9\u011b\3\2\2\2;\u011d\3\2\2\2=\u011f\3\2\2\2?\u0121\3")
        buf.write("\2\2\2A\u0123\3\2\2\2C\u0125\3\2\2\2E\u0128\3\2\2\2G\u012b")
        buf.write("\3\2\2\2I\u012e\3\2\2\2K\u0130\3\2\2\2M\u0133\3\2\2\2")
        buf.write("O\u0135\3\2\2\2Q\u0138\3\2\2\2S\u013a\3\2\2\2U\u013d\3")
        buf.write("\2\2\2W\u0140\3\2\2\2Y\u0142\3\2\2\2[\u0146\3\2\2\2]\u0148")
        buf.write("\3\2\2\2_\u014a\3\2\2\2a\u014c\3\2\2\2c\u014e\3\2\2\2")
        buf.write("e\u0150\3\2\2\2g\u0152\3\2\2\2i\u0154\3\2\2\2k\u0156\3")
        buf.write("\2\2\2m\u0158\3\2\2\2o\u015a\3\2\2\2q\u015c\3\2\2\2s\u015f")
        buf.write("\3\2\2\2u\u0168\3\2\2\2wx\t\2\2\2x\4\3\2\2\2y{\t\3\2\2")
        buf.write("zy\3\2\2\2{|\3\2\2\2|z\3\2\2\2|}\3\2\2\2}~\3\2\2\2~\177")
        buf.write("\b\3\2\2\177\6\3\2\2\2\u0080\u0081\7\61\2\2\u0081\u0082")
        buf.write("\7,\2\2\u0082\u0086\3\2\2\2\u0083\u0085\13\2\2\2\u0084")
        buf.write("\u0083\3\2\2\2\u0085\u0088\3\2\2\2\u0086\u0087\3\2\2\2")
        buf.write("\u0086\u0084\3\2\2\2\u0087\u0089\3\2\2\2\u0088\u0086\3")
        buf.write("\2\2\2\u0089\u008a\7,\2\2\u008a\u008b\7\61\2\2\u008b\u008c")
        buf.write("\3\2\2\2\u008c\u008d\b\4\2\2\u008d\b\3\2\2\2\u008e\u008f")
        buf.write("\7\61\2\2\u008f\u0090\7\61\2\2\u0090\u0094\3\2\2\2\u0091")
        buf.write("\u0093\n\4\2\2\u0092\u0091\3\2\2\2\u0093\u0096\3\2\2\2")
        buf.write("\u0094\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0097\3")
        buf.write("\2\2\2\u0096\u0094\3\2\2\2\u0097\u0098\b\5\2\2\u0098\n")
        buf.write("\3\2\2\2\u0099\u009d\t\5\2\2\u009a\u009c\5\3\2\2\u009b")
        buf.write("\u009a\3\2\2\2\u009c\u009f\3\2\2\2\u009d\u009b\3\2\2\2")
        buf.write("\u009d\u009e\3\2\2\2\u009e\f\3\2\2\2\u009f\u009d\3\2\2")
        buf.write("\2\u00a0\u00a2\7B\2\2\u00a1\u00a3\5\3\2\2\u00a2\u00a1")
        buf.write("\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4")
        buf.write("\u00a5\3\2\2\2\u00a5\16\3\2\2\2\u00a6\u00a7\7d\2\2\u00a7")
        buf.write("\u00a8\7t\2\2\u00a8\u00a9\7g\2\2\u00a9\u00aa\7c\2\2\u00aa")
        buf.write("\u00ab\7m\2\2\u00ab\20\3\2\2\2\u00ac\u00ad\7e\2\2\u00ad")
        buf.write("\u00ae\7q\2\2\u00ae\u00af\7p\2\2\u00af\u00b0\7v\2\2\u00b0")
        buf.write("\u00b1\7k\2\2\u00b1\u00b2\7p\2\2\u00b2\u00b3\7w\2\2\u00b3")
        buf.write("\u00b4\7g\2\2\u00b4\22\3\2\2\2\u00b5\u00b6\7k\2\2\u00b6")
        buf.write("\u00b7\7h\2\2\u00b7\24\3\2\2\2\u00b8\u00b9\7g\2\2\u00b9")
        buf.write("\u00ba\7n\2\2\u00ba\u00bb\7u\2\2\u00bb\u00bc\7g\2\2\u00bc")
        buf.write("\26\3\2\2\2\u00bd\u00be\7h\2\2\u00be\u00bf\7q\2\2\u00bf")
        buf.write("\u00c0\7t\2\2\u00c0\30\3\2\2\2\u00c1\u00c2\7v\2\2\u00c2")
        buf.write("\u00c3\7t\2\2\u00c3\u00c4\7w\2\2\u00c4\u00c5\7g\2\2\u00c5")
        buf.write("\32\3\2\2\2\u00c6\u00c7\7h\2\2\u00c7\u00c8\7c\2\2\u00c8")
        buf.write("\u00c9\7n\2\2\u00c9\u00ca\7u\2\2\u00ca\u00cb\7g\2\2\u00cb")
        buf.write("\34\3\2\2\2\u00cc\u00cd\7k\2\2\u00cd\u00ce\7p\2\2\u00ce")
        buf.write("\u00cf\7v\2\2\u00cf\36\3\2\2\2\u00d0\u00d1\7h\2\2\u00d1")
        buf.write("\u00d2\7n\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4\7c\2\2\u00d4")
        buf.write("\u00d5\7v\2\2\u00d5 \3\2\2\2\u00d6\u00d7\7d\2\2\u00d7")
        buf.write("\u00d8\7q\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da\7n\2\2\u00da")
        buf.write("\"\3\2\2\2\u00db\u00dc\7u\2\2\u00dc\u00dd\7v\2\2\u00dd")
        buf.write("\u00de\7t\2\2\u00de\u00df\7k\2\2\u00df\u00e0\7p\2\2\u00e0")
        buf.write("\u00e1\7i\2\2\u00e1$\3\2\2\2\u00e2\u00e3\7t\2\2\u00e3")
        buf.write("\u00e4\7g\2\2\u00e4\u00e5\7v\2\2\u00e5\u00e6\7w\2\2\u00e6")
        buf.write("\u00e7\7t\2\2\u00e7\u00e8\7p\2\2\u00e8&\3\2\2\2\u00e9")
        buf.write("\u00ea\7p\2\2\u00ea\u00eb\7w\2\2\u00eb\u00ec\7n\2\2\u00ec")
        buf.write("\u00ed\7n\2\2\u00ed(\3\2\2\2\u00ee\u00ef\7e\2\2\u00ef")
        buf.write("\u00f0\7n\2\2\u00f0\u00f1\7c\2\2\u00f1\u00f2\7u\2\2\u00f2")
        buf.write("\u00f3\7u\2\2\u00f3*\3\2\2\2\u00f4\u00f5\7e\2\2\u00f5")
        buf.write("\u00f6\7q\2\2\u00f6\u00f7\7p\2\2\u00f7\u00f8\7u\2\2\u00f8")
        buf.write("\u00f9\7v\2\2\u00f9\u00fa\7t\2\2\u00fa\u00fb\7w\2\2\u00fb")
        buf.write("\u00fc\7e\2\2\u00fc\u00fd\7v\2\2\u00fd\u00fe\7q\2\2\u00fe")
        buf.write("\u00ff\7t\2\2\u00ff,\3\2\2\2\u0100\u0101\7x\2\2\u0101")
        buf.write("\u0102\7c\2\2\u0102\u0103\7t\2\2\u0103.\3\2\2\2\u0104")
        buf.write("\u0105\7u\2\2\u0105\u0106\7g\2\2\u0106\u0107\7n\2\2\u0107")
        buf.write("\u0108\7h\2\2\u0108\60\3\2\2\2\u0109\u010a\7x\2\2\u010a")
        buf.write("\u010b\7q\2\2\u010b\u010c\7k\2\2\u010c\u010d\7f\2\2\u010d")
        buf.write("\62\3\2\2\2\u010e\u010f\7e\2\2\u010f\u0110\7q\2\2\u0110")
        buf.write("\u0111\7p\2\2\u0111\u0112\7u\2\2\u0112\u0113\7v\2\2\u0113")
        buf.write("\64\3\2\2\2\u0114\u0115\7h\2\2\u0115\u0116\7w\2\2\u0116")
        buf.write("\u0117\7p\2\2\u0117\u0118\7e\2\2\u0118\66\3\2\2\2\u0119")
        buf.write("\u011a\7-\2\2\u011a8\3\2\2\2\u011b\u011c\7/\2\2\u011c")
        buf.write(":\3\2\2\2\u011d\u011e\7,\2\2\u011e<\3\2\2\2\u011f\u0120")
        buf.write("\7\61\2\2\u0120>\3\2\2\2\u0121\u0122\7^\2\2\u0122@\3\2")
        buf.write("\2\2\u0123\u0124\7#\2\2\u0124B\3\2\2\2\u0125\u0126\7(")
        buf.write("\2\2\u0126\u0127\7(\2\2\u0127D\3\2\2\2\u0128\u0129\7~")
        buf.write("\2\2\u0129\u012a\7~\2\2\u012aF\3\2\2\2\u012b\u012c\7?")
        buf.write("\2\2\u012c\u012d\7?\2\2\u012dH\3\2\2\2\u012e\u012f\7?")
        buf.write("\2\2\u012fJ\3\2\2\2\u0130\u0131\7#\2\2\u0131\u0132\7?")
        buf.write("\2\2\u0132L\3\2\2\2\u0133\u0134\7>\2\2\u0134N\3\2\2\2")
        buf.write("\u0135\u0136\7>\2\2\u0136\u0137\7?\2\2\u0137P\3\2\2\2")
        buf.write("\u0138\u0139\7@\2\2\u0139R\3\2\2\2\u013a\u013b\7@\2\2")
        buf.write("\u013b\u013c\7?\2\2\u013cT\3\2\2\2\u013d\u013e\7<\2\2")
        buf.write("\u013e\u013f\7?\2\2\u013fV\3\2\2\2\u0140\u0141\7`\2\2")
        buf.write("\u0141X\3\2\2\2\u0142\u0143\7p\2\2\u0143\u0144\7g\2\2")
        buf.write("\u0144\u0145\7y\2\2\u0145Z\3\2\2\2\u0146\u0147\7\'\2\2")
        buf.write("\u0147\\\3\2\2\2\u0148\u0149\7*\2\2\u0149^\3\2\2\2\u014a")
        buf.write("\u014b\7+\2\2\u014b`\3\2\2\2\u014c\u014d\7]\2\2\u014d")
        buf.write("b\3\2\2\2\u014e\u014f\7_\2\2\u014fd\3\2\2\2\u0150\u0151")
        buf.write("\7\60\2\2\u0151f\3\2\2\2\u0152\u0153\7.\2\2\u0153h\3\2")
        buf.write("\2\2\u0154\u0155\7=\2\2\u0155j\3\2\2\2\u0156\u0157\7<")
        buf.write("\2\2\u0157l\3\2\2\2\u0158\u0159\7}\2\2\u0159n\3\2\2\2")
        buf.write("\u015a\u015b\7\177\2\2\u015bp\3\2\2\2\u015c\u015d\13\2")
        buf.write("\2\2\u015d\u015e\b9\3\2\u015er\3\2\2\2\u015f\u0163\7$")
        buf.write("\2\2\u0160\u0162\n\4\2\2\u0161\u0160\3\2\2\2\u0162\u0165")
        buf.write("\3\2\2\2\u0163\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164")
        buf.write("\u0166\3\2\2\2\u0165\u0163\3\2\2\2\u0166\u0167\b:\4\2")
        buf.write("\u0167t\3\2\2\2\u0168\u0169\7^\2\2\u0169\u016a\n\6\2\2")
        buf.write("\u016a\u016b\b;\5\2\u016bv\3\2\2\2\t\2|\u0086\u0094\u009d")
        buf.write("\u00a4\u0163\6\b\2\2\39\2\3:\3\3;\4")
        return buf.getvalue()


class CSlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    BLOCK_COMMENT = 2
    LINE_COMMENT = 3
    ID = 4
    AT_ID = 5
    BREAK = 6
    CONTINUE = 7
    IF = 8
    ELSE = 9
    FOR = 10
    TRUE = 11
    FALSE = 12
    INT = 13
    FLOAT = 14
    BOOL = 15
    STRING = 16
    RETURN = 17
    NULL = 18
    CLASS = 19
    CONSTRUCTOR = 20
    VAR = 21
    SELF = 22
    VOID = 23
    CONST = 24
    FUNC = 25
    PLUS = 26
    MINUS = 27
    STAR = 28
    SLASH = 29
    BACKSLASH = 30
    BANG = 31
    ANDAND = 32
    OROR = 33
    EQEQ = 34
    EQ = 35
    BANGEQ = 36
    LT = 37
    LTEQ = 38
    GT = 39
    GTEQ = 40
    COLONEQ = 41
    CARET = 42
    NEW = 43
    PERCENT = 44
    LPAREN = 45
    RPAREN = 46
    LBRACK = 47
    RBRACK = 48
    DOT = 49
    COMMA = 50
    SEMI = 51
    COLON = 52
    LBRACE = 53
    RBRACE = 54
    ERROR_TOKEN = 55
    UNCLOSE_STRING = 56
    ILLEGAL_ESCAPE = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'break'", "'continue'", "'if'", "'else'", "'for'", "'true'", 
            "'false'", "'int'", "'float'", "'bool'", "'string'", "'return'", 
            "'null'", "'class'", "'constructor'", "'var'", "'self'", "'void'", 
            "'const'", "'func'", "'+'", "'-'", "'*'", "'/'", "'\\'", "'!'", 
            "'&&'", "'||'", "'=='", "'='", "'!='", "'<'", "'<='", "'>'", 
            "'>='", "':='", "'^'", "'new'", "'%'", "'('", "')'", "'['", 
            "']'", "'.'", "','", "';'", "':'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "BLOCK_COMMENT", "LINE_COMMENT", "ID", "AT_ID", "BREAK", 
            "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", "INT", "FLOAT", 
            "BOOL", "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", 
            "VAR", "SELF", "VOID", "CONST", "FUNC", "PLUS", "MINUS", "STAR", 
            "SLASH", "BACKSLASH", "BANG", "ANDAND", "OROR", "EQEQ", "EQ", 
            "BANGEQ", "LT", "LTEQ", "GT", "GTEQ", "COLONEQ", "CARET", "NEW", 
            "PERCENT", "LPAREN", "RPAREN", "LBRACK", "RBRACK", "DOT", "COMMA", 
            "SEMI", "COLON", "LBRACE", "RBRACE", "ERROR_TOKEN", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "CHAR", "WS", "BLOCK_COMMENT", "LINE_COMMENT", "ID", "AT_ID", 
                  "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", 
                  "INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", 
                  "CONSTRUCTOR", "VAR", "SELF", "VOID", "CONST", "FUNC", 
                  "PLUS", "MINUS", "STAR", "SLASH", "BACKSLASH", "BANG", 
                  "ANDAND", "OROR", "EQEQ", "EQ", "BANGEQ", "LT", "LTEQ", 
                  "GT", "GTEQ", "COLONEQ", "CARET", "NEW", "PERCENT", "LPAREN", 
                  "RPAREN", "LBRACK", "RBRACK", "DOT", "COMMA", "SEMI", 
                  "COLON", "LBRACE", "RBRACE", "ERROR_TOKEN", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "CSlang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[55] = self.ERROR_TOKEN_action 
            actions[56] = self.UNCLOSE_STRING_action 
            actions[57] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise Exception("ERROR_TOKEN")
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise Exception("UNCLOSE_STRING")
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise Exception("ILLEGAL_ESCAPE")
     


