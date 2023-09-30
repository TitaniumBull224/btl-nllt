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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u01bd\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"")
        buf.write("\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3")
        buf.write("(\3)\3)\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60")
        buf.write("\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\6\64\u0142\n")
        buf.write("\64\r\64\16\64\u0143\3\65\6\65\u0147\n\65\r\65\16\65\u0148")
        buf.write("\3\65\3\65\3\65\3\65\3\65\5\65\u0150\n\65\3\66\3\66\5")
        buf.write("\66\u0154\n\66\3\67\3\67\7\67\u0158\n\67\f\67\16\67\u015b")
        buf.write("\13\67\3\67\3\67\3\67\38\38\38\38\78\u0164\n8\f8\168\u0167")
        buf.write("\138\38\38\38\38\38\39\39\39\39\79\u0172\n9\f9\169\u0175")
        buf.write("\139\39\39\3:\3:\7:\u017b\n:\f:\16:\u017e\13:\3;\3;\6")
        buf.write(";\u0182\n;\r;\16;\u0183\3<\3<\7<\u0188\n<\f<\16<\u018b")
        buf.write("\13<\3=\3=\5=\u018f\n=\3=\6=\u0192\n=\r=\16=\u0193\3>")
        buf.write("\3>\3?\3?\3?\5?\u019b\n?\3@\6@\u019e\n@\r@\16@\u019f\3")
        buf.write("@\3@\3A\3A\7A\u01a6\nA\fA\16A\u01a9\13A\3A\3A\3B\3B\3")
        buf.write("B\3B\7B\u01b1\nB\fB\16B\u01b4\13B\3B\3B\3B\3B\3B\3C\3")
        buf.write("C\3C\3\u0165\2D\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65")
        buf.write("i\66k\67m8o9q:s;u<w\2y\2{\2}\2\177=\u0081>\u0083?\u0085")
        buf.write("@\3\2\f\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\4\2GG")
        buf.write("gg\4\2--//\3\2\62;\6\2\f\f\17\17$$^^\t\2$$^^ddhhppttv")
        buf.write("v\5\2\n\f\16\17\"\"\t\2))^^ddhhppttvv\2\u01ca\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2u\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2")
        buf.write("\u0083\3\2\2\2\2\u0085\3\2\2\2\3\u0087\3\2\2\2\5\u008d")
        buf.write("\3\2\2\2\7\u0096\3\2\2\2\t\u0099\3\2\2\2\13\u009e\3\2")
        buf.write("\2\2\r\u00a2\3\2\2\2\17\u00a7\3\2\2\2\21\u00ad\3\2\2\2")
        buf.write("\23\u00b1\3\2\2\2\25\u00b7\3\2\2\2\27\u00bc\3\2\2\2\31")
        buf.write("\u00c3\3\2\2\2\33\u00ca\3\2\2\2\35\u00cf\3\2\2\2\37\u00d5")
        buf.write("\3\2\2\2!\u00e1\3\2\2\2#\u00e5\3\2\2\2%\u00ea\3\2\2\2")
        buf.write("\'\u00ef\3\2\2\2)\u00f5\3\2\2\2+\u00fa\3\2\2\2-\u00fc")
        buf.write("\3\2\2\2/\u00fe\3\2\2\2\61\u0100\3\2\2\2\63\u0102\3\2")
        buf.write("\2\2\65\u0104\3\2\2\2\67\u0106\3\2\2\29\u0108\3\2\2\2")
        buf.write(";\u010b\3\2\2\2=\u010e\3\2\2\2?\u0111\3\2\2\2A\u0114\3")
        buf.write("\2\2\2C\u0116\3\2\2\2E\u0119\3\2\2\2G\u011b\3\2\2\2I\u011e")
        buf.write("\3\2\2\2K\u0120\3\2\2\2M\u0123\3\2\2\2O\u0125\3\2\2\2")
        buf.write("Q\u0128\3\2\2\2S\u012c\3\2\2\2U\u012e\3\2\2\2W\u0130\3")
        buf.write("\2\2\2Y\u0132\3\2\2\2[\u0134\3\2\2\2]\u0136\3\2\2\2_\u0138")
        buf.write("\3\2\2\2a\u013a\3\2\2\2c\u013c\3\2\2\2e\u013e\3\2\2\2")
        buf.write("g\u0141\3\2\2\2i\u0146\3\2\2\2k\u0153\3\2\2\2m\u0155\3")
        buf.write("\2\2\2o\u015f\3\2\2\2q\u016d\3\2\2\2s\u0178\3\2\2\2u\u017f")
        buf.write("\3\2\2\2w\u0185\3\2\2\2y\u018c\3\2\2\2{\u0195\3\2\2\2")
        buf.write("}\u019a\3\2\2\2\177\u019d\3\2\2\2\u0081\u01a3\3\2\2\2")
        buf.write("\u0083\u01ac\3\2\2\2\u0085\u01ba\3\2\2\2\u0087\u0088\7")
        buf.write("d\2\2\u0088\u0089\7t\2\2\u0089\u008a\7g\2\2\u008a\u008b")
        buf.write("\7c\2\2\u008b\u008c\7m\2\2\u008c\4\3\2\2\2\u008d\u008e")
        buf.write("\7e\2\2\u008e\u008f\7q\2\2\u008f\u0090\7p\2\2\u0090\u0091")
        buf.write("\7v\2\2\u0091\u0092\7k\2\2\u0092\u0093\7p\2\2\u0093\u0094")
        buf.write("\7w\2\2\u0094\u0095\7g\2\2\u0095\6\3\2\2\2\u0096\u0097")
        buf.write("\7k\2\2\u0097\u0098\7h\2\2\u0098\b\3\2\2\2\u0099\u009a")
        buf.write("\7g\2\2\u009a\u009b\7n\2\2\u009b\u009c\7u\2\2\u009c\u009d")
        buf.write("\7g\2\2\u009d\n\3\2\2\2\u009e\u009f\7h\2\2\u009f\u00a0")
        buf.write("\7q\2\2\u00a0\u00a1\7t\2\2\u00a1\f\3\2\2\2\u00a2\u00a3")
        buf.write("\7v\2\2\u00a3\u00a4\7t\2\2\u00a4\u00a5\7w\2\2\u00a5\u00a6")
        buf.write("\7g\2\2\u00a6\16\3\2\2\2\u00a7\u00a8\7h\2\2\u00a8\u00a9")
        buf.write("\7c\2\2\u00a9\u00aa\7n\2\2\u00aa\u00ab\7u\2\2\u00ab\u00ac")
        buf.write("\7g\2\2\u00ac\20\3\2\2\2\u00ad\u00ae\7k\2\2\u00ae\u00af")
        buf.write("\7p\2\2\u00af\u00b0\7v\2\2\u00b0\22\3\2\2\2\u00b1\u00b2")
        buf.write("\7h\2\2\u00b2\u00b3\7n\2\2\u00b3\u00b4\7q\2\2\u00b4\u00b5")
        buf.write("\7c\2\2\u00b5\u00b6\7v\2\2\u00b6\24\3\2\2\2\u00b7\u00b8")
        buf.write("\7d\2\2\u00b8\u00b9\7q\2\2\u00b9\u00ba\7q\2\2\u00ba\u00bb")
        buf.write("\7n\2\2\u00bb\26\3\2\2\2\u00bc\u00bd\7u\2\2\u00bd\u00be")
        buf.write("\7v\2\2\u00be\u00bf\7t\2\2\u00bf\u00c0\7k\2\2\u00c0\u00c1")
        buf.write("\7p\2\2\u00c1\u00c2\7i\2\2\u00c2\30\3\2\2\2\u00c3\u00c4")
        buf.write("\7t\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6\7v\2\2\u00c6\u00c7")
        buf.write("\7w\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9\7p\2\2\u00c9\32")
        buf.write("\3\2\2\2\u00ca\u00cb\7p\2\2\u00cb\u00cc\7w\2\2\u00cc\u00cd")
        buf.write("\7n\2\2\u00cd\u00ce\7n\2\2\u00ce\34\3\2\2\2\u00cf\u00d0")
        buf.write("\7e\2\2\u00d0\u00d1\7n\2\2\u00d1\u00d2\7c\2\2\u00d2\u00d3")
        buf.write("\7u\2\2\u00d3\u00d4\7u\2\2\u00d4\36\3\2\2\2\u00d5\u00d6")
        buf.write("\7e\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8\7p\2\2\u00d8\u00d9")
        buf.write("\7u\2\2\u00d9\u00da\7v\2\2\u00da\u00db\7t\2\2\u00db\u00dc")
        buf.write("\7w\2\2\u00dc\u00dd\7e\2\2\u00dd\u00de\7v\2\2\u00de\u00df")
        buf.write("\7q\2\2\u00df\u00e0\7t\2\2\u00e0 \3\2\2\2\u00e1\u00e2")
        buf.write("\7x\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4\7t\2\2\u00e4\"")
        buf.write("\3\2\2\2\u00e5\u00e6\7u\2\2\u00e6\u00e7\7g\2\2\u00e7\u00e8")
        buf.write("\7n\2\2\u00e8\u00e9\7h\2\2\u00e9$\3\2\2\2\u00ea\u00eb")
        buf.write("\7x\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee")
        buf.write("\7f\2\2\u00ee&\3\2\2\2\u00ef\u00f0\7e\2\2\u00f0\u00f1")
        buf.write("\7q\2\2\u00f1\u00f2\7p\2\2\u00f2\u00f3\7u\2\2\u00f3\u00f4")
        buf.write("\7v\2\2\u00f4(\3\2\2\2\u00f5\u00f6\7h\2\2\u00f6\u00f7")
        buf.write("\7w\2\2\u00f7\u00f8\7p\2\2\u00f8\u00f9\7e\2\2\u00f9*\3")
        buf.write("\2\2\2\u00fa\u00fb\7-\2\2\u00fb,\3\2\2\2\u00fc\u00fd\7")
        buf.write("/\2\2\u00fd.\3\2\2\2\u00fe\u00ff\7,\2\2\u00ff\60\3\2\2")
        buf.write("\2\u0100\u0101\7\61\2\2\u0101\62\3\2\2\2\u0102\u0103\7")
        buf.write("^\2\2\u0103\64\3\2\2\2\u0104\u0105\7\'\2\2\u0105\66\3")
        buf.write("\2\2\2\u0106\u0107\7#\2\2\u01078\3\2\2\2\u0108\u0109\7")
        buf.write("(\2\2\u0109\u010a\7(\2\2\u010a:\3\2\2\2\u010b\u010c\7")
        buf.write("~\2\2\u010c\u010d\7~\2\2\u010d<\3\2\2\2\u010e\u010f\7")
        buf.write("?\2\2\u010f\u0110\7?\2\2\u0110>\3\2\2\2\u0111\u0112\7")
        buf.write("#\2\2\u0112\u0113\7?\2\2\u0113@\3\2\2\2\u0114\u0115\7")
        buf.write(">\2\2\u0115B\3\2\2\2\u0116\u0117\7>\2\2\u0117\u0118\7")
        buf.write("?\2\2\u0118D\3\2\2\2\u0119\u011a\7@\2\2\u011aF\3\2\2\2")
        buf.write("\u011b\u011c\7@\2\2\u011c\u011d\7?\2\2\u011dH\3\2\2\2")
        buf.write("\u011e\u011f\7?\2\2\u011fJ\3\2\2\2\u0120\u0121\7<\2\2")
        buf.write("\u0121\u0122\7?\2\2\u0122L\3\2\2\2\u0123\u0124\7`\2\2")
        buf.write("\u0124N\3\2\2\2\u0125\u0126\7>\2\2\u0126\u0127\7/\2\2")
        buf.write("\u0127P\3\2\2\2\u0128\u0129\7p\2\2\u0129\u012a\7g\2\2")
        buf.write("\u012a\u012b\7y\2\2\u012bR\3\2\2\2\u012c\u012d\7*\2\2")
        buf.write("\u012dT\3\2\2\2\u012e\u012f\7+\2\2\u012fV\3\2\2\2\u0130")
        buf.write("\u0131\7]\2\2\u0131X\3\2\2\2\u0132\u0133\7_\2\2\u0133")
        buf.write("Z\3\2\2\2\u0134\u0135\7}\2\2\u0135\\\3\2\2\2\u0136\u0137")
        buf.write("\7\177\2\2\u0137^\3\2\2\2\u0138\u0139\7\60\2\2\u0139`")
        buf.write("\3\2\2\2\u013a\u013b\7.\2\2\u013bb\3\2\2\2\u013c\u013d")
        buf.write("\7=\2\2\u013dd\3\2\2\2\u013e\u013f\7<\2\2\u013ff\3\2\2")
        buf.write("\2\u0140\u0142\5{>\2\u0141\u0140\3\2\2\2\u0142\u0143\3")
        buf.write("\2\2\2\u0143\u0141\3\2\2\2\u0143\u0144\3\2\2\2\u0144h")
        buf.write("\3\2\2\2\u0145\u0147\5{>\2\u0146\u0145\3\2\2\2\u0147\u0148")
        buf.write("\3\2\2\2\u0148\u0146\3\2\2\2\u0148\u0149\3\2\2\2\u0149")
        buf.write("\u014f\3\2\2\2\u014a\u0150\5w<\2\u014b\u0150\5y=\2\u014c")
        buf.write("\u014d\5w<\2\u014d\u014e\5y=\2\u014e\u0150\3\2\2\2\u014f")
        buf.write("\u014a\3\2\2\2\u014f\u014b\3\2\2\2\u014f\u014c\3\2\2\2")
        buf.write("\u0150j\3\2\2\2\u0151\u0154\5\r\7\2\u0152\u0154\5\17\b")
        buf.write("\2\u0153\u0151\3\2\2\2\u0153\u0152\3\2\2\2\u0154l\3\2")
        buf.write("\2\2\u0155\u0159\7$\2\2\u0156\u0158\5}?\2\u0157\u0156")
        buf.write("\3\2\2\2\u0158\u015b\3\2\2\2\u0159\u0157\3\2\2\2\u0159")
        buf.write("\u015a\3\2\2\2\u015a\u015c\3\2\2\2\u015b\u0159\3\2\2\2")
        buf.write("\u015c\u015d\7$\2\2\u015d\u015e\b\67\2\2\u015en\3\2\2")
        buf.write("\2\u015f\u0160\7\61\2\2\u0160\u0161\7,\2\2\u0161\u0165")
        buf.write("\3\2\2\2\u0162\u0164\13\2\2\2\u0163\u0162\3\2\2\2\u0164")
        buf.write("\u0167\3\2\2\2\u0165\u0166\3\2\2\2\u0165\u0163\3\2\2\2")
        buf.write("\u0166\u0168\3\2\2\2\u0167\u0165\3\2\2\2\u0168\u0169\7")
        buf.write(",\2\2\u0169\u016a\7\61\2\2\u016a\u016b\3\2\2\2\u016b\u016c")
        buf.write("\b8\3\2\u016cp\3\2\2\2\u016d\u016e\7\61\2\2\u016e\u016f")
        buf.write("\7\61\2\2\u016f\u0173\3\2\2\2\u0170\u0172\n\2\2\2\u0171")
        buf.write("\u0170\3\2\2\2\u0172\u0175\3\2\2\2\u0173\u0171\3\2\2\2")
        buf.write("\u0173\u0174\3\2\2\2\u0174\u0176\3\2\2\2\u0175\u0173\3")
        buf.write("\2\2\2\u0176\u0177\b9\3\2\u0177r\3\2\2\2\u0178\u017c\t")
        buf.write("\3\2\2\u0179\u017b\t\4\2\2\u017a\u0179\3\2\2\2\u017b\u017e")
        buf.write("\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017d")
        buf.write("t\3\2\2\2\u017e\u017c\3\2\2\2\u017f\u0181\7B\2\2\u0180")
        buf.write("\u0182\t\4\2\2\u0181\u0180\3\2\2\2\u0182\u0183\3\2\2\2")
        buf.write("\u0183\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184v\3\2\2")
        buf.write("\2\u0185\u0189\5_\60\2\u0186\u0188\5{>\2\u0187\u0186\3")
        buf.write("\2\2\2\u0188\u018b\3\2\2\2\u0189\u0187\3\2\2\2\u0189\u018a")
        buf.write("\3\2\2\2\u018ax\3\2\2\2\u018b\u0189\3\2\2\2\u018c\u018e")
        buf.write("\t\5\2\2\u018d\u018f\t\6\2\2\u018e\u018d\3\2\2\2\u018e")
        buf.write("\u018f\3\2\2\2\u018f\u0191\3\2\2\2\u0190\u0192\5{>\2\u0191")
        buf.write("\u0190\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0191\3\2\2\2")
        buf.write("\u0193\u0194\3\2\2\2\u0194z\3\2\2\2\u0195\u0196\t\7\2")
        buf.write("\2\u0196|\3\2\2\2\u0197\u019b\n\b\2\2\u0198\u0199\7^\2")
        buf.write("\2\u0199\u019b\t\t\2\2\u019a\u0197\3\2\2\2\u019a\u0198")
        buf.write("\3\2\2\2\u019b~\3\2\2\2\u019c\u019e\t\n\2\2\u019d\u019c")
        buf.write("\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u019d\3\2\2\2\u019f")
        buf.write("\u01a0\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a2\b@\3\2")
        buf.write("\u01a2\u0080\3\2\2\2\u01a3\u01a7\7$\2\2\u01a4\u01a6\5")
        buf.write("}?\2\u01a5\u01a4\3\2\2\2\u01a6\u01a9\3\2\2\2\u01a7\u01a5")
        buf.write("\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01aa\3\2\2\2\u01a9")
        buf.write("\u01a7\3\2\2\2\u01aa\u01ab\bA\4\2\u01ab\u0082\3\2\2\2")
        buf.write("\u01ac\u01b2\7$\2\2\u01ad\u01ae\7^\2\2\u01ae\u01b1\t\13")
        buf.write("\2\2\u01af\u01b1\n\b\2\2\u01b0\u01ad\3\2\2\2\u01b0\u01af")
        buf.write("\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2")
        buf.write("\u01b3\3\2\2\2\u01b3\u01b5\3\2\2\2\u01b4\u01b2\3\2\2\2")
        buf.write("\u01b5\u01b6\7^\2\2\u01b6\u01b7\n\13\2\2\u01b7\u01b8\3")
        buf.write("\2\2\2\u01b8\u01b9\bB\5\2\u01b9\u0084\3\2\2\2\u01ba\u01bb")
        buf.write("\13\2\2\2\u01bb\u01bc\bC\6\2\u01bc\u0086\3\2\2\2\24\2")
        buf.write("\u0143\u0148\u014f\u0153\u0159\u0165\u0173\u017c\u0183")
        buf.write("\u0189\u018e\u0193\u019a\u019f\u01a7\u01b0\u01b2\7\3\67")
        buf.write("\2\b\2\2\3A\3\3B\4\3C\5")
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
    BOOL_LIT = 53
    STR_LIT = 54
    BLOCK_COMMENT = 55
    LINE_COMMENT = 56
    ID = 57
    AT_ID = 58
    WS = 59
    UNCLOSE_STRING = 60
    ILLEGAL_ESCAPE = 61
    ERROR_CHAR = 62

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
            "CM", "SM", "COL", "INT_LIT", "FLOAT_LIT", "BOOL_LIT", "STR_LIT", 
            "BLOCK_COMMENT", "LINE_COMMENT", "ID", "AT_ID", "WS", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", 
                  "INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", 
                  "CONSTRUCTOR", "VAR", "SELF", "VOID", "CONST", "FUNC", 
                  "PLUS", "MINUS", "MUL", "DIV_FLOAT", "DIV_INT", "MOD", 
                  "NEG", "AND", "OR", "EQ", "NEQ", "LT", "LTEQ", "GT", "GTEQ", 
                  "DECLARE", "ASSIGN", "CONCATE", "ARROW", "NEW", "LPN", 
                  "RPN", "LBK", "RBK", "LBR", "RBR", "DOT", "CM", "SM", 
                  "COL", "INT_LIT", "FLOAT_LIT", "BOOL_LIT", "STR_LIT", 
                  "BLOCK_COMMENT", "LINE_COMMENT", "ID", "AT_ID", "FLOAT_DEC", 
                  "FLOAT_EXP", "DIGIT", "STR_CHAR", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[53] = self.STR_LIT_action 
            actions[63] = self.UNCLOSE_STRING_action 
            actions[64] = self.ILLEGAL_ESCAPE_action 
            actions[65] = self.ERROR_CHAR_action 
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
            raise Exception(self.text)
     


