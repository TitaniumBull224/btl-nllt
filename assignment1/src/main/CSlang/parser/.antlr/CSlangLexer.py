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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u01b7\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3")
        buf.write("#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3")
        buf.write(")\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\63\3\63\3\64\6\64\u0140\n\64\r\64\16")
        buf.write("\64\u0141\3\65\6\65\u0145\n\65\r\65\16\65\u0146\3\65\3")
        buf.write("\65\3\65\3\65\3\65\5\65\u014e\n\65\3\66\3\66\7\66\u0152")
        buf.write("\n\66\f\66\16\66\u0155\13\66\3\66\3\66\3\66\3\67\3\67")
        buf.write("\3\67\3\67\7\67\u015e\n\67\f\67\16\67\u0161\13\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\38\38\38\38\78\u016c\n8\f8\168\u016f")
        buf.write("\138\38\38\39\39\79\u0175\n9\f9\169\u0178\139\3:\3:\6")
        buf.write(":\u017c\n:\r:\16:\u017d\3;\3;\7;\u0182\n;\f;\16;\u0185")
        buf.write("\13;\3<\3<\5<\u0189\n<\3<\6<\u018c\n<\r<\16<\u018d\3=")
        buf.write("\3=\3>\3>\3>\5>\u0195\n>\3?\6?\u0198\n?\r?\16?\u0199\3")
        buf.write("?\3?\3@\3@\7@\u01a0\n@\f@\16@\u01a3\13@\3@\3@\3A\3A\3")
        buf.write("A\3A\7A\u01ab\nA\fA\16A\u01ae\13A\3A\3A\3A\3A\3A\3B\3")
        buf.write("B\3B\3\u015f\2C\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65")
        buf.write("i\66k\67m8o9q:s;u\2w\2y\2{\2}<\177=\u0081>\u0083?\3\2")
        buf.write("\f\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\4\2GGgg\4\2")
        buf.write("--//\3\2\62;\6\2\f\f\17\17$$^^\t\2$$^^ddhhppttvv\5\2\13")
        buf.write("\f\17\17\"\"\t\2))^^ddhhppttvv\2\u01c3\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\3\u0085\3\2\2\2\5\u008b\3\2\2\2\7\u0094\3\2\2")
        buf.write("\2\t\u0097\3\2\2\2\13\u009c\3\2\2\2\r\u00a0\3\2\2\2\17")
        buf.write("\u00a5\3\2\2\2\21\u00ab\3\2\2\2\23\u00af\3\2\2\2\25\u00b5")
        buf.write("\3\2\2\2\27\u00ba\3\2\2\2\31\u00c1\3\2\2\2\33\u00c8\3")
        buf.write("\2\2\2\35\u00cd\3\2\2\2\37\u00d3\3\2\2\2!\u00df\3\2\2")
        buf.write("\2#\u00e3\3\2\2\2%\u00e8\3\2\2\2\'\u00ed\3\2\2\2)\u00f3")
        buf.write("\3\2\2\2+\u00f8\3\2\2\2-\u00fa\3\2\2\2/\u00fc\3\2\2\2")
        buf.write("\61\u00fe\3\2\2\2\63\u0100\3\2\2\2\65\u0102\3\2\2\2\67")
        buf.write("\u0104\3\2\2\29\u0106\3\2\2\2;\u0109\3\2\2\2=\u010c\3")
        buf.write("\2\2\2?\u010f\3\2\2\2A\u0112\3\2\2\2C\u0114\3\2\2\2E\u0117")
        buf.write("\3\2\2\2G\u0119\3\2\2\2I\u011c\3\2\2\2K\u011e\3\2\2\2")
        buf.write("M\u0121\3\2\2\2O\u0123\3\2\2\2Q\u0126\3\2\2\2S\u012a\3")
        buf.write("\2\2\2U\u012c\3\2\2\2W\u012e\3\2\2\2Y\u0130\3\2\2\2[\u0132")
        buf.write("\3\2\2\2]\u0134\3\2\2\2_\u0136\3\2\2\2a\u0138\3\2\2\2")
        buf.write("c\u013a\3\2\2\2e\u013c\3\2\2\2g\u013f\3\2\2\2i\u0144\3")
        buf.write("\2\2\2k\u014f\3\2\2\2m\u0159\3\2\2\2o\u0167\3\2\2\2q\u0172")
        buf.write("\3\2\2\2s\u0179\3\2\2\2u\u017f\3\2\2\2w\u0186\3\2\2\2")
        buf.write("y\u018f\3\2\2\2{\u0194\3\2\2\2}\u0197\3\2\2\2\177\u019d")
        buf.write("\3\2\2\2\u0081\u01a6\3\2\2\2\u0083\u01b4\3\2\2\2\u0085")
        buf.write("\u0086\7d\2\2\u0086\u0087\7t\2\2\u0087\u0088\7g\2\2\u0088")
        buf.write("\u0089\7c\2\2\u0089\u008a\7m\2\2\u008a\4\3\2\2\2\u008b")
        buf.write("\u008c\7e\2\2\u008c\u008d\7q\2\2\u008d\u008e\7p\2\2\u008e")
        buf.write("\u008f\7v\2\2\u008f\u0090\7k\2\2\u0090\u0091\7p\2\2\u0091")
        buf.write("\u0092\7w\2\2\u0092\u0093\7g\2\2\u0093\6\3\2\2\2\u0094")
        buf.write("\u0095\7k\2\2\u0095\u0096\7h\2\2\u0096\b\3\2\2\2\u0097")
        buf.write("\u0098\7g\2\2\u0098\u0099\7n\2\2\u0099\u009a\7u\2\2\u009a")
        buf.write("\u009b\7g\2\2\u009b\n\3\2\2\2\u009c\u009d\7h\2\2\u009d")
        buf.write("\u009e\7q\2\2\u009e\u009f\7t\2\2\u009f\f\3\2\2\2\u00a0")
        buf.write("\u00a1\7v\2\2\u00a1\u00a2\7t\2\2\u00a2\u00a3\7w\2\2\u00a3")
        buf.write("\u00a4\7g\2\2\u00a4\16\3\2\2\2\u00a5\u00a6\7h\2\2\u00a6")
        buf.write("\u00a7\7c\2\2\u00a7\u00a8\7n\2\2\u00a8\u00a9\7u\2\2\u00a9")
        buf.write("\u00aa\7g\2\2\u00aa\20\3\2\2\2\u00ab\u00ac\7k\2\2\u00ac")
        buf.write("\u00ad\7p\2\2\u00ad\u00ae\7v\2\2\u00ae\22\3\2\2\2\u00af")
        buf.write("\u00b0\7h\2\2\u00b0\u00b1\7n\2\2\u00b1\u00b2\7q\2\2\u00b2")
        buf.write("\u00b3\7c\2\2\u00b3\u00b4\7v\2\2\u00b4\24\3\2\2\2\u00b5")
        buf.write("\u00b6\7d\2\2\u00b6\u00b7\7q\2\2\u00b7\u00b8\7q\2\2\u00b8")
        buf.write("\u00b9\7n\2\2\u00b9\26\3\2\2\2\u00ba\u00bb\7u\2\2\u00bb")
        buf.write("\u00bc\7v\2\2\u00bc\u00bd\7t\2\2\u00bd\u00be\7k\2\2\u00be")
        buf.write("\u00bf\7p\2\2\u00bf\u00c0\7i\2\2\u00c0\30\3\2\2\2\u00c1")
        buf.write("\u00c2\7t\2\2\u00c2\u00c3\7g\2\2\u00c3\u00c4\7v\2\2\u00c4")
        buf.write("\u00c5\7w\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7\7p\2\2\u00c7")
        buf.write("\32\3\2\2\2\u00c8\u00c9\7p\2\2\u00c9\u00ca\7w\2\2\u00ca")
        buf.write("\u00cb\7n\2\2\u00cb\u00cc\7n\2\2\u00cc\34\3\2\2\2\u00cd")
        buf.write("\u00ce\7e\2\2\u00ce\u00cf\7n\2\2\u00cf\u00d0\7c\2\2\u00d0")
        buf.write("\u00d1\7u\2\2\u00d1\u00d2\7u\2\2\u00d2\36\3\2\2\2\u00d3")
        buf.write("\u00d4\7e\2\2\u00d4\u00d5\7q\2\2\u00d5\u00d6\7p\2\2\u00d6")
        buf.write("\u00d7\7u\2\2\u00d7\u00d8\7v\2\2\u00d8\u00d9\7t\2\2\u00d9")
        buf.write("\u00da\7w\2\2\u00da\u00db\7e\2\2\u00db\u00dc\7v\2\2\u00dc")
        buf.write("\u00dd\7q\2\2\u00dd\u00de\7t\2\2\u00de \3\2\2\2\u00df")
        buf.write("\u00e0\7x\2\2\u00e0\u00e1\7c\2\2\u00e1\u00e2\7t\2\2\u00e2")
        buf.write("\"\3\2\2\2\u00e3\u00e4\7u\2\2\u00e4\u00e5\7g\2\2\u00e5")
        buf.write("\u00e6\7n\2\2\u00e6\u00e7\7h\2\2\u00e7$\3\2\2\2\u00e8")
        buf.write("\u00e9\7x\2\2\u00e9\u00ea\7q\2\2\u00ea\u00eb\7k\2\2\u00eb")
        buf.write("\u00ec\7f\2\2\u00ec&\3\2\2\2\u00ed\u00ee\7e\2\2\u00ee")
        buf.write("\u00ef\7q\2\2\u00ef\u00f0\7p\2\2\u00f0\u00f1\7u\2\2\u00f1")
        buf.write("\u00f2\7v\2\2\u00f2(\3\2\2\2\u00f3\u00f4\7h\2\2\u00f4")
        buf.write("\u00f5\7w\2\2\u00f5\u00f6\7p\2\2\u00f6\u00f7\7e\2\2\u00f7")
        buf.write("*\3\2\2\2\u00f8\u00f9\7-\2\2\u00f9,\3\2\2\2\u00fa\u00fb")
        buf.write("\7/\2\2\u00fb.\3\2\2\2\u00fc\u00fd\7,\2\2\u00fd\60\3\2")
        buf.write("\2\2\u00fe\u00ff\7\61\2\2\u00ff\62\3\2\2\2\u0100\u0101")
        buf.write("\7^\2\2\u0101\64\3\2\2\2\u0102\u0103\7\'\2\2\u0103\66")
        buf.write("\3\2\2\2\u0104\u0105\7#\2\2\u01058\3\2\2\2\u0106\u0107")
        buf.write("\7(\2\2\u0107\u0108\7(\2\2\u0108:\3\2\2\2\u0109\u010a")
        buf.write("\7~\2\2\u010a\u010b\7~\2\2\u010b<\3\2\2\2\u010c\u010d")
        buf.write("\7?\2\2\u010d\u010e\7?\2\2\u010e>\3\2\2\2\u010f\u0110")
        buf.write("\7#\2\2\u0110\u0111\7?\2\2\u0111@\3\2\2\2\u0112\u0113")
        buf.write("\7>\2\2\u0113B\3\2\2\2\u0114\u0115\7>\2\2\u0115\u0116")
        buf.write("\7?\2\2\u0116D\3\2\2\2\u0117\u0118\7@\2\2\u0118F\3\2\2")
        buf.write("\2\u0119\u011a\7@\2\2\u011a\u011b\7?\2\2\u011bH\3\2\2")
        buf.write("\2\u011c\u011d\7?\2\2\u011dJ\3\2\2\2\u011e\u011f\7<\2")
        buf.write("\2\u011f\u0120\7?\2\2\u0120L\3\2\2\2\u0121\u0122\7`\2")
        buf.write("\2\u0122N\3\2\2\2\u0123\u0124\7>\2\2\u0124\u0125\7/\2")
        buf.write("\2\u0125P\3\2\2\2\u0126\u0127\7p\2\2\u0127\u0128\7g\2")
        buf.write("\2\u0128\u0129\7y\2\2\u0129R\3\2\2\2\u012a\u012b\7*\2")
        buf.write("\2\u012bT\3\2\2\2\u012c\u012d\7+\2\2\u012dV\3\2\2\2\u012e")
        buf.write("\u012f\7]\2\2\u012fX\3\2\2\2\u0130\u0131\7_\2\2\u0131")
        buf.write("Z\3\2\2\2\u0132\u0133\7}\2\2\u0133\\\3\2\2\2\u0134\u0135")
        buf.write("\7\177\2\2\u0135^\3\2\2\2\u0136\u0137\7\60\2\2\u0137`")
        buf.write("\3\2\2\2\u0138\u0139\7.\2\2\u0139b\3\2\2\2\u013a\u013b")
        buf.write("\7=\2\2\u013bd\3\2\2\2\u013c\u013d\7<\2\2\u013df\3\2\2")
        buf.write("\2\u013e\u0140\5y=\2\u013f\u013e\3\2\2\2\u0140\u0141\3")
        buf.write("\2\2\2\u0141\u013f\3\2\2\2\u0141\u0142\3\2\2\2\u0142h")
        buf.write("\3\2\2\2\u0143\u0145\5y=\2\u0144\u0143\3\2\2\2\u0145\u0146")
        buf.write("\3\2\2\2\u0146\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147")
        buf.write("\u014d\3\2\2\2\u0148\u014e\5u;\2\u0149\u014e\5w<\2\u014a")
        buf.write("\u014b\5u;\2\u014b\u014c\5w<\2\u014c\u014e\3\2\2\2\u014d")
        buf.write("\u0148\3\2\2\2\u014d\u0149\3\2\2\2\u014d\u014a\3\2\2\2")
        buf.write("\u014ej\3\2\2\2\u014f\u0153\7$\2\2\u0150\u0152\5{>\2\u0151")
        buf.write("\u0150\3\2\2\2\u0152\u0155\3\2\2\2\u0153\u0151\3\2\2\2")
        buf.write("\u0153\u0154\3\2\2\2\u0154\u0156\3\2\2\2\u0155\u0153\3")
        buf.write("\2\2\2\u0156\u0157\7$\2\2\u0157\u0158\b\66\2\2\u0158l")
        buf.write("\3\2\2\2\u0159\u015a\7\61\2\2\u015a\u015b\7,\2\2\u015b")
        buf.write("\u015f\3\2\2\2\u015c\u015e\13\2\2\2\u015d\u015c\3\2\2")
        buf.write("\2\u015e\u0161\3\2\2\2\u015f\u0160\3\2\2\2\u015f\u015d")
        buf.write("\3\2\2\2\u0160\u0162\3\2\2\2\u0161\u015f\3\2\2\2\u0162")
        buf.write("\u0163\7,\2\2\u0163\u0164\7\61\2\2\u0164\u0165\3\2\2\2")
        buf.write("\u0165\u0166\b\67\3\2\u0166n\3\2\2\2\u0167\u0168\7\61")
        buf.write("\2\2\u0168\u0169\7\61\2\2\u0169\u016d\3\2\2\2\u016a\u016c")
        buf.write("\n\2\2\2\u016b\u016a\3\2\2\2\u016c\u016f\3\2\2\2\u016d")
        buf.write("\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u0170\3\2\2\2")
        buf.write("\u016f\u016d\3\2\2\2\u0170\u0171\b8\3\2\u0171p\3\2\2\2")
        buf.write("\u0172\u0176\t\3\2\2\u0173\u0175\t\4\2\2\u0174\u0173\3")
        buf.write("\2\2\2\u0175\u0178\3\2\2\2\u0176\u0174\3\2\2\2\u0176\u0177")
        buf.write("\3\2\2\2\u0177r\3\2\2\2\u0178\u0176\3\2\2\2\u0179\u017b")
        buf.write("\7B\2\2\u017a\u017c\t\4\2\2\u017b\u017a\3\2\2\2\u017c")
        buf.write("\u017d\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017e\3\2\2\2")
        buf.write("\u017et\3\2\2\2\u017f\u0183\5_\60\2\u0180\u0182\5y=\2")
        buf.write("\u0181\u0180\3\2\2\2\u0182\u0185\3\2\2\2\u0183\u0181\3")
        buf.write("\2\2\2\u0183\u0184\3\2\2\2\u0184v\3\2\2\2\u0185\u0183")
        buf.write("\3\2\2\2\u0186\u0188\t\5\2\2\u0187\u0189\t\6\2\2\u0188")
        buf.write("\u0187\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018b\3\2\2\2")
        buf.write("\u018a\u018c\5y=\2\u018b\u018a\3\2\2\2\u018c\u018d\3\2")
        buf.write("\2\2\u018d\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018ex\3")
        buf.write("\2\2\2\u018f\u0190\t\7\2\2\u0190z\3\2\2\2\u0191\u0195")
        buf.write("\n\b\2\2\u0192\u0193\7^\2\2\u0193\u0195\t\t\2\2\u0194")
        buf.write("\u0191\3\2\2\2\u0194\u0192\3\2\2\2\u0195|\3\2\2\2\u0196")
        buf.write("\u0198\t\n\2\2\u0197\u0196\3\2\2\2\u0198\u0199\3\2\2\2")
        buf.write("\u0199\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u019b\3")
        buf.write("\2\2\2\u019b\u019c\b?\3\2\u019c~\3\2\2\2\u019d\u01a1\7")
        buf.write("$\2\2\u019e\u01a0\5{>\2\u019f\u019e\3\2\2\2\u01a0\u01a3")
        buf.write("\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2")
        buf.write("\u01a4\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01a5\b@\4\2")
        buf.write("\u01a5\u0080\3\2\2\2\u01a6\u01ac\7$\2\2\u01a7\u01a8\7")
        buf.write("^\2\2\u01a8\u01ab\t\13\2\2\u01a9\u01ab\n\b\2\2\u01aa\u01a7")
        buf.write("\3\2\2\2\u01aa\u01a9\3\2\2\2\u01ab\u01ae\3\2\2\2\u01ac")
        buf.write("\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01af\3\2\2\2")
        buf.write("\u01ae\u01ac\3\2\2\2\u01af\u01b0\7^\2\2\u01b0\u01b1\n")
        buf.write("\13\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b3\bA\5\2\u01b3\u0082")
        buf.write("\3\2\2\2\u01b4\u01b5\13\2\2\2\u01b5\u01b6\bB\6\2\u01b6")
        buf.write("\u0084\3\2\2\2\23\2\u0141\u0146\u014d\u0153\u015f\u016d")
        buf.write("\u0176\u017d\u0183\u0188\u018d\u0194\u0199\u01a1\u01aa")
        buf.write("\u01ac\7\3\66\2\b\2\2\3@\3\3A\4\3B\5")
        return buf.getvalue()


class CSlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BREAK = 1
    CONTINUE = 2
    IF = 3
    ELSE = 4
    FOR = 5
    TRUE = 6
    FALSE = 7
    INT = 8
    FLOAT = 9
    BOOL = 10
    STRING = 11
    RETURN = 12
    NULL = 13
    CLASS = 14
    CONSTRUCTOR = 15
    VAR = 16
    SELF = 17
    VOID = 18
    CONST = 19
    FUNC = 20
    PLUS = 21
    MINUS = 22
    MUL = 23
    DIV_FLOAT = 24
    DIV_INT = 25
    MOD = 26
    NEG = 27
    AND = 28
    OR = 29
    EQ = 30
    NEQ = 31
    LT = 32
    LTEQ = 33
    GT = 34
    GTEQ = 35
    DECLARE = 36
    ASSIGN = 37
    CONCATE = 38
    ARROW = 39
    NEW = 40
    LPN = 41
    RPN = 42
    LBK = 43
    RBK = 44
    LBR = 45
    RBR = 46
    DOT = 47
    CM = 48
    SM = 49
    COL = 50
    INT_LIT = 51
    FLOAT_LIT = 52
    STR_LIT = 53
    BLOCK_COMMENT = 54
    LINE_COMMENT = 55
    ID = 56
    AT_ID = 57
    WS = 58
    UNCLOSE_STRING = 59
    ILLEGAL_ESCAPE = 60
    ERROR_CHAR = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'break'", "'continue'", "'if'", "'else'", "'for'", "'true'", 
            "'false'", "'int'", "'float'", "'bool'", "'string'", "'return'", 
            "'null'", "'class'", "'constructor'", "'var'", "'self'", "'void'", 
            "'const'", "'func'", "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", 
            "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", 
            "'>='", "'='", "':='", "'^'", "'<-'", "'new'", "'('", "')'", 
            "'['", "']'", "'{'", "'}'", "'.'", "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", "INT", 
            "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", 
            "VAR", "SELF", "VOID", "CONST", "FUNC", "PLUS", "MINUS", "MUL", 
            "DIV_FLOAT", "DIV_INT", "MOD", "NEG", "AND", "OR", "EQ", "NEQ", 
            "LT", "LTEQ", "GT", "GTEQ", "DECLARE", "ASSIGN", "CONCATE", 
            "ARROW", "NEW", "LPN", "RPN", "LBK", "RBK", "LBR", "RBR", "DOT", 
            "CM", "SM", "COL", "INT_LIT", "FLOAT_LIT", "STR_LIT", "BLOCK_COMMENT", 
            "LINE_COMMENT", "ID", "AT_ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", 
                  "INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", 
                  "CONSTRUCTOR", "VAR", "SELF", "VOID", "CONST", "FUNC", 
                  "PLUS", "MINUS", "MUL", "DIV_FLOAT", "DIV_INT", "MOD", 
                  "NEG", "AND", "OR", "EQ", "NEQ", "LT", "LTEQ", "GT", "GTEQ", 
                  "DECLARE", "ASSIGN", "CONCATE", "ARROW", "NEW", "LPN", 
                  "RPN", "LBK", "RBK", "LBR", "RBR", "DOT", "CM", "SM", 
                  "COL", "INT_LIT", "FLOAT_LIT", "STR_LIT", "BLOCK_COMMENT", 
                  "LINE_COMMENT", "ID", "AT_ID", "FLOAT_DEC", "FLOAT_EXP", 
                  "DIGIT", "STR_CHAR", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

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
            actions[52] = self.STR_LIT_action 
            actions[62] = self.UNCLOSE_STRING_action 
            actions[63] = self.ILLEGAL_ESCAPE_action 
            actions[64] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STR_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text[1:]; raise UncloseString(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:]; raise IllegalEscape(self.text)
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


