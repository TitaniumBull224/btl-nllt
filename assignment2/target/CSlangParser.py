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
        buf.write("\u01f7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\5\3n\n\3\3\4\3\4\3\4\5\4s\n\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5~\n\5\3\6\3\6\3\6\3")
        buf.write("\6\5\6\u0084\n\6\3\7\3\7\5\7\u0088\n\7\3\b\3\b\3\b\5\b")
        buf.write("\u008d\n\b\3\t\3\t\3\t\5\t\u0092\n\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00a0\n\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00aa\n\13\3\f\3\f")
        buf.write("\3\f\5\f\u00af\n\f\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\5\16\u00b9\n\16\3\16\3\16\3\16\3\16\5\16\u00bf\n\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\5\16\u00c7\n\16\3\16\3\16")
        buf.write("\5\16\u00cb\n\16\3\17\3\17\3\17\3\17\3\17\5\17\u00d2\n")
        buf.write("\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u00dd\n\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3")
        buf.write("\24\3\24\5\24\u00e9\n\24\3\25\3\25\3\25\3\25\3\25\5\25")
        buf.write("\u00f0\n\25\3\26\3\26\3\26\3\26\3\26\5\26\u00f7\n\26\3")
        buf.write("\27\3\27\3\27\3\27\3\27\5\27\u00fe\n\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\7\30\u0106\n\30\f\30\16\30\u0109\13\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u0111\n\31\f\31\16")
        buf.write("\31\u0114\13\31\3\32\3\32\3\32\3\32\3\32\3\32\7\32\u011c")
        buf.write("\n\32\f\32\16\32\u011f\13\32\3\33\3\33\3\33\5\33\u0124")
        buf.write("\n\33\3\34\3\34\3\34\5\34\u0129\n\34\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\5\35\u0131\n\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\5\36\u013b\n\36\3\36\3\36\3\36\5\36\u0140")
        buf.write("\n\36\7\36\u0142\n\36\f\36\16\36\u0145\13\36\3\37\3\37")
        buf.write("\5\37\u0149\n\37\3 \3 \3 \3 \5 \u014f\n \3!\3!\3!\3!\3")
        buf.write("!\5!\u0156\n!\3\"\3\"\5\"\u015a\n\"\3\"\3\"\5\"\u015e")
        buf.write("\n\"\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\5$\u016a\n$\3%\3%\3")
        buf.write("&\3&\3&\3&\3\'\3\'\5\'\u0174\n\'\3(\3(\3(\3(\3(\5(\u017b")
        buf.write("\n(\3)\3)\3)\3)\5)\u0181\n)\3*\3*\5*\u0185\n*\3*\3*\3")
        buf.write("*\3*\5*\u018b\n*\3*\3*\3*\3*\3*\3*\3*\3*\3*\5*\u0196\n")
        buf.write("*\3*\3*\3*\3*\3*\3*\3*\3*\3*\5*\u01a1\n*\3*\3*\3*\3*\3")
        buf.write("*\3*\3*\5*\u01aa\n*\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\7,\u01b8\n,\f,\16,\u01bb\13,\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\5-\u01c5\n-\3-\3-\3-\5-\u01ca\n-\7-\u01cc\n-\f-\16-")
        buf.write("\u01cf\13-\3.\3.\5.\u01d3\n.\3/\3/\3/\3/\3/\3/\5/\u01db")
        buf.write("\n/\3\60\3\60\5\60\u01df\n\60\3\61\3\61\3\61\3\61\3\61")
        buf.write("\5\61\u01e6\n\61\3\61\3\61\3\61\3\61\3\62\3\62\5\62\u01ee")
        buf.write("\n\62\3\62\3\62\3\62\3\63\3\63\5\63\u01f5\n\63\3\63\2")
        buf.write("\b.\60\62:VX\64\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bd\2\n\4\2")
        buf.write("\n\r::\3\2 %\3\2\36\37\3\2\27\30\3\2\31\34\3\2:;\3\2\b")
        buf.write("\t\4\2\22\22\25\25\2\u0206\2f\3\2\2\2\4m\3\2\2\2\6o\3")
        buf.write("\2\2\2\b}\3\2\2\2\n\u0083\3\2\2\2\f\u0087\3\2\2\2\16\u0089")
        buf.write("\3\2\2\2\20\u008e\3\2\2\2\22\u009f\3\2\2\2\24\u00a9\3")
        buf.write("\2\2\2\26\u00ae\3\2\2\2\30\u00b2\3\2\2\2\32\u00ca\3\2")
        buf.write("\2\2\34\u00d1\3\2\2\2\36\u00d3\3\2\2\2 \u00dc\3\2\2\2")
        buf.write("\"\u00de\3\2\2\2$\u00e2\3\2\2\2&\u00e8\3\2\2\2(\u00ef")
        buf.write("\3\2\2\2*\u00f6\3\2\2\2,\u00fd\3\2\2\2.\u00ff\3\2\2\2")
        buf.write("\60\u010a\3\2\2\2\62\u0115\3\2\2\2\64\u0123\3\2\2\2\66")
        buf.write("\u0128\3\2\2\28\u0130\3\2\2\2:\u0132\3\2\2\2<\u0148\3")
        buf.write("\2\2\2>\u014e\3\2\2\2@\u0155\3\2\2\2B\u0159\3\2\2\2D\u015f")
        buf.write("\3\2\2\2F\u0169\3\2\2\2H\u016b\3\2\2\2J\u016d\3\2\2\2")
        buf.write("L\u0173\3\2\2\2N\u017a\3\2\2\2P\u0180\3\2\2\2R\u01a9\3")
        buf.write("\2\2\2T\u01ab\3\2\2\2V\u01af\3\2\2\2X\u01bc\3\2\2\2Z\u01d2")
        buf.write("\3\2\2\2\\\u01da\3\2\2\2^\u01de\3\2\2\2`\u01e0\3\2\2\2")
        buf.write("b\u01ed\3\2\2\2d\u01f4\3\2\2\2fg\5\4\3\2gh\7\2\2\3h\3")
        buf.write("\3\2\2\2ij\5\6\4\2jk\5\4\3\2kn\3\2\2\2ln\5\6\4\2mi\3\2")
        buf.write("\2\2ml\3\2\2\2n\5\3\2\2\2or\7\20\2\2pq\7:\2\2qs\7)\2\2")
        buf.write("rp\3\2\2\2rs\3\2\2\2st\3\2\2\2tu\7:\2\2uv\7/\2\2vw\5\b")
        buf.write("\5\2wx\7\60\2\2x\7\3\2\2\2yz\5\n\6\2z{\5\b\5\2{~\3\2\2")
        buf.write("\2|~\3\2\2\2}y\3\2\2\2}|\3\2\2\2~\t\3\2\2\2\177\u0080")
        buf.write("\5\f\7\2\u0080\u0081\7\63\2\2\u0081\u0084\3\2\2\2\u0082")
        buf.write("\u0084\5\32\16\2\u0083\177\3\2\2\2\u0083\u0082\3\2\2\2")
        buf.write("\u0084\13\3\2\2\2\u0085\u0088\5\16\b\2\u0086\u0088\5\20")
        buf.write("\t\2\u0087\u0085\3\2\2\2\u0087\u0086\3\2\2\2\u0088\r\3")
        buf.write("\2\2\2\u0089\u008c\7\22\2\2\u008a\u008d\5\22\n\2\u008b")
        buf.write("\u008d\5\24\13\2\u008c\u008a\3\2\2\2\u008c\u008b\3\2\2")
        buf.write("\2\u008d\17\3\2\2\2\u008e\u0091\7\25\2\2\u008f\u0092\5")
        buf.write("\22\n\2\u0090\u0092\5\24\13\2\u0091\u008f\3\2\2\2\u0091")
        buf.write("\u0090\3\2\2\2\u0092\21\3\2\2\2\u0093\u0094\5D#\2\u0094")
        buf.write("\u0095\7\62\2\2\u0095\u0096\5\22\n\2\u0096\u0097\7\62")
        buf.write("\2\2\u0097\u0098\5*\26\2\u0098\u00a0\3\2\2\2\u0099\u009a")
        buf.write("\5D#\2\u009a\u009b\7\64\2\2\u009b\u009c\5\26\f\2\u009c")
        buf.write("\u009d\7&\2\2\u009d\u009e\5*\26\2\u009e\u00a0\3\2\2\2")
        buf.write("\u009f\u0093\3\2\2\2\u009f\u0099\3\2\2\2\u00a0\23\3\2")
        buf.write("\2\2\u00a1\u00a2\5D#\2\u00a2\u00a3\7\62\2\2\u00a3\u00a4")
        buf.write("\5\24\13\2\u00a4\u00aa\3\2\2\2\u00a5\u00a6\5D#\2\u00a6")
        buf.write("\u00a7\7\64\2\2\u00a7\u00a8\5\26\f\2\u00a8\u00aa\3\2\2")
        buf.write("\2\u00a9\u00a1\3\2\2\2\u00a9\u00a5\3\2\2\2\u00aa\25\3")
        buf.write("\2\2\2\u00ab\u00ac\7-\2\2\u00ac\u00ad\7\65\2\2\u00ad\u00af")
        buf.write("\7.\2\2\u00ae\u00ab\3\2\2\2\u00ae\u00af\3\2\2\2\u00af")
        buf.write("\u00b0\3\2\2\2\u00b0\u00b1\5\30\r\2\u00b1\27\3\2\2\2\u00b2")
        buf.write("\u00b3\t\2\2\2\u00b3\31\3\2\2\2\u00b4\u00b5\7\26\2\2\u00b5")
        buf.write("\u00b6\5D#\2\u00b6\u00b8\7+\2\2\u00b7\u00b9\5\34\17\2")
        buf.write("\u00b8\u00b7\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\3")
        buf.write("\2\2\2\u00ba\u00bb\7,\2\2\u00bb\u00be\7\64\2\2\u00bc\u00bf")
        buf.write("\5\26\f\2\u00bd\u00bf\7\24\2\2\u00be\u00bc\3\2\2\2\u00be")
        buf.write("\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c1\5\"\22")
        buf.write("\2\u00c1\u00cb\3\2\2\2\u00c2\u00c3\7\26\2\2\u00c3\u00c4")
        buf.write("\7\21\2\2\u00c4\u00c6\7+\2\2\u00c5\u00c7\5\34\17\2\u00c6")
        buf.write("\u00c5\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8\3\2\2\2")
        buf.write("\u00c8\u00c9\7,\2\2\u00c9\u00cb\5\"\22\2\u00ca\u00b4\3")
        buf.write("\2\2\2\u00ca\u00c2\3\2\2\2\u00cb\33\3\2\2\2\u00cc\u00cd")
        buf.write("\5\36\20\2\u00cd\u00ce\7\62\2\2\u00ce\u00cf\5\34\17\2")
        buf.write("\u00cf\u00d2\3\2\2\2\u00d0\u00d2\5\36\20\2\u00d1\u00cc")
        buf.write("\3\2\2\2\u00d1\u00d0\3\2\2\2\u00d2\35\3\2\2\2\u00d3\u00d4")
        buf.write("\5 \21\2\u00d4\u00d5\7\64\2\2\u00d5\u00d6\5\26\f\2\u00d6")
        buf.write("\37\3\2\2\2\u00d7\u00d8\5D#\2\u00d8\u00d9\7\62\2\2\u00d9")
        buf.write("\u00da\5 \21\2\u00da\u00dd\3\2\2\2\u00db\u00dd\5D#\2\u00dc")
        buf.write("\u00d7\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd!\3\2\2\2\u00de")
        buf.write("\u00df\7/\2\2\u00df\u00e0\5P)\2\u00e0\u00e1\7\60\2\2\u00e1")
        buf.write("#\3\2\2\2\u00e2\u00e3\7+\2\2\u00e3\u00e4\5&\24\2\u00e4")
        buf.write("\u00e5\7,\2\2\u00e5%\3\2\2\2\u00e6\u00e9\5(\25\2\u00e7")
        buf.write("\u00e9\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e8\u00e7\3\2\2\2")
        buf.write("\u00e9\'\3\2\2\2\u00ea\u00eb\5*\26\2\u00eb\u00ec\7\62")
        buf.write("\2\2\u00ec\u00ed\5(\25\2\u00ed\u00f0\3\2\2\2\u00ee\u00f0")
        buf.write("\5*\26\2\u00ef\u00ea\3\2\2\2\u00ef\u00ee\3\2\2\2\u00f0")
        buf.write(")\3\2\2\2\u00f1\u00f2\5,\27\2\u00f2\u00f3\7(\2\2\u00f3")
        buf.write("\u00f4\5,\27\2\u00f4\u00f7\3\2\2\2\u00f5\u00f7\5,\27\2")
        buf.write("\u00f6\u00f1\3\2\2\2\u00f6\u00f5\3\2\2\2\u00f7+\3\2\2")
        buf.write("\2\u00f8\u00f9\5.\30\2\u00f9\u00fa\t\3\2\2\u00fa\u00fb")
        buf.write("\5.\30\2\u00fb\u00fe\3\2\2\2\u00fc\u00fe\5.\30\2\u00fd")
        buf.write("\u00f8\3\2\2\2\u00fd\u00fc\3\2\2\2\u00fe-\3\2\2\2\u00ff")
        buf.write("\u0100\b\30\1\2\u0100\u0101\5\60\31\2\u0101\u0107\3\2")
        buf.write("\2\2\u0102\u0103\f\4\2\2\u0103\u0104\t\4\2\2\u0104\u0106")
        buf.write("\5\60\31\2\u0105\u0102\3\2\2\2\u0106\u0109\3\2\2\2\u0107")
        buf.write("\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108/\3\2\2\2\u0109")
        buf.write("\u0107\3\2\2\2\u010a\u010b\b\31\1\2\u010b\u010c\5\62\32")
        buf.write("\2\u010c\u0112\3\2\2\2\u010d\u010e\f\4\2\2\u010e\u010f")
        buf.write("\t\5\2\2\u010f\u0111\5\62\32\2\u0110\u010d\3\2\2\2\u0111")
        buf.write("\u0114\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0113\3\2\2\2")
        buf.write("\u0113\61\3\2\2\2\u0114\u0112\3\2\2\2\u0115\u0116\b\32")
        buf.write("\1\2\u0116\u0117\5\64\33\2\u0117\u011d\3\2\2\2\u0118\u0119")
        buf.write("\f\4\2\2\u0119\u011a\t\6\2\2\u011a\u011c\5\64\33\2\u011b")
        buf.write("\u0118\3\2\2\2\u011c\u011f\3\2\2\2\u011d\u011b\3\2\2\2")
        buf.write("\u011d\u011e\3\2\2\2\u011e\63\3\2\2\2\u011f\u011d\3\2")
        buf.write("\2\2\u0120\u0121\7\35\2\2\u0121\u0124\5\64\33\2\u0122")
        buf.write("\u0124\5\66\34\2\u0123\u0120\3\2\2\2\u0123\u0122\3\2\2")
        buf.write("\2\u0124\65\3\2\2\2\u0125\u0126\7\30\2\2\u0126\u0129\5")
        buf.write("\66\34\2\u0127\u0129\58\35\2\u0128\u0125\3\2\2\2\u0128")
        buf.write("\u0127\3\2\2\2\u0129\67\3\2\2\2\u012a\u012b\5:\36\2\u012b")
        buf.write("\u012c\7-\2\2\u012c\u012d\5*\26\2\u012d\u012e\7.\2\2\u012e")
        buf.write("\u0131\3\2\2\2\u012f\u0131\5:\36\2\u0130\u012a\3\2\2\2")
        buf.write("\u0130\u012f\3\2\2\2\u01319\3\2\2\2\u0132\u0133\b\36\1")
        buf.write("\2\u0133\u0134\5<\37\2\u0134\u0143\3\2\2\2\u0135\u013a")
        buf.write("\f\4\2\2\u0136\u0137\7-\2\2\u0137\u0138\5*\26\2\u0138")
        buf.write("\u0139\7.\2\2\u0139\u013b\3\2\2\2\u013a\u0136\3\2\2\2")
        buf.write("\u013a\u013b\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013d\7")
        buf.write("\61\2\2\u013d\u013f\7:\2\2\u013e\u0140\5$\23\2\u013f\u013e")
        buf.write("\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u0142\3\2\2\2\u0141")
        buf.write("\u0135\3\2\2\2\u0142\u0145\3\2\2\2\u0143\u0141\3\2\2\2")
        buf.write("\u0143\u0144\3\2\2\2\u0144;\3\2\2\2\u0145\u0143\3\2\2")
        buf.write("\2\u0146\u0149\5B\"\2\u0147\u0149\5> \2\u0148\u0146\3")
        buf.write("\2\2\2\u0148\u0147\3\2\2\2\u0149=\3\2\2\2\u014a\u014b")
        buf.write("\7*\2\2\u014b\u014c\7:\2\2\u014c\u014f\5$\23\2\u014d\u014f")
        buf.write("\5@!\2\u014e\u014a\3\2\2\2\u014e\u014d\3\2\2\2\u014f?")
        buf.write("\3\2\2\2\u0150\u0151\7+\2\2\u0151\u0152\5*\26\2\u0152")
        buf.write("\u0153\7,\2\2\u0153\u0156\3\2\2\2\u0154\u0156\5F$\2\u0155")
        buf.write("\u0150\3\2\2\2\u0155\u0154\3\2\2\2\u0156A\3\2\2\2\u0157")
        buf.write("\u0158\7:\2\2\u0158\u015a\7\61\2\2\u0159\u0157\3\2\2\2")
        buf.write("\u0159\u015a\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u015d\7")
        buf.write(";\2\2\u015c\u015e\5$\23\2\u015d\u015c\3\2\2\2\u015d\u015e")
        buf.write("\3\2\2\2\u015eC\3\2\2\2\u015f\u0160\t\7\2\2\u0160E\3\2")
        buf.write("\2\2\u0161\u016a\7\65\2\2\u0162\u016a\7\66\2\2\u0163\u016a")
        buf.write("\5H%\2\u0164\u016a\7\67\2\2\u0165\u016a\5J&\2\u0166\u016a")
        buf.write("\7\17\2\2\u0167\u016a\7\23\2\2\u0168\u016a\5D#\2\u0169")
        buf.write("\u0161\3\2\2\2\u0169\u0162\3\2\2\2\u0169\u0163\3\2\2\2")
        buf.write("\u0169\u0164\3\2\2\2\u0169\u0165\3\2\2\2\u0169\u0166\3")
        buf.write("\2\2\2\u0169\u0167\3\2\2\2\u0169\u0168\3\2\2\2\u016aG")
        buf.write("\3\2\2\2\u016b\u016c\t\b\2\2\u016cI\3\2\2\2\u016d\u016e")
        buf.write("\7-\2\2\u016e\u016f\5N(\2\u016f\u0170\7.\2\2\u0170K\3")
        buf.write("\2\2\2\u0171\u0174\5N(\2\u0172\u0174\3\2\2\2\u0173\u0171")
        buf.write("\3\2\2\2\u0173\u0172\3\2\2\2\u0174M\3\2\2\2\u0175\u0176")
        buf.write("\5F$\2\u0176\u0177\7\62\2\2\u0177\u0178\5N(\2\u0178\u017b")
        buf.write("\3\2\2\2\u0179\u017b\5F$\2\u017a\u0175\3\2\2\2\u017a\u0179")
        buf.write("\3\2\2\2\u017bO\3\2\2\2\u017c\u017d\5R*\2\u017d\u017e")
        buf.write("\5P)\2\u017e\u0181\3\2\2\2\u017f\u0181\3\2\2\2\u0180\u017c")
        buf.write("\3\2\2\2\u0180\u017f\3\2\2\2\u0181Q\3\2\2\2\u0182\u0184")
        buf.write("\7\5\2\2\u0183\u0185\5\"\22\2\u0184\u0183\3\2\2\2\u0184")
        buf.write("\u0185\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0187\5*\26\2")
        buf.write("\u0187\u018a\5\"\22\2\u0188\u0189\7\6\2\2\u0189\u018b")
        buf.write("\5\"\22\2\u018a\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018b")
        buf.write("\u01aa\3\2\2\2\u018c\u018d\7\7\2\2\u018d\u018e\5T+\2\u018e")
        buf.write("\u018f\7\63\2\2\u018f\u0190\5*\26\2\u0190\u0191\7\63\2")
        buf.write("\2\u0191\u0192\5T+\2\u0192\u0193\5\"\22\2\u0193\u01aa")
        buf.write("\3\2\2\2\u0194\u0196\t\t\2\2\u0195\u0194\3\2\2\2\u0195")
        buf.write("\u0196\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0198\5T+\2\u0198")
        buf.write("\u0199\7\63\2\2\u0199\u01aa\3\2\2\2\u019a\u019b\7\3\2")
        buf.write("\2\u019b\u01aa\7\63\2\2\u019c\u019d\7\4\2\2\u019d\u01aa")
        buf.write("\7\63\2\2\u019e\u01a0\7\16\2\2\u019f\u01a1\5*\26\2\u01a0")
        buf.write("\u019f\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a2\3\2\2\2")
        buf.write("\u01a2\u01aa\7\63\2\2\u01a3\u01a4\5^\60\2\u01a4\u01a5")
        buf.write("\7\63\2\2\u01a5\u01aa\3\2\2\2\u01a6\u01a7\5d\63\2\u01a7")
        buf.write("\u01a8\7\63\2\2\u01a8\u01aa\3\2\2\2\u01a9\u0182\3\2\2")
        buf.write("\2\u01a9\u018c\3\2\2\2\u01a9\u0195\3\2\2\2\u01a9\u019a")
        buf.write("\3\2\2\2\u01a9\u019c\3\2\2\2\u01a9\u019e\3\2\2\2\u01a9")
        buf.write("\u01a3\3\2\2\2\u01a9\u01a6\3\2\2\2\u01aaS\3\2\2\2\u01ab")
        buf.write("\u01ac\5V,\2\u01ac\u01ad\7\'\2\2\u01ad\u01ae\5*\26\2\u01ae")
        buf.write("U\3\2\2\2\u01af\u01b0\b,\1\2\u01b0\u01b1\5X-\2\u01b1\u01b9")
        buf.write("\3\2\2\2\u01b2\u01b3\f\4\2\2\u01b3\u01b4\7-\2\2\u01b4")
        buf.write("\u01b5\5*\26\2\u01b5\u01b6\7.\2\2\u01b6\u01b8\3\2\2\2")
        buf.write("\u01b7\u01b2\3\2\2\2\u01b8\u01bb\3\2\2\2\u01b9\u01b7\3")
        buf.write("\2\2\2\u01b9\u01ba\3\2\2\2\u01baW\3\2\2\2\u01bb\u01b9")
        buf.write("\3\2\2\2\u01bc\u01bd\b-\1\2\u01bd\u01be\5Z.\2\u01be\u01cd")
        buf.write("\3\2\2\2\u01bf\u01c4\f\4\2\2\u01c0\u01c1\7-\2\2\u01c1")
        buf.write("\u01c2\5*\26\2\u01c2\u01c3\7.\2\2\u01c3\u01c5\3\2\2\2")
        buf.write("\u01c4\u01c0\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c6\3")
        buf.write("\2\2\2\u01c6\u01c7\7\61\2\2\u01c7\u01c9\7:\2\2\u01c8\u01ca")
        buf.write("\5$\23\2\u01c9\u01c8\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca")
        buf.write("\u01cc\3\2\2\2\u01cb\u01bf\3\2\2\2\u01cc\u01cf\3\2\2\2")
        buf.write("\u01cd\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ceY\3\2\2")
        buf.write("\2\u01cf\u01cd\3\2\2\2\u01d0\u01d3\5B\"\2\u01d1\u01d3")
        buf.write("\5\\/\2\u01d2\u01d0\3\2\2\2\u01d2\u01d1\3\2\2\2\u01d3")
        buf.write("[\3\2\2\2\u01d4\u01d5\7+\2\2\u01d5\u01d6\5V,\2\u01d6\u01d7")
        buf.write("\7,\2\2\u01d7\u01db\3\2\2\2\u01d8\u01db\7\23\2\2\u01d9")
        buf.write("\u01db\5D#\2\u01da\u01d4\3\2\2\2\u01da\u01d8\3\2\2\2\u01da")
        buf.write("\u01d9\3\2\2\2\u01db]\3\2\2\2\u01dc\u01df\5`\61\2\u01dd")
        buf.write("\u01df\5b\62\2\u01de\u01dc\3\2\2\2\u01de\u01dd\3\2\2\2")
        buf.write("\u01df_\3\2\2\2\u01e0\u01e5\5:\36\2\u01e1\u01e2\7-\2\2")
        buf.write("\u01e2\u01e3\5*\26\2\u01e3\u01e4\7.\2\2\u01e4\u01e6\3")
        buf.write("\2\2\2\u01e5\u01e1\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e7")
        buf.write("\3\2\2\2\u01e7\u01e8\7\61\2\2\u01e8\u01e9\7:\2\2\u01e9")
        buf.write("\u01ea\5$\23\2\u01eaa\3\2\2\2\u01eb\u01ec\7:\2\2\u01ec")
        buf.write("\u01ee\7\61\2\2\u01ed\u01eb\3\2\2\2\u01ed\u01ee\3\2\2")
        buf.write("\2\u01ee\u01ef\3\2\2\2\u01ef\u01f0\7;\2\2\u01f0\u01f1")
        buf.write("\5$\23\2\u01f1c\3\2\2\2\u01f2\u01f5\5\16\b\2\u01f3\u01f5")
        buf.write("\5\20\t\2\u01f4\u01f2\3\2\2\2\u01f4\u01f3\3\2\2\2\u01f5")
        buf.write("e\3\2\2\2\67mr}\u0083\u0087\u008c\u0091\u009f\u00a9\u00ae")
        buf.write("\u00b8\u00be\u00c6\u00ca\u00d1\u00dc\u00e8\u00ef\u00f6")
        buf.write("\u00fd\u0107\u0112\u011d\u0123\u0128\u0130\u013a\u013f")
        buf.write("\u0143\u0148\u014e\u0155\u0159\u015d\u0169\u0173\u017a")
        buf.write("\u0180\u0184\u018a\u0195\u01a0\u01a9\u01b9\u01c4\u01c9")
        buf.write("\u01cd\u01d2\u01da\u01de\u01e5\u01ed\u01f4")
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
    RULE_statpart = 32
    RULE_identifier = 33
    RULE_lit = 34
    RULE_boollit = 35
    RULE_arraylit = 36
    RULE_litlist = 37
    RULE_litprime = 38
    RULE_stmtlist = 39
    RULE_stmt = 40
    RULE_stmtassign = 41
    RULE_lhs = 42
    RULE_lhsinst = 43
    RULE_lhsstat = 44
    RULE_lhsparen = 45
    RULE_stmtinvoc = 46
    RULE_stmtinvocinst = 47
    RULE_stmtinvocstat = 48
    RULE_stmtdecl = 49

    ruleNames =  [ "program", "classdecllist", "classdecl", "memberlist", 
                   "member", "attribute", "vardecl", "constdecl", "attlistdecl", 
                   "attlistnodecl", "atttyp", "typ", "method", "paramlist", 
                   "params", "param", "blockstmt", "parenexpr", "exprlist", 
                   "exprprime", "exprstr", "exprrel", "exprlog", "expradd", 
                   "exprmul", "exprnot", "exprsign", "exprindex", "exprinst", 
                   "exprstat", "exprobj", "exprparen", "statpart", "identifier", 
                   "lit", "boollit", "arraylit", "litlist", "litprime", 
                   "stmtlist", "stmt", "stmtassign", "lhs", "lhsinst", "lhsstat", 
                   "lhsparen", "stmtinvoc", "stmtinvocinst", "stmtinvocstat", 
                   "stmtdecl" ]

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
            self.state = 100
            self.classdecllist()
            self.state = 101
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
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.classdecl()
                self.state = 104
                self.classdecllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
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
            self.state = 109
            self.match(CSlangParser.CLASS)
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 110
                self.match(CSlangParser.ID)
                self.state = 111
                self.match(CSlangParser.LARROW)


            self.state = 114
            self.match(CSlangParser.ID)
            self.state = 115
            self.match(CSlangParser.LBR)
            self.state = 116
            self.memberlist()
            self.state = 117
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
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST, CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.member()
                self.state = 120
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
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.attribute()
                self.state = 126
                self.match(CSlangParser.SM)
                pass
            elif token in [CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
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
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.vardecl()
                pass
            elif token in [CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
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
            self.state = 135
            self.match(CSlangParser.VAR)
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 136
                self.attlistdecl()
                pass

            elif la_ == 2:
                self.state = 137
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
            self.state = 140
            self.match(CSlangParser.CONST)
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 141
                self.attlistdecl()
                pass

            elif la_ == 2:
                self.state = 142
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
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.identifier()
                self.state = 146
                self.match(CSlangParser.CM)
                self.state = 147
                self.attlistdecl()
                self.state = 148
                self.match(CSlangParser.CM)
                self.state = 149
                self.exprstr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.identifier()
                self.state = 152
                self.match(CSlangParser.COL)
                self.state = 153
                self.atttyp()
                self.state = 154
                self.match(CSlangParser.DECLARE)
                self.state = 155
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
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.identifier()
                self.state = 160
                self.match(CSlangParser.CM)
                self.state = 161
                self.attlistnodecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.identifier()
                self.state = 164
                self.match(CSlangParser.COL)
                self.state = 165
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
        self.enterRule(localctx, 20, self.RULE_atttyp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LBK:
                self.state = 169
                self.match(CSlangParser.LBK)
                self.state = 170
                self.match(CSlangParser.INTLIT)
                self.state = 171
                self.match(CSlangParser.RBK)


            self.state = 174
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

        def blockstmt(self):
            return self.getTypedRuleContext(CSlangParser.BlockstmtContext,0)


        def atttyp(self):
            return self.getTypedRuleContext(CSlangParser.AtttypContext,0)


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
        self.enterRule(localctx, 24, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.state = 200
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
                self.state = 188
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.LBK, CSlangParser.ID]:
                    self.state = 186
                    self.atttyp()
                    pass
                elif token in [CSlangParser.VOID]:
                    self.state = 187
                    self.match(CSlangParser.VOID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 190
                self.blockstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.match(CSlangParser.FUNC)
                self.state = 193
                self.match(CSlangParser.CONSTRUCTOR)
                self.state = 194
                self.match(CSlangParser.LPN)
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ID or _la==CSlangParser.ATID:
                    self.state = 195
                    self.paramlist()


                self.state = 198
                self.match(CSlangParser.RPN)
                self.state = 199
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
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.params()
                self.state = 203
                self.match(CSlangParser.CM)
                self.state = 204
                self.paramlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
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
            self.state = 209
            self.param()
            self.state = 210
            self.match(CSlangParser.COL)
            self.state = 211
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
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.identifier()
                self.state = 214
                self.match(CSlangParser.CM)
                self.state = 215
                self.param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
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
            self.state = 220
            self.match(CSlangParser.LBR)
            self.state = 221
            self.stmtlist()
            self.state = 222
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
            self.state = 224
            self.match(CSlangParser.LPN)
            self.state = 225
            self.exprlist()
            self.state = 226
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
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.SUB, CSlangParser.NEG, CSlangParser.NEW, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRLIT, CSlangParser.ID, CSlangParser.ATID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
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
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.exprstr()
                self.state = 233
                self.match(CSlangParser.CM)
                self.state = 234
                self.exprprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
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
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.exprrel()
                self.state = 240
                self.match(CSlangParser.CONCATE)
                self.state = 241
                self.exprrel()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
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
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.exprlog(0)
                self.state = 247
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.EQ) | (1 << CSlangParser.NEQ) | (1 << CSlangParser.LT) | (1 << CSlangParser.LTEQ) | (1 << CSlangParser.GT) | (1 << CSlangParser.GTEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 248
                self.exprlog(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
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
            self.state = 254
            self.expradd(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 261
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprlogContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprlog)
                    self.state = 256
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 257
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.AND or _la==CSlangParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 258
                    self.expradd(0) 
                self.state = 263
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
            self.state = 265
            self.exprmul(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 272
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExpraddContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expradd)
                    self.state = 267
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 268
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.ADD or _la==CSlangParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 269
                    self.exprmul(0) 
                self.state = 274
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
            self.state = 276
            self.exprnot()
            self._ctx.stop = self._input.LT(-1)
            self.state = 283
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprmulContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprmul)
                    self.state = 278
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 279
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.MUL) | (1 << CSlangParser.DIVFLOAT) | (1 << CSlangParser.DIVINT) | (1 << CSlangParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 280
                    self.exprnot() 
                self.state = 285
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
            self.state = 289
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.match(CSlangParser.NEG)
                self.state = 287
                self.exprnot()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.SUB, CSlangParser.NEW, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRLIT, CSlangParser.ID, CSlangParser.ATID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
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
            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.match(CSlangParser.SUB)
                self.state = 292
                self.exprsign()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRLIT, CSlangParser.ID, CSlangParser.ATID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
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
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.exprinst(0)
                self.state = 297
                self.match(CSlangParser.LBK)
                self.state = 298
                self.exprstr()
                self.state = 299
                self.match(CSlangParser.RBK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
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
            self.state = 305
            self.exprstat()
            self._ctx.stop = self._input.LT(-1)
            self.state = 321
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprinstContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprinst)
                    self.state = 307
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 312
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==CSlangParser.LBK:
                        self.state = 308
                        self.match(CSlangParser.LBK)
                        self.state = 309
                        self.exprstr()
                        self.state = 310
                        self.match(CSlangParser.RBK)


                    self.state = 314
                    self.match(CSlangParser.DOT)
                    self.state = 315
                    self.match(CSlangParser.ID)
                    self.state = 317
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        self.state = 316
                        self.parenexpr()

             
                self.state = 323
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

        def statpart(self):
            return self.getTypedRuleContext(CSlangParser.StatpartContext,0)


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
        try:
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self.statpart()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
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
            self.state = 332
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.match(CSlangParser.NEW)
                self.state = 329
                self.match(CSlangParser.ID)
                self.state = 330
                self.parenexpr()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRLIT, CSlangParser.ID, CSlangParser.ATID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
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
            self.state = 339
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LPN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.match(CSlangParser.LPN)
                self.state = 335
                self.exprstr()
                self.state = 336
                self.match(CSlangParser.RPN)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.LBK, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRLIT, CSlangParser.ID, CSlangParser.ATID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
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


    class StatpartContext(ParserRuleContext):
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


        def getRuleIndex(self):
            return CSlangParser.RULE_statpart

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatpart" ):
                return visitor.visitStatpart(self)
            else:
                return visitor.visitChildren(self)




    def statpart(self):

        localctx = CSlangParser.StatpartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_statpart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 341
                self.match(CSlangParser.ID)
                self.state = 342
                self.match(CSlangParser.DOT)


            self.state = 345
            self.match(CSlangParser.ATID)
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 346
                self.parenexpr()


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
        self.enterRule(localctx, 66, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
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
        self.enterRule(localctx, 68, self.RULE_lit)
        try:
            self.state = 359
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.match(CSlangParser.INTLIT)
                pass
            elif token in [CSlangParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
                self.match(CSlangParser.FLOATLIT)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 353
                self.boollit()
                pass
            elif token in [CSlangParser.STRLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 354
                self.match(CSlangParser.STRLIT)
                pass
            elif token in [CSlangParser.LBK]:
                self.enterOuterAlt(localctx, 5)
                self.state = 355
                self.arraylit()
                pass
            elif token in [CSlangParser.NULL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 356
                self.match(CSlangParser.NULL)
                pass
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 7)
                self.state = 357
                self.match(CSlangParser.SELF)
                pass
            elif token in [CSlangParser.ID, CSlangParser.ATID]:
                self.enterOuterAlt(localctx, 8)
                self.state = 358
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
        self.enterRule(localctx, 70, self.RULE_boollit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
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
        self.enterRule(localctx, 72, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(CSlangParser.LBK)
            self.state = 364
            self.litprime()
            self.state = 365
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
        self.enterRule(localctx, 74, self.RULE_litlist)
        try:
            self.state = 369
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.LBK, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRLIT, CSlangParser.ID, CSlangParser.ATID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
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
        self.enterRule(localctx, 76, self.RULE_litprime)
        try:
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                self.lit()
                self.state = 372
                self.match(CSlangParser.CM)
                self.state = 373
                self.litprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
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
        self.enterRule(localctx, 78, self.RULE_stmtlist)
        try:
            self.state = 382
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.BREAK, CSlangParser.CONTINUE, CSlangParser.IF, CSlangParser.FOR, CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.RETURN, CSlangParser.NULL, CSlangParser.VAR, CSlangParser.SELF, CSlangParser.CONST, CSlangParser.NEW, CSlangParser.LPN, CSlangParser.LBK, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRLIT, CSlangParser.ID, CSlangParser.ATID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
                self.stmt()
                self.state = 379
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
        self.enterRule(localctx, 80, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 423
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.match(CSlangParser.IF)
                self.state = 386
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.LBR:
                    self.state = 385
                    self.blockstmt()


                self.state = 388
                self.exprstr()
                self.state = 389
                self.blockstmt()
                self.state = 392
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ELSE:
                    self.state = 390
                    self.match(CSlangParser.ELSE)
                    self.state = 391
                    self.blockstmt()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.match(CSlangParser.FOR)
                self.state = 395
                self.stmtassign()
                self.state = 396
                self.match(CSlangParser.SM)
                self.state = 397
                self.exprstr()
                self.state = 398
                self.match(CSlangParser.SM)
                self.state = 399
                self.stmtassign()
                self.state = 400
                self.blockstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 403
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.VAR or _la==CSlangParser.CONST:
                    self.state = 402
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 405
                self.stmtassign()
                self.state = 406
                self.match(CSlangParser.SM)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 408
                self.match(CSlangParser.BREAK)
                self.state = 409
                self.match(CSlangParser.SM)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 410
                self.match(CSlangParser.CONTINUE)
                self.state = 411
                self.match(CSlangParser.SM)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 412
                self.match(CSlangParser.RETURN)
                self.state = 414
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NEG) | (1 << CSlangParser.NEW) | (1 << CSlangParser.LPN) | (1 << CSlangParser.LBK) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.STRLIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.ATID))) != 0):
                    self.state = 413
                    self.exprstr()


                self.state = 416
                self.match(CSlangParser.SM)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 417
                self.stmtinvoc()
                self.state = 418
                self.match(CSlangParser.SM)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 420
                self.stmtdecl()
                self.state = 421
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
            self.state = 425
            self.lhs(0)
            self.state = 426
            self.match(CSlangParser.ASSIGN)
            self.state = 427
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
            self.state = 430
            self.lhsinst(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 439
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.LhsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                    self.state = 432
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 433
                    self.match(CSlangParser.LBK)
                    self.state = 434
                    self.exprstr()
                    self.state = 435
                    self.match(CSlangParser.RBK) 
                self.state = 441
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

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

        def LBK(self):
            return self.getToken(CSlangParser.LBK, 0)

        def exprstr(self):
            return self.getTypedRuleContext(CSlangParser.ExprstrContext,0)


        def RBK(self):
            return self.getToken(CSlangParser.RBK, 0)

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
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_lhsinst, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.lhsstat()
            self._ctx.stop = self._input.LT(-1)
            self.state = 459
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.LhsinstContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lhsinst)
                    self.state = 445
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 450
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==CSlangParser.LBK:
                        self.state = 446
                        self.match(CSlangParser.LBK)
                        self.state = 447
                        self.exprstr()
                        self.state = 448
                        self.match(CSlangParser.RBK)


                    self.state = 452
                    self.match(CSlangParser.DOT)
                    self.state = 453
                    self.match(CSlangParser.ID)
                    self.state = 455
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                    if la_ == 1:
                        self.state = 454
                        self.parenexpr()

             
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


    class LhsstatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statpart(self):
            return self.getTypedRuleContext(CSlangParser.StatpartContext,0)


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
        try:
            self.state = 464
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.statpart()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
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
        self.enterRule(localctx, 90, self.RULE_lhsparen)
        try:
            self.state = 472
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LPN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 466
                self.match(CSlangParser.LPN)
                self.state = 467
                self.lhs(0)
                self.state = 468
                self.match(CSlangParser.RPN)
                pass
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 470
                self.match(CSlangParser.SELF)
                pass
            elif token in [CSlangParser.ID, CSlangParser.ATID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 471
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
        self.enterRule(localctx, 92, self.RULE_stmtinvoc)
        try:
            self.state = 476
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 474
                self.stmtinvocinst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 475
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
        self.enterRule(localctx, 94, self.RULE_stmtinvocinst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.exprinst(0)
            self.state = 483
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LBK:
                self.state = 479
                self.match(CSlangParser.LBK)
                self.state = 480
                self.exprstr()
                self.state = 481
                self.match(CSlangParser.RBK)


            self.state = 485
            self.match(CSlangParser.DOT)
            self.state = 486
            self.match(CSlangParser.ID)
            self.state = 487
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
        self.enterRule(localctx, 96, self.RULE_stmtinvocstat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 489
                self.match(CSlangParser.ID)
                self.state = 490
                self.match(CSlangParser.DOT)


            self.state = 493
            self.match(CSlangParser.ATID)
            self.state = 494
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
        self.enterRule(localctx, 98, self.RULE_stmtdecl)
        try:
            self.state = 498
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 496
                self.vardecl()
                pass
            elif token in [CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 497
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
                return self.precpred(self._ctx, 2)
         

    def lhs_sempred(self, localctx:LhsContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def lhsinst_sempred(self, localctx:LhsinstContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




