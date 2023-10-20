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
        buf.write("\u01fc\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3f\n\3\3\4\3\4\3\4")
        buf.write("\3\4\5\4l\n\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5")
        buf.write("w\n\5\3\6\3\6\3\6\3\6\5\6}\n\6\3\7\3\7\3\7\5\7\u0082\n")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b")
        buf.write("\u0090\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u009a\n")
        buf.write("\t\3\n\3\n\5\n\u009e\n\n\3\n\3\n\5\n\u00a2\n\n\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\5\16\u00b4\n\16\3\16\3\16\3\16\3\16\5\16\u00ba")
        buf.write("\n\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00c3\n")
        buf.write("\16\3\16\3\16\5\16\u00c7\n\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\5\17\u00d1\n\17\3\20\3\20\3\20\3\20\5")
        buf.write("\20\u00d7\n\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\5\23\u00e3\n\23\3\24\3\24\3\24\3\24\3\24\5")
        buf.write("\24\u00ea\n\24\3\25\3\25\3\25\3\25\3\25\5\25\u00f1\n\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\5\26\u00f8\n\26\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\27\7\27\u0100\n\27\f\27\16\27\u0103\13")
        buf.write("\27\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u010b\n\30\f\30")
        buf.write("\16\30\u010e\13\30\3\31\3\31\3\31\3\31\3\31\3\31\7\31")
        buf.write("\u0116\n\31\f\31\16\31\u0119\13\31\3\32\3\32\3\32\5\32")
        buf.write("\u011e\n\32\3\33\3\33\3\33\5\33\u0123\n\33\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\5\34\u012b\n\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\5\35\u0133\n\35\3\35\5\35\u0136\n\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\5\35\u013d\n\35\7\35\u013f\n\35\f\35")
        buf.write("\16\35\u0142\13\35\3\36\3\36\3\36\5\36\u0147\n\36\3\36")
        buf.write("\3\36\3\36\5\36\u014c\n\36\3\36\5\36\u014f\n\36\3\37\3")
        buf.write("\37\3\37\3\37\5\37\u0155\n\37\3 \3 \3 \3 \3 \3 \5 \u015d")
        buf.write("\n \3!\3!\3\"\3\"\3\"\3\"\3\"\5\"\u0166\n\"\3#\3#\3#\3")
        buf.write("#\3#\5#\u016d\n#\3#\3#\3$\3$\3$\3$\5$\u0175\n$\3%\3%\3")
        buf.write("%\3%\5%\u017b\n%\3&\3&\3&\3&\3&\5&\u0182\n&\3\'\3\'\3")
        buf.write("\'\3\'\5\'\u0188\n\'\3(\3(\3)\3)\3)\3)\5)\u0190\n)\3*")
        buf.write("\3*\3*\5*\u0195\n*\3*\3*\3*\3*\3*\3*\5*\u019d\n*\3*\3")
        buf.write("*\3*\3*\3*\5*\u01a4\n*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\5*\u01b5\n*\3*\3*\3*\3*\3*\3*\3*\5*\u01be")
        buf.write("\n*\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\7,\u01cc\n,\f")
        buf.write(",\16,\u01cf\13,\3-\3-\3-\3-\3-\3-\5-\u01d7\n-\3-\5-\u01da")
        buf.write("\n-\3-\3-\3-\3-\3-\5-\u01e1\n-\7-\u01e3\n-\f-\16-\u01e6")
        buf.write("\13-\3.\3.\3.\5.\u01eb\n.\3.\3.\3.\5.\u01f0\n.\3.\5.\u01f3")
        buf.write("\n.\3/\3/\3/\3/\3/\5/\u01fa\n/\3/\2\b,.\608VX\60\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJLNPRTVXZ\\\2\13\4\2\22\22\25\25\3\2\n\r\3\2")
        buf.write(" %\3\2\36\37\3\2\27\30\3\2\31\34\4\2\23\23::\3\2:;\3\2")
        buf.write("\b\t\2\u0211\2^\3\2\2\2\4e\3\2\2\2\6g\3\2\2\2\bv\3\2\2")
        buf.write("\2\n|\3\2\2\2\f~\3\2\2\2\16\u008f\3\2\2\2\20\u0099\3\2")
        buf.write("\2\2\22\u00a1\3\2\2\2\24\u00a3\3\2\2\2\26\u00a5\3\2\2")
        buf.write("\2\30\u00a9\3\2\2\2\32\u00c6\3\2\2\2\34\u00d0\3\2\2\2")
        buf.write("\36\u00d6\3\2\2\2 \u00d8\3\2\2\2\"\u00dc\3\2\2\2$\u00e2")
        buf.write("\3\2\2\2&\u00e9\3\2\2\2(\u00f0\3\2\2\2*\u00f7\3\2\2\2")
        buf.write(",\u00f9\3\2\2\2.\u0104\3\2\2\2\60\u010f\3\2\2\2\62\u011d")
        buf.write("\3\2\2\2\64\u0122\3\2\2\2\66\u012a\3\2\2\28\u0135\3\2")
        buf.write("\2\2:\u014e\3\2\2\2<\u0154\3\2\2\2>\u015c\3\2\2\2@\u015e")
        buf.write("\3\2\2\2B\u0165\3\2\2\2D\u0167\3\2\2\2F\u0174\3\2\2\2")
        buf.write("H\u017a\3\2\2\2J\u0181\3\2\2\2L\u0187\3\2\2\2N\u0189\3")
        buf.write("\2\2\2P\u018f\3\2\2\2R\u01bd\3\2\2\2T\u01bf\3\2\2\2V\u01c3")
        buf.write("\3\2\2\2X\u01d9\3\2\2\2Z\u01f2\3\2\2\2\\\u01f9\3\2\2\2")
        buf.write("^_\5\4\3\2_`\7\2\2\3`\3\3\2\2\2ab\5\6\4\2bc\5\4\3\2cf")
        buf.write("\3\2\2\2df\5\6\4\2ea\3\2\2\2ed\3\2\2\2f\5\3\2\2\2gk\7")
        buf.write("\20\2\2hi\7:\2\2il\7)\2\2jl\3\2\2\2kh\3\2\2\2kj\3\2\2")
        buf.write("\2lm\3\2\2\2mn\7:\2\2no\7/\2\2op\5\b\5\2pq\7\60\2\2q\7")
        buf.write("\3\2\2\2rs\5\n\6\2st\5\b\5\2tw\3\2\2\2uw\3\2\2\2vr\3\2")
        buf.write("\2\2vu\3\2\2\2w\t\3\2\2\2xy\5\f\7\2yz\7\63\2\2z}\3\2\2")
        buf.write("\2{}\5\32\16\2|x\3\2\2\2|{\3\2\2\2}\13\3\2\2\2~\u0081")
        buf.write("\t\2\2\2\177\u0082\5\16\b\2\u0080\u0082\5\20\t\2\u0081")
        buf.write("\177\3\2\2\2\u0081\u0080\3\2\2\2\u0082\r\3\2\2\2\u0083")
        buf.write("\u0084\5@!\2\u0084\u0085\7\62\2\2\u0085\u0086\5\16\b\2")
        buf.write("\u0086\u0087\7\62\2\2\u0087\u0088\5(\25\2\u0088\u0090")
        buf.write("\3\2\2\2\u0089\u008a\5@!\2\u008a\u008b\7\64\2\2\u008b")
        buf.write("\u008c\5\22\n\2\u008c\u008d\7&\2\2\u008d\u008e\5(\25\2")
        buf.write("\u008e\u0090\3\2\2\2\u008f\u0083\3\2\2\2\u008f\u0089\3")
        buf.write("\2\2\2\u0090\17\3\2\2\2\u0091\u0092\5@!\2\u0092\u0093")
        buf.write("\7\62\2\2\u0093\u0094\5\20\t\2\u0094\u009a\3\2\2\2\u0095")
        buf.write("\u0096\5@!\2\u0096\u0097\7\64\2\2\u0097\u0098\5\22\n\2")
        buf.write("\u0098\u009a\3\2\2\2\u0099\u0091\3\2\2\2\u0099\u0095\3")
        buf.write("\2\2\2\u009a\21\3\2\2\2\u009b\u009e\5\26\f\2\u009c\u009e")
        buf.write("\3\2\2\2\u009d\u009b\3\2\2\2\u009d\u009c\3\2\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009f\u00a2\5\24\13\2\u00a0\u00a2\5\30")
        buf.write("\r\2\u00a1\u009d\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2\23")
        buf.write("\3\2\2\2\u00a3\u00a4\t\3\2\2\u00a4\25\3\2\2\2\u00a5\u00a6")
        buf.write("\7-\2\2\u00a6\u00a7\7\65\2\2\u00a7\u00a8\7.\2\2\u00a8")
        buf.write("\27\3\2\2\2\u00a9\u00aa\7*\2\2\u00aa\u00ab\7:\2\2\u00ab")
        buf.write("\u00ac\7+\2\2\u00ac\u00ad\7,\2\2\u00ad\31\3\2\2\2\u00ae")
        buf.write("\u00af\7\26\2\2\u00af\u00b0\5@!\2\u00b0\u00b3\7+\2\2\u00b1")
        buf.write("\u00b4\5\34\17\2\u00b2\u00b4\3\2\2\2\u00b3\u00b1\3\2\2")
        buf.write("\2\u00b3\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6")
        buf.write("\7,\2\2\u00b6\u00b9\7\64\2\2\u00b7\u00ba\5\24\13\2\u00b8")
        buf.write("\u00ba\7\24\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00b8\3\2\2")
        buf.write("\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc\5 \21\2\u00bc\u00c7")
        buf.write("\3\2\2\2\u00bd\u00be\7\26\2\2\u00be\u00bf\7\21\2\2\u00bf")
        buf.write("\u00c2\7+\2\2\u00c0\u00c3\5\34\17\2\u00c1\u00c3\3\2\2")
        buf.write("\2\u00c2\u00c0\3\2\2\2\u00c2\u00c1\3\2\2\2\u00c3\u00c4")
        buf.write("\3\2\2\2\u00c4\u00c5\7,\2\2\u00c5\u00c7\5 \21\2\u00c6")
        buf.write("\u00ae\3\2\2\2\u00c6\u00bd\3\2\2\2\u00c7\33\3\2\2\2\u00c8")
        buf.write("\u00c9\5\36\20\2\u00c9\u00ca\7\62\2\2\u00ca\u00cb\5\34")
        buf.write("\17\2\u00cb\u00d1\3\2\2\2\u00cc\u00cd\5\36\20\2\u00cd")
        buf.write("\u00ce\7\64\2\2\u00ce\u00cf\5\24\13\2\u00cf\u00d1\3\2")
        buf.write("\2\2\u00d0\u00c8\3\2\2\2\u00d0\u00cc\3\2\2\2\u00d1\35")
        buf.write("\3\2\2\2\u00d2\u00d3\7:\2\2\u00d3\u00d4\7\62\2\2\u00d4")
        buf.write("\u00d7\5\36\20\2\u00d5\u00d7\7:\2\2\u00d6\u00d2\3\2\2")
        buf.write("\2\u00d6\u00d5\3\2\2\2\u00d7\37\3\2\2\2\u00d8\u00d9\7")
        buf.write("/\2\2\u00d9\u00da\5P)\2\u00da\u00db\7\60\2\2\u00db!\3")
        buf.write("\2\2\2\u00dc\u00dd\7+\2\2\u00dd\u00de\5$\23\2\u00de\u00df")
        buf.write("\7,\2\2\u00df#\3\2\2\2\u00e0\u00e3\5&\24\2\u00e1\u00e3")
        buf.write("\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e1\3\2\2\2\u00e3")
        buf.write("%\3\2\2\2\u00e4\u00e5\5(\25\2\u00e5\u00e6\7\62\2\2\u00e6")
        buf.write("\u00e7\5$\23\2\u00e7\u00ea\3\2\2\2\u00e8\u00ea\5(\25\2")
        buf.write("\u00e9\u00e4\3\2\2\2\u00e9\u00e8\3\2\2\2\u00ea\'\3\2\2")
        buf.write("\2\u00eb\u00ec\5*\26\2\u00ec\u00ed\7(\2\2\u00ed\u00ee")
        buf.write("\5*\26\2\u00ee\u00f1\3\2\2\2\u00ef\u00f1\5*\26\2\u00f0")
        buf.write("\u00eb\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1)\3\2\2\2\u00f2")
        buf.write("\u00f3\5,\27\2\u00f3\u00f4\t\4\2\2\u00f4\u00f5\5,\27\2")
        buf.write("\u00f5\u00f8\3\2\2\2\u00f6\u00f8\5,\27\2\u00f7\u00f2\3")
        buf.write("\2\2\2\u00f7\u00f6\3\2\2\2\u00f8+\3\2\2\2\u00f9\u00fa")
        buf.write("\b\27\1\2\u00fa\u00fb\5.\30\2\u00fb\u0101\3\2\2\2\u00fc")
        buf.write("\u00fd\f\4\2\2\u00fd\u00fe\t\5\2\2\u00fe\u0100\5.\30\2")
        buf.write("\u00ff\u00fc\3\2\2\2\u0100\u0103\3\2\2\2\u0101\u00ff\3")
        buf.write("\2\2\2\u0101\u0102\3\2\2\2\u0102-\3\2\2\2\u0103\u0101")
        buf.write("\3\2\2\2\u0104\u0105\b\30\1\2\u0105\u0106\5\60\31\2\u0106")
        buf.write("\u010c\3\2\2\2\u0107\u0108\f\4\2\2\u0108\u0109\t\6\2\2")
        buf.write("\u0109\u010b\5\60\31\2\u010a\u0107\3\2\2\2\u010b\u010e")
        buf.write("\3\2\2\2\u010c\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d")
        buf.write("/\3\2\2\2\u010e\u010c\3\2\2\2\u010f\u0110\b\31\1\2\u0110")
        buf.write("\u0111\5\62\32\2\u0111\u0117\3\2\2\2\u0112\u0113\f\4\2")
        buf.write("\2\u0113\u0114\t\7\2\2\u0114\u0116\5\62\32\2\u0115\u0112")
        buf.write("\3\2\2\2\u0116\u0119\3\2\2\2\u0117\u0115\3\2\2\2\u0117")
        buf.write("\u0118\3\2\2\2\u0118\61\3\2\2\2\u0119\u0117\3\2\2\2\u011a")
        buf.write("\u011b\7\35\2\2\u011b\u011e\5\62\32\2\u011c\u011e\5\64")
        buf.write("\33\2\u011d\u011a\3\2\2\2\u011d\u011c\3\2\2\2\u011e\63")
        buf.write("\3\2\2\2\u011f\u0120\7\30\2\2\u0120\u0123\5\64\33\2\u0121")
        buf.write("\u0123\5\66\34\2\u0122\u011f\3\2\2\2\u0122\u0121\3\2\2")
        buf.write("\2\u0123\65\3\2\2\2\u0124\u0125\58\35\2\u0125\u0126\7")
        buf.write("-\2\2\u0126\u0127\5(\25\2\u0127\u0128\7.\2\2\u0128\u012b")
        buf.write("\3\2\2\2\u0129\u012b\58\35\2\u012a\u0124\3\2\2\2\u012a")
        buf.write("\u0129\3\2\2\2\u012b\67\3\2\2\2\u012c\u012d\b\35\1\2\u012d")
        buf.write("\u012e\7\23\2\2\u012e\u012f\7\61\2\2\u012f\u0132\7:\2")
        buf.write("\2\u0130\u0133\5\"\22\2\u0131\u0133\3\2\2\2\u0132\u0130")
        buf.write("\3\2\2\2\u0132\u0131\3\2\2\2\u0133\u0136\3\2\2\2\u0134")
        buf.write("\u0136\5:\36\2\u0135\u012c\3\2\2\2\u0135\u0134\3\2\2\2")
        buf.write("\u0136\u0140\3\2\2\2\u0137\u0138\f\5\2\2\u0138\u0139\7")
        buf.write("\61\2\2\u0139\u013c\7:\2\2\u013a\u013d\5\"\22\2\u013b")
        buf.write("\u013d\3\2\2\2\u013c\u013a\3\2\2\2\u013c\u013b\3\2\2\2")
        buf.write("\u013d\u013f\3\2\2\2\u013e\u0137\3\2\2\2\u013f\u0142\3")
        buf.write("\2\2\2\u0140\u013e\3\2\2\2\u0140\u0141\3\2\2\2\u01419")
        buf.write("\3\2\2\2\u0142\u0140\3\2\2\2\u0143\u0144\t\b\2\2\u0144")
        buf.write("\u0147\7\61\2\2\u0145\u0147\3\2\2\2\u0146\u0143\3\2\2")
        buf.write("\2\u0146\u0145\3\2\2\2\u0147\u0148\3\2\2\2\u0148\u014b")
        buf.write("\7;\2\2\u0149\u014c\5\"\22\2\u014a\u014c\3\2\2\2\u014b")
        buf.write("\u0149\3\2\2\2\u014b\u014a\3\2\2\2\u014c\u014f\3\2\2\2")
        buf.write("\u014d\u014f\5<\37\2\u014e\u0146\3\2\2\2\u014e\u014d\3")
        buf.write("\2\2\2\u014f;\3\2\2\2\u0150\u0151\7*\2\2\u0151\u0152\7")
        buf.write(":\2\2\u0152\u0155\5\"\22\2\u0153\u0155\5> \2\u0154\u0150")
        buf.write("\3\2\2\2\u0154\u0153\3\2\2\2\u0155=\3\2\2\2\u0156\u0157")
        buf.write("\7+\2\2\u0157\u0158\5(\25\2\u0158\u0159\7,\2\2\u0159\u015d")
        buf.write("\3\2\2\2\u015a\u015d\5@!\2\u015b\u015d\5B\"\2\u015c\u0156")
        buf.write("\3\2\2\2\u015c\u015a\3\2\2\2\u015c\u015b\3\2\2\2\u015d")
        buf.write("?\3\2\2\2\u015e\u015f\t\t\2\2\u015fA\3\2\2\2\u0160\u0166")
        buf.write("\7\65\2\2\u0161\u0166\7\66\2\2\u0162\u0166\5N(\2\u0163")
        buf.write("\u0166\7\67\2\2\u0164\u0166\5D#\2\u0165\u0160\3\2\2\2")
        buf.write("\u0165\u0161\3\2\2\2\u0165\u0162\3\2\2\2\u0165\u0163\3")
        buf.write("\2\2\2\u0165\u0164\3\2\2\2\u0166C\3\2\2\2\u0167\u016c")
        buf.write("\7-\2\2\u0168\u016d\5F$\2\u0169\u016d\5H%\2\u016a\u016d")
        buf.write("\5J&\2\u016b\u016d\5L\'\2\u016c\u0168\3\2\2\2\u016c\u0169")
        buf.write("\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016b\3\2\2\2\u016d")
        buf.write("\u016e\3\2\2\2\u016e\u016f\7.\2\2\u016fE\3\2\2\2\u0170")
        buf.write("\u0171\7\65\2\2\u0171\u0172\7\62\2\2\u0172\u0175\5F$\2")
        buf.write("\u0173\u0175\7\65\2\2\u0174\u0170\3\2\2\2\u0174\u0173")
        buf.write("\3\2\2\2\u0175G\3\2\2\2\u0176\u0177\7\66\2\2\u0177\u0178")
        buf.write("\7\62\2\2\u0178\u017b\5H%\2\u0179\u017b\7\66\2\2\u017a")
        buf.write("\u0176\3\2\2\2\u017a\u0179\3\2\2\2\u017bI\3\2\2\2\u017c")
        buf.write("\u017d\5N(\2\u017d\u017e\7\62\2\2\u017e\u017f\5J&\2\u017f")
        buf.write("\u0182\3\2\2\2\u0180\u0182\5N(\2\u0181\u017c\3\2\2\2\u0181")
        buf.write("\u0180\3\2\2\2\u0182K\3\2\2\2\u0183\u0184\7\67\2\2\u0184")
        buf.write("\u0185\7\62\2\2\u0185\u0188\5L\'\2\u0186\u0188\7\67\2")
        buf.write("\2\u0187\u0183\3\2\2\2\u0187\u0186\3\2\2\2\u0188M\3\2")
        buf.write("\2\2\u0189\u018a\t\n\2\2\u018aO\3\2\2\2\u018b\u018c\5")
        buf.write("R*\2\u018c\u018d\5P)\2\u018d\u0190\3\2\2\2\u018e\u0190")
        buf.write("\3\2\2\2\u018f\u018b\3\2\2\2\u018f\u018e\3\2\2\2\u0190")
        buf.write("Q\3\2\2\2\u0191\u0195\7\22\2\2\u0192\u0195\7\25\2\2\u0193")
        buf.write("\u0195\3\2\2\2\u0194\u0191\3\2\2\2\u0194\u0192\3\2\2\2")
        buf.write("\u0194\u0193\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0197\5")
        buf.write("T+\2\u0197\u0198\7\63\2\2\u0198\u01be\3\2\2\2\u0199\u019c")
        buf.write("\7\5\2\2\u019a\u019d\5 \21\2\u019b\u019d\3\2\2\2\u019c")
        buf.write("\u019a\3\2\2\2\u019c\u019b\3\2\2\2\u019d\u019e\3\2\2\2")
        buf.write("\u019e\u019f\5(\25\2\u019f\u01a3\5 \21\2\u01a0\u01a1\7")
        buf.write("\6\2\2\u01a1\u01a4\5 \21\2\u01a2\u01a4\3\2\2\2\u01a3\u01a0")
        buf.write("\3\2\2\2\u01a3\u01a2\3\2\2\2\u01a4\u01be\3\2\2\2\u01a5")
        buf.write("\u01a6\7\7\2\2\u01a6\u01a7\5T+\2\u01a7\u01a8\7\63\2\2")
        buf.write("\u01a8\u01a9\5*\26\2\u01a9\u01aa\7\63\2\2\u01aa\u01ab")
        buf.write("\5T+\2\u01ab\u01ac\5 \21\2\u01ac\u01be\3\2\2\2\u01ad\u01ae")
        buf.write("\7\3\2\2\u01ae\u01be\7\63\2\2\u01af\u01b0\7\4\2\2\u01b0")
        buf.write("\u01be\7\63\2\2\u01b1\u01b4\7\16\2\2\u01b2\u01b5\5(\25")
        buf.write("\2\u01b3\u01b5\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4\u01b3")
        buf.write("\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01be\7\63\2\2\u01b7")
        buf.write("\u01b8\58\35\2\u01b8\u01b9\7\63\2\2\u01b9\u01be\3\2\2")
        buf.write("\2\u01ba\u01bb\5\f\7\2\u01bb\u01bc\7\63\2\2\u01bc\u01be")
        buf.write("\3\2\2\2\u01bd\u0194\3\2\2\2\u01bd\u0199\3\2\2\2\u01bd")
        buf.write("\u01a5\3\2\2\2\u01bd\u01ad\3\2\2\2\u01bd\u01af\3\2\2\2")
        buf.write("\u01bd\u01b1\3\2\2\2\u01bd\u01b7\3\2\2\2\u01bd\u01ba\3")
        buf.write("\2\2\2\u01beS\3\2\2\2\u01bf\u01c0\5V,\2\u01c0\u01c1\7")
        buf.write("\'\2\2\u01c1\u01c2\5(\25\2\u01c2U\3\2\2\2\u01c3\u01c4")
        buf.write("\b,\1\2\u01c4\u01c5\5X-\2\u01c5\u01cd\3\2\2\2\u01c6\u01c7")
        buf.write("\f\4\2\2\u01c7\u01c8\7-\2\2\u01c8\u01c9\5(\25\2\u01c9")
        buf.write("\u01ca\7.\2\2\u01ca\u01cc\3\2\2\2\u01cb\u01c6\3\2\2\2")
        buf.write("\u01cc\u01cf\3\2\2\2\u01cd\u01cb\3\2\2\2\u01cd\u01ce\3")
        buf.write("\2\2\2\u01ceW\3\2\2\2\u01cf\u01cd\3\2\2\2\u01d0\u01d1")
        buf.write("\b-\1\2\u01d1\u01d2\7\23\2\2\u01d2\u01d3\7\61\2\2\u01d3")
        buf.write("\u01d6\7:\2\2\u01d4\u01d7\5\"\22\2\u01d5\u01d7\3\2\2\2")
        buf.write("\u01d6\u01d4\3\2\2\2\u01d6\u01d5\3\2\2\2\u01d7\u01da\3")
        buf.write("\2\2\2\u01d8\u01da\5Z.\2\u01d9\u01d0\3\2\2\2\u01d9\u01d8")
        buf.write("\3\2\2\2\u01da\u01e4\3\2\2\2\u01db\u01dc\f\5\2\2\u01dc")
        buf.write("\u01dd\7\61\2\2\u01dd\u01e0\7:\2\2\u01de\u01e1\5\"\22")
        buf.write("\2\u01df\u01e1\3\2\2\2\u01e0\u01de\3\2\2\2\u01e0\u01df")
        buf.write("\3\2\2\2\u01e1\u01e3\3\2\2\2\u01e2\u01db\3\2\2\2\u01e3")
        buf.write("\u01e6\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2")
        buf.write("\u01e5Y\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e7\u01e8\t\b\2")
        buf.write("\2\u01e8\u01eb\7\61\2\2\u01e9\u01eb\3\2\2\2\u01ea\u01e7")
        buf.write("\3\2\2\2\u01ea\u01e9\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec")
        buf.write("\u01ef\7;\2\2\u01ed\u01f0\5\"\22\2\u01ee\u01f0\3\2\2\2")
        buf.write("\u01ef\u01ed\3\2\2\2\u01ef\u01ee\3\2\2\2\u01f0\u01f3\3")
        buf.write("\2\2\2\u01f1\u01f3\5\\/\2\u01f2\u01ea\3\2\2\2\u01f2\u01f1")
        buf.write("\3\2\2\2\u01f3[\3\2\2\2\u01f4\u01f5\7+\2\2\u01f5\u01f6")
        buf.write("\5V,\2\u01f6\u01f7\7,\2\2\u01f7\u01fa\3\2\2\2\u01f8\u01fa")
        buf.write("\5@!\2\u01f9\u01f4\3\2\2\2\u01f9\u01f8\3\2\2\2\u01fa]")
        buf.write("\3\2\2\29ekv|\u0081\u008f\u0099\u009d\u00a1\u00b3\u00b9")
        buf.write("\u00c2\u00c6\u00d0\u00d6\u00e2\u00e9\u00f0\u00f7\u0101")
        buf.write("\u010c\u0117\u011d\u0122\u012a\u0132\u0135\u013c\u0140")
        buf.write("\u0146\u014b\u014e\u0154\u015c\u0165\u016c\u0174\u017a")
        buf.write("\u0181\u0187\u018f\u0194\u019c\u01a3\u01b4\u01bd\u01cd")
        buf.write("\u01d6\u01d9\u01e0\u01e4\u01ea\u01ef\u01f2\u01f9")
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
                      "STR_LIT", "BLOCK_COMMENT", "LINE_COMMENT", "ID", 
                      "AT_ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
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
    RULE_blockstmt = 15
    RULE_parenexpr = 16
    RULE_expressions = 17
    RULE_exprprime = 18
    RULE_exprstr = 19
    RULE_exprrel = 20
    RULE_exprlog = 21
    RULE_expradd = 22
    RULE_exprmul = 23
    RULE_exprnot = 24
    RULE_exprsign = 25
    RULE_exprindex = 26
    RULE_exprinst = 27
    RULE_exprstat = 28
    RULE_exprobj = 29
    RULE_exprparen = 30
    RULE_identifiers = 31
    RULE_literals = 32
    RULE_arrayliteral = 33
    RULE_arrint = 34
    RULE_arrfloat = 35
    RULE_arrbool = 36
    RULE_arrstr = 37
    RULE_boolliteral = 38
    RULE_statements = 39
    RULE_stmt = 40
    RULE_stmtassign = 41
    RULE_lhs = 42
    RULE_lhsinst = 43
    RULE_lhsstat = 44
    RULE_lhsparen = 45

    ruleNames =  [ "program", "classdecllist", "classdecl", "memberlist", 
                   "member", "attribute", "attlistdecl", "attlistnodecl", 
                   "atttyp", "typ", "arraytyp", "classtyp", "method", "paramlist", 
                   "params", "blockstmt", "parenexpr", "expressions", "exprprime", 
                   "exprstr", "exprrel", "exprlog", "expradd", "exprmul", 
                   "exprnot", "exprsign", "exprindex", "exprinst", "exprstat", 
                   "exprobj", "exprparen", "identifiers", "literals", "arrayliteral", 
                   "arrint", "arrfloat", "arrbool", "arrstr", "boolliteral", 
                   "statements", "stmt", "stmtassign", "lhs", "lhsinst", 
                   "lhsstat", "lhsparen" ]

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
    STR_LIT=53
    BLOCK_COMMENT=54
    LINE_COMMENT=55
    ID=56
    AT_ID=57
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
            self.state = 92
            self.classdecllist()
            self.state = 93
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
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.classdecl()
                self.state = 96
                self.classdecllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
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
            self.state = 101
            self.match(CSlangParser.CLASS)
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 102
                self.match(CSlangParser.ID)
                self.state = 103
                self.match(CSlangParser.ARROW)
                pass

            elif la_ == 2:
                pass


            self.state = 107
            self.match(CSlangParser.ID)
            self.state = 108
            self.match(CSlangParser.LBR)
            self.state = 109
            self.memberlist()
            self.state = 110
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
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST, CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.member()
                self.state = 113
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
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.attribute()
                self.state = 119
                self.match(CSlangParser.SM)
                pass
            elif token in [CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
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
            self.state = 124
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 125
                self.attlistdecl()
                pass

            elif la_ == 2:
                self.state = 126
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttlistdecl" ):
                return visitor.visitAttlistdecl(self)
            else:
                return visitor.visitChildren(self)




    def attlistdecl(self):

        localctx = CSlangParser.AttlistdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attlistdecl)
        try:
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.identifiers()
                self.state = 130
                self.match(CSlangParser.CM)
                self.state = 131
                self.attlistdecl()
                self.state = 132
                self.match(CSlangParser.CM)
                self.state = 133
                self.exprstr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.identifiers()
                self.state = 136
                self.match(CSlangParser.COL)
                self.state = 137
                self.atttyp()
                self.state = 138
                self.match(CSlangParser.DECLARE)
                self.state = 139
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttlistnodecl" ):
                return visitor.visitAttlistnodecl(self)
            else:
                return visitor.visitChildren(self)




    def attlistnodecl(self):

        localctx = CSlangParser.AttlistnodeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attlistnodecl)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.identifiers()
                self.state = 144
                self.match(CSlangParser.CM)
                self.state = 145
                self.attlistnodecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.identifiers()
                self.state = 148
                self.match(CSlangParser.COL)
                self.state = 149
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtttyp" ):
                return visitor.visitAtttyp(self)
            else:
                return visitor.visitChildren(self)




    def atttyp(self):

        localctx = CSlangParser.AtttypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_atttyp)
        try:
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.LBK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.LBK]:
                    self.state = 153
                    self.arraytyp()
                    pass
                elif token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 157
                self.typ()
                pass
            elif token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
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
            self.state = 161
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraytyp" ):
                return visitor.visitArraytyp(self)
            else:
                return visitor.visitChildren(self)




    def arraytyp(self):

        localctx = CSlangParser.ArraytypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_arraytyp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(CSlangParser.LBK)
            self.state = 164
            self.match(CSlangParser.INT_LIT)
            self.state = 165
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClasstyp" ):
                return visitor.visitClasstyp(self)
            else:
                return visitor.visitChildren(self)




    def classtyp(self):

        localctx = CSlangParser.ClasstypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_classtyp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(CSlangParser.NEW)
            self.state = 168
            self.match(CSlangParser.ID)
            self.state = 169
            self.match(CSlangParser.LPN)
            self.state = 170
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

        def blockstmt(self):
            return self.getTypedRuleContext(CSlangParser.BlockstmtContext,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = CSlangParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_method)
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.match(CSlangParser.FUNC)
                self.state = 173
                self.identifiers()
                self.state = 174
                self.match(CSlangParser.LPN)
                self.state = 177
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.ID]:
                    self.state = 175
                    self.paramlist()
                    pass
                elif token in [CSlangParser.RPN]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 179
                self.match(CSlangParser.RPN)
                self.state = 180
                self.match(CSlangParser.COL)
                self.state = 183
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING]:
                    self.state = 181
                    self.typ()
                    pass
                elif token in [CSlangParser.VOID]:
                    self.state = 182
                    self.match(CSlangParser.VOID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 185
                self.blockstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.match(CSlangParser.FUNC)
                self.state = 188
                self.match(CSlangParser.CONSTRUCTOR)
                self.state = 189
                self.match(CSlangParser.LPN)
                self.state = 192
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.ID]:
                    self.state = 190
                    self.paramlist()
                    pass
                elif token in [CSlangParser.RPN]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 194
                self.match(CSlangParser.RPN)
                self.state = 195
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
        self.enterRule(localctx, 26, self.RULE_paramlist)
        try:
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.params()
                self.state = 199
                self.match(CSlangParser.CM)
                self.state = 200
                self.paramlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.params()
                self.state = 203
                self.match(CSlangParser.COL)
                self.state = 204
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
        self.enterRule(localctx, 28, self.RULE_params)
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.match(CSlangParser.ID)
                self.state = 209
                self.match(CSlangParser.CM)
                self.state = 210
                self.params()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
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

        def statements(self):
            return self.getTypedRuleContext(CSlangParser.StatementsContext,0)


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
        self.enterRule(localctx, 30, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(CSlangParser.LBR)
            self.state = 215
            self.statements()
            self.state = 216
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

        def expressions(self):
            return self.getTypedRuleContext(CSlangParser.ExpressionsContext,0)


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
        self.enterRule(localctx, 32, self.RULE_parenexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(CSlangParser.LPN)
            self.state = 219
            self.expressions()
            self.state = 220
            self.match(CSlangParser.RPN)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressions" ):
                return visitor.visitExpressions(self)
            else:
                return visitor.visitChildren(self)




    def expressions(self):

        localctx = CSlangParser.ExpressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expressions)
        try:
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.MINUS, CSlangParser.NEG, CSlangParser.NEW, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.INT_LIT, CSlangParser.FLOAT_LIT, CSlangParser.STR_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprprime" ):
                return visitor.visitExprprime(self)
            else:
                return visitor.visitChildren(self)




    def exprprime(self):

        localctx = CSlangParser.ExprprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_exprprime)
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.exprstr()
                self.state = 227
                self.match(CSlangParser.CM)
                self.state = 228
                self.expressions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
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
        self.enterRule(localctx, 38, self.RULE_exprstr)
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.exprrel()
                self.state = 234
                self.match(CSlangParser.CONCATE)
                self.state = 235
                self.exprrel()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
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
        self.enterRule(localctx, 40, self.RULE_exprrel)
        self._la = 0 # Token type
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.exprlog(0)
                self.state = 241
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.EQ) | (1 << CSlangParser.NEQ) | (1 << CSlangParser.LT) | (1 << CSlangParser.LTEQ) | (1 << CSlangParser.GT) | (1 << CSlangParser.GTEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 242
                self.exprlog(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
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
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_exprlog, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.expradd(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 255
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprlogContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprlog)
                    self.state = 250
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 251
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.AND or _la==CSlangParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 252
                    self.expradd(0) 
                self.state = 257
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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expradd, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.exprmul(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 266
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExpraddContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expradd)
                    self.state = 261
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 262
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.PLUS or _la==CSlangParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 263
                    self.exprmul(0) 
                self.state = 268
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
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_exprmul, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.exprnot()
            self._ctx.stop = self._input.LT(-1)
            self.state = 277
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprmulContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprmul)
                    self.state = 272
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 273
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.MUL) | (1 << CSlangParser.DIV_FLOAT) | (1 << CSlangParser.DIV_INT) | (1 << CSlangParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 274
                    self.exprnot() 
                self.state = 279
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprnot" ):
                return visitor.visitExprnot(self)
            else:
                return visitor.visitChildren(self)




    def exprnot(self):

        localctx = CSlangParser.ExprnotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_exprnot)
        try:
            self.state = 283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.match(CSlangParser.NEG)
                self.state = 281
                self.exprnot()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.MINUS, CSlangParser.NEW, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.INT_LIT, CSlangParser.FLOAT_LIT, CSlangParser.STR_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprsign" ):
                return visitor.visitExprsign(self)
            else:
                return visitor.visitChildren(self)




    def exprsign(self):

        localctx = CSlangParser.ExprsignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_exprsign)
        try:
            self.state = 288
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.match(CSlangParser.MINUS)
                self.state = 286
                self.exprsign()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.INT_LIT, CSlangParser.FLOAT_LIT, CSlangParser.STR_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
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
        self.enterRule(localctx, 52, self.RULE_exprindex)
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.exprinst(0)
                self.state = 291
                self.match(CSlangParser.LBK)
                self.state = 292
                self.exprstr()
                self.state = 293
                self.match(CSlangParser.RBK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
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

        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def parenexpr(self):
            return self.getTypedRuleContext(CSlangParser.ParenexprContext,0)


        def exprstat(self):
            return self.getTypedRuleContext(CSlangParser.ExprstatContext,0)


        def exprinst(self):
            return self.getTypedRuleContext(CSlangParser.ExprinstContext,0)


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
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_exprinst, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 299
                self.match(CSlangParser.SELF)
                self.state = 300
                self.match(CSlangParser.DOT)
                self.state = 301
                self.match(CSlangParser.ID)
                self.state = 304
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 302
                    self.parenexpr()
                    pass

                elif la_ == 2:
                    pass


                pass

            elif la_ == 2:
                self.state = 306
                self.exprstat()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 318
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprinstContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprinst)
                    self.state = 309
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 310
                    self.match(CSlangParser.DOT)
                    self.state = 311
                    self.match(CSlangParser.ID)
                    self.state = 314
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        self.state = 312
                        self.parenexpr()
                        pass

                    elif la_ == 2:
                        pass

             
                self.state = 320
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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

        def parenexpr(self):
            return self.getTypedRuleContext(CSlangParser.ParenexprContext,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

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
        self.enterRule(localctx, 56, self.RULE_exprstat)
        self._la = 0 # Token type
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.SELF, CSlangParser.ID]:
                    self.state = 321
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.SELF or _la==CSlangParser.ID):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 322
                    self.match(CSlangParser.DOT)
                    pass
                elif token in [CSlangParser.AT_ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 326
                self.match(CSlangParser.AT_ID)
                self.state = 329
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                if la_ == 1:
                    self.state = 327
                    self.parenexpr()
                    pass

                elif la_ == 2:
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
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
        self.enterRule(localctx, 58, self.RULE_exprobj)
        try:
            self.state = 338
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.match(CSlangParser.NEW)
                self.state = 335
                self.match(CSlangParser.ID)
                self.state = 336
                self.parenexpr()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.INT_LIT, CSlangParser.FLOAT_LIT, CSlangParser.STR_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
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

        def identifiers(self):
            return self.getTypedRuleContext(CSlangParser.IdentifiersContext,0)


        def literals(self):
            return self.getTypedRuleContext(CSlangParser.LiteralsContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exprparen

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprparen" ):
                return visitor.visitExprparen(self)
            else:
                return visitor.visitChildren(self)




    def exprparen(self):

        localctx = CSlangParser.ExprparenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_exprparen)
        try:
            self.state = 346
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LPN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.match(CSlangParser.LPN)
                self.state = 341
                self.exprstr()
                self.state = 342
                self.match(CSlangParser.RPN)
                pass
            elif token in [CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.identifiers()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.LBK, CSlangParser.INT_LIT, CSlangParser.FLOAT_LIT, CSlangParser.STR_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 345
                self.literals()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifiers" ):
                return visitor.visitIdentifiers(self)
            else:
                return visitor.visitChildren(self)




    def identifiers(self):

        localctx = CSlangParser.IdentifiersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_identifiers)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
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

        def boolliteral(self):
            return self.getTypedRuleContext(CSlangParser.BoolliteralContext,0)


        def STR_LIT(self):
            return self.getToken(CSlangParser.STR_LIT, 0)

        def arrayliteral(self):
            return self.getTypedRuleContext(CSlangParser.ArrayliteralContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = CSlangParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_literals)
        try:
            self.state = 355
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.match(CSlangParser.INT_LIT)
                pass
            elif token in [CSlangParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
                self.match(CSlangParser.FLOAT_LIT)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 352
                self.boolliteral()
                pass
            elif token in [CSlangParser.STR_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 353
                self.match(CSlangParser.STR_LIT)
                pass
            elif token in [CSlangParser.LBK]:
                self.enterOuterAlt(localctx, 5)
                self.state = 354
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayliteral" ):
                return visitor.visitArrayliteral(self)
            else:
                return visitor.visitChildren(self)




    def arrayliteral(self):

        localctx = CSlangParser.ArrayliteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_arrayliteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(CSlangParser.LBK)
            self.state = 362
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT_LIT]:
                self.state = 358
                self.arrint()
                pass
            elif token in [CSlangParser.FLOAT_LIT]:
                self.state = 359
                self.arrfloat()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE]:
                self.state = 360
                self.arrbool()
                pass
            elif token in [CSlangParser.STR_LIT]:
                self.state = 361
                self.arrstr()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 364
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrint" ):
                return visitor.visitArrint(self)
            else:
                return visitor.visitChildren(self)




    def arrint(self):

        localctx = CSlangParser.ArrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_arrint)
        try:
            self.state = 370
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.match(CSlangParser.INT_LIT)
                self.state = 367
                self.match(CSlangParser.CM)
                self.state = 368
                self.arrint()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrfloat" ):
                return visitor.visitArrfloat(self)
            else:
                return visitor.visitChildren(self)




    def arrfloat(self):

        localctx = CSlangParser.ArrfloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_arrfloat)
        try:
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.match(CSlangParser.FLOAT_LIT)
                self.state = 373
                self.match(CSlangParser.CM)
                self.state = 374
                self.arrfloat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
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

        def boolliteral(self):
            return self.getTypedRuleContext(CSlangParser.BoolliteralContext,0)


        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def arrbool(self):
            return self.getTypedRuleContext(CSlangParser.ArrboolContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_arrbool

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrbool" ):
                return visitor.visitArrbool(self)
            else:
                return visitor.visitChildren(self)




    def arrbool(self):

        localctx = CSlangParser.ArrboolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_arrbool)
        try:
            self.state = 383
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
                self.boolliteral()
                self.state = 379
                self.match(CSlangParser.CM)
                self.state = 380
                self.arrbool()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 382
                self.boolliteral()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrstr" ):
                return visitor.visitArrstr(self)
            else:
                return visitor.visitChildren(self)




    def arrstr(self):

        localctx = CSlangParser.ArrstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_arrstr)
        try:
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 385
                self.match(CSlangParser.STR_LIT)
                self.state = 386
                self.match(CSlangParser.CM)
                self.state = 387
                self.arrstr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self.match(CSlangParser.STR_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolliteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(CSlangParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(CSlangParser.FALSE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_boolliteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolliteral" ):
                return visitor.visitBoolliteral(self)
            else:
                return visitor.visitChildren(self)




    def boolliteral(self):

        localctx = CSlangParser.BoolliteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_boolliteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = CSlangParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_statements)
        try:
            self.state = 397
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.BREAK, CSlangParser.CONTINUE, CSlangParser.IF, CSlangParser.FOR, CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.RETURN, CSlangParser.VAR, CSlangParser.SELF, CSlangParser.CONST, CSlangParser.NEW, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.INT_LIT, CSlangParser.FLOAT_LIT, CSlangParser.STR_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.stmt()
                self.state = 394
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

        def exprinst(self):
            return self.getTypedRuleContext(CSlangParser.ExprinstContext,0)


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
        self.enterRule(localctx, 80, self.RULE_stmt)
        try:
            self.state = 443
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.VAR]:
                    self.state = 399
                    self.match(CSlangParser.VAR)
                    pass
                elif token in [CSlangParser.CONST]:
                    self.state = 400
                    self.match(CSlangParser.CONST)
                    pass
                elif token in [CSlangParser.SELF, CSlangParser.LPN, CSlangParser.ID, CSlangParser.AT_ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 404
                self.stmtassign()
                self.state = 405
                self.match(CSlangParser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
                self.match(CSlangParser.IF)
                self.state = 410
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.LBR]:
                    self.state = 408
                    self.blockstmt()
                    pass
                elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.MINUS, CSlangParser.NEG, CSlangParser.NEW, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.INT_LIT, CSlangParser.FLOAT_LIT, CSlangParser.STR_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 412
                self.exprstr()
                self.state = 413
                self.blockstmt()
                self.state = 417
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.ELSE]:
                    self.state = 414
                    self.match(CSlangParser.ELSE)
                    self.state = 415
                    self.blockstmt()
                    pass
                elif token in [CSlangParser.BREAK, CSlangParser.CONTINUE, CSlangParser.IF, CSlangParser.FOR, CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.RETURN, CSlangParser.VAR, CSlangParser.SELF, CSlangParser.CONST, CSlangParser.NEW, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.RBR, CSlangParser.INT_LIT, CSlangParser.FLOAT_LIT, CSlangParser.STR_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 419
                self.match(CSlangParser.FOR)
                self.state = 420
                self.stmtassign()
                self.state = 421
                self.match(CSlangParser.SM)
                self.state = 422
                self.exprrel()
                self.state = 423
                self.match(CSlangParser.SM)
                self.state = 424
                self.stmtassign()
                self.state = 425
                self.blockstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 427
                self.match(CSlangParser.BREAK)
                self.state = 428
                self.match(CSlangParser.SM)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 429
                self.match(CSlangParser.CONTINUE)
                self.state = 430
                self.match(CSlangParser.SM)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 431
                self.match(CSlangParser.RETURN)
                self.state = 434
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.MINUS, CSlangParser.NEG, CSlangParser.NEW, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.INT_LIT, CSlangParser.FLOAT_LIT, CSlangParser.STR_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                    self.state = 432
                    self.exprstr()
                    pass
                elif token in [CSlangParser.SM]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 436
                self.match(CSlangParser.SM)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 437
                self.exprinst(0)
                self.state = 438
                self.match(CSlangParser.SM)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 440
                self.attribute()
                self.state = 441
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
        self.enterRule(localctx, 82, self.RULE_stmtassign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.lhs(0)
            self.state = 446
            self.match(CSlangParser.ASSIGN)
            self.state = 447
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
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.lhsinst(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 459
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.LhsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                    self.state = 452
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 453
                    self.match(CSlangParser.LBK)
                    self.state = 454
                    self.exprstr()
                    self.state = 455
                    self.match(CSlangParser.RBK) 
                self.state = 461
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

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

        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def parenexpr(self):
            return self.getTypedRuleContext(CSlangParser.ParenexprContext,0)


        def lhsstat(self):
            return self.getTypedRuleContext(CSlangParser.LhsstatContext,0)


        def lhsinst(self):
            return self.getTypedRuleContext(CSlangParser.LhsinstContext,0)


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
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_lhsinst, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.state = 463
                self.match(CSlangParser.SELF)
                self.state = 464
                self.match(CSlangParser.DOT)
                self.state = 465
                self.match(CSlangParser.ID)
                self.state = 468
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                if la_ == 1:
                    self.state = 466
                    self.parenexpr()
                    pass

                elif la_ == 2:
                    pass


                pass

            elif la_ == 2:
                self.state = 470
                self.lhsstat()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 482
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.LhsinstContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lhsinst)
                    self.state = 473
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 474
                    self.match(CSlangParser.DOT)
                    self.state = 475
                    self.match(CSlangParser.ID)
                    self.state = 478
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                    if la_ == 1:
                        self.state = 476
                        self.parenexpr()
                        pass

                    elif la_ == 2:
                        pass

             
                self.state = 484
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

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

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def parenexpr(self):
            return self.getTypedRuleContext(CSlangParser.ParenexprContext,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

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
        self.enterRule(localctx, 88, self.RULE_lhsstat)
        self._la = 0 # Token type
        try:
            self.state = 496
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 488
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.SELF, CSlangParser.ID]:
                    self.state = 485
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.SELF or _la==CSlangParser.ID):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 486
                    self.match(CSlangParser.DOT)
                    pass
                elif token in [CSlangParser.AT_ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 490
                self.match(CSlangParser.AT_ID)
                self.state = 493
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
                if la_ == 1:
                    self.state = 491
                    self.parenexpr()
                    pass

                elif la_ == 2:
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 495
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

        def identifiers(self):
            return self.getTypedRuleContext(CSlangParser.IdentifiersContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_lhsparen

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhsparen" ):
                return visitor.visitLhsparen(self)
            else:
                return visitor.visitChildren(self)




    def lhsparen(self):

        localctx = CSlangParser.LhsparenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_lhsparen)
        try:
            self.state = 503
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LPN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 498
                self.match(CSlangParser.LPN)
                self.state = 499
                self.lhs(0)
                self.state = 500
                self.match(CSlangParser.RPN)
                pass
            elif token in [CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 502
                self.identifiers()
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[21] = self.exprlog_sempred
        self._predicates[22] = self.expradd_sempred
        self._predicates[23] = self.exprmul_sempred
        self._predicates[27] = self.exprinst_sempred
        self._predicates[42] = self.lhs_sempred
        self._predicates[43] = self.lhsinst_sempred
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
                return self.precpred(self._ctx, 3)
         

    def lhs_sempred(self, localctx:LhsContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def lhsinst_sempred(self, localctx:LhsinstContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         




