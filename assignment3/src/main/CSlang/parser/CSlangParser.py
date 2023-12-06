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
        buf.write("\u01ef\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\5\3l\n\3\3\4\3\4\3\4\5\4q\n\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\5\5\5|\n\5\3\6\3\6\3\6\3\6\5\6\u0082")
        buf.write("\n\6\3\7\3\7\5\7\u0086\n\7\3\b\3\b\3\b\5\b\u008b\n\b\3")
        buf.write("\t\3\t\3\t\5\t\u0090\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\5\n\u009e\n\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\5\13\u00a8\n\13\3\f\3\f\3\f\5\f\u00ad")
        buf.write("\n\f\3\f\3\f\5\f\u00b1\n\f\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\5\16\u00b9\n\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\5\16\u00c4\n\16\3\16\3\16\5\16\u00c8\n\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\5\17\u00cf\n\17\3\20\3\20\3\20\3")
        buf.write("\20\3\21\3\21\3\21\3\21\3\21\5\21\u00da\n\21\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\5\24\u00e6\n")
        buf.write("\24\3\25\3\25\3\25\3\25\3\25\5\25\u00ed\n\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\5\26\u00f4\n\26\3\27\3\27\3\27\3\27\3")
        buf.write("\27\5\27\u00fb\n\27\3\30\3\30\3\30\3\30\3\30\3\30\7\30")
        buf.write("\u0103\n\30\f\30\16\30\u0106\13\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\7\31\u010e\n\31\f\31\16\31\u0111\13\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\7\32\u0119\n\32\f\32\16\32\u011c")
        buf.write("\13\32\3\33\3\33\3\33\5\33\u0121\n\33\3\34\3\34\3\34\5")
        buf.write("\34\u0126\n\34\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u012e")
        buf.write("\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0138")
        buf.write("\n\36\3\36\3\36\3\36\5\36\u013d\n\36\7\36\u013f\n\36\f")
        buf.write("\36\16\36\u0142\13\36\3\37\3\37\5\37\u0146\n\37\3\37\3")
        buf.write("\37\5\37\u014a\n\37\3\37\5\37\u014d\n\37\3 \3 \3 \3 \5")
        buf.write(" \u0153\n \3!\3!\3!\3!\3!\5!\u015a\n!\3\"\3\"\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\5#\u0166\n#\3$\3$\3%\3%\3%\3%\3&\3&\5")
        buf.write("&\u0170\n&\3\'\3\'\3\'\3\'\3\'\5\'\u0177\n\'\3(\3(\3(")
        buf.write("\3(\5(\u017d\n(\3)\3)\5)\u0181\n)\3)\3)\3)\3)\5)\u0187")
        buf.write("\n)\3)\3)\3)\3)\3)\3)\3)\3)\3)\5)\u0192\n)\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\5)\u019d\n)\3)\3)\3)\3)\3)\3)\3)\5)\u01a6")
        buf.write("\n)\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\5+\u01b2\n+\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\5,\u01bc\n,\3,\3,\7,\u01c0\n,\f,\16,")
        buf.write("\u01c3\13,\3-\3-\5-\u01c7\n-\3-\3-\5-\u01cb\n-\3.\3.\3")
        buf.write(".\3.\3.\3.\5.\u01d3\n.\3/\3/\5/\u01d7\n/\3\60\3\60\3\60")
        buf.write("\3\60\3\60\5\60\u01de\n\60\3\60\3\60\3\60\3\60\3\61\3")
        buf.write("\61\5\61\u01e6\n\61\3\61\3\61\3\61\3\62\3\62\5\62\u01ed")
        buf.write("\n\62\3\62\2\7.\60\62:V\63\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\")
        buf.write("^`b\2\n\4\2\n\r::\3\2 %\3\2\36\37\3\2\27\30\3\2\31\34")
        buf.write("\3\2:;\3\2\b\t\4\2\22\22\25\25\2\u01ff\2d\3\2\2\2\4k\3")
        buf.write("\2\2\2\6m\3\2\2\2\b{\3\2\2\2\n\u0081\3\2\2\2\f\u0085\3")
        buf.write("\2\2\2\16\u0087\3\2\2\2\20\u008c\3\2\2\2\22\u009d\3\2")
        buf.write("\2\2\24\u00a7\3\2\2\2\26\u00b0\3\2\2\2\30\u00b2\3\2\2")
        buf.write("\2\32\u00c7\3\2\2\2\34\u00ce\3\2\2\2\36\u00d0\3\2\2\2")
        buf.write(" \u00d9\3\2\2\2\"\u00db\3\2\2\2$\u00df\3\2\2\2&\u00e5")
        buf.write("\3\2\2\2(\u00ec\3\2\2\2*\u00f3\3\2\2\2,\u00fa\3\2\2\2")
        buf.write(".\u00fc\3\2\2\2\60\u0107\3\2\2\2\62\u0112\3\2\2\2\64\u0120")
        buf.write("\3\2\2\2\66\u0125\3\2\2\28\u012d\3\2\2\2:\u012f\3\2\2")
        buf.write("\2<\u014c\3\2\2\2>\u0152\3\2\2\2@\u0159\3\2\2\2B\u015b")
        buf.write("\3\2\2\2D\u0165\3\2\2\2F\u0167\3\2\2\2H\u0169\3\2\2\2")
        buf.write("J\u016f\3\2\2\2L\u0176\3\2\2\2N\u017c\3\2\2\2P\u01a5\3")
        buf.write("\2\2\2R\u01a7\3\2\2\2T\u01b1\3\2\2\2V\u01b3\3\2\2\2X\u01ca")
        buf.write("\3\2\2\2Z\u01d2\3\2\2\2\\\u01d6\3\2\2\2^\u01d8\3\2\2\2")
        buf.write("`\u01e5\3\2\2\2b\u01ec\3\2\2\2de\5\4\3\2ef\7\2\2\3f\3")
        buf.write("\3\2\2\2gh\5\6\4\2hi\5\4\3\2il\3\2\2\2jl\5\6\4\2kg\3\2")
        buf.write("\2\2kj\3\2\2\2l\5\3\2\2\2mp\7\20\2\2no\7:\2\2oq\7)\2\2")
        buf.write("pn\3\2\2\2pq\3\2\2\2qr\3\2\2\2rs\7:\2\2st\7/\2\2tu\5\b")
        buf.write("\5\2uv\7\60\2\2v\7\3\2\2\2wx\5\n\6\2xy\5\b\5\2y|\3\2\2")
        buf.write("\2z|\3\2\2\2{w\3\2\2\2{z\3\2\2\2|\t\3\2\2\2}~\5\f\7\2")
        buf.write("~\177\7\63\2\2\177\u0082\3\2\2\2\u0080\u0082\5\32\16\2")
        buf.write("\u0081}\3\2\2\2\u0081\u0080\3\2\2\2\u0082\13\3\2\2\2\u0083")
        buf.write("\u0086\5\16\b\2\u0084\u0086\5\20\t\2\u0085\u0083\3\2\2")
        buf.write("\2\u0085\u0084\3\2\2\2\u0086\r\3\2\2\2\u0087\u008a\7\22")
        buf.write("\2\2\u0088\u008b\5\22\n\2\u0089\u008b\5\24\13\2\u008a")
        buf.write("\u0088\3\2\2\2\u008a\u0089\3\2\2\2\u008b\17\3\2\2\2\u008c")
        buf.write("\u008f\7\25\2\2\u008d\u0090\5\22\n\2\u008e\u0090\5\24")
        buf.write("\13\2\u008f\u008d\3\2\2\2\u008f\u008e\3\2\2\2\u0090\21")
        buf.write("\3\2\2\2\u0091\u0092\5B\"\2\u0092\u0093\7\62\2\2\u0093")
        buf.write("\u0094\5\22\n\2\u0094\u0095\7\62\2\2\u0095\u0096\5*\26")
        buf.write("\2\u0096\u009e\3\2\2\2\u0097\u0098\5B\"\2\u0098\u0099")
        buf.write("\7\64\2\2\u0099\u009a\5\26\f\2\u009a\u009b\7&\2\2\u009b")
        buf.write("\u009c\5*\26\2\u009c\u009e\3\2\2\2\u009d\u0091\3\2\2\2")
        buf.write("\u009d\u0097\3\2\2\2\u009e\23\3\2\2\2\u009f\u00a0\5B\"")
        buf.write("\2\u00a0\u00a1\7\62\2\2\u00a1\u00a2\5\24\13\2\u00a2\u00a8")
        buf.write("\3\2\2\2\u00a3\u00a4\5B\"\2\u00a4\u00a5\7\64\2\2\u00a5")
        buf.write("\u00a6\5\26\f\2\u00a6\u00a8\3\2\2\2\u00a7\u009f\3\2\2")
        buf.write("\2\u00a7\u00a3\3\2\2\2\u00a8\25\3\2\2\2\u00a9\u00aa\7")
        buf.write("-\2\2\u00aa\u00ab\7\65\2\2\u00ab\u00ad\7.\2\2\u00ac\u00a9")
        buf.write("\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae")
        buf.write("\u00b1\5\30\r\2\u00af\u00b1\7\24\2\2\u00b0\u00ac\3\2\2")
        buf.write("\2\u00b0\u00af\3\2\2\2\u00b1\27\3\2\2\2\u00b2\u00b3\t")
        buf.write("\2\2\2\u00b3\31\3\2\2\2\u00b4\u00b5\7\26\2\2\u00b5\u00b6")
        buf.write("\5B\"\2\u00b6\u00b8\7+\2\2\u00b7\u00b9\5\34\17\2\u00b8")
        buf.write("\u00b7\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\3\2\2\2")
        buf.write("\u00ba\u00bb\7,\2\2\u00bb\u00bc\7\64\2\2\u00bc\u00bd\5")
        buf.write("\26\f\2\u00bd\u00be\5\"\22\2\u00be\u00c8\3\2\2\2\u00bf")
        buf.write("\u00c0\7\26\2\2\u00c0\u00c1\7\21\2\2\u00c1\u00c3\7+\2")
        buf.write("\2\u00c2\u00c4\5\34\17\2\u00c3\u00c2\3\2\2\2\u00c3\u00c4")
        buf.write("\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c6\7,\2\2\u00c6")
        buf.write("\u00c8\5\"\22\2\u00c7\u00b4\3\2\2\2\u00c7\u00bf\3\2\2")
        buf.write("\2\u00c8\33\3\2\2\2\u00c9\u00ca\5\36\20\2\u00ca\u00cb")
        buf.write("\7\62\2\2\u00cb\u00cc\5\34\17\2\u00cc\u00cf\3\2\2\2\u00cd")
        buf.write("\u00cf\5\36\20\2\u00ce\u00c9\3\2\2\2\u00ce\u00cd\3\2\2")
        buf.write("\2\u00cf\35\3\2\2\2\u00d0\u00d1\5 \21\2\u00d1\u00d2\7")
        buf.write("\64\2\2\u00d2\u00d3\5\26\f\2\u00d3\37\3\2\2\2\u00d4\u00d5")
        buf.write("\5B\"\2\u00d5\u00d6\7\62\2\2\u00d6\u00d7\5 \21\2\u00d7")
        buf.write("\u00da\3\2\2\2\u00d8\u00da\5B\"\2\u00d9\u00d4\3\2\2\2")
        buf.write("\u00d9\u00d8\3\2\2\2\u00da!\3\2\2\2\u00db\u00dc\7/\2\2")
        buf.write("\u00dc\u00dd\5N(\2\u00dd\u00de\7\60\2\2\u00de#\3\2\2\2")
        buf.write("\u00df\u00e0\7+\2\2\u00e0\u00e1\5&\24\2\u00e1\u00e2\7")
        buf.write(",\2\2\u00e2%\3\2\2\2\u00e3\u00e6\5(\25\2\u00e4\u00e6\3")
        buf.write("\2\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e4\3\2\2\2\u00e6\'")
        buf.write("\3\2\2\2\u00e7\u00e8\5*\26\2\u00e8\u00e9\7\62\2\2\u00e9")
        buf.write("\u00ea\5(\25\2\u00ea\u00ed\3\2\2\2\u00eb\u00ed\5*\26\2")
        buf.write("\u00ec\u00e7\3\2\2\2\u00ec\u00eb\3\2\2\2\u00ed)\3\2\2")
        buf.write("\2\u00ee\u00ef\5,\27\2\u00ef\u00f0\7(\2\2\u00f0\u00f1")
        buf.write("\5,\27\2\u00f1\u00f4\3\2\2\2\u00f2\u00f4\5,\27\2\u00f3")
        buf.write("\u00ee\3\2\2\2\u00f3\u00f2\3\2\2\2\u00f4+\3\2\2\2\u00f5")
        buf.write("\u00f6\5.\30\2\u00f6\u00f7\t\3\2\2\u00f7\u00f8\5.\30\2")
        buf.write("\u00f8\u00fb\3\2\2\2\u00f9\u00fb\5.\30\2\u00fa\u00f5\3")
        buf.write("\2\2\2\u00fa\u00f9\3\2\2\2\u00fb-\3\2\2\2\u00fc\u00fd")
        buf.write("\b\30\1\2\u00fd\u00fe\5\60\31\2\u00fe\u0104\3\2\2\2\u00ff")
        buf.write("\u0100\f\4\2\2\u0100\u0101\t\4\2\2\u0101\u0103\5\60\31")
        buf.write("\2\u0102\u00ff\3\2\2\2\u0103\u0106\3\2\2\2\u0104\u0102")
        buf.write("\3\2\2\2\u0104\u0105\3\2\2\2\u0105/\3\2\2\2\u0106\u0104")
        buf.write("\3\2\2\2\u0107\u0108\b\31\1\2\u0108\u0109\5\62\32\2\u0109")
        buf.write("\u010f\3\2\2\2\u010a\u010b\f\4\2\2\u010b\u010c\t\5\2\2")
        buf.write("\u010c\u010e\5\62\32\2\u010d\u010a\3\2\2\2\u010e\u0111")
        buf.write("\3\2\2\2\u010f\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110")
        buf.write("\61\3\2\2\2\u0111\u010f\3\2\2\2\u0112\u0113\b\32\1\2\u0113")
        buf.write("\u0114\5\64\33\2\u0114\u011a\3\2\2\2\u0115\u0116\f\4\2")
        buf.write("\2\u0116\u0117\t\6\2\2\u0117\u0119\5\64\33\2\u0118\u0115")
        buf.write("\3\2\2\2\u0119\u011c\3\2\2\2\u011a\u0118\3\2\2\2\u011a")
        buf.write("\u011b\3\2\2\2\u011b\63\3\2\2\2\u011c\u011a\3\2\2\2\u011d")
        buf.write("\u011e\7\35\2\2\u011e\u0121\5\64\33\2\u011f\u0121\5\66")
        buf.write("\34\2\u0120\u011d\3\2\2\2\u0120\u011f\3\2\2\2\u0121\65")
        buf.write("\3\2\2\2\u0122\u0123\7\30\2\2\u0123\u0126\5\66\34\2\u0124")
        buf.write("\u0126\58\35\2\u0125\u0122\3\2\2\2\u0125\u0124\3\2\2\2")
        buf.write("\u0126\67\3\2\2\2\u0127\u0128\5:\36\2\u0128\u0129\7-\2")
        buf.write("\2\u0129\u012a\5*\26\2\u012a\u012b\7.\2\2\u012b\u012e")
        buf.write("\3\2\2\2\u012c\u012e\5:\36\2\u012d\u0127\3\2\2\2\u012d")
        buf.write("\u012c\3\2\2\2\u012e9\3\2\2\2\u012f\u0130\b\36\1\2\u0130")
        buf.write("\u0131\5<\37\2\u0131\u0140\3\2\2\2\u0132\u0137\f\4\2\2")
        buf.write("\u0133\u0134\7-\2\2\u0134\u0135\5*\26\2\u0135\u0136\7")
        buf.write(".\2\2\u0136\u0138\3\2\2\2\u0137\u0133\3\2\2\2\u0137\u0138")
        buf.write("\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013a\7\61\2\2\u013a")
        buf.write("\u013c\7:\2\2\u013b\u013d\5$\23\2\u013c\u013b\3\2\2\2")
        buf.write("\u013c\u013d\3\2\2\2\u013d\u013f\3\2\2\2\u013e\u0132\3")
        buf.write("\2\2\2\u013f\u0142\3\2\2\2\u0140\u013e\3\2\2\2\u0140\u0141")
        buf.write("\3\2\2\2\u0141;\3\2\2\2\u0142\u0140\3\2\2\2\u0143\u0144")
        buf.write("\7:\2\2\u0144\u0146\7\61\2\2\u0145\u0143\3\2\2\2\u0145")
        buf.write("\u0146\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0149\7;\2\2")
        buf.write("\u0148\u014a\5$\23\2\u0149\u0148\3\2\2\2\u0149\u014a\3")
        buf.write("\2\2\2\u014a\u014d\3\2\2\2\u014b\u014d\5> \2\u014c\u0145")
        buf.write("\3\2\2\2\u014c\u014b\3\2\2\2\u014d=\3\2\2\2\u014e\u014f")
        buf.write("\7*\2\2\u014f\u0150\7:\2\2\u0150\u0153\5$\23\2\u0151\u0153")
        buf.write("\5@!\2\u0152\u014e\3\2\2\2\u0152\u0151\3\2\2\2\u0153?")
        buf.write("\3\2\2\2\u0154\u0155\7+\2\2\u0155\u0156\5*\26\2\u0156")
        buf.write("\u0157\7,\2\2\u0157\u015a\3\2\2\2\u0158\u015a\5D#\2\u0159")
        buf.write("\u0154\3\2\2\2\u0159\u0158\3\2\2\2\u015aA\3\2\2\2\u015b")
        buf.write("\u015c\t\7\2\2\u015cC\3\2\2\2\u015d\u0166\7\65\2\2\u015e")
        buf.write("\u0166\7\66\2\2\u015f\u0166\5F$\2\u0160\u0166\7\67\2\2")
        buf.write("\u0161\u0166\5H%\2\u0162\u0166\7\17\2\2\u0163\u0166\7")
        buf.write("\23\2\2\u0164\u0166\5B\"\2\u0165\u015d\3\2\2\2\u0165\u015e")
        buf.write("\3\2\2\2\u0165\u015f\3\2\2\2\u0165\u0160\3\2\2\2\u0165")
        buf.write("\u0161\3\2\2\2\u0165\u0162\3\2\2\2\u0165\u0163\3\2\2\2")
        buf.write("\u0165\u0164\3\2\2\2\u0166E\3\2\2\2\u0167\u0168\t\b\2")
        buf.write("\2\u0168G\3\2\2\2\u0169\u016a\7-\2\2\u016a\u016b\5L\'")
        buf.write("\2\u016b\u016c\7.\2\2\u016cI\3\2\2\2\u016d\u0170\5L\'")
        buf.write("\2\u016e\u0170\3\2\2\2\u016f\u016d\3\2\2\2\u016f\u016e")
        buf.write("\3\2\2\2\u0170K\3\2\2\2\u0171\u0172\5D#\2\u0172\u0173")
        buf.write("\7\62\2\2\u0173\u0174\5L\'\2\u0174\u0177\3\2\2\2\u0175")
        buf.write("\u0177\5D#\2\u0176\u0171\3\2\2\2\u0176\u0175\3\2\2\2\u0177")
        buf.write("M\3\2\2\2\u0178\u0179\5P)\2\u0179\u017a\5N(\2\u017a\u017d")
        buf.write("\3\2\2\2\u017b\u017d\3\2\2\2\u017c\u0178\3\2\2\2\u017c")
        buf.write("\u017b\3\2\2\2\u017dO\3\2\2\2\u017e\u0180\7\5\2\2\u017f")
        buf.write("\u0181\5\"\22\2\u0180\u017f\3\2\2\2\u0180\u0181\3\2\2")
        buf.write("\2\u0181\u0182\3\2\2\2\u0182\u0183\5*\26\2\u0183\u0186")
        buf.write("\5\"\22\2\u0184\u0185\7\6\2\2\u0185\u0187\5\"\22\2\u0186")
        buf.write("\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u01a6\3\2\2\2")
        buf.write("\u0188\u0189\7\7\2\2\u0189\u018a\5R*\2\u018a\u018b\7\63")
        buf.write("\2\2\u018b\u018c\5*\26\2\u018c\u018d\7\63\2\2\u018d\u018e")
        buf.write("\5R*\2\u018e\u018f\5\"\22\2\u018f\u01a6\3\2\2\2\u0190")
        buf.write("\u0192\t\t\2\2\u0191\u0190\3\2\2\2\u0191\u0192\3\2\2\2")
        buf.write("\u0192\u0193\3\2\2\2\u0193\u0194\5R*\2\u0194\u0195\7\63")
        buf.write("\2\2\u0195\u01a6\3\2\2\2\u0196\u0197\7\3\2\2\u0197\u01a6")
        buf.write("\7\63\2\2\u0198\u0199\7\4\2\2\u0199\u01a6\7\63\2\2\u019a")
        buf.write("\u019c\7\16\2\2\u019b\u019d\5*\26\2\u019c\u019b\3\2\2")
        buf.write("\2\u019c\u019d\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u01a6")
        buf.write("\7\63\2\2\u019f\u01a0\5\\/\2\u01a0\u01a1\7\63\2\2\u01a1")
        buf.write("\u01a6\3\2\2\2\u01a2\u01a3\5b\62\2\u01a3\u01a4\7\63\2")
        buf.write("\2\u01a4\u01a6\3\2\2\2\u01a5\u017e\3\2\2\2\u01a5\u0188")
        buf.write("\3\2\2\2\u01a5\u0191\3\2\2\2\u01a5\u0196\3\2\2\2\u01a5")
        buf.write("\u0198\3\2\2\2\u01a5\u019a\3\2\2\2\u01a5\u019f\3\2\2\2")
        buf.write("\u01a5\u01a2\3\2\2\2\u01a6Q\3\2\2\2\u01a7\u01a8\5T+\2")
        buf.write("\u01a8\u01a9\7\'\2\2\u01a9\u01aa\5*\26\2\u01aaS\3\2\2")
        buf.write("\2\u01ab\u01ac\5V,\2\u01ac\u01ad\7-\2\2\u01ad\u01ae\5")
        buf.write("*\26\2\u01ae\u01af\7.\2\2\u01af\u01b2\3\2\2\2\u01b0\u01b2")
        buf.write("\5V,\2\u01b1\u01ab\3\2\2\2\u01b1\u01b0\3\2\2\2\u01b2U")
        buf.write("\3\2\2\2\u01b3\u01b4\b,\1\2\u01b4\u01b5\5X-\2\u01b5\u01c1")
        buf.write("\3\2\2\2\u01b6\u01bb\f\4\2\2\u01b7\u01b8\7-\2\2\u01b8")
        buf.write("\u01b9\5*\26\2\u01b9\u01ba\7.\2\2\u01ba\u01bc\3\2\2\2")
        buf.write("\u01bb\u01b7\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01bd\3")
        buf.write("\2\2\2\u01bd\u01be\7\61\2\2\u01be\u01c0\7:\2\2\u01bf\u01b6")
        buf.write("\3\2\2\2\u01c0\u01c3\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c1")
        buf.write("\u01c2\3\2\2\2\u01c2W\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c4")
        buf.write("\u01c5\7:\2\2\u01c5\u01c7\7\61\2\2\u01c6\u01c4\3\2\2\2")
        buf.write("\u01c6\u01c7\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01cb\7")
        buf.write(";\2\2\u01c9\u01cb\5Z.\2\u01ca\u01c6\3\2\2\2\u01ca\u01c9")
        buf.write("\3\2\2\2\u01cbY\3\2\2\2\u01cc\u01cd\7+\2\2\u01cd\u01ce")
        buf.write("\5T+\2\u01ce\u01cf\7,\2\2\u01cf\u01d3\3\2\2\2\u01d0\u01d3")
        buf.write("\7\23\2\2\u01d1\u01d3\5B\"\2\u01d2\u01cc\3\2\2\2\u01d2")
        buf.write("\u01d0\3\2\2\2\u01d2\u01d1\3\2\2\2\u01d3[\3\2\2\2\u01d4")
        buf.write("\u01d7\5^\60\2\u01d5\u01d7\5`\61\2\u01d6\u01d4\3\2\2\2")
        buf.write("\u01d6\u01d5\3\2\2\2\u01d7]\3\2\2\2\u01d8\u01dd\5:\36")
        buf.write("\2\u01d9\u01da\7-\2\2\u01da\u01db\5*\26\2\u01db\u01dc")
        buf.write("\7.\2\2\u01dc\u01de\3\2\2\2\u01dd\u01d9\3\2\2\2\u01dd")
        buf.write("\u01de\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01e0\7\61\2")
        buf.write("\2\u01e0\u01e1\7:\2\2\u01e1\u01e2\5$\23\2\u01e2_\3\2\2")
        buf.write("\2\u01e3\u01e4\7:\2\2\u01e4\u01e6\7\61\2\2\u01e5\u01e3")
        buf.write("\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7")
        buf.write("\u01e8\7;\2\2\u01e8\u01e9\5$\23\2\u01e9a\3\2\2\2\u01ea")
        buf.write("\u01ed\5\16\b\2\u01eb\u01ed\5\20\t\2\u01ec\u01ea\3\2\2")
        buf.write("\2\u01ec\u01eb\3\2\2\2\u01edc\3\2\2\2\67kp{\u0081\u0085")
        buf.write("\u008a\u008f\u009d\u00a7\u00ac\u00b0\u00b8\u00c3\u00c7")
        buf.write("\u00ce\u00d9\u00e5\u00ec\u00f3\u00fa\u0104\u010f\u011a")
        buf.write("\u0120\u0125\u012d\u0137\u013c\u0140\u0145\u0149\u014c")
        buf.write("\u0152\u0159\u0165\u016f\u0176\u017c\u0180\u0186\u0191")
        buf.write("\u019c\u01a5\u01b1\u01bb\u01c1\u01c6\u01ca\u01d2\u01d6")
        buf.write("\u01dd\u01e5\u01ec")
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
    RULE_vardecl = 6
    RULE_constdecl = 7
    RULE_attlistdecl = 8
    RULE_attlistnodecl = 9
    RULE_atttyp = 10
    RULE_typ = 11
    RULE_method = 12
    RULE_paramlist = 13
    RULE_params = 14
    RULE_param = 15
    RULE_blockstmt = 16
    RULE_parenexpr = 17
    RULE_exprlist = 18
    RULE_exprprime = 19
    RULE_exprstr = 20
    RULE_exprrel = 21
    RULE_exprlog = 22
    RULE_expradd = 23
    RULE_exprmul = 24
    RULE_exprnot = 25
    RULE_exprsign = 26
    RULE_exprindex = 27
    RULE_exprinst = 28
    RULE_exprstat = 29
    RULE_exprobj = 30
    RULE_exprparen = 31
    RULE_identifier = 32
    RULE_lit = 33
    RULE_boollit = 34
    RULE_arraylit = 35
    RULE_litlist = 36
    RULE_litprime = 37
    RULE_stmtlist = 38
    RULE_stmt = 39
    RULE_stmtassign = 40
    RULE_lhs = 41
    RULE_lhsinst = 42
    RULE_lhsstat = 43
    RULE_lhsparen = 44
    RULE_stmtinvoc = 45
    RULE_stmtinvocinst = 46
    RULE_stmtinvocstat = 47
    RULE_stmtdecl = 48

    ruleNames =  [ "program", "classdecllist", "classdecl", "memberlist", 
                   "member", "attribute", "vardecl", "constdecl", "attlistdecl", 
                   "attlistnodecl", "atttyp", "typ", "method", "paramlist", 
                   "params", "param", "blockstmt", "parenexpr", "exprlist", 
                   "exprprime", "exprstr", "exprrel", "exprlog", "expradd", 
                   "exprmul", "exprnot", "exprsign", "exprindex", "exprinst", 
                   "exprstat", "exprobj", "exprparen", "identifier", "lit", 
                   "boollit", "arraylit", "litlist", "litprime", "stmtlist", 
                   "stmt", "stmtassign", "lhs", "lhsinst", "lhsstat", "lhsparen", 
                   "stmtinvoc", "stmtinvocinst", "stmtinvocstat", "stmtdecl" ]

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
            self.state = 98
            self.classdecllist()
            self.state = 99
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
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.classdecl()
                self.state = 102
                self.classdecllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
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
            self.state = 107
            self.match(CSlangParser.CLASS)
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 108
                self.match(CSlangParser.ID)
                self.state = 109
                self.match(CSlangParser.LARROW)


            self.state = 112
            self.match(CSlangParser.ID)
            self.state = 113
            self.match(CSlangParser.LBR)
            self.state = 114
            self.memberlist()
            self.state = 115
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
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST, CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.member()
                self.state = 118
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
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.attribute()
                self.state = 124
                self.match(CSlangParser.SM)
                pass
            elif token in [CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
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

        def vardecl(self):
            return self.getTypedRuleContext(CSlangParser.VardeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(CSlangParser.ConstdeclContext,0)


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
        try:
            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.vardecl()
                pass
            elif token in [CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.constdecl()
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


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def attlistdecl(self):
            return self.getTypedRuleContext(CSlangParser.AttlistdeclContext,0)


        def attlistnodecl(self):
            return self.getTypedRuleContext(CSlangParser.AttlistnodeclContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = CSlangParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(CSlangParser.VAR)
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 134
                self.attlistdecl()
                pass

            elif la_ == 2:
                self.state = 135
                self.attlistnodecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def attlistdecl(self):
            return self.getTypedRuleContext(CSlangParser.AttlistdeclContext,0)


        def attlistnodecl(self):
            return self.getTypedRuleContext(CSlangParser.AttlistnodeclContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_constdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstdecl" ):
                return visitor.visitConstdecl(self)
            else:
                return visitor.visitChildren(self)




    def constdecl(self):

        localctx = CSlangParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_constdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(CSlangParser.CONST)
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 139
                self.attlistdecl()
                pass

            elif la_ == 2:
                self.state = 140
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
        self.enterRule(localctx, 16, self.RULE_attlistdecl)
        try:
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.identifier()
                self.state = 144
                self.match(CSlangParser.CM)
                self.state = 145
                self.attlistdecl()
                self.state = 146
                self.match(CSlangParser.CM)
                self.state = 147
                self.exprstr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.identifier()
                self.state = 150
                self.match(CSlangParser.COL)
                self.state = 151
                self.atttyp()
                self.state = 152
                self.match(CSlangParser.DECLARE)
                self.state = 153
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
        self.enterRule(localctx, 18, self.RULE_attlistnodecl)
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.identifier()
                self.state = 158
                self.match(CSlangParser.CM)
                self.state = 159
                self.attlistnodecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.identifier()
                self.state = 162
                self.match(CSlangParser.COL)
                self.state = 163
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

        def VOID(self):
            return self.getToken(CSlangParser.VOID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_atttyp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtttyp" ):
                return visitor.visitAtttyp(self)
            else:
                return visitor.visitChildren(self)




    def atttyp(self):

        localctx = CSlangParser.AtttypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_atttyp)
        self._la = 0 # Token type
        try:
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.LBK, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.LBK:
                    self.state = 167
                    self.match(CSlangParser.LBK)
                    self.state = 168
                    self.match(CSlangParser.INTLIT)
                    self.state = 169
                    self.match(CSlangParser.RBK)


                self.state = 172
                self.typ()
                pass
            elif token in [CSlangParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.match(CSlangParser.VOID)
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
        self.enterRule(localctx, 22, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
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

        def atttyp(self):
            return self.getTypedRuleContext(CSlangParser.AtttypContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(CSlangParser.BlockstmtContext,0)


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
        self.enterRule(localctx, 24, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.match(CSlangParser.FUNC)
                self.state = 179
                self.identifier()
                self.state = 180
                self.match(CSlangParser.LPN)
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ID or _la==CSlangParser.ATID:
                    self.state = 181
                    self.paramlist()


                self.state = 184
                self.match(CSlangParser.RPN)
                self.state = 185
                self.match(CSlangParser.COL)
                self.state = 186
                self.atttyp()
                self.state = 187
                self.blockstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.match(CSlangParser.FUNC)
                self.state = 190
                self.match(CSlangParser.CONSTRUCTOR)
                self.state = 191
                self.match(CSlangParser.LPN)
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ID or _la==CSlangParser.ATID:
                    self.state = 192
                    self.paramlist()


                self.state = 195
                self.match(CSlangParser.RPN)
                self.state = 196
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
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.params()
                self.state = 200
                self.match(CSlangParser.CM)
                self.state = 201
                self.paramlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.params()
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

        def param(self):
            return self.getTypedRuleContext(CSlangParser.ParamContext,0)


        def COL(self):
            return self.getToken(CSlangParser.COL, 0)

        def atttyp(self):
            return self.getTypedRuleContext(CSlangParser.AtttypContext,0)


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
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.param()
            self.state = 207
            self.match(CSlangParser.COL)
            self.state = 208
            self.atttyp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CSlangParser.IdentifierContext,0)


        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def param(self):
            return self.getTypedRuleContext(CSlangParser.ParamContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = CSlangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_param)
        try:
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.identifier()
                self.state = 211
                self.match(CSlangParser.CM)
                self.state = 212
                self.param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.identifier()
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
        self.enterRule(localctx, 32, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(CSlangParser.LBR)
            self.state = 218
            self.stmtlist()
            self.state = 219
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
        self.enterRule(localctx, 34, self.RULE_parenexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(CSlangParser.LPN)
            self.state = 222
            self.exprlist()
            self.state = 223
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
        self.enterRule(localctx, 36, self.RULE_exprlist)
        try:
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.SUB, CSlangParser.NEG, CSlangParser.NEW, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRLIT, CSlangParser.ID, CSlangParser.ATID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
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

        def exprprime(self):
            return self.getTypedRuleContext(CSlangParser.ExprprimeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exprprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprprime" ):
                return visitor.visitExprprime(self)
            else:
                return visitor.visitChildren(self)




    def exprprime(self):

        localctx = CSlangParser.ExprprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_exprprime)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.exprstr()
                self.state = 230
                self.match(CSlangParser.CM)
                self.state = 231
                self.exprprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
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
        self.enterRule(localctx, 40, self.RULE_exprstr)
        try:
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.exprrel()
                self.state = 237
                self.match(CSlangParser.CONCATE)
                self.state = 238
                self.exprrel()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
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
        self.enterRule(localctx, 42, self.RULE_exprrel)
        self._la = 0 # Token type
        try:
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.exprlog(0)
                self.state = 244
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.EQ) | (1 << CSlangParser.NEQ) | (1 << CSlangParser.LT) | (1 << CSlangParser.LTEQ) | (1 << CSlangParser.GT) | (1 << CSlangParser.GTEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 245
                self.exprlog(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_exprlog, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.expradd(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 258
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprlogContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprlog)
                    self.state = 253
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 254
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.AND or _la==CSlangParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 255
                    self.expradd(0) 
                self.state = 260
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expradd, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.exprmul(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExpraddContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expradd)
                    self.state = 264
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 265
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.ADD or _la==CSlangParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 266
                    self.exprmul(0) 
                self.state = 271
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_exprmul, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.exprnot()
            self._ctx.stop = self._input.LT(-1)
            self.state = 280
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprmulContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprmul)
                    self.state = 275
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 276
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.MUL) | (1 << CSlangParser.DIVFLOAT) | (1 << CSlangParser.DIVINT) | (1 << CSlangParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 277
                    self.exprnot() 
                self.state = 282
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
        self.enterRule(localctx, 50, self.RULE_exprnot)
        try:
            self.state = 286
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.match(CSlangParser.NEG)
                self.state = 284
                self.exprnot()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.SUB, CSlangParser.NEW, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRLIT, CSlangParser.ID, CSlangParser.ATID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
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
        self.enterRule(localctx, 52, self.RULE_exprsign)
        try:
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.match(CSlangParser.SUB)
                self.state = 289
                self.exprsign()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRLIT, CSlangParser.ID, CSlangParser.ATID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
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
        self.enterRule(localctx, 54, self.RULE_exprindex)
        try:
            self.state = 299
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.exprinst(0)
                self.state = 294
                self.match(CSlangParser.LBK)
                self.state = 295
                self.exprstr()
                self.state = 296
                self.match(CSlangParser.RBK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
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

        def LBK(self):
            return self.getToken(CSlangParser.LBK, 0)

        def exprstr(self):
            return self.getTypedRuleContext(CSlangParser.ExprstrContext,0)


        def RBK(self):
            return self.getToken(CSlangParser.RBK, 0)

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
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_exprinst, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.exprstat()
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
                    self.state = 304
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 309
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==CSlangParser.LBK:
                        self.state = 305
                        self.match(CSlangParser.LBK)
                        self.state = 306
                        self.exprstr()
                        self.state = 307
                        self.match(CSlangParser.RBK)


                    self.state = 311
                    self.match(CSlangParser.DOT)
                    self.state = 312
                    self.match(CSlangParser.ID)
                    self.state = 314
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        self.state = 313
                        self.parenexpr()

             
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
        self.enterRule(localctx, 58, self.RULE_exprstat)
        self._la = 0 # Token type
        try:
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ID:
                    self.state = 321
                    self.match(CSlangParser.ID)
                    self.state = 322
                    self.match(CSlangParser.DOT)


                self.state = 325
                self.match(CSlangParser.ATID)
                self.state = 327
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                if la_ == 1:
                    self.state = 326
                    self.parenexpr()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 329
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
        self.enterRule(localctx, 60, self.RULE_exprobj)
        try:
            self.state = 336
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.match(CSlangParser.NEW)
                self.state = 333
                self.match(CSlangParser.ID)
                self.state = 334
                self.parenexpr()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRLIT, CSlangParser.ID, CSlangParser.ATID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
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
        self.enterRule(localctx, 62, self.RULE_exprparen)
        try:
            self.state = 343
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LPN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.match(CSlangParser.LPN)
                self.state = 339
                self.exprstr()
                self.state = 340
                self.match(CSlangParser.RPN)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.LBK, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRLIT, CSlangParser.ID, CSlangParser.ATID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
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
        self.enterRule(localctx, 64, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
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
        self.enterRule(localctx, 66, self.RULE_lit)
        try:
            self.state = 355
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.match(CSlangParser.INTLIT)
                pass
            elif token in [CSlangParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.match(CSlangParser.FLOATLIT)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 349
                self.boollit()
                pass
            elif token in [CSlangParser.STRLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 350
                self.match(CSlangParser.STRLIT)
                pass
            elif token in [CSlangParser.LBK]:
                self.enterOuterAlt(localctx, 5)
                self.state = 351
                self.arraylit()
                pass
            elif token in [CSlangParser.NULL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 352
                self.match(CSlangParser.NULL)
                pass
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 7)
                self.state = 353
                self.match(CSlangParser.SELF)
                pass
            elif token in [CSlangParser.ID, CSlangParser.ATID]:
                self.enterOuterAlt(localctx, 8)
                self.state = 354
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
        self.enterRule(localctx, 68, self.RULE_boollit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
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
        self.enterRule(localctx, 70, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(CSlangParser.LBK)
            self.state = 360
            self.litprime()
            self.state = 361
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
        self.enterRule(localctx, 72, self.RULE_litlist)
        try:
            self.state = 365
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.LBK, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRLIT, CSlangParser.ID, CSlangParser.ATID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 363
                self.litprime()
                pass
            elif token in [CSlangParser.EOF]:
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

        def litprime(self):
            return self.getTypedRuleContext(CSlangParser.LitprimeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_litprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLitprime" ):
                return visitor.visitLitprime(self)
            else:
                return visitor.visitChildren(self)




    def litprime(self):

        localctx = CSlangParser.LitprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_litprime)
        try:
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.lit()
                self.state = 368
                self.match(CSlangParser.CM)
                self.state = 369
                self.litprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 371
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
        self.enterRule(localctx, 76, self.RULE_stmtlist)
        try:
            self.state = 378
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.BREAK, CSlangParser.CONTINUE, CSlangParser.IF, CSlangParser.FOR, CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.RETURN, CSlangParser.NULL, CSlangParser.VAR, CSlangParser.SELF, CSlangParser.CONST, CSlangParser.NEW, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRLIT, CSlangParser.ID, CSlangParser.ATID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.stmt()
                self.state = 375
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

        def BREAK(self):
            return self.getToken(CSlangParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(CSlangParser.CONTINUE, 0)

        def RETURN(self):
            return self.getToken(CSlangParser.RETURN, 0)

        def stmtinvoc(self):
            return self.getTypedRuleContext(CSlangParser.StmtinvocContext,0)


        def stmtdecl(self):
            return self.getTypedRuleContext(CSlangParser.StmtdeclContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = CSlangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 419
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.match(CSlangParser.IF)
                self.state = 382
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.LBR:
                    self.state = 381
                    self.blockstmt()


                self.state = 384
                self.exprstr()
                self.state = 385
                self.blockstmt()
                self.state = 388
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ELSE:
                    self.state = 386
                    self.match(CSlangParser.ELSE)
                    self.state = 387
                    self.blockstmt()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 390
                self.match(CSlangParser.FOR)
                self.state = 391
                self.stmtassign()
                self.state = 392
                self.match(CSlangParser.SM)
                self.state = 393
                self.exprstr()
                self.state = 394
                self.match(CSlangParser.SM)
                self.state = 395
                self.stmtassign()
                self.state = 396
                self.blockstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 399
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.VAR or _la==CSlangParser.CONST:
                    self.state = 398
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 401
                self.stmtassign()
                self.state = 402
                self.match(CSlangParser.SM)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 404
                self.match(CSlangParser.BREAK)
                self.state = 405
                self.match(CSlangParser.SM)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 406
                self.match(CSlangParser.CONTINUE)
                self.state = 407
                self.match(CSlangParser.SM)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 408
                self.match(CSlangParser.RETURN)
                self.state = 410
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NEG) | (1 << CSlangParser.NEW) | (1 << CSlangParser.LPN) | (1 << CSlangParser.LBK) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.STRLIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.ATID))) != 0):
                    self.state = 409
                    self.exprstr()


                self.state = 412
                self.match(CSlangParser.SM)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 413
                self.stmtinvoc()
                self.state = 414
                self.match(CSlangParser.SM)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 416
                self.stmtdecl()
                self.state = 417
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
        self.enterRule(localctx, 80, self.RULE_stmtassign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.lhs()
            self.state = 422
            self.match(CSlangParser.ASSIGN)
            self.state = 423
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




    def lhs(self):

        localctx = CSlangParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_lhs)
        try:
            self.state = 431
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 425
                self.lhsinst(0)
                self.state = 426
                self.match(CSlangParser.LBK)
                self.state = 427
                self.exprstr()
                self.state = 428
                self.match(CSlangParser.RBK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
                self.lhsinst(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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

        def LBK(self):
            return self.getToken(CSlangParser.LBK, 0)

        def exprstr(self):
            return self.getTypedRuleContext(CSlangParser.ExprstrContext,0)


        def RBK(self):
            return self.getToken(CSlangParser.RBK, 0)

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
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_lhsinst, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.lhsstat()
            self._ctx.stop = self._input.LT(-1)
            self.state = 447
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.LhsinstContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lhsinst)
                    self.state = 436
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 441
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==CSlangParser.LBK:
                        self.state = 437
                        self.match(CSlangParser.LBK)
                        self.state = 438
                        self.exprstr()
                        self.state = 439
                        self.match(CSlangParser.RBK)


                    self.state = 443
                    self.match(CSlangParser.DOT)
                    self.state = 444
                    self.match(CSlangParser.ID) 
                self.state = 449
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

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
        self.enterRule(localctx, 86, self.RULE_lhsstat)
        self._la = 0 # Token type
        try:
            self.state = 456
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 452
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ID:
                    self.state = 450
                    self.match(CSlangParser.ID)
                    self.state = 451
                    self.match(CSlangParser.DOT)


                self.state = 454
                self.match(CSlangParser.ATID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 455
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
        self.enterRule(localctx, 88, self.RULE_lhsparen)
        try:
            self.state = 464
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LPN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 458
                self.match(CSlangParser.LPN)
                self.state = 459
                self.lhs()
                self.state = 460
                self.match(CSlangParser.RPN)
                pass
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 462
                self.match(CSlangParser.SELF)
                pass
            elif token in [CSlangParser.ID, CSlangParser.ATID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 463
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

        def stmtinvocinst(self):
            return self.getTypedRuleContext(CSlangParser.StmtinvocinstContext,0)


        def stmtinvocstat(self):
            return self.getTypedRuleContext(CSlangParser.StmtinvocstatContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmtinvoc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtinvoc" ):
                return visitor.visitStmtinvoc(self)
            else:
                return visitor.visitChildren(self)




    def stmtinvoc(self):

        localctx = CSlangParser.StmtinvocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_stmtinvoc)
        try:
            self.state = 468
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 466
                self.stmtinvocinst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 467
                self.stmtinvocstat()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtinvocinstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprinst(self):
            return self.getTypedRuleContext(CSlangParser.ExprinstContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def parenexpr(self):
            return self.getTypedRuleContext(CSlangParser.ParenexprContext,0)


        def LBK(self):
            return self.getToken(CSlangParser.LBK, 0)

        def exprstr(self):
            return self.getTypedRuleContext(CSlangParser.ExprstrContext,0)


        def RBK(self):
            return self.getToken(CSlangParser.RBK, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_stmtinvocinst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtinvocinst" ):
                return visitor.visitStmtinvocinst(self)
            else:
                return visitor.visitChildren(self)




    def stmtinvocinst(self):

        localctx = CSlangParser.StmtinvocinstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_stmtinvocinst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.exprinst(0)
            self.state = 475
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LBK:
                self.state = 471
                self.match(CSlangParser.LBK)
                self.state = 472
                self.exprstr()
                self.state = 473
                self.match(CSlangParser.RBK)


            self.state = 477
            self.match(CSlangParser.DOT)
            self.state = 478
            self.match(CSlangParser.ID)
            self.state = 479
            self.parenexpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtinvocstatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATID(self):
            return self.getToken(CSlangParser.ATID, 0)

        def parenexpr(self):
            return self.getTypedRuleContext(CSlangParser.ParenexprContext,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_stmtinvocstat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtinvocstat" ):
                return visitor.visitStmtinvocstat(self)
            else:
                return visitor.visitChildren(self)




    def stmtinvocstat(self):

        localctx = CSlangParser.StmtinvocstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_stmtinvocstat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 481
                self.match(CSlangParser.ID)
                self.state = 482
                self.match(CSlangParser.DOT)


            self.state = 485
            self.match(CSlangParser.ATID)
            self.state = 486
            self.parenexpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(CSlangParser.VardeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(CSlangParser.ConstdeclContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmtdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtdecl" ):
                return visitor.visitStmtdecl(self)
            else:
                return visitor.visitChildren(self)




    def stmtdecl(self):

        localctx = CSlangParser.StmtdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_stmtdecl)
        try:
            self.state = 490
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 488
                self.vardecl()
                pass
            elif token in [CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 489
                self.constdecl()
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
        self._predicates[22] = self.exprlog_sempred
        self._predicates[23] = self.expradd_sempred
        self._predicates[24] = self.exprmul_sempred
        self._predicates[28] = self.exprinst_sempred
        self._predicates[42] = self.lhsinst_sempred
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
         

    def lhsinst_sempred(self, localctx:LhsinstContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




