# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3?")
        buf.write("\u01da\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\5\3b\n\3\3\4\3\4\3\4\5\4g\n\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5r\n\5\3\6\3\6\3\6")
        buf.write("\3\6\5\6x\n\6\3\7\3\7\3\7\5\7}\n\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u008b\n\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\5\t\u0095\n\t\3\n\3\n\3\n\5\n\u009a")
        buf.write("\n\n\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\5\f\u00a4\n\f\3")
        buf.write("\f\3\f\3\f\3\f\5\f\u00aa\n\f\3\f\3\f\3\f\3\f\3\f\3\f\5")
        buf.write("\f\u00b2\n\f\3\f\3\f\5\f\u00b6\n\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\5\r\u00c0\n\r\3\16\3\16\3\16\3\16\5\16\u00c6")
        buf.write("\n\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\5\21\u00d2\n\21\3\22\3\22\3\22\3\22\3\22\5\22\u00d9\n")
        buf.write("\22\3\23\3\23\3\23\3\23\3\23\5\23\u00e0\n\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\5\24\u00e7\n\24\3\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\7\25\u00ef\n\25\f\25\16\25\u00f2\13\25\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\7\26\u00fa\n\26\f\26\16\26\u00fd")
        buf.write("\13\26\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u0105\n\27\f")
        buf.write("\27\16\27\u0108\13\27\3\30\3\30\3\30\5\30\u010d\n\30\3")
        buf.write("\31\3\31\3\31\5\31\u0112\n\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\5\32\u011a\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\5\33\u0123\n\33\7\33\u0125\n\33\f\33\16\33\u0128\13")
        buf.write("\33\3\34\3\34\5\34\u012c\n\34\3\34\3\34\5\34\u0130\n\34")
        buf.write("\3\34\5\34\u0133\n\34\3\35\3\35\3\35\3\35\5\35\u0139\n")
        buf.write("\35\3\36\3\36\3\36\3\36\3\36\5\36\u0140\n\36\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3 \3 \3 \3 \5 \u014c\n \3!\3!\3\"\3\"\3\"")
        buf.write("\3\"\3#\3#\5#\u0156\n#\3$\3$\3$\3$\3$\5$\u015d\n$\3%\3")
        buf.write("%\3%\3%\5%\u0163\n%\3&\5&\u0166\n&\3&\3&\3&\3&\3&\5&\u016d")
        buf.write("\n&\3&\3&\3&\3&\5&\u0173\n&\3&\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\5&\u0183\n&\3&\3&\3&\3&\3&\3&\3&\5&\u018c")
        buf.write("\n&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\7(\u019a\n")
        buf.write("(\f(\16(\u019d\13(\3)\3)\3)\3)\3)\3)\3)\5)\u01a6\n)\7")
        buf.write(")\u01a8\n)\f)\16)\u01ab\13)\3*\3*\5*\u01af\n*\3*\3*\5")
        buf.write("*\u01b3\n*\3*\5*\u01b6\n*\3+\3+\3+\3+\3+\3+\5+\u01be\n")
        buf.write("+\3,\3,\3,\3,\3,\3,\3,\5,\u01c7\n,\7,\u01c9\n,\f,\16,")
        buf.write("\u01cc\13,\3-\3-\5-\u01d0\n-\3-\3-\5-\u01d4\n-\3-\3-\5")
        buf.write("-\u01d8\n-\3-\2\t(*,\64NPV.\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX\2\n")
        buf.write("\4\2\22\22\25\25\4\2\n\r::\3\2 %\3\2\36\37\3\2\27\30\3")
        buf.write("\2\31\34\3\2:;\3\2\b\t\2\u01ef\2Z\3\2\2\2\4a\3\2\2\2\6")
        buf.write("c\3\2\2\2\bq\3\2\2\2\nw\3\2\2\2\fy\3\2\2\2\16\u008a\3")
        buf.write("\2\2\2\20\u0094\3\2\2\2\22\u0099\3\2\2\2\24\u009d\3\2")
        buf.write("\2\2\26\u00b5\3\2\2\2\30\u00bf\3\2\2\2\32\u00c5\3\2\2")
        buf.write("\2\34\u00c7\3\2\2\2\36\u00cb\3\2\2\2 \u00d1\3\2\2\2\"")
        buf.write("\u00d8\3\2\2\2$\u00df\3\2\2\2&\u00e6\3\2\2\2(\u00e8\3")
        buf.write("\2\2\2*\u00f3\3\2\2\2,\u00fe\3\2\2\2.\u010c\3\2\2\2\60")
        buf.write("\u0111\3\2\2\2\62\u0119\3\2\2\2\64\u011b\3\2\2\2\66\u0132")
        buf.write("\3\2\2\28\u0138\3\2\2\2:\u013f\3\2\2\2<\u0141\3\2\2\2")
        buf.write(">\u014b\3\2\2\2@\u014d\3\2\2\2B\u014f\3\2\2\2D\u0155\3")
        buf.write("\2\2\2F\u015c\3\2\2\2H\u0162\3\2\2\2J\u018b\3\2\2\2L\u018d")
        buf.write("\3\2\2\2N\u0191\3\2\2\2P\u019e\3\2\2\2R\u01b5\3\2\2\2")
        buf.write("T\u01bd\3\2\2\2V\u01bf\3\2\2\2X\u01d7\3\2\2\2Z[\5\4\3")
        buf.write("\2[\\\7\2\2\3\\\3\3\2\2\2]^\5\6\4\2^_\5\4\3\2_b\3\2\2")
        buf.write("\2`b\5\6\4\2a]\3\2\2\2a`\3\2\2\2b\5\3\2\2\2cf\7\20\2\2")
        buf.write("de\7:\2\2eg\7)\2\2fd\3\2\2\2fg\3\2\2\2gh\3\2\2\2hi\7:")
        buf.write("\2\2ij\7/\2\2jk\5\b\5\2kl\7\60\2\2l\7\3\2\2\2mn\5\n\6")
        buf.write("\2no\5\b\5\2or\3\2\2\2pr\3\2\2\2qm\3\2\2\2qp\3\2\2\2r")
        buf.write("\t\3\2\2\2st\5\f\7\2tu\7\63\2\2ux\3\2\2\2vx\5\26\f\2w")
        buf.write("s\3\2\2\2wv\3\2\2\2x\13\3\2\2\2y|\t\2\2\2z}\5\16\b\2{")
        buf.write("}\5\20\t\2|z\3\2\2\2|{\3\2\2\2}\r\3\2\2\2~\177\5<\37\2")
        buf.write("\177\u0080\7\62\2\2\u0080\u0081\5\16\b\2\u0081\u0082\7")
        buf.write("\62\2\2\u0082\u0083\5$\23\2\u0083\u008b\3\2\2\2\u0084")
        buf.write("\u0085\5<\37\2\u0085\u0086\7\64\2\2\u0086\u0087\5\22\n")
        buf.write("\2\u0087\u0088\7&\2\2\u0088\u0089\5$\23\2\u0089\u008b")
        buf.write("\3\2\2\2\u008a~\3\2\2\2\u008a\u0084\3\2\2\2\u008b\17\3")
        buf.write("\2\2\2\u008c\u008d\5<\37\2\u008d\u008e\7\62\2\2\u008e")
        buf.write("\u008f\5\20\t\2\u008f\u0095\3\2\2\2\u0090\u0091\5<\37")
        buf.write("\2\u0091\u0092\7\64\2\2\u0092\u0093\5\22\n\2\u0093\u0095")
        buf.write("\3\2\2\2\u0094\u008c\3\2\2\2\u0094\u0090\3\2\2\2\u0095")
        buf.write("\21\3\2\2\2\u0096\u0097\7-\2\2\u0097\u0098\7\65\2\2\u0098")
        buf.write("\u009a\7.\2\2\u0099\u0096\3\2\2\2\u0099\u009a\3\2\2\2")
        buf.write("\u009a\u009b\3\2\2\2\u009b\u009c\5\24\13\2\u009c\23\3")
        buf.write("\2\2\2\u009d\u009e\t\3\2\2\u009e\25\3\2\2\2\u009f\u00a0")
        buf.write("\7\26\2\2\u00a0\u00a1\5<\37\2\u00a1\u00a3\7+\2\2\u00a2")
        buf.write("\u00a4\5\30\r\2\u00a3\u00a2\3\2\2\2\u00a3\u00a4\3\2\2")
        buf.write("\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6\7,\2\2\u00a6\u00a9")
        buf.write("\7\64\2\2\u00a7\u00aa\5\24\13\2\u00a8\u00aa\7\24\2\2\u00a9")
        buf.write("\u00a7\3\2\2\2\u00a9\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2")
        buf.write("\u00ab\u00ac\5\34\17\2\u00ac\u00b6\3\2\2\2\u00ad\u00ae")
        buf.write("\7\26\2\2\u00ae\u00af\7\21\2\2\u00af\u00b1\7+\2\2\u00b0")
        buf.write("\u00b2\5\30\r\2\u00b1\u00b0\3\2\2\2\u00b1\u00b2\3\2\2")
        buf.write("\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4\7,\2\2\u00b4\u00b6")
        buf.write("\5\34\17\2\u00b5\u009f\3\2\2\2\u00b5\u00ad\3\2\2\2\u00b6")
        buf.write("\27\3\2\2\2\u00b7\u00b8\5\32\16\2\u00b8\u00b9\7\62\2\2")
        buf.write("\u00b9\u00ba\5\30\r\2\u00ba\u00c0\3\2\2\2\u00bb\u00bc")
        buf.write("\5\32\16\2\u00bc\u00bd\7\64\2\2\u00bd\u00be\5\24\13\2")
        buf.write("\u00be\u00c0\3\2\2\2\u00bf\u00b7\3\2\2\2\u00bf\u00bb\3")
        buf.write("\2\2\2\u00c0\31\3\2\2\2\u00c1\u00c2\7:\2\2\u00c2\u00c3")
        buf.write("\7\62\2\2\u00c3\u00c6\5\32\16\2\u00c4\u00c6\7:\2\2\u00c5")
        buf.write("\u00c1\3\2\2\2\u00c5\u00c4\3\2\2\2\u00c6\33\3\2\2\2\u00c7")
        buf.write("\u00c8\7/\2\2\u00c8\u00c9\5H%\2\u00c9\u00ca\7\60\2\2\u00ca")
        buf.write("\35\3\2\2\2\u00cb\u00cc\7+\2\2\u00cc\u00cd\5 \21\2\u00cd")
        buf.write("\u00ce\7,\2\2\u00ce\37\3\2\2\2\u00cf\u00d2\5\"\22\2\u00d0")
        buf.write("\u00d2\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d1\u00d0\3\2\2\2")
        buf.write("\u00d2!\3\2\2\2\u00d3\u00d4\5$\23\2\u00d4\u00d5\7\62\2")
        buf.write("\2\u00d5\u00d6\5 \21\2\u00d6\u00d9\3\2\2\2\u00d7\u00d9")
        buf.write("\5$\23\2\u00d8\u00d3\3\2\2\2\u00d8\u00d7\3\2\2\2\u00d9")
        buf.write("#\3\2\2\2\u00da\u00db\5&\24\2\u00db\u00dc\7(\2\2\u00dc")
        buf.write("\u00dd\5&\24\2\u00dd\u00e0\3\2\2\2\u00de\u00e0\5&\24\2")
        buf.write("\u00df\u00da\3\2\2\2\u00df\u00de\3\2\2\2\u00e0%\3\2\2")
        buf.write("\2\u00e1\u00e2\5(\25\2\u00e2\u00e3\t\4\2\2\u00e3\u00e4")
        buf.write("\5(\25\2\u00e4\u00e7\3\2\2\2\u00e5\u00e7\5(\25\2\u00e6")
        buf.write("\u00e1\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7\'\3\2\2\2\u00e8")
        buf.write("\u00e9\b\25\1\2\u00e9\u00ea\5*\26\2\u00ea\u00f0\3\2\2")
        buf.write("\2\u00eb\u00ec\f\4\2\2\u00ec\u00ed\t\5\2\2\u00ed\u00ef")
        buf.write("\5*\26\2\u00ee\u00eb\3\2\2\2\u00ef\u00f2\3\2\2\2\u00f0")
        buf.write("\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1)\3\2\2\2\u00f2")
        buf.write("\u00f0\3\2\2\2\u00f3\u00f4\b\26\1\2\u00f4\u00f5\5,\27")
        buf.write("\2\u00f5\u00fb\3\2\2\2\u00f6\u00f7\f\4\2\2\u00f7\u00f8")
        buf.write("\t\6\2\2\u00f8\u00fa\5,\27\2\u00f9\u00f6\3\2\2\2\u00fa")
        buf.write("\u00fd\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2")
        buf.write("\u00fc+\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fe\u00ff\b\27\1")
        buf.write("\2\u00ff\u0100\5.\30\2\u0100\u0106\3\2\2\2\u0101\u0102")
        buf.write("\f\4\2\2\u0102\u0103\t\7\2\2\u0103\u0105\5.\30\2\u0104")
        buf.write("\u0101\3\2\2\2\u0105\u0108\3\2\2\2\u0106\u0104\3\2\2\2")
        buf.write("\u0106\u0107\3\2\2\2\u0107-\3\2\2\2\u0108\u0106\3\2\2")
        buf.write("\2\u0109\u010a\7\35\2\2\u010a\u010d\5.\30\2\u010b\u010d")
        buf.write("\5\60\31\2\u010c\u0109\3\2\2\2\u010c\u010b\3\2\2\2\u010d")
        buf.write("/\3\2\2\2\u010e\u010f\7\30\2\2\u010f\u0112\5\60\31\2\u0110")
        buf.write("\u0112\5\62\32\2\u0111\u010e\3\2\2\2\u0111\u0110\3\2\2")
        buf.write("\2\u0112\61\3\2\2\2\u0113\u0114\5\64\33\2\u0114\u0115")
        buf.write("\7-\2\2\u0115\u0116\5$\23\2\u0116\u0117\7.\2\2\u0117\u011a")
        buf.write("\3\2\2\2\u0118\u011a\5\64\33\2\u0119\u0113\3\2\2\2\u0119")
        buf.write("\u0118\3\2\2\2\u011a\63\3\2\2\2\u011b\u011c\b\33\1\2\u011c")
        buf.write("\u011d\5\66\34\2\u011d\u0126\3\2\2\2\u011e\u011f\f\4\2")
        buf.write("\2\u011f\u0120\7\61\2\2\u0120\u0122\7:\2\2\u0121\u0123")
        buf.write("\5\36\20\2\u0122\u0121\3\2\2\2\u0122\u0123\3\2\2\2\u0123")
        buf.write("\u0125\3\2\2\2\u0124\u011e\3\2\2\2\u0125\u0128\3\2\2\2")
        buf.write("\u0126\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127\65\3\2")
        buf.write("\2\2\u0128\u0126\3\2\2\2\u0129\u012a\7:\2\2\u012a\u012c")
        buf.write("\7\61\2\2\u012b\u0129\3\2\2\2\u012b\u012c\3\2\2\2\u012c")
        buf.write("\u012d\3\2\2\2\u012d\u012f\7;\2\2\u012e\u0130\5\36\20")
        buf.write("\2\u012f\u012e\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u0133")
        buf.write("\3\2\2\2\u0131\u0133\58\35\2\u0132\u012b\3\2\2\2\u0132")
        buf.write("\u0131\3\2\2\2\u0133\67\3\2\2\2\u0134\u0135\7*\2\2\u0135")
        buf.write("\u0136\7:\2\2\u0136\u0139\5\36\20\2\u0137\u0139\5:\36")
        buf.write("\2\u0138\u0134\3\2\2\2\u0138\u0137\3\2\2\2\u01399\3\2")
        buf.write("\2\2\u013a\u013b\7+\2\2\u013b\u013c\5$\23\2\u013c\u013d")
        buf.write("\7,\2\2\u013d\u0140\3\2\2\2\u013e\u0140\5> \2\u013f\u013a")
        buf.write("\3\2\2\2\u013f\u013e\3\2\2\2\u0140;\3\2\2\2\u0141\u0142")
        buf.write("\t\b\2\2\u0142=\3\2\2\2\u0143\u014c\7\65\2\2\u0144\u014c")
        buf.write("\7\66\2\2\u0145\u014c\5@!\2\u0146\u014c\7\67\2\2\u0147")
        buf.write("\u014c\5B\"\2\u0148\u014c\7\17\2\2\u0149\u014c\7\23\2")
        buf.write("\2\u014a\u014c\5<\37\2\u014b\u0143\3\2\2\2\u014b\u0144")
        buf.write("\3\2\2\2\u014b\u0145\3\2\2\2\u014b\u0146\3\2\2\2\u014b")
        buf.write("\u0147\3\2\2\2\u014b\u0148\3\2\2\2\u014b\u0149\3\2\2\2")
        buf.write("\u014b\u014a\3\2\2\2\u014c?\3\2\2\2\u014d\u014e\t\t\2")
        buf.write("\2\u014eA\3\2\2\2\u014f\u0150\7-\2\2\u0150\u0151\5F$\2")
        buf.write("\u0151\u0152\7.\2\2\u0152C\3\2\2\2\u0153\u0156\5F$\2\u0154")
        buf.write("\u0156\3\2\2\2\u0155\u0153\3\2\2\2\u0155\u0154\3\2\2\2")
        buf.write("\u0156E\3\2\2\2\u0157\u0158\5> \2\u0158\u0159\7\62\2\2")
        buf.write("\u0159\u015a\5D#\2\u015a\u015d\3\2\2\2\u015b\u015d\5>")
        buf.write(" \2\u015c\u0157\3\2\2\2\u015c\u015b\3\2\2\2\u015dG\3\2")
        buf.write("\2\2\u015e\u015f\5J&\2\u015f\u0160\5H%\2\u0160\u0163\3")
        buf.write("\2\2\2\u0161\u0163\3\2\2\2\u0162\u015e\3\2\2\2\u0162\u0161")
        buf.write("\3\2\2\2\u0163I\3\2\2\2\u0164\u0166\t\2\2\2\u0165\u0164")
        buf.write("\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0167\3\2\2\2\u0167")
        buf.write("\u0168\5L\'\2\u0168\u0169\7\63\2\2\u0169\u018c\3\2\2\2")
        buf.write("\u016a\u016c\7\5\2\2\u016b\u016d\5\34\17\2\u016c\u016b")
        buf.write("\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016e\3\2\2\2\u016e")
        buf.write("\u016f\5$\23\2\u016f\u0172\5\34\17\2\u0170\u0171\7\6\2")
        buf.write("\2\u0171\u0173\5\34\17\2\u0172\u0170\3\2\2\2\u0172\u0173")
        buf.write("\3\2\2\2\u0173\u018c\3\2\2\2\u0174\u0175\7\7\2\2\u0175")
        buf.write("\u0176\5L\'\2\u0176\u0177\7\63\2\2\u0177\u0178\5&\24\2")
        buf.write("\u0178\u0179\7\63\2\2\u0179\u017a\5L\'\2\u017a\u017b\5")
        buf.write("\34\17\2\u017b\u018c\3\2\2\2\u017c\u017d\7\3\2\2\u017d")
        buf.write("\u018c\7\63\2\2\u017e\u017f\7\4\2\2\u017f\u018c\7\63\2")
        buf.write("\2\u0180\u0182\7\16\2\2\u0181\u0183\5$\23\2\u0182\u0181")
        buf.write("\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0184\3\2\2\2\u0184")
        buf.write("\u018c\7\63\2\2\u0185\u0186\5V,\2\u0186\u0187\7\63\2\2")
        buf.write("\u0187\u018c\3\2\2\2\u0188\u0189\5\f\7\2\u0189\u018a\7")
        buf.write("\63\2\2\u018a\u018c\3\2\2\2\u018b\u0165\3\2\2\2\u018b")
        buf.write("\u016a\3\2\2\2\u018b\u0174\3\2\2\2\u018b\u017c\3\2\2\2")
        buf.write("\u018b\u017e\3\2\2\2\u018b\u0180\3\2\2\2\u018b\u0185\3")
        buf.write("\2\2\2\u018b\u0188\3\2\2\2\u018cK\3\2\2\2\u018d\u018e")
        buf.write("\5N(\2\u018e\u018f\7\'\2\2\u018f\u0190\5$\23\2\u0190M")
        buf.write("\3\2\2\2\u0191\u0192\b(\1\2\u0192\u0193\5P)\2\u0193\u019b")
        buf.write("\3\2\2\2\u0194\u0195\f\4\2\2\u0195\u0196\7-\2\2\u0196")
        buf.write("\u0197\5$\23\2\u0197\u0198\7.\2\2\u0198\u019a\3\2\2\2")
        buf.write("\u0199\u0194\3\2\2\2\u019a\u019d\3\2\2\2\u019b\u0199\3")
        buf.write("\2\2\2\u019b\u019c\3\2\2\2\u019cO\3\2\2\2\u019d\u019b")
        buf.write("\3\2\2\2\u019e\u019f\b)\1\2\u019f\u01a0\5R*\2\u01a0\u01a9")
        buf.write("\3\2\2\2\u01a1\u01a2\f\4\2\2\u01a2\u01a3\7\61\2\2\u01a3")
        buf.write("\u01a5\7:\2\2\u01a4\u01a6\5\36\20\2\u01a5\u01a4\3\2\2")
        buf.write("\2\u01a5\u01a6\3\2\2\2\u01a6\u01a8\3\2\2\2\u01a7\u01a1")
        buf.write("\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9")
        buf.write("\u01aa\3\2\2\2\u01aaQ\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac")
        buf.write("\u01ad\7:\2\2\u01ad\u01af\7\61\2\2\u01ae\u01ac\3\2\2\2")
        buf.write("\u01ae\u01af\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01b2\7")
        buf.write(";\2\2\u01b1\u01b3\5\36\20\2\u01b2\u01b1\3\2\2\2\u01b2")
        buf.write("\u01b3\3\2\2\2\u01b3\u01b6\3\2\2\2\u01b4\u01b6\5T+\2\u01b5")
        buf.write("\u01ae\3\2\2\2\u01b5\u01b4\3\2\2\2\u01b6S\3\2\2\2\u01b7")
        buf.write("\u01b8\7+\2\2\u01b8\u01b9\5N(\2\u01b9\u01ba\7,\2\2\u01ba")
        buf.write("\u01be\3\2\2\2\u01bb\u01be\7\23\2\2\u01bc\u01be\5<\37")
        buf.write("\2\u01bd\u01b7\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd\u01bc")
        buf.write("\3\2\2\2\u01beU\3\2\2\2\u01bf\u01c0\b,\1\2\u01c0\u01c1")
        buf.write("\5X-\2\u01c1\u01ca\3\2\2\2\u01c2\u01c3\f\4\2\2\u01c3\u01c4")
        buf.write("\7\61\2\2\u01c4\u01c6\7:\2\2\u01c5\u01c7\5\36\20\2\u01c6")
        buf.write("\u01c5\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c9\3\2\2\2")
        buf.write("\u01c8\u01c2\3\2\2\2\u01c9\u01cc\3\2\2\2\u01ca\u01c8\3")
        buf.write("\2\2\2\u01ca\u01cb\3\2\2\2\u01cbW\3\2\2\2\u01cc\u01ca")
        buf.write("\3\2\2\2\u01cd\u01ce\7:\2\2\u01ce\u01d0\7\61\2\2\u01cf")
        buf.write("\u01cd\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d1\3\2\2\2")
        buf.write("\u01d1\u01d3\7;\2\2\u01d2\u01d4\5\36\20\2\u01d3\u01d2")
        buf.write("\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d8\3\2\2\2\u01d5")
        buf.write("\u01d8\7\23\2\2\u01d6\u01d8\5<\37\2\u01d7\u01cf\3\2\2")
        buf.write("\2\u01d7\u01d5\3\2\2\2\u01d7\u01d6\3\2\2\2\u01d8Y\3\2")
        buf.write("\2\2\66afqw|\u008a\u0094\u0099\u00a3\u00a9\u00b1\u00b5")
        buf.write("\u00bf\u00c5\u00d1\u00d8\u00df\u00e6\u00f0\u00fb\u0106")
        buf.write("\u010c\u0111\u0119\u0122\u0126\u012b\u012f\u0132\u0138")
        buf.write("\u013f\u014b\u0155\u015c\u0162\u0165\u016c\u0172\u0182")
        buf.write("\u018b\u019b\u01a5\u01a9\u01ae\u01b2\u01b5\u01bd\u01c6")
        buf.write("\u01ca\u01cf\u01d3\u01d7")
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
                      "VOID", "CONST", "FUNC", "ADD", "SUB", "MUL", "DIVFLOAT", 
                      "DIVINT", "MOD", "NEG", "AND", "OR", "EQ", "NEQ", 
                      "LT", "LTEQ", "GT", "GTEQ", "DECLARE", "ASSIGN", "CONCATE", 
                      "LARROW", "NEW", "LPN", "RPN", "LBK", "RBK", "LBR", 
                      "RBR", "DOT", "CM", "SM", "COL", "INTLIT", "FLOATLIT", 
                      "STRLIT", "BLOCK_COMMENT", "LINE_COMMENT", "ID", "ATID", 
                      "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
    RULE_method = 10
    RULE_paramlist = 11
    RULE_params = 12
    RULE_blockstmt = 13
    RULE_parenexpr = 14
    RULE_exprlist = 15
    RULE_exprprime = 16
    RULE_exprstr = 17
    RULE_exprrel = 18
    RULE_exprlog = 19
    RULE_expradd = 20
    RULE_exprmul = 21
    RULE_exprnot = 22
    RULE_exprsign = 23
    RULE_exprindex = 24
    RULE_exprinst = 25
    RULE_exprstat = 26
    RULE_exprobj = 27
    RULE_exprparen = 28
    RULE_identifier = 29
    RULE_lit = 30
    RULE_boollit = 31
    RULE_arraylit = 32
    RULE_litlist = 33
    RULE_litprime = 34
    RULE_stmtlist = 35
    RULE_stmt = 36
    RULE_stmtassign = 37
    RULE_lhs = 38
    RULE_lhsinst = 39
    RULE_lhsstat = 40
    RULE_lhsparen = 41
    RULE_stmtinvoc = 42
    RULE_stmtinvocstat = 43

    ruleNames =  [ "program", "classdecllist", "classdecl", "memberlist", 
                   "member", "attribute", "attlistdecl", "attlistnodecl", 
                   "atttyp", "typ", "method", "paramlist", "params", "blockstmt", 
                   "parenexpr", "exprlist", "exprprime", "exprstr", "exprrel", 
                   "exprlog", "expradd", "exprmul", "exprnot", "exprsign", 
                   "exprindex", "exprinst", "exprstat", "exprobj", "exprparen", 
                   "identifier", "lit", "boollit", "arraylit", "litlist", 
                   "litprime", "stmtlist", "stmt", "stmtassign", "lhs", 
                   "lhsinst", "lhsstat", "lhsparen", "stmtinvoc", "stmtinvocstat" ]

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
    ADD=21
    SUB=22
    MUL=23
    DIVFLOAT=24
    DIVINT=25
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
    LARROW=39
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
    INTLIT=51
    FLOATLIT=52
    STRLIT=53
    BLOCK_COMMENT=54
    LINE_COMMENT=55
    ID=56
    ATID=57
    WS=58
    UNCLOSE_STRING=59
    ILLEGAL_ESCAPE=60
    ERROR_CHAR=61

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = CSlangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.classdecllist()
            self.state = 89
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassdecllist" ):
                return visitor.visitClassdecllist(self)
            else:
                return visitor.visitChildren(self)




    def classdecllist(self):

        localctx = CSlangParser.ClassdecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classdecllist)
        try:
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.classdecl()
                self.state = 92
                self.classdecllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
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

        def LARROW(self):
            return self.getToken(CSlangParser.LARROW, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_classdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassdecl" ):
                return visitor.visitClassdecl(self)
            else:
                return visitor.visitChildren(self)




    def classdecl(self):

        localctx = CSlangParser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(CSlangParser.CLASS)
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 98
                self.match(CSlangParser.ID)
                self.state = 99
                self.match(CSlangParser.LARROW)


            self.state = 102
            self.match(CSlangParser.ID)
            self.state = 103
            self.match(CSlangParser.LBR)
            self.state = 104
            self.memberlist()
            self.state = 105
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberlist" ):
                return visitor.visitMemberlist(self)
            else:
                return visitor.visitChildren(self)




    def memberlist(self):

        localctx = CSlangParser.MemberlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_memberlist)
        try:
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST, CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.member()
                self.state = 108
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember" ):
                return visitor.visitMember(self)
            else:
                return visitor.visitChildren(self)




    def member(self):

        localctx = CSlangParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_member)
        try:
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.attribute()
                self.state = 114
                self.match(CSlangParser.SM)
                pass
            elif token in [CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = CSlangParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 120
                self.attlistdecl()
                pass

            elif la_ == 2:
                self.state = 121
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

        def identifier(self):
            return self.getTypedRuleContext(CSlangParser.IdentifierContext,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttlistdecl" ):
                return visitor.visitAttlistdecl(self)
            else:
                return visitor.visitChildren(self)




    def attlistdecl(self):

        localctx = CSlangParser.AttlistdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attlistdecl)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.identifier()
                self.state = 125
                self.match(CSlangParser.CM)
                self.state = 126
                self.attlistdecl()
                self.state = 127
                self.match(CSlangParser.CM)
                self.state = 128
                self.exprstr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.identifier()
                self.state = 131
                self.match(CSlangParser.COL)
                self.state = 132
                self.atttyp()
                self.state = 133
                self.match(CSlangParser.DECLARE)
                self.state = 134
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

        def identifier(self):
            return self.getTypedRuleContext(CSlangParser.IdentifierContext,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttlistnodecl" ):
                return visitor.visitAttlistnodecl(self)
            else:
                return visitor.visitChildren(self)




    def attlistnodecl(self):

        localctx = CSlangParser.AttlistnodeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attlistnodecl)
        try:
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.identifier()
                self.state = 139
                self.match(CSlangParser.CM)
                self.state = 140
                self.attlistnodecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.identifier()
                self.state = 143
                self.match(CSlangParser.COL)
                self.state = 144
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


        def LBK(self):
            return self.getToken(CSlangParser.LBK, 0)

        def INTLIT(self):
            return self.getToken(CSlangParser.INTLIT, 0)

        def RBK(self):
            return self.getToken(CSlangParser.RBK, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_atttyp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtttyp" ):
                return visitor.visitAtttyp(self)
            else:
                return visitor.visitChildren(self)




    def atttyp(self):

        localctx = CSlangParser.AtttypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_atttyp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LBK:
                self.state = 148
                self.match(CSlangParser.LBK)
                self.state = 149
                self.match(CSlangParser.INTLIT)
                self.state = 150
                self.match(CSlangParser.RBK)


            self.state = 153
            self.typ()
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

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = CSlangParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.INT) | (1 << CSlangParser.FLOAT) | (1 << CSlangParser.BOOL) | (1 << CSlangParser.STRING) | (1 << CSlangParser.ID))) != 0)):
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


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSlangParser.IdentifierContext,0)


        def LPN(self):
            return self.getToken(CSlangParser.LPN, 0)

        def RPN(self):
            return self.getToken(CSlangParser.RPN, 0)

        def COL(self):
            return self.getToken(CSlangParser.COL, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(CSlangParser.BlockstmtContext,0)


        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def VOID(self):
            return self.getToken(CSlangParser.VOID, 0)

        def paramlist(self):
            return self.getTypedRuleContext(CSlangParser.ParamlistContext,0)


        def CONSTRUCTOR(self):
            return self.getToken(CSlangParser.CONSTRUCTOR, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = CSlangParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.match(CSlangParser.FUNC)
                self.state = 158
                self.identifier()
                self.state = 159
                self.match(CSlangParser.LPN)
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ID:
                    self.state = 160
                    self.paramlist()


                self.state = 163
                self.match(CSlangParser.RPN)
                self.state = 164
                self.match(CSlangParser.COL)
                self.state = 167
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.ID]:
                    self.state = 165
                    self.typ()
                    pass
                elif token in [CSlangParser.VOID]:
                    self.state = 166
                    self.match(CSlangParser.VOID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 169
                self.blockstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.match(CSlangParser.FUNC)
                self.state = 172
                self.match(CSlangParser.CONSTRUCTOR)
                self.state = 173
                self.match(CSlangParser.LPN)
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ID:
                    self.state = 174
                    self.paramlist()


                self.state = 177
                self.match(CSlangParser.RPN)
                self.state = 178
                self.blockstmt()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = CSlangParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_paramlist)
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.params()
                self.state = 182
                self.match(CSlangParser.CM)
                self.state = 183
                self.paramlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.params()
                self.state = 186
                self.match(CSlangParser.COL)
                self.state = 187
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = CSlangParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_params)
        try:
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.match(CSlangParser.ID)
                self.state = 192
                self.match(CSlangParser.CM)
                self.state = 193
                self.params()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.match(CSlangParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBR(self):
            return self.getToken(CSlangParser.LBR, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(CSlangParser.StmtlistContext,0)


        def RBR(self):
            return self.getToken(CSlangParser.RBR, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = CSlangParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(CSlangParser.LBR)
            self.state = 198
            self.stmtlist()
            self.state = 199
            self.match(CSlangParser.RBR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParenexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPN(self):
            return self.getToken(CSlangParser.LPN, 0)

        def exprlist(self):
            return self.getTypedRuleContext(CSlangParser.ExprlistContext,0)


        def RPN(self):
            return self.getToken(CSlangParser.RPN, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_parenexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenexpr" ):
                return visitor.visitParenexpr(self)
            else:
                return visitor.visitChildren(self)




    def parenexpr(self):

        localctx = CSlangParser.ParenexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_parenexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(CSlangParser.LPN)
            self.state = 202
            self.exprlist()
            self.state = 203
            self.match(CSlangParser.RPN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprprime(self):
            return self.getTypedRuleContext(CSlangParser.ExprprimeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = CSlangParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_exprlist)
        try:
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.SUB, CSlangParser.NEG, CSlangParser.NEW, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRLIT, CSlangParser.ID, CSlangParser.ATID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
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

        def exprlist(self):
            return self.getTypedRuleContext(CSlangParser.ExprlistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exprprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprprime" ):
                return visitor.visitExprprime(self)
            else:
                return visitor.visitChildren(self)




    def exprprime(self):

        localctx = CSlangParser.ExprprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_exprprime)
        try:
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.exprstr()
                self.state = 210
                self.match(CSlangParser.CM)
                self.state = 211
                self.exprlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprstr" ):
                return visitor.visitExprstr(self)
            else:
                return visitor.visitChildren(self)




    def exprstr(self):

        localctx = CSlangParser.ExprstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_exprstr)
        try:
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.exprrel()
                self.state = 217
                self.match(CSlangParser.CONCATE)
                self.state = 218
                self.exprrel()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprrel" ):
                return visitor.visitExprrel(self)
            else:
                return visitor.visitChildren(self)




    def exprrel(self):

        localctx = CSlangParser.ExprrelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_exprrel)
        self._la = 0 # Token type
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.exprlog(0)
                self.state = 224
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.EQ) | (1 << CSlangParser.NEQ) | (1 << CSlangParser.LT) | (1 << CSlangParser.LTEQ) | (1 << CSlangParser.GT) | (1 << CSlangParser.GTEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 225
                self.exprlog(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlog" ):
                return visitor.visitExprlog(self)
            else:
                return visitor.visitChildren(self)



    def exprlog(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.ExprlogContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_exprlog, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.expradd(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 238
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprlogContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprlog)
                    self.state = 233
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 234
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.AND or _la==CSlangParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 235
                    self.expradd(0) 
                self.state = 240
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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


        def ADD(self):
            return self.getToken(CSlangParser.ADD, 0)

        def SUB(self):
            return self.getToken(CSlangParser.SUB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expradd

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpradd" ):
                return visitor.visitExpradd(self)
            else:
                return visitor.visitChildren(self)



    def expradd(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.ExpraddContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expradd, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.exprmul(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 249
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExpraddContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expradd)
                    self.state = 244
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 245
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.ADD or _la==CSlangParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 246
                    self.exprmul(0) 
                self.state = 251
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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

        def DIVFLOAT(self):
            return self.getToken(CSlangParser.DIVFLOAT, 0)

        def DIVINT(self):
            return self.getToken(CSlangParser.DIVINT, 0)

        def MOD(self):
            return self.getToken(CSlangParser.MOD, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exprmul

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprmul" ):
                return visitor.visitExprmul(self)
            else:
                return visitor.visitChildren(self)



    def exprmul(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.ExprmulContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_exprmul, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.exprnot()
            self._ctx.stop = self._input.LT(-1)
            self.state = 260
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprmulContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprmul)
                    self.state = 255
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 256
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.MUL) | (1 << CSlangParser.DIVFLOAT) | (1 << CSlangParser.DIVINT) | (1 << CSlangParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 257
                    self.exprnot() 
                self.state = 262
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprnot" ):
                return visitor.visitExprnot(self)
            else:
                return visitor.visitChildren(self)




    def exprnot(self):

        localctx = CSlangParser.ExprnotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_exprnot)
        try:
            self.state = 266
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.match(CSlangParser.NEG)
                self.state = 264
                self.exprnot()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.SUB, CSlangParser.NEW, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRLIT, CSlangParser.ID, CSlangParser.ATID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
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

        def SUB(self):
            return self.getToken(CSlangParser.SUB, 0)

        def exprsign(self):
            return self.getTypedRuleContext(CSlangParser.ExprsignContext,0)


        def exprindex(self):
            return self.getTypedRuleContext(CSlangParser.ExprindexContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exprsign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprsign" ):
                return visitor.visitExprsign(self)
            else:
                return visitor.visitChildren(self)




    def exprsign(self):

        localctx = CSlangParser.ExprsignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_exprsign)
        try:
            self.state = 271
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.match(CSlangParser.SUB)
                self.state = 269
                self.exprsign()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRLIT, CSlangParser.ID, CSlangParser.ATID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprindex" ):
                return visitor.visitExprindex(self)
            else:
                return visitor.visitChildren(self)




    def exprindex(self):

        localctx = CSlangParser.ExprindexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_exprindex)
        try:
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.exprinst(0)
                self.state = 274
                self.match(CSlangParser.LBK)
                self.state = 275
                self.exprstr()
                self.state = 276
                self.match(CSlangParser.RBK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
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

        def parenexpr(self):
            return self.getTypedRuleContext(CSlangParser.ParenexprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exprinst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprinst" ):
                return visitor.visitExprinst(self)
            else:
                return visitor.visitChildren(self)



    def exprinst(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.ExprinstContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_exprinst, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.exprstat()
            self._ctx.stop = self._input.LT(-1)
            self.state = 292
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprinstContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprinst)
                    self.state = 284
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 285
                    self.match(CSlangParser.DOT)
                    self.state = 286
                    self.match(CSlangParser.ID)
                    self.state = 288
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        self.state = 287
                        self.parenexpr()

             
                self.state = 294
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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

        def ATID(self):
            return self.getToken(CSlangParser.ATID, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def parenexpr(self):
            return self.getTypedRuleContext(CSlangParser.ParenexprContext,0)


        def exprobj(self):
            return self.getTypedRuleContext(CSlangParser.ExprobjContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exprstat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprstat" ):
                return visitor.visitExprstat(self)
            else:
                return visitor.visitChildren(self)




    def exprstat(self):

        localctx = CSlangParser.ExprstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_exprstat)
        self._la = 0 # Token type
        try:
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ID:
                    self.state = 295
                    self.match(CSlangParser.ID)
                    self.state = 296
                    self.match(CSlangParser.DOT)


                self.state = 299
                self.match(CSlangParser.ATID)
                self.state = 301
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 300
                    self.parenexpr()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
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

        def parenexpr(self):
            return self.getTypedRuleContext(CSlangParser.ParenexprContext,0)


        def exprparen(self):
            return self.getTypedRuleContext(CSlangParser.ExprparenContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exprobj

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprobj" ):
                return visitor.visitExprobj(self)
            else:
                return visitor.visitChildren(self)




    def exprobj(self):

        localctx = CSlangParser.ExprobjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_exprobj)
        try:
            self.state = 310
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.match(CSlangParser.NEW)
                self.state = 307
                self.match(CSlangParser.ID)
                self.state = 308
                self.parenexpr()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRLIT, CSlangParser.ID, CSlangParser.ATID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
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

        def lit(self):
            return self.getTypedRuleContext(CSlangParser.LitContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exprparen

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprparen" ):
                return visitor.visitExprparen(self)
            else:
                return visitor.visitChildren(self)




    def exprparen(self):

        localctx = CSlangParser.ExprparenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_exprparen)
        try:
            self.state = 317
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LPN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.match(CSlangParser.LPN)
                self.state = 313
                self.exprstr()
                self.state = 314
                self.match(CSlangParser.RPN)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.LBK, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRLIT, CSlangParser.ID, CSlangParser.ATID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                self.lit()
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


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def ATID(self):
            return self.getToken(CSlangParser.ATID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = CSlangParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            _la = self._input.LA(1)
            if not(_la==CSlangParser.ID or _la==CSlangParser.ATID):
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


    class LitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(CSlangParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(CSlangParser.FLOATLIT, 0)

        def boollit(self):
            return self.getTypedRuleContext(CSlangParser.BoollitContext,0)


        def STRLIT(self):
            return self.getToken(CSlangParser.STRLIT, 0)

        def arraylit(self):
            return self.getTypedRuleContext(CSlangParser.ArraylitContext,0)


        def NULL(self):
            return self.getToken(CSlangParser.NULL, 0)

        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSlangParser.IdentifierContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit" ):
                return visitor.visitLit(self)
            else:
                return visitor.visitChildren(self)




    def lit(self):

        localctx = CSlangParser.LitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_lit)
        try:
            self.state = 329
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.match(CSlangParser.INTLIT)
                pass
            elif token in [CSlangParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
                self.match(CSlangParser.FLOATLIT)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 323
                self.boollit()
                pass
            elif token in [CSlangParser.STRLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 324
                self.match(CSlangParser.STRLIT)
                pass
            elif token in [CSlangParser.LBK]:
                self.enterOuterAlt(localctx, 5)
                self.state = 325
                self.arraylit()
                pass
            elif token in [CSlangParser.NULL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 326
                self.match(CSlangParser.NULL)
                pass
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 7)
                self.state = 327
                self.match(CSlangParser.SELF)
                pass
            elif token in [CSlangParser.ID, CSlangParser.ATID]:
                self.enterOuterAlt(localctx, 8)
                self.state = 328
                self.identifier()
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


    class BoollitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(CSlangParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(CSlangParser.FALSE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_boollit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoollit" ):
                return visitor.visitBoollit(self)
            else:
                return visitor.visitChildren(self)




    def boollit(self):

        localctx = CSlangParser.BoollitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_boollit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            _la = self._input.LA(1)
            if not(_la==CSlangParser.TRUE or _la==CSlangParser.FALSE):
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


    class ArraylitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBK(self):
            return self.getToken(CSlangParser.LBK, 0)

        def litprime(self):
            return self.getTypedRuleContext(CSlangParser.LitprimeContext,0)


        def RBK(self):
            return self.getToken(CSlangParser.RBK, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_arraylit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylit" ):
                return visitor.visitArraylit(self)
            else:
                return visitor.visitChildren(self)




    def arraylit(self):

        localctx = CSlangParser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(CSlangParser.LBK)
            self.state = 334
            self.litprime()
            self.state = 335
            self.match(CSlangParser.RBK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LitlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def litprime(self):
            return self.getTypedRuleContext(CSlangParser.LitprimeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_litlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLitlist" ):
                return visitor.visitLitlist(self)
            else:
                return visitor.visitChildren(self)




    def litlist(self):

        localctx = CSlangParser.LitlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_litlist)
        try:
            self.state = 339
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.LBK, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRLIT, CSlangParser.ID, CSlangParser.ATID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.litprime()
                pass
            elif token in [CSlangParser.RBK]:
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


    class LitprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lit(self):
            return self.getTypedRuleContext(CSlangParser.LitContext,0)


        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def litlist(self):
            return self.getTypedRuleContext(CSlangParser.LitlistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_litprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLitprime" ):
                return visitor.visitLitprime(self)
            else:
                return visitor.visitChildren(self)




    def litprime(self):

        localctx = CSlangParser.LitprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_litprime)
        try:
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.lit()
                self.state = 342
                self.match(CSlangParser.CM)
                self.state = 343
                self.litlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
                self.lit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(CSlangParser.StmtContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(CSlangParser.StmtlistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = CSlangParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_stmtlist)
        try:
            self.state = 352
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.BREAK, CSlangParser.CONTINUE, CSlangParser.IF, CSlangParser.FOR, CSlangParser.RETURN, CSlangParser.VAR, CSlangParser.SELF, CSlangParser.CONST, CSlangParser.LPN, CSlangParser.ID, CSlangParser.ATID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.stmt()
                self.state = 349
                self.stmtlist()
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


        def blockstmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.BlockstmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.BlockstmtContext,i)


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

        def stmtinvoc(self):
            return self.getTypedRuleContext(CSlangParser.StmtinvocContext,0)


        def attribute(self):
            return self.getTypedRuleContext(CSlangParser.AttributeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = CSlangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 393
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.VAR or _la==CSlangParser.CONST:
                    self.state = 354
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 357
                self.stmtassign()
                self.state = 358
                self.match(CSlangParser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 360
                self.match(CSlangParser.IF)
                self.state = 362
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.LBR:
                    self.state = 361
                    self.blockstmt()


                self.state = 364
                self.exprstr()
                self.state = 365
                self.blockstmt()
                self.state = 368
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ELSE:
                    self.state = 366
                    self.match(CSlangParser.ELSE)
                    self.state = 367
                    self.blockstmt()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 370
                self.match(CSlangParser.FOR)
                self.state = 371
                self.stmtassign()
                self.state = 372
                self.match(CSlangParser.SM)
                self.state = 373
                self.exprrel()
                self.state = 374
                self.match(CSlangParser.SM)
                self.state = 375
                self.stmtassign()
                self.state = 376
                self.blockstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 378
                self.match(CSlangParser.BREAK)
                self.state = 379
                self.match(CSlangParser.SM)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 380
                self.match(CSlangParser.CONTINUE)
                self.state = 381
                self.match(CSlangParser.SM)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 382
                self.match(CSlangParser.RETURN)
                self.state = 384
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NEG) | (1 << CSlangParser.NEW) | (1 << CSlangParser.LPN) | (1 << CSlangParser.LBK) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.STRLIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.ATID))) != 0):
                    self.state = 383
                    self.exprstr()


                self.state = 386
                self.match(CSlangParser.SM)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 387
                self.stmtinvoc(0)
                self.state = 388
                self.match(CSlangParser.SM)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 390
                self.attribute()
                self.state = 391
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

        def lhs(self):
            return self.getTypedRuleContext(CSlangParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(CSlangParser.ASSIGN, 0)

        def exprstr(self):
            return self.getTypedRuleContext(CSlangParser.ExprstrContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmtassign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtassign" ):
                return visitor.visitStmtassign(self)
            else:
                return visitor.visitChildren(self)




    def stmtassign(self):

        localctx = CSlangParser.StmtassignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_stmtassign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.lhs(0)
            self.state = 396
            self.match(CSlangParser.ASSIGN)
            self.state = 397
            self.exprstr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhsinst(self):
            return self.getTypedRuleContext(CSlangParser.LhsinstContext,0)


        def lhs(self):
            return self.getTypedRuleContext(CSlangParser.LhsContext,0)


        def LBK(self):
            return self.getToken(CSlangParser.LBK, 0)

        def exprstr(self):
            return self.getTypedRuleContext(CSlangParser.ExprstrContext,0)


        def RBK(self):
            return self.getToken(CSlangParser.RBK, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)



    def lhs(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.LhsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.lhsinst(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 409
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.LhsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                    self.state = 402
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 403
                    self.match(CSlangParser.LBK)
                    self.state = 404
                    self.exprstr()
                    self.state = 405
                    self.match(CSlangParser.RBK) 
                self.state = 411
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LhsinstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhsstat(self):
            return self.getTypedRuleContext(CSlangParser.LhsstatContext,0)


        def lhsinst(self):
            return self.getTypedRuleContext(CSlangParser.LhsinstContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def parenexpr(self):
            return self.getTypedRuleContext(CSlangParser.ParenexprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_lhsinst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhsinst" ):
                return visitor.visitLhsinst(self)
            else:
                return visitor.visitChildren(self)



    def lhsinst(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.LhsinstContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_lhsinst, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.lhsstat()
            self._ctx.stop = self._input.LT(-1)
            self.state = 423
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.LhsinstContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lhsinst)
                    self.state = 415
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 416
                    self.match(CSlangParser.DOT)
                    self.state = 417
                    self.match(CSlangParser.ID)
                    self.state = 419
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
                    if la_ == 1:
                        self.state = 418
                        self.parenexpr()

             
                self.state = 425
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LhsstatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATID(self):
            return self.getToken(CSlangParser.ATID, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def parenexpr(self):
            return self.getTypedRuleContext(CSlangParser.ParenexprContext,0)


        def lhsparen(self):
            return self.getTypedRuleContext(CSlangParser.LhsparenContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_lhsstat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhsstat" ):
                return visitor.visitLhsstat(self)
            else:
                return visitor.visitChildren(self)




    def lhsstat(self):

        localctx = CSlangParser.LhsstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_lhsstat)
        self._la = 0 # Token type
        try:
            self.state = 435
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ID:
                    self.state = 426
                    self.match(CSlangParser.ID)
                    self.state = 427
                    self.match(CSlangParser.DOT)


                self.state = 430
                self.match(CSlangParser.ATID)
                self.state = 432
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                if la_ == 1:
                    self.state = 431
                    self.parenexpr()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 434
                self.lhsparen()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsparenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPN(self):
            return self.getToken(CSlangParser.LPN, 0)

        def lhs(self):
            return self.getTypedRuleContext(CSlangParser.LhsContext,0)


        def RPN(self):
            return self.getToken(CSlangParser.RPN, 0)

        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSlangParser.IdentifierContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_lhsparen

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhsparen" ):
                return visitor.visitLhsparen(self)
            else:
                return visitor.visitChildren(self)




    def lhsparen(self):

        localctx = CSlangParser.LhsparenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_lhsparen)
        try:
            self.state = 443
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LPN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 437
                self.match(CSlangParser.LPN)
                self.state = 438
                self.lhs(0)
                self.state = 439
                self.match(CSlangParser.RPN)
                pass
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 441
                self.match(CSlangParser.SELF)
                pass
            elif token in [CSlangParser.ID, CSlangParser.ATID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 442
                self.identifier()
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


    class StmtinvocContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmtinvocstat(self):
            return self.getTypedRuleContext(CSlangParser.StmtinvocstatContext,0)


        def stmtinvoc(self):
            return self.getTypedRuleContext(CSlangParser.StmtinvocContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def parenexpr(self):
            return self.getTypedRuleContext(CSlangParser.ParenexprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmtinvoc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtinvoc" ):
                return visitor.visitStmtinvoc(self)
            else:
                return visitor.visitChildren(self)



    def stmtinvoc(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.StmtinvocContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_stmtinvoc, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.stmtinvocstat()
            self._ctx.stop = self._input.LT(-1)
            self.state = 456
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.StmtinvocContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_stmtinvoc)
                    self.state = 448
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 449
                    self.match(CSlangParser.DOT)
                    self.state = 450
                    self.match(CSlangParser.ID)
                    self.state = 452
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                    if la_ == 1:
                        self.state = 451
                        self.parenexpr()

             
                self.state = 458
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StmtinvocstatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATID(self):
            return self.getToken(CSlangParser.ATID, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def parenexpr(self):
            return self.getTypedRuleContext(CSlangParser.ParenexprContext,0)


        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSlangParser.IdentifierContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmtinvocstat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtinvocstat" ):
                return visitor.visitStmtinvocstat(self)
            else:
                return visitor.visitChildren(self)




    def stmtinvocstat(self):

        localctx = CSlangParser.StmtinvocstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_stmtinvocstat)
        self._la = 0 # Token type
        try:
            self.state = 469
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 461
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ID:
                    self.state = 459
                    self.match(CSlangParser.ID)
                    self.state = 460
                    self.match(CSlangParser.DOT)


                self.state = 463
                self.match(CSlangParser.ATID)
                self.state = 465
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
                if la_ == 1:
                    self.state = 464
                    self.parenexpr()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 467
                self.match(CSlangParser.SELF)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 468
                self.identifier()
                pass


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
        self._predicates[19] = self.exprlog_sempred
        self._predicates[20] = self.expradd_sempred
        self._predicates[21] = self.exprmul_sempred
        self._predicates[25] = self.exprinst_sempred
        self._predicates[38] = self.lhs_sempred
        self._predicates[39] = self.lhsinst_sempred
        self._predicates[42] = self.stmtinvoc_sempred
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
         

    def lhs_sempred(self, localctx:LhsContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def lhsinst_sempred(self, localctx:LhsinstContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def stmtinvoc_sempred(self, localctx:StmtinvocContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




