# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("\u00b0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\3\6\3")
        buf.write("\33\n\3\r\3\16\3\34\3\3\3\3\3\4\3\4\3\4\3\4\7\4%\n\4\f")
        buf.write("\4\16\4(\13\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\7\5")
        buf.write("\63\n\5\f\5\16\5\66\13\5\3\5\3\5\3\6\3\6\7\6<\n\6\f\6")
        buf.write("\16\6?\13\6\3\7\3\7\6\7C\n\7\r\7\16\7D\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5")
        buf.write("\b\u00a9\n\b\3\t\3\t\3\n\3\n\3\13\3\13\3&\2\f\3\2\5\3")
        buf.write("\7\4\t\5\13\6\r\7\17\b\21\t\23\n\25\13\3\2\6\6\2\62;C")
        buf.write("\\aac|\5\2\n\f\16\17\"\"\4\2\f\f\17\17\5\2C\\aac|\2\u00c7")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\3\27\3\2\2\2\5\32\3\2\2\2\7 \3\2\2\2\t.\3\2\2\2")
        buf.write("\139\3\2\2\2\r@\3\2\2\2\17\u00a8\3\2\2\2\21\u00aa\3\2")
        buf.write("\2\2\23\u00ac\3\2\2\2\25\u00ae\3\2\2\2\27\30\t\2\2\2\30")
        buf.write("\4\3\2\2\2\31\33\t\3\2\2\32\31\3\2\2\2\33\34\3\2\2\2\34")
        buf.write("\32\3\2\2\2\34\35\3\2\2\2\35\36\3\2\2\2\36\37\b\3\2\2")
        buf.write("\37\6\3\2\2\2 !\7\61\2\2!\"\7,\2\2\"&\3\2\2\2#%\13\2\2")
        buf.write("\2$#\3\2\2\2%(\3\2\2\2&\'\3\2\2\2&$\3\2\2\2\')\3\2\2\2")
        buf.write("(&\3\2\2\2)*\7,\2\2*+\7\61\2\2+,\3\2\2\2,-\b\4\2\2-\b")
        buf.write("\3\2\2\2./\7\61\2\2/\60\7\61\2\2\60\64\3\2\2\2\61\63\n")
        buf.write("\4\2\2\62\61\3\2\2\2\63\66\3\2\2\2\64\62\3\2\2\2\64\65")
        buf.write("\3\2\2\2\65\67\3\2\2\2\66\64\3\2\2\2\678\b\5\2\28\n\3")
        buf.write("\2\2\29=\t\5\2\2:<\5\3\2\2;:\3\2\2\2<?\3\2\2\2=;\3\2\2")
        buf.write("\2=>\3\2\2\2>\f\3\2\2\2?=\3\2\2\2@B\7B\2\2AC\5\3\2\2B")
        buf.write("A\3\2\2\2CD\3\2\2\2DB\3\2\2\2DE\3\2\2\2E\16\3\2\2\2FG")
        buf.write("\7d\2\2GH\7t\2\2HI\7g\2\2IJ\7c\2\2J\u00a9\7m\2\2KL\7e")
        buf.write("\2\2LM\7q\2\2MN\7p\2\2NO\7v\2\2OP\7k\2\2PQ\7p\2\2QR\7")
        buf.write("w\2\2R\u00a9\7g\2\2ST\7k\2\2T\u00a9\7h\2\2UV\7g\2\2VW")
        buf.write("\7n\2\2WX\7u\2\2X\u00a9\7g\2\2YZ\7h\2\2Z[\7q\2\2[\u00a9")
        buf.write("\7t\2\2\\]\7v\2\2]^\7t\2\2^_\7w\2\2_\u00a9\7g\2\2`a\7")
        buf.write("h\2\2ab\7c\2\2bc\7n\2\2cd\7u\2\2d\u00a9\7g\2\2ef\7k\2")
        buf.write("\2fg\7p\2\2g\u00a9\7v\2\2hi\7h\2\2ij\7n\2\2jk\7q\2\2k")
        buf.write("l\7c\2\2l\u00a9\7v\2\2mn\7d\2\2no\7q\2\2op\7q\2\2p\u00a9")
        buf.write("\7n\2\2qr\7u\2\2rs\7v\2\2st\7t\2\2tu\7k\2\2uv\7p\2\2v")
        buf.write("\u00a9\7i\2\2wx\7t\2\2xy\7g\2\2yz\7v\2\2z{\7w\2\2{|\7")
        buf.write("t\2\2|\u00a9\7p\2\2}~\7p\2\2~\177\7w\2\2\177\u0080\7n")
        buf.write("\2\2\u0080\u00a9\7n\2\2\u0081\u0082\7e\2\2\u0082\u0083")
        buf.write("\7n\2\2\u0083\u0084\7c\2\2\u0084\u0085\7u\2\2\u0085\u00a9")
        buf.write("\7u\2\2\u0086\u0087\7e\2\2\u0087\u0088\7q\2\2\u0088\u0089")
        buf.write("\7p\2\2\u0089\u008a\7u\2\2\u008a\u008b\7v\2\2\u008b\u008c")
        buf.write("\7t\2\2\u008c\u008d\7w\2\2\u008d\u008e\7e\2\2\u008e\u008f")
        buf.write("\7v\2\2\u008f\u0090\7q\2\2\u0090\u00a9\7t\2\2\u0091\u0092")
        buf.write("\7x\2\2\u0092\u0093\7c\2\2\u0093\u00a9\7t\2\2\u0094\u0095")
        buf.write("\7u\2\2\u0095\u0096\7g\2\2\u0096\u0097\7n\2\2\u0097\u00a9")
        buf.write("\7h\2\2\u0098\u0099\7p\2\2\u0099\u009a\7g\2\2\u009a\u00a9")
        buf.write("\7y\2\2\u009b\u009c\7x\2\2\u009c\u009d\7q\2\2\u009d\u009e")
        buf.write("\7k\2\2\u009e\u00a9\7f\2\2\u009f\u00a0\7e\2\2\u00a0\u00a1")
        buf.write("\7q\2\2\u00a1\u00a2\7p\2\2\u00a2\u00a3\7u\2\2\u00a3\u00a9")
        buf.write("\7v\2\2\u00a4\u00a5\7h\2\2\u00a5\u00a6\7w\2\2\u00a6\u00a7")
        buf.write("\7p\2\2\u00a7\u00a9\7e\2\2\u00a8F\3\2\2\2\u00a8K\3\2\2")
        buf.write("\2\u00a8S\3\2\2\2\u00a8U\3\2\2\2\u00a8Y\3\2\2\2\u00a8")
        buf.write("\\\3\2\2\2\u00a8`\3\2\2\2\u00a8e\3\2\2\2\u00a8h\3\2\2")
        buf.write("\2\u00a8m\3\2\2\2\u00a8q\3\2\2\2\u00a8w\3\2\2\2\u00a8")
        buf.write("}\3\2\2\2\u00a8\u0081\3\2\2\2\u00a8\u0086\3\2\2\2\u00a8")
        buf.write("\u0091\3\2\2\2\u00a8\u0094\3\2\2\2\u00a8\u0098\3\2\2\2")
        buf.write("\u00a8\u009b\3\2\2\2\u00a8\u009f\3\2\2\2\u00a8\u00a4\3")
        buf.write("\2\2\2\u00a9\20\3\2\2\2\u00aa\u00ab\13\2\2\2\u00ab\22")
        buf.write("\3\2\2\2\u00ac\u00ad\13\2\2\2\u00ad\24\3\2\2\2\u00ae\u00af")
        buf.write("\13\2\2\2\u00af\26\3\2\2\2\t\2\34&\64=D\u00a8\3\b\2\2")
        return buf.getvalue()


class CSlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    BLOCK_COMMENT = 2
    LINE_COMMENT = 3
    ID = 4
    AT_ID = 5
    KEYWORD = 6
    ERROR_CHAR = 7
    UNCLOSE_STRING = 8
    ILLEGAL_ESCAPE = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "WS", "BLOCK_COMMENT", "LINE_COMMENT", "ID", "AT_ID", "KEYWORD", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "CHAR", "WS", "BLOCK_COMMENT", "LINE_COMMENT", "ID", "AT_ID", 
                  "KEYWORD", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "CSlang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


