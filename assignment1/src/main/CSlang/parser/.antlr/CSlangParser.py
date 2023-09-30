# Generated from d:\Program\XAMPP\htdocs\btl-nllt\assignment1\src\main\CSlang\parser\CSlang.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u01b6\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\5\3\\\n\3\3\4\3\4\3\4\3\4\5\4b\n\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\5\5\5m\n\5\3\6\3\6\3\6\3\6\5\6s\n\6")
        buf.write("\3\7\3\7\3\7\5\7x\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\5\b\u0086\n\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\5\t\u0090\n\t\3\n\3\n\5\n\u0094\n\n\3\n\3\n\5")
        buf.write("\n\u0098\n\n\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\16\3\16\5\16\u00aa\n\16\3\16\3\16")
        buf.write("\3\16\3\16\5\16\u00b0\n\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\5\16\u00b9\n\16\3\16\3\16\5\16\u00bd\n\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00c7\n\17\3")
        buf.write("\20\3\20\3\20\3\20\5\20\u00cd\n\20\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\5\22\u00d5\n\22\3\23\3\23\3\23\3\23\3\23\5")
        buf.write("\23\u00dc\n\23\3\24\3\24\3\24\3\24\3\24\5\24\u00e3\n\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\5\25\u00ea\n\25\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\7\26\u00f2\n\26\f\26\16\26\u00f5\13")
        buf.write("\26\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u00fd\n\27\f\27")
        buf.write("\16\27\u0100\13\27\3\30\3\30\3\30\3\30\3\30\3\30\7\30")
        buf.write("\u0108\n\30\f\30\16\30\u010b\13\30\3\31\3\31\3\31\5\31")
        buf.write("\u0110\n\31\3\32\3\32\3\32\5\32\u0115\n\32\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\5\33\u011d\n\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u012a\n\34\7")
        buf.write("\34\u012c\n\34\f\34\16\34\u012f\13\34\3\35\3\35\3\35\5")
        buf.write("\35\u0134\n\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u013c")
        buf.write("\n\35\3\35\5\35\u013f\n\35\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\5\36\u0148\n\36\3\37\3\37\3\37\3\37\3\37\5\37")
        buf.write("\u014f\n\37\3 \3 \3 \5 \u0154\n \3!\3!\3\"\3\"\3\"\3\"")
        buf.write("\3\"\5\"\u015d\n\"\3#\3#\3#\3#\3#\5#\u0164\n#\3#\3#\3")
        buf.write("$\3$\3$\3$\5$\u016c\n$\3%\3%\3%\3%\5%\u0172\n%\3&\3&\3")
        buf.write("&\3&\5&\u0178\n&\3\'\3\'\3\'\3\'\5\'\u017e\n\'\3(\3(\3")
        buf.write("(\3(\5(\u0184\n(\3)\3)\3)\5)\u0189\n)\3)\3)\3)\3)\3)\3")
        buf.write(")\5)\u0191\n)\3)\3)\3)\3)\3)\5)\u0198\n)\3)\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\5")
        buf.write(")\u01b0\n)\3*\3*\3*\3*\3*\2\6*,.\66+\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPR\2\n\4\2\22\22\25\25\3\2\n\r\3\2 %\3\2\36\37\3\2\27")
        buf.write("\30\3\2\31\34\4\2\23\23;;\3\2;<\2\u01c5\2T\3\2\2\2\4[")
        buf.write("\3\2\2\2\6]\3\2\2\2\bl\3\2\2\2\nr\3\2\2\2\ft\3\2\2\2\16")
        buf.write("\u0085\3\2\2\2\20\u008f\3\2\2\2\22\u0097\3\2\2\2\24\u0099")
        buf.write("\3\2\2\2\26\u009b\3\2\2\2\30\u009f\3\2\2\2\32\u00bc\3")
        buf.write("\2\2\2\34\u00c6\3\2\2\2\36\u00cc\3\2\2\2 \u00ce\3\2\2")
        buf.write("\2\"\u00d4\3\2\2\2$\u00db\3\2\2\2&\u00e2\3\2\2\2(\u00e9")
        buf.write("\3\2\2\2*\u00eb\3\2\2\2,\u00f6\3\2\2\2.\u0101\3\2\2\2")
        buf.write("\60\u010f\3\2\2\2\62\u0114\3\2\2\2\64\u011c\3\2\2\2\66")
        buf.write("\u011e\3\2\2\28\u013e\3\2\2\2:\u0147\3\2\2\2<\u014e\3")
        buf.write("\2\2\2>\u0153\3\2\2\2@\u0155\3\2\2\2B\u015c\3\2\2\2D\u015e")
        buf.write("\3\2\2\2F\u016b\3\2\2\2H\u0171\3\2\2\2J\u0177\3\2\2\2")
        buf.write("L\u017d\3\2\2\2N\u0183\3\2\2\2P\u01af\3\2\2\2R\u01b1\3")
        buf.write("\2\2\2TU\5\4\3\2UV\7\2\2\3V\3\3\2\2\2WX\5\6\4\2XY\5\4")
        buf.write("\3\2Y\\\3\2\2\2Z\\\5\6\4\2[W\3\2\2\2[Z\3\2\2\2\\\5\3\2")
        buf.write("\2\2]a\7\20\2\2^_\7;\2\2_b\7)\2\2`b\3\2\2\2a^\3\2\2\2")
        buf.write("a`\3\2\2\2bc\3\2\2\2cd\7;\2\2de\7/\2\2ef\5\b\5\2fg\7\60")
        buf.write("\2\2g\7\3\2\2\2hi\5\n\6\2ij\5\b\5\2jm\3\2\2\2km\3\2\2")
        buf.write("\2lh\3\2\2\2lk\3\2\2\2m\t\3\2\2\2no\5\f\7\2op\7\63\2\2")
        buf.write("ps\3\2\2\2qs\5\32\16\2rn\3\2\2\2rq\3\2\2\2s\13\3\2\2\2")
        buf.write("tw\t\2\2\2ux\5\16\b\2vx\5\20\t\2wu\3\2\2\2wv\3\2\2\2x")
        buf.write("\r\3\2\2\2yz\5@!\2z{\7\62\2\2{|\5\16\b\2|}\7\62\2\2}~")
        buf.write("\5&\24\2~\u0086\3\2\2\2\177\u0080\5@!\2\u0080\u0081\7")
        buf.write("\64\2\2\u0081\u0082\5\22\n\2\u0082\u0083\7&\2\2\u0083")
        buf.write("\u0084\5&\24\2\u0084\u0086\3\2\2\2\u0085y\3\2\2\2\u0085")
        buf.write("\177\3\2\2\2\u0086\17\3\2\2\2\u0087\u0088\5@!\2\u0088")
        buf.write("\u0089\7\62\2\2\u0089\u008a\5\20\t\2\u008a\u0090\3\2\2")
        buf.write("\2\u008b\u008c\5@!\2\u008c\u008d\7\64\2\2\u008d\u008e")
        buf.write("\5\22\n\2\u008e\u0090\3\2\2\2\u008f\u0087\3\2\2\2\u008f")
        buf.write("\u008b\3\2\2\2\u0090\21\3\2\2\2\u0091\u0094\5\26\f\2\u0092")
        buf.write("\u0094\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0092\3\2\2\2")
        buf.write("\u0094\u0095\3\2\2\2\u0095\u0098\5\24\13\2\u0096\u0098")
        buf.write("\5\30\r\2\u0097\u0093\3\2\2\2\u0097\u0096\3\2\2\2\u0098")
        buf.write("\23\3\2\2\2\u0099\u009a\t\3\2\2\u009a\25\3\2\2\2\u009b")
        buf.write("\u009c\7-\2\2\u009c\u009d\7\65\2\2\u009d\u009e\7.\2\2")
        buf.write("\u009e\27\3\2\2\2\u009f\u00a0\7*\2\2\u00a0\u00a1\7;\2")
        buf.write("\2\u00a1\u00a2\7+\2\2\u00a2\u00a3\7,\2\2\u00a3\31\3\2")
        buf.write("\2\2\u00a4\u00a5\7\26\2\2\u00a5\u00a6\5@!\2\u00a6\u00a9")
        buf.write("\7+\2\2\u00a7\u00aa\5\34\17\2\u00a8\u00aa\3\2\2\2\u00a9")
        buf.write("\u00a7\3\2\2\2\u00a9\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2")
        buf.write("\u00ab\u00ac\7,\2\2\u00ac\u00af\7\64\2\2\u00ad\u00b0\5")
        buf.write("\24\13\2\u00ae\u00b0\7\24\2\2\u00af\u00ad\3\2\2\2\u00af")
        buf.write("\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2\5 \21\2")
        buf.write("\u00b2\u00bd\3\2\2\2\u00b3\u00b4\7\26\2\2\u00b4\u00b5")
        buf.write("\7\21\2\2\u00b5\u00b8\7+\2\2\u00b6\u00b9\5\34\17\2\u00b7")
        buf.write("\u00b9\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8\u00b7\3\2\2\2")
        buf.write("\u00b9\u00ba\3\2\2\2\u00ba\u00bb\7,\2\2\u00bb\u00bd\5")
        buf.write(" \21\2\u00bc\u00a4\3\2\2\2\u00bc\u00b3\3\2\2\2\u00bd\33")
        buf.write("\3\2\2\2\u00be\u00bf\5\36\20\2\u00bf\u00c0\7\62\2\2\u00c0")
        buf.write("\u00c1\5\34\17\2\u00c1\u00c7\3\2\2\2\u00c2\u00c3\5\36")
        buf.write("\20\2\u00c3\u00c4\7\64\2\2\u00c4\u00c5\5\24\13\2\u00c5")
        buf.write("\u00c7\3\2\2\2\u00c6\u00be\3\2\2\2\u00c6\u00c2\3\2\2\2")
        buf.write("\u00c7\35\3\2\2\2\u00c8\u00c9\7;\2\2\u00c9\u00ca\7\62")
        buf.write("\2\2\u00ca\u00cd\5\36\20\2\u00cb\u00cd\7;\2\2\u00cc\u00c8")
        buf.write("\3\2\2\2\u00cc\u00cb\3\2\2\2\u00cd\37\3\2\2\2\u00ce\u00cf")
        buf.write("\7/\2\2\u00cf\u00d0\5N(\2\u00d0\u00d1\7\60\2\2\u00d1!")
        buf.write("\3\2\2\2\u00d2\u00d5\5$\23\2\u00d3\u00d5\3\2\2\2\u00d4")
        buf.write("\u00d2\3\2\2\2\u00d4\u00d3\3\2\2\2\u00d5#\3\2\2\2\u00d6")
        buf.write("\u00d7\5&\24\2\u00d7\u00d8\7\62\2\2\u00d8\u00d9\5\"\22")
        buf.write("\2\u00d9\u00dc\3\2\2\2\u00da\u00dc\5&\24\2\u00db\u00d6")
        buf.write("\3\2\2\2\u00db\u00da\3\2\2\2\u00dc%\3\2\2\2\u00dd\u00de")
        buf.write("\5(\25\2\u00de\u00df\7(\2\2\u00df\u00e0\5(\25\2\u00e0")
        buf.write("\u00e3\3\2\2\2\u00e1\u00e3\5(\25\2\u00e2\u00dd\3\2\2\2")
        buf.write("\u00e2\u00e1\3\2\2\2\u00e3\'\3\2\2\2\u00e4\u00e5\5*\26")
        buf.write("\2\u00e5\u00e6\t\4\2\2\u00e6\u00e7\5*\26\2\u00e7\u00ea")
        buf.write("\3\2\2\2\u00e8\u00ea\5*\26\2\u00e9\u00e4\3\2\2\2\u00e9")
        buf.write("\u00e8\3\2\2\2\u00ea)\3\2\2\2\u00eb\u00ec\b\26\1\2\u00ec")
        buf.write("\u00ed\5,\27\2\u00ed\u00f3\3\2\2\2\u00ee\u00ef\f\4\2\2")
        buf.write("\u00ef\u00f0\t\5\2\2\u00f0\u00f2\5,\27\2\u00f1\u00ee\3")
        buf.write("\2\2\2\u00f2\u00f5\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f3\u00f4")
        buf.write("\3\2\2\2\u00f4+\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f6\u00f7")
        buf.write("\b\27\1\2\u00f7\u00f8\5.\30\2\u00f8\u00fe\3\2\2\2\u00f9")
        buf.write("\u00fa\f\4\2\2\u00fa\u00fb\t\6\2\2\u00fb\u00fd\5.\30\2")
        buf.write("\u00fc\u00f9\3\2\2\2\u00fd\u0100\3\2\2\2\u00fe\u00fc\3")
        buf.write("\2\2\2\u00fe\u00ff\3\2\2\2\u00ff-\3\2\2\2\u0100\u00fe")
        buf.write("\3\2\2\2\u0101\u0102\b\30\1\2\u0102\u0103\5\60\31\2\u0103")
        buf.write("\u0109\3\2\2\2\u0104\u0105\f\4\2\2\u0105\u0106\t\7\2\2")
        buf.write("\u0106\u0108\5\60\31\2\u0107\u0104\3\2\2\2\u0108\u010b")
        buf.write("\3\2\2\2\u0109\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a")
        buf.write("/\3\2\2\2\u010b\u0109\3\2\2\2\u010c\u010d\7\35\2\2\u010d")
        buf.write("\u0110\5\60\31\2\u010e\u0110\5\62\32\2\u010f\u010c\3\2")
        buf.write("\2\2\u010f\u010e\3\2\2\2\u0110\61\3\2\2\2\u0111\u0112")
        buf.write("\7\30\2\2\u0112\u0115\5\62\32\2\u0113\u0115\5\64\33\2")
        buf.write("\u0114\u0111\3\2\2\2\u0114\u0113\3\2\2\2\u0115\63\3\2")
        buf.write("\2\2\u0116\u0117\5\66\34\2\u0117\u0118\7-\2\2\u0118\u0119")
        buf.write("\5&\24\2\u0119\u011a\7.\2\2\u011a\u011d\3\2\2\2\u011b")
        buf.write("\u011d\5\66\34\2\u011c\u0116\3\2\2\2\u011c\u011b\3\2\2")
        buf.write("\2\u011d\65\3\2\2\2\u011e\u011f\b\34\1\2\u011f\u0120\5")
        buf.write("8\35\2\u0120\u012d\3\2\2\2\u0121\u0122\f\4\2\2\u0122\u0123")
        buf.write("\7\61\2\2\u0123\u0129\7;\2\2\u0124\u0125\7+\2\2\u0125")
        buf.write("\u0126\5\"\22\2\u0126\u0127\7,\2\2\u0127\u012a\3\2\2\2")
        buf.write("\u0128\u012a\3\2\2\2\u0129\u0124\3\2\2\2\u0129\u0128\3")
        buf.write("\2\2\2\u012a\u012c\3\2\2\2\u012b\u0121\3\2\2\2\u012c\u012f")
        buf.write("\3\2\2\2\u012d\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012e")
        buf.write("\67\3\2\2\2\u012f\u012d\3\2\2\2\u0130\u0131\t\b\2\2\u0131")
        buf.write("\u0134\7\61\2\2\u0132\u0134\3\2\2\2\u0133\u0130\3\2\2")
        buf.write("\2\u0133\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u013b")
        buf.write("\7<\2\2\u0136\u0137\7+\2\2\u0137\u0138\5\"\22\2\u0138")
        buf.write("\u0139\7,\2\2\u0139\u013c\3\2\2\2\u013a\u013c\3\2\2\2")
        buf.write("\u013b\u0136\3\2\2\2\u013b\u013a\3\2\2\2\u013c\u013f\3")
        buf.write("\2\2\2\u013d\u013f\5:\36\2\u013e\u0133\3\2\2\2\u013e\u013d")
        buf.write("\3\2\2\2\u013f9\3\2\2\2\u0140\u0141\7*\2\2\u0141\u0142")
        buf.write("\7;\2\2\u0142\u0143\7+\2\2\u0143\u0144\5\"\22\2\u0144")
        buf.write("\u0145\7,\2\2\u0145\u0148\3\2\2\2\u0146\u0148\5<\37\2")
        buf.write("\u0147\u0140\3\2\2\2\u0147\u0146\3\2\2\2\u0148;\3\2\2")
        buf.write("\2\u0149\u014a\7+\2\2\u014a\u014b\5&\24\2\u014b\u014c")
        buf.write("\7,\2\2\u014c\u014f\3\2\2\2\u014d\u014f\5> \2\u014e\u0149")
        buf.write("\3\2\2\2\u014e\u014d\3\2\2\2\u014f=\3\2\2\2\u0150\u0154")
        buf.write("\5@!\2\u0151\u0154\5B\"\2\u0152\u0154\7\23\2\2\u0153\u0150")
        buf.write("\3\2\2\2\u0153\u0151\3\2\2\2\u0153\u0152\3\2\2\2\u0154")
        buf.write("?\3\2\2\2\u0155\u0156\t\t\2\2\u0156A\3\2\2\2\u0157\u015d")
        buf.write("\7\65\2\2\u0158\u015d\7\66\2\2\u0159\u015d\7\67\2\2\u015a")
        buf.write("\u015d\78\2\2\u015b\u015d\5D#\2\u015c\u0157\3\2\2\2\u015c")
        buf.write("\u0158\3\2\2\2\u015c\u0159\3\2\2\2\u015c\u015a\3\2\2\2")
        buf.write("\u015c\u015b\3\2\2\2\u015dC\3\2\2\2\u015e\u0163\7-\2\2")
        buf.write("\u015f\u0164\5F$\2\u0160\u0164\5H%\2\u0161\u0164\5J&\2")
        buf.write("\u0162\u0164\5L\'\2\u0163\u015f\3\2\2\2\u0163\u0160\3")
        buf.write("\2\2\2\u0163\u0161\3\2\2\2\u0163\u0162\3\2\2\2\u0164\u0165")
        buf.write("\3\2\2\2\u0165\u0166\7.\2\2\u0166E\3\2\2\2\u0167\u0168")
        buf.write("\7\65\2\2\u0168\u0169\7\62\2\2\u0169\u016c\5F$\2\u016a")
        buf.write("\u016c\7\65\2\2\u016b\u0167\3\2\2\2\u016b\u016a\3\2\2")
        buf.write("\2\u016cG\3\2\2\2\u016d\u016e\7\66\2\2\u016e\u016f\7\62")
        buf.write("\2\2\u016f\u0172\5H%\2\u0170\u0172\7\66\2\2\u0171\u016d")
        buf.write("\3\2\2\2\u0171\u0170\3\2\2\2\u0172I\3\2\2\2\u0173\u0174")
        buf.write("\7\67\2\2\u0174\u0175\7\62\2\2\u0175\u0178\5J&\2\u0176")
        buf.write("\u0178\7\67\2\2\u0177\u0173\3\2\2\2\u0177\u0176\3\2\2")
        buf.write("\2\u0178K\3\2\2\2\u0179\u017a\78\2\2\u017a\u017b\7\62")
        buf.write("\2\2\u017b\u017e\5L\'\2\u017c\u017e\78\2\2\u017d\u0179")
        buf.write("\3\2\2\2\u017d\u017c\3\2\2\2\u017eM\3\2\2\2\u017f\u0180")
        buf.write("\5P)\2\u0180\u0181\5N(\2\u0181\u0184\3\2\2\2\u0182\u0184")
        buf.write("\3\2\2\2\u0183\u017f\3\2\2\2\u0183\u0182\3\2\2\2\u0184")
        buf.write("O\3\2\2\2\u0185\u0189\7\22\2\2\u0186\u0189\7\25\2\2\u0187")
        buf.write("\u0189\3\2\2\2\u0188\u0185\3\2\2\2\u0188\u0186\3\2\2\2")
        buf.write("\u0188\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018b\5")
        buf.write("R*\2\u018b\u018c\7\63\2\2\u018c\u01b0\3\2\2\2\u018d\u0190")
        buf.write("\7\5\2\2\u018e\u0191\5 \21\2\u018f\u0191\3\2\2\2\u0190")
        buf.write("\u018e\3\2\2\2\u0190\u018f\3\2\2\2\u0191\u0192\3\2\2\2")
        buf.write("\u0192\u0193\5&\24\2\u0193\u0197\5 \21\2\u0194\u0195\7")
        buf.write("\6\2\2\u0195\u0198\5 \21\2\u0196\u0198\3\2\2\2\u0197\u0194")
        buf.write("\3\2\2\2\u0197\u0196\3\2\2\2\u0198\u01b0\3\2\2\2\u0199")
        buf.write("\u019a\7\7\2\2\u019a\u019b\5R*\2\u019b\u019c\7\63\2\2")
        buf.write("\u019c\u019d\5(\25\2\u019d\u019e\7\63\2\2\u019e\u019f")
        buf.write("\5R*\2\u019f\u01a0\5 \21\2\u01a0\u01b0\3\2\2\2\u01a1\u01a2")
        buf.write("\7\3\2\2\u01a2\u01b0\7\63\2\2\u01a3\u01a4\7\4\2\2\u01a4")
        buf.write("\u01b0\7\63\2\2\u01a5\u01a6\7\16\2\2\u01a6\u01a7\5&\24")
        buf.write("\2\u01a7\u01a8\7\63\2\2\u01a8\u01b0\3\2\2\2\u01a9\u01aa")
        buf.write("\5\66\34\2\u01aa\u01ab\7\63\2\2\u01ab\u01b0\3\2\2\2\u01ac")
        buf.write("\u01ad\5\f\7\2\u01ad\u01ae\7\63\2\2\u01ae\u01b0\3\2\2")
        buf.write("\2\u01af\u0188\3\2\2\2\u01af\u018d\3\2\2\2\u01af\u0199")
        buf.write("\3\2\2\2\u01af\u01a1\3\2\2\2\u01af\u01a3\3\2\2\2\u01af")
        buf.write("\u01a5\3\2\2\2\u01af\u01a9\3\2\2\2\u01af\u01ac\3\2\2\2")
        buf.write("\u01b0Q\3\2\2\2\u01b1\u01b2\5\64\33\2\u01b2\u01b3\7\'")
        buf.write("\2\2\u01b3\u01b4\5&\24\2\u01b4S\3\2\2\2.[alrw\u0085\u008f")
        buf.write("\u0093\u0097\u00a9\u00af\u00b8\u00bc\u00c6\u00cc\u00d4")
        buf.write("\u00db\u00e2\u00e9\u00f3\u00fe\u0109\u010f\u0114\u011c")
        buf.write("\u0129\u012d\u0133\u013b\u013e\u0147\u014e\u0153\u015c")
        buf.write("\u0163\u016b\u0171\u0177\u017d\u0183\u0188\u0190\u0197")
        buf.write("\u01af")
        return buf.getvalue()


class CSlangParser ( Parser ):

    grammarFileName = "CSlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'break'", "'continue'", "'if'", "'else'", 
                     "'for'", "'true'", "'false'", "'int'", "'float'", "'bool'", 
                     "'string'", "'return'", "'null'", "'class'", "'constructor'", 
                     "'var'", "'self'", "'void'", "'const'", "'func'", "'+'", 
                     "'-'", "'*'", "'/'", "'\\'", "'%'", "'!'", "'&&'", 
                     "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'='", "':='", "'^'", "'<-'", "'new'", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "'.'", "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", 
                      "TRUE", "FALSE", "INT", "FLOAT", "BOOL", "STRING", 
                      "RETURN", "NULL", "CLASS", "CONSTRUCTOR", "VAR", "SELF", 
                      "VOID", "CONST", "FUNC", "PLUS", "MINUS", "MUL", "DIV_FLOAT", 
                      "DIV_INT", "MOD", "NEG", "AND", "OR", "EQ", "NEQ", 
                      "LT", "LTEQ", "GT", "GTEQ", "DECLARE", "ASSIGN", "CONCATE", 
                      "ARROW", "NEW", "LPN", "RPN", "LBK", "RBK", "LBR", 
                      "RBR", "DOT", "CM", "SM", "COL", "INT_LIT", "FLOAT_LIT", 
                      "BOOL_LIT", "STR_LIT", "BLOCK_COMMENT", "LINE_COMMENT", 
                      "ID", "AT_ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_classdecllist = 1
    RULE_classdecl = 2
    RULE_memberlist = 3
    RULE_member = 4
    RULE_attribute = 5
    RULE_attlistdecl = 6
    RULE_attlistnodecl = 7
    RULE_atttyp = 8
    RULE_typ = 9
    RULE_arraytyp = 10
    RULE_classtyp = 11
    RULE_method = 12
    RULE_paramlist = 13
    RULE_params = 14
    RULE_stmtblock = 15
    RULE_expressions = 16
    RULE_exprprime = 17
    RULE_exprstr = 18
    RULE_exprrel = 19
    RULE_exprlog = 20
    RULE_expradd = 21
    RULE_exprmul = 22
    RULE_exprnot = 23
    RULE_exprsign = 24
    RULE_exprindex = 25
    RULE_exprinst = 26
    RULE_exprstat = 27
    RULE_exprobj = 28
    RULE_exprparen = 29
    RULE_exprlelf = 30
    RULE_identifiers = 31
    RULE_literals = 32
    RULE_arrayliteral = 33
    RULE_arrint = 34
    RULE_arrfloat = 35
    RULE_arrbool = 36
    RULE_arrstr = 37
    RULE_statements = 38
    RULE_stmt = 39
    RULE_stmtassign = 40

    ruleNames =  [ "program", "classdecllist", "classdecl", "memberlist", 
                   "member", "attribute", "attlistdecl", "attlistnodecl", 
                   "atttyp", "typ", "arraytyp", "classtyp", "method", "paramlist", 
                   "params", "stmtblock", "expressions", "exprprime", "exprstr", 
                   "exprrel", "exprlog", "expradd", "exprmul", "exprnot", 
                   "exprsign", "exprindex", "exprinst", "exprstat", "exprobj", 
                   "exprparen", "exprlelf", "identifiers", "literals", "arrayliteral", 
                   "arrint", "arrfloat", "arrbool", "arrstr", "statements", 
                   "stmt", "stmtassign" ]

    EOF = Token.EOF
    BREAK=1
    CONTINUE=2
    IF=3
    ELSE=4
    FOR=5
    TRUE=6
    FALSE=7
    INT=8
    FLOAT=9
    BOOL=10
    STRING=11
    RETURN=12
    NULL=13
    CLASS=14
    CONSTRUCTOR=15
    VAR=16
    SELF=17
    VOID=18
    CONST=19
    FUNC=20
    PLUS=21
    MINUS=22
    MUL=23
    DIV_FLOAT=24
    DIV_INT=25
    MOD=26
    NEG=27
    AND=28
    OR=29
    EQ=30
    NEQ=31
    LT=32
    LTEQ=33
    GT=34
    GTEQ=35
    DECLARE=36
    ASSIGN=37
    CONCATE=38
    ARROW=39
    NEW=40
    LPN=41
    RPN=42
    LBK=43
    RBK=44
    LBR=45
    RBR=46
    DOT=47
    CM=48
    SM=49
    COL=50
    INT_LIT=51
    FLOAT_LIT=52
    BOOL_LIT=53
    STR_LIT=54
    BLOCK_COMMENT=55
    LINE_COMMENT=56
    ID=57
    AT_ID=58
    WS=59
    UNCLOSE_STRING=60
    ILLEGAL_ESCAPE=61
    ERROR_CHAR=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classdecllist(self):
            return self.getTypedRuleContext(CSlangParser.ClassdecllistContext,0)


        def EOF(self):
            return self.getToken(CSlangParser.EOF, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_program




    def program(self):

        localctx = CSlangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.classdecllist()
            self.state = 83
            self.match(CSlangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classdecl(self):
            return self.getTypedRuleContext(CSlangParser.ClassdeclContext,0)


        def classdecllist(self):
            return self.getTypedRuleContext(CSlangParser.ClassdecllistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_classdecllist




    def classdecllist(self):

        localctx = CSlangParser.ClassdecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classdecllist)
        try:
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.classdecl()
                self.state = 86
                self.classdecllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.classdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(CSlangParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.ID)
            else:
                return self.getToken(CSlangParser.ID, i)

        def LBR(self):
            return self.getToken(CSlangParser.LBR, 0)

        def memberlist(self):
            return self.getTypedRuleContext(CSlangParser.MemberlistContext,0)


        def RBR(self):
            return self.getToken(CSlangParser.RBR, 0)

        def ARROW(self):
            return self.getToken(CSlangParser.ARROW, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_classdecl




    def classdecl(self):

        localctx = CSlangParser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(CSlangParser.CLASS)
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 92
                self.match(CSlangParser.ID)
                self.state = 93
                self.match(CSlangParser.ARROW)
                pass

            elif la_ == 2:
                pass


            self.state = 97
            self.match(CSlangParser.ID)
            self.state = 98
            self.match(CSlangParser.LBR)
            self.state = 99
            self.memberlist()
            self.state = 100
            self.match(CSlangParser.RBR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(CSlangParser.MemberContext,0)


        def memberlist(self):
            return self.getTypedRuleContext(CSlangParser.MemberlistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_memberlist




    def memberlist(self):

        localctx = CSlangParser.MemberlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_memberlist)
        try:
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST, CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.member()
                self.state = 103
                self.memberlist()
                pass
            elif token in [CSlangParser.RBR]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self):
            return self.getTypedRuleContext(CSlangParser.AttributeContext,0)


        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def method(self):
            return self.getTypedRuleContext(CSlangParser.MethodContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_member




    def member(self):

        localctx = CSlangParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_member)
        try:
            self.state = 112
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.attribute()
                self.state = 109
                self.match(CSlangParser.SM)
                pass
            elif token in [CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.method()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def attlistdecl(self):
            return self.getTypedRuleContext(CSlangParser.AttlistdeclContext,0)


        def attlistnodecl(self):
            return self.getTypedRuleContext(CSlangParser.AttlistnodeclContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attribute




    def attribute(self):

        localctx = CSlangParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 115
                self.attlistdecl()
                pass

            elif la_ == 2:
                self.state = 116
                self.attlistnodecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttlistdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifiers(self):
            return self.getTypedRuleContext(CSlangParser.IdentifiersContext,0)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def attlistdecl(self):
            return self.getTypedRuleContext(CSlangParser.AttlistdeclContext,0)


        def exprstr(self):
            return self.getTypedRuleContext(CSlangParser.ExprstrContext,0)


        def COL(self):
            return self.getToken(CSlangParser.COL, 0)

        def atttyp(self):
            return self.getTypedRuleContext(CSlangParser.AtttypContext,0)


        def DECLARE(self):
            return self.getToken(CSlangParser.DECLARE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_attlistdecl




    def attlistdecl(self):

        localctx = CSlangParser.AttlistdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attlistdecl)
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.identifiers()
                self.state = 120
                self.match(CSlangParser.CM)
                self.state = 121
                self.attlistdecl()
                self.state = 122
                self.match(CSlangParser.CM)
                self.state = 123
                self.exprstr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.identifiers()
                self.state = 126
                self.match(CSlangParser.COL)
                self.state = 127
                self.atttyp()
                self.state = 128
                self.match(CSlangParser.DECLARE)
                self.state = 129
                self.exprstr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttlistnodeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifiers(self):
            return self.getTypedRuleContext(CSlangParser.IdentifiersContext,0)


        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def attlistnodecl(self):
            return self.getTypedRuleContext(CSlangParser.AttlistnodeclContext,0)


        def COL(self):
            return self.getToken(CSlangParser.COL, 0)

        def atttyp(self):
            return self.getTypedRuleContext(CSlangParser.AtttypContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attlistnodecl




    def attlistnodecl(self):

        localctx = CSlangParser.AttlistnodeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attlistnodecl)
        try:
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.identifiers()
                self.state = 134
                self.match(CSlangParser.CM)
                self.state = 135
                self.attlistnodecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.identifiers()
                self.state = 138
                self.match(CSlangParser.COL)
                self.state = 139
                self.atttyp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtttypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def arraytyp(self):
            return self.getTypedRuleContext(CSlangParser.ArraytypContext,0)


        def classtyp(self):
            return self.getTypedRuleContext(CSlangParser.ClasstypContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_atttyp




    def atttyp(self):

        localctx = CSlangParser.AtttypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_atttyp)
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.LBK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.LBK]:
                    self.state = 143
                    self.arraytyp()
                    pass
                elif token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 147
                self.typ()
                pass
            elif token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.classtyp()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CSlangParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(CSlangParser.BOOL, 0)

        def STRING(self):
            return self.getToken(CSlangParser.STRING, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_typ




    def typ(self):

        localctx = CSlangParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.INT) | (1 << CSlangParser.FLOAT) | (1 << CSlangParser.BOOL) | (1 << CSlangParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraytypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBK(self):
            return self.getToken(CSlangParser.LBK, 0)

        def INT_LIT(self):
            return self.getToken(CSlangParser.INT_LIT, 0)

        def RBK(self):
            return self.getToken(CSlangParser.RBK, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_arraytyp




    def arraytyp(self):

        localctx = CSlangParser.ArraytypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_arraytyp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(CSlangParser.LBK)
            self.state = 154
            self.match(CSlangParser.INT_LIT)
            self.state = 155
            self.match(CSlangParser.RBK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClasstypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(CSlangParser.NEW, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LPN(self):
            return self.getToken(CSlangParser.LPN, 0)

        def RPN(self):
            return self.getToken(CSlangParser.RPN, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_classtyp




    def classtyp(self):

        localctx = CSlangParser.ClasstypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_classtyp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(CSlangParser.NEW)
            self.state = 158
            self.match(CSlangParser.ID)
            self.state = 159
            self.match(CSlangParser.LPN)
            self.state = 160
            self.match(CSlangParser.RPN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def identifiers(self):
            return self.getTypedRuleContext(CSlangParser.IdentifiersContext,0)


        def LPN(self):
            return self.getToken(CSlangParser.LPN, 0)

        def RPN(self):
            return self.getToken(CSlangParser.RPN, 0)

        def COL(self):
            return self.getToken(CSlangParser.COL, 0)

        def stmtblock(self):
            return self.getTypedRuleContext(CSlangParser.StmtblockContext,0)


        def paramlist(self):
            return self.getTypedRuleContext(CSlangParser.ParamlistContext,0)


        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def VOID(self):
            return self.getToken(CSlangParser.VOID, 0)

        def CONSTRUCTOR(self):
            return self.getToken(CSlangParser.CONSTRUCTOR, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_method




    def method(self):

        localctx = CSlangParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_method)
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(CSlangParser.FUNC)
                self.state = 163
                self.identifiers()
                self.state = 164
                self.match(CSlangParser.LPN)
                self.state = 167
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.ID]:
                    self.state = 165
                    self.paramlist()
                    pass
                elif token in [CSlangParser.RPN]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 169
                self.match(CSlangParser.RPN)
                self.state = 170
                self.match(CSlangParser.COL)
                self.state = 173
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING]:
                    self.state = 171
                    self.typ()
                    pass
                elif token in [CSlangParser.VOID]:
                    self.state = 172
                    self.match(CSlangParser.VOID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 175
                self.stmtblock()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.match(CSlangParser.FUNC)
                self.state = 178
                self.match(CSlangParser.CONSTRUCTOR)
                self.state = 179
                self.match(CSlangParser.LPN)
                self.state = 182
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.ID]:
                    self.state = 180
                    self.paramlist()
                    pass
                elif token in [CSlangParser.RPN]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 184
                self.match(CSlangParser.RPN)
                self.state = 185
                self.stmtblock()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def params(self):
            return self.getTypedRuleContext(CSlangParser.ParamsContext,0)


        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def paramlist(self):
            return self.getTypedRuleContext(CSlangParser.ParamlistContext,0)


        def COL(self):
            return self.getToken(CSlangParser.COL, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_paramlist




    def paramlist(self):

        localctx = CSlangParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_paramlist)
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.params()
                self.state = 189
                self.match(CSlangParser.CM)
                self.state = 190
                self.paramlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.params()
                self.state = 193
                self.match(CSlangParser.COL)
                self.state = 194
                self.typ()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def params(self):
            return self.getTypedRuleContext(CSlangParser.ParamsContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_params




    def params(self):

        localctx = CSlangParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_params)
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.match(CSlangParser.ID)
                self.state = 199
                self.match(CSlangParser.CM)
                self.state = 200
                self.params()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.match(CSlangParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtblockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBR(self):
            return self.getToken(CSlangParser.LBR, 0)

        def statements(self):
            return self.getTypedRuleContext(CSlangParser.StatementsContext,0)


        def RBR(self):
            return self.getToken(CSlangParser.RBR, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_stmtblock




    def stmtblock(self):

        localctx = CSlangParser.StmtblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_stmtblock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(CSlangParser.LBR)
            self.state = 205
            self.statements()
            self.state = 206
            self.match(CSlangParser.RBR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprprime(self):
            return self.getTypedRuleContext(CSlangParser.ExprprimeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expressions




    def expressions(self):

        localctx = CSlangParser.ExpressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expressions)
        try:
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.SELF, CSlangParser.MINUS, CSlangParser.NEG, CSlangParser.NEW, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.INT_LIT, CSlangParser.FLOAT_LIT, CSlangParser.BOOL_LIT, CSlangParser.STR_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.exprprime()
                pass
            elif token in [CSlangParser.RPN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprstr(self):
            return self.getTypedRuleContext(CSlangParser.ExprstrContext,0)


        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def expressions(self):
            return self.getTypedRuleContext(CSlangParser.ExpressionsContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exprprime




    def exprprime(self):

        localctx = CSlangParser.ExprprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_exprprime)
        try:
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.exprstr()
                self.state = 213
                self.match(CSlangParser.CM)
                self.state = 214
                self.expressions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.exprstr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprstrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprrel(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExprrelContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExprrelContext,i)


        def CONCATE(self):
            return self.getToken(CSlangParser.CONCATE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exprstr




    def exprstr(self):

        localctx = CSlangParser.ExprstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_exprstr)
        try:
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.exprrel()
                self.state = 220
                self.match(CSlangParser.CONCATE)
                self.state = 221
                self.exprrel()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.exprrel()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprrelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprlog(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExprlogContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExprlogContext,i)


        def EQ(self):
            return self.getToken(CSlangParser.EQ, 0)

        def NEQ(self):
            return self.getToken(CSlangParser.NEQ, 0)

        def LT(self):
            return self.getToken(CSlangParser.LT, 0)

        def LTEQ(self):
            return self.getToken(CSlangParser.LTEQ, 0)

        def GT(self):
            return self.getToken(CSlangParser.GT, 0)

        def GTEQ(self):
            return self.getToken(CSlangParser.GTEQ, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exprrel




    def exprrel(self):

        localctx = CSlangParser.ExprrelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_exprrel)
        self._la = 0 # Token type
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.exprlog(0)
                self.state = 227
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.EQ) | (1 << CSlangParser.NEQ) | (1 << CSlangParser.LT) | (1 << CSlangParser.LTEQ) | (1 << CSlangParser.GT) | (1 << CSlangParser.GTEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 228
                self.exprlog(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.exprlog(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlogContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expradd(self):
            return self.getTypedRuleContext(CSlangParser.ExpraddContext,0)


        def exprlog(self):
            return self.getTypedRuleContext(CSlangParser.ExprlogContext,0)


        def AND(self):
            return self.getToken(CSlangParser.AND, 0)

        def OR(self):
            return self.getToken(CSlangParser.OR, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exprlog



    def exprlog(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.ExprlogContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_exprlog, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.expradd(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 241
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprlogContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprlog)
                    self.state = 236
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 237
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.AND or _la==CSlangParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 238
                    self.expradd(0) 
                self.state = 243
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExpraddContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprmul(self):
            return self.getTypedRuleContext(CSlangParser.ExprmulContext,0)


        def expradd(self):
            return self.getTypedRuleContext(CSlangParser.ExpraddContext,0)


        def PLUS(self):
            return self.getToken(CSlangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(CSlangParser.MINUS, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expradd



    def expradd(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.ExpraddContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expradd, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.exprmul(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 252
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExpraddContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expradd)
                    self.state = 247
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 248
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.PLUS or _la==CSlangParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 249
                    self.exprmul(0) 
                self.state = 254
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprmulContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprnot(self):
            return self.getTypedRuleContext(CSlangParser.ExprnotContext,0)


        def exprmul(self):
            return self.getTypedRuleContext(CSlangParser.ExprmulContext,0)


        def MUL(self):
            return self.getToken(CSlangParser.MUL, 0)

        def DIV_FLOAT(self):
            return self.getToken(CSlangParser.DIV_FLOAT, 0)

        def DIV_INT(self):
            return self.getToken(CSlangParser.DIV_INT, 0)

        def MOD(self):
            return self.getToken(CSlangParser.MOD, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exprmul



    def exprmul(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.ExprmulContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_exprmul, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.exprnot()
            self._ctx.stop = self._input.LT(-1)
            self.state = 263
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprmulContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprmul)
                    self.state = 258
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 259
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.MUL) | (1 << CSlangParser.DIV_FLOAT) | (1 << CSlangParser.DIV_INT) | (1 << CSlangParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 260
                    self.exprnot() 
                self.state = 265
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprnotContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEG(self):
            return self.getToken(CSlangParser.NEG, 0)

        def exprnot(self):
            return self.getTypedRuleContext(CSlangParser.ExprnotContext,0)


        def exprsign(self):
            return self.getTypedRuleContext(CSlangParser.ExprsignContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exprnot




    def exprnot(self):

        localctx = CSlangParser.ExprnotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_exprnot)
        try:
            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(CSlangParser.NEG)
                self.state = 267
                self.exprnot()
                pass
            elif token in [CSlangParser.SELF, CSlangParser.MINUS, CSlangParser.NEW, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.INT_LIT, CSlangParser.FLOAT_LIT, CSlangParser.BOOL_LIT, CSlangParser.STR_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.exprsign()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprsignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(CSlangParser.MINUS, 0)

        def exprsign(self):
            return self.getTypedRuleContext(CSlangParser.ExprsignContext,0)


        def exprindex(self):
            return self.getTypedRuleContext(CSlangParser.ExprindexContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exprsign




    def exprsign(self):

        localctx = CSlangParser.ExprsignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_exprsign)
        try:
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.match(CSlangParser.MINUS)
                self.state = 272
                self.exprsign()
                pass
            elif token in [CSlangParser.SELF, CSlangParser.NEW, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.INT_LIT, CSlangParser.FLOAT_LIT, CSlangParser.BOOL_LIT, CSlangParser.STR_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.exprindex()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprindexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprinst(self):
            return self.getTypedRuleContext(CSlangParser.ExprinstContext,0)


        def LBK(self):
            return self.getToken(CSlangParser.LBK, 0)

        def exprstr(self):
            return self.getTypedRuleContext(CSlangParser.ExprstrContext,0)


        def RBK(self):
            return self.getToken(CSlangParser.RBK, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exprindex




    def exprindex(self):

        localctx = CSlangParser.ExprindexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_exprindex)
        try:
            self.state = 282
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.exprinst(0)
                self.state = 277
                self.match(CSlangParser.LBK)
                self.state = 278
                self.exprstr()
                self.state = 279
                self.match(CSlangParser.RBK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.exprinst(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprinstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprstat(self):
            return self.getTypedRuleContext(CSlangParser.ExprstatContext,0)


        def exprinst(self):
            return self.getTypedRuleContext(CSlangParser.ExprinstContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LPN(self):
            return self.getToken(CSlangParser.LPN, 0)

        def expressions(self):
            return self.getTypedRuleContext(CSlangParser.ExpressionsContext,0)


        def RPN(self):
            return self.getToken(CSlangParser.RPN, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exprinst



    def exprinst(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.ExprinstContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_exprinst, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.exprstat()
            self._ctx.stop = self._input.LT(-1)
            self.state = 299
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprinstContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprinst)
                    self.state = 287
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 288
                    self.match(CSlangParser.DOT)
                    self.state = 289
                    self.match(CSlangParser.ID)
                    self.state = 295
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                    if la_ == 1:
                        self.state = 290
                        self.match(CSlangParser.LPN)
                        self.state = 291
                        self.expressions()
                        self.state = 292
                        self.match(CSlangParser.RPN)
                        pass

                    elif la_ == 2:
                        pass

             
                self.state = 301
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprstatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def LPN(self):
            return self.getToken(CSlangParser.LPN, 0)

        def expressions(self):
            return self.getTypedRuleContext(CSlangParser.ExpressionsContext,0)


        def RPN(self):
            return self.getToken(CSlangParser.RPN, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def exprobj(self):
            return self.getTypedRuleContext(CSlangParser.ExprobjContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exprstat




    def exprstat(self):

        localctx = CSlangParser.ExprstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_exprstat)
        self._la = 0 # Token type
        try:
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.SELF, CSlangParser.ID]:
                    self.state = 302
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.SELF or _la==CSlangParser.ID):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 303
                    self.match(CSlangParser.DOT)
                    pass
                elif token in [CSlangParser.AT_ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 307
                self.match(CSlangParser.AT_ID)
                self.state = 313
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                if la_ == 1:
                    self.state = 308
                    self.match(CSlangParser.LPN)
                    self.state = 309
                    self.expressions()
                    self.state = 310
                    self.match(CSlangParser.RPN)
                    pass

                elif la_ == 2:
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.exprobj()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprobjContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(CSlangParser.NEW, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LPN(self):
            return self.getToken(CSlangParser.LPN, 0)

        def expressions(self):
            return self.getTypedRuleContext(CSlangParser.ExpressionsContext,0)


        def RPN(self):
            return self.getToken(CSlangParser.RPN, 0)

        def exprparen(self):
            return self.getTypedRuleContext(CSlangParser.ExprparenContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exprobj




    def exprobj(self):

        localctx = CSlangParser.ExprobjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_exprobj)
        try:
            self.state = 325
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.match(CSlangParser.NEW)
                self.state = 319
                self.match(CSlangParser.ID)
                self.state = 320
                self.match(CSlangParser.LPN)
                self.state = 321
                self.expressions()
                self.state = 322
                self.match(CSlangParser.RPN)
                pass
            elif token in [CSlangParser.SELF, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.INT_LIT, CSlangParser.FLOAT_LIT, CSlangParser.BOOL_LIT, CSlangParser.STR_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.exprparen()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprparenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPN(self):
            return self.getToken(CSlangParser.LPN, 0)

        def exprstr(self):
            return self.getTypedRuleContext(CSlangParser.ExprstrContext,0)


        def RPN(self):
            return self.getToken(CSlangParser.RPN, 0)

        def exprlelf(self):
            return self.getTypedRuleContext(CSlangParser.ExprlelfContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exprparen




    def exprparen(self):

        localctx = CSlangParser.ExprparenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_exprparen)
        try:
            self.state = 332
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LPN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.match(CSlangParser.LPN)
                self.state = 328
                self.exprstr()
                self.state = 329
                self.match(CSlangParser.RPN)
                pass
            elif token in [CSlangParser.SELF, CSlangParser.LBK, CSlangParser.INT_LIT, CSlangParser.FLOAT_LIT, CSlangParser.BOOL_LIT, CSlangParser.STR_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
                self.exprlelf()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlelfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifiers(self):
            return self.getTypedRuleContext(CSlangParser.IdentifiersContext,0)


        def literals(self):
            return self.getTypedRuleContext(CSlangParser.LiteralsContext,0)


        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exprlelf




    def exprlelf(self):

        localctx = CSlangParser.ExprlelfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_exprlelf)
        try:
            self.state = 337
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.identifiers()
                pass
            elif token in [CSlangParser.LBK, CSlangParser.INT_LIT, CSlangParser.FLOAT_LIT, CSlangParser.BOOL_LIT, CSlangParser.STR_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                self.literals()
                pass
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 336
                self.match(CSlangParser.SELF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifiersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_identifiers




    def identifiers(self):

        localctx = CSlangParser.IdentifiersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_identifiers)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            _la = self._input.LA(1)
            if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(CSlangParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(CSlangParser.FLOAT_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(CSlangParser.BOOL_LIT, 0)

        def STR_LIT(self):
            return self.getToken(CSlangParser.STR_LIT, 0)

        def arrayliteral(self):
            return self.getTypedRuleContext(CSlangParser.ArrayliteralContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_literals




    def literals(self):

        localctx = CSlangParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_literals)
        try:
            self.state = 346
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.match(CSlangParser.INT_LIT)
                pass
            elif token in [CSlangParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
                self.match(CSlangParser.FLOAT_LIT)
                pass
            elif token in [CSlangParser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 343
                self.match(CSlangParser.BOOL_LIT)
                pass
            elif token in [CSlangParser.STR_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 344
                self.match(CSlangParser.STR_LIT)
                pass
            elif token in [CSlangParser.LBK]:
                self.enterOuterAlt(localctx, 5)
                self.state = 345
                self.arrayliteral()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayliteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBK(self):
            return self.getToken(CSlangParser.LBK, 0)

        def RBK(self):
            return self.getToken(CSlangParser.RBK, 0)

        def arrint(self):
            return self.getTypedRuleContext(CSlangParser.ArrintContext,0)


        def arrfloat(self):
            return self.getTypedRuleContext(CSlangParser.ArrfloatContext,0)


        def arrbool(self):
            return self.getTypedRuleContext(CSlangParser.ArrboolContext,0)


        def arrstr(self):
            return self.getTypedRuleContext(CSlangParser.ArrstrContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_arrayliteral




    def arrayliteral(self):

        localctx = CSlangParser.ArrayliteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_arrayliteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(CSlangParser.LBK)
            self.state = 353
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT_LIT]:
                self.state = 349
                self.arrint()
                pass
            elif token in [CSlangParser.FLOAT_LIT]:
                self.state = 350
                self.arrfloat()
                pass
            elif token in [CSlangParser.BOOL_LIT]:
                self.state = 351
                self.arrbool()
                pass
            elif token in [CSlangParser.STR_LIT]:
                self.state = 352
                self.arrstr()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 355
            self.match(CSlangParser.RBK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(CSlangParser.INT_LIT, 0)

        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def arrint(self):
            return self.getTypedRuleContext(CSlangParser.ArrintContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_arrint




    def arrint(self):

        localctx = CSlangParser.ArrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_arrint)
        try:
            self.state = 361
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.match(CSlangParser.INT_LIT)
                self.state = 358
                self.match(CSlangParser.CM)
                self.state = 359
                self.arrint()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 360
                self.match(CSlangParser.INT_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrfloatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT_LIT(self):
            return self.getToken(CSlangParser.FLOAT_LIT, 0)

        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def arrfloat(self):
            return self.getTypedRuleContext(CSlangParser.ArrfloatContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_arrfloat




    def arrfloat(self):

        localctx = CSlangParser.ArrfloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_arrfloat)
        try:
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 363
                self.match(CSlangParser.FLOAT_LIT)
                self.state = 364
                self.match(CSlangParser.CM)
                self.state = 365
                self.arrfloat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self.match(CSlangParser.FLOAT_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrboolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL_LIT(self):
            return self.getToken(CSlangParser.BOOL_LIT, 0)

        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def arrbool(self):
            return self.getTypedRuleContext(CSlangParser.ArrboolContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_arrbool




    def arrbool(self):

        localctx = CSlangParser.ArrboolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_arrbool)
        try:
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.match(CSlangParser.BOOL_LIT)
                self.state = 370
                self.match(CSlangParser.CM)
                self.state = 371
                self.arrbool()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 372
                self.match(CSlangParser.BOOL_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrstrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR_LIT(self):
            return self.getToken(CSlangParser.STR_LIT, 0)

        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def arrstr(self):
            return self.getTypedRuleContext(CSlangParser.ArrstrContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_arrstr




    def arrstr(self):

        localctx = CSlangParser.ArrstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_arrstr)
        try:
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.match(CSlangParser.STR_LIT)
                self.state = 376
                self.match(CSlangParser.CM)
                self.state = 377
                self.arrstr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
                self.match(CSlangParser.STR_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(CSlangParser.StmtContext,0)


        def statements(self):
            return self.getTypedRuleContext(CSlangParser.StatementsContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_statements




    def statements(self):

        localctx = CSlangParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_statements)
        try:
            self.state = 385
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.BREAK, CSlangParser.CONTINUE, CSlangParser.IF, CSlangParser.FOR, CSlangParser.RETURN, CSlangParser.VAR, CSlangParser.SELF, CSlangParser.CONST, CSlangParser.NEW, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.INT_LIT, CSlangParser.FLOAT_LIT, CSlangParser.BOOL_LIT, CSlangParser.STR_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.stmt()
                self.state = 382
                self.statements()
                pass
            elif token in [CSlangParser.RBR]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmtassign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.StmtassignContext)
            else:
                return self.getTypedRuleContext(CSlangParser.StmtassignContext,i)


        def SM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.SM)
            else:
                return self.getToken(CSlangParser.SM, i)

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def IF(self):
            return self.getToken(CSlangParser.IF, 0)

        def exprstr(self):
            return self.getTypedRuleContext(CSlangParser.ExprstrContext,0)


        def stmtblock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.StmtblockContext)
            else:
                return self.getTypedRuleContext(CSlangParser.StmtblockContext,i)


        def ELSE(self):
            return self.getToken(CSlangParser.ELSE, 0)

        def FOR(self):
            return self.getToken(CSlangParser.FOR, 0)

        def exprrel(self):
            return self.getTypedRuleContext(CSlangParser.ExprrelContext,0)


        def BREAK(self):
            return self.getToken(CSlangParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(CSlangParser.CONTINUE, 0)

        def RETURN(self):
            return self.getToken(CSlangParser.RETURN, 0)

        def exprinst(self):
            return self.getTypedRuleContext(CSlangParser.ExprinstContext,0)


        def attribute(self):
            return self.getTypedRuleContext(CSlangParser.AttributeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmt




    def stmt(self):

        localctx = CSlangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_stmt)
        try:
            self.state = 429
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.VAR]:
                    self.state = 387
                    self.match(CSlangParser.VAR)
                    pass
                elif token in [CSlangParser.CONST]:
                    self.state = 388
                    self.match(CSlangParser.CONST)
                    pass
                elif token in [CSlangParser.SELF, CSlangParser.NEW, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.INT_LIT, CSlangParser.FLOAT_LIT, CSlangParser.BOOL_LIT, CSlangParser.STR_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 392
                self.stmtassign()
                self.state = 393
                self.match(CSlangParser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.match(CSlangParser.IF)
                self.state = 398
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.LBR]:
                    self.state = 396
                    self.stmtblock()
                    pass
                elif token in [CSlangParser.SELF, CSlangParser.MINUS, CSlangParser.NEG, CSlangParser.NEW, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.INT_LIT, CSlangParser.FLOAT_LIT, CSlangParser.BOOL_LIT, CSlangParser.STR_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 400
                self.exprstr()
                self.state = 401
                self.stmtblock()
                self.state = 405
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.ELSE]:
                    self.state = 402
                    self.match(CSlangParser.ELSE)
                    self.state = 403
                    self.stmtblock()
                    pass
                elif token in [CSlangParser.BREAK, CSlangParser.CONTINUE, CSlangParser.IF, CSlangParser.FOR, CSlangParser.RETURN, CSlangParser.VAR, CSlangParser.SELF, CSlangParser.CONST, CSlangParser.NEW, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.RBR, CSlangParser.INT_LIT, CSlangParser.FLOAT_LIT, CSlangParser.BOOL_LIT, CSlangParser.STR_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 407
                self.match(CSlangParser.FOR)
                self.state = 408
                self.stmtassign()
                self.state = 409
                self.match(CSlangParser.SM)
                self.state = 410
                self.exprrel()
                self.state = 411
                self.match(CSlangParser.SM)
                self.state = 412
                self.stmtassign()
                self.state = 413
                self.stmtblock()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 415
                self.match(CSlangParser.BREAK)
                self.state = 416
                self.match(CSlangParser.SM)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 417
                self.match(CSlangParser.CONTINUE)
                self.state = 418
                self.match(CSlangParser.SM)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 419
                self.match(CSlangParser.RETURN)
                self.state = 420
                self.exprstr()
                self.state = 421
                self.match(CSlangParser.SM)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 423
                self.exprinst(0)
                self.state = 424
                self.match(CSlangParser.SM)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 426
                self.attribute()
                self.state = 427
                self.match(CSlangParser.SM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtassignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprindex(self):
            return self.getTypedRuleContext(CSlangParser.ExprindexContext,0)


        def ASSIGN(self):
            return self.getToken(CSlangParser.ASSIGN, 0)

        def exprstr(self):
            return self.getTypedRuleContext(CSlangParser.ExprstrContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmtassign




    def stmtassign(self):

        localctx = CSlangParser.StmtassignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_stmtassign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.exprindex()
            self.state = 432
            self.match(CSlangParser.ASSIGN)
            self.state = 433
            self.exprstr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[20] = self.exprlog_sempred
        self._predicates[21] = self.expradd_sempred
        self._predicates[22] = self.exprmul_sempred
        self._predicates[26] = self.exprinst_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exprlog_sempred(self, localctx:ExprlogContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expradd_sempred(self, localctx:ExpraddContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exprmul_sempred(self, localctx:ExprmulContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exprinst_sempred(self, localctx:ExprinstContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




