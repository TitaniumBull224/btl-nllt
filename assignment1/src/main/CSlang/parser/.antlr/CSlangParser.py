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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3;")
        buf.write("\b\4\2\t\2\3\2\3\2\3\2\3\2\2\2\3\2\2\2\2\6\2\4\3\2\2\2")
        buf.write("\4\5\7\6\2\2\5\6\7\2\2\3\6\3\3\2\2\2\2")
        return buf.getvalue()


class CSlangParser ( Parser ):

    grammarFileName = "CSlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'break'", "'continue'", 
                     "'if'", "'else'", "'for'", "'true'", "'false'", "'int'", 
                     "'float'", "'bool'", "'string'", "'return'", "'null'", 
                     "'class'", "'constructor'", "'var'", "'self'", "'void'", 
                     "'const'", "'func'", "'+'", "'-'", "'*'", "'/'", "'\\'", 
                     "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "':='", "'^'", "'new'", "'%'", 
                     "'('", "')'", "'['", "']'", "'.'", "','", "';'", "':'", 
                     "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "WS", "BLOCK_COMMENT", "LINE_COMMENT", 
                      "ID", "AT_ID", "BREAK", "CONTINUE", "IF", "ELSE", 
                      "FOR", "TRUE", "FALSE", "INT", "FLOAT", "BOOL", "STRING", 
                      "RETURN", "NULL", "CLASS", "CONSTRUCTOR", "VAR", "SELF", 
                      "VOID", "CONST", "FUNC", "PLUS", "MINUS", "STAR", 
                      "SLASH", "BACKSLASH", "BANG", "ANDAND", "OROR", "EQEQ", 
                      "EQ", "BANGEQ", "LT", "LTEQ", "GT", "GTEQ", "COLONEQ", 
                      "CARET", "NEW", "PERCENT", "LPAREN", "RPAREN", "LBRACK", 
                      "RBRACK", "DOT", "COMMA", "SEMI", "COLON", "LBRACE", 
                      "RBRACE", "ERROR_TOKEN", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    WS=1
    BLOCK_COMMENT=2
    LINE_COMMENT=3
    ID=4
    AT_ID=5
    BREAK=6
    CONTINUE=7
    IF=8
    ELSE=9
    FOR=10
    TRUE=11
    FALSE=12
    INT=13
    FLOAT=14
    BOOL=15
    STRING=16
    RETURN=17
    NULL=18
    CLASS=19
    CONSTRUCTOR=20
    VAR=21
    SELF=22
    VOID=23
    CONST=24
    FUNC=25
    PLUS=26
    MINUS=27
    STAR=28
    SLASH=29
    BACKSLASH=30
    BANG=31
    ANDAND=32
    OROR=33
    EQEQ=34
    EQ=35
    BANGEQ=36
    LT=37
    LTEQ=38
    GT=39
    GTEQ=40
    COLONEQ=41
    CARET=42
    NEW=43
    PERCENT=44
    LPAREN=45
    RPAREN=46
    LBRACK=47
    RBRACK=48
    DOT=49
    COMMA=50
    SEMI=51
    COLON=52
    LBRACE=53
    RBRACE=54
    ERROR_TOKEN=55
    UNCLOSE_STRING=56
    ILLEGAL_ESCAPE=57

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

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def EOF(self):
            return self.getToken(CSlangParser.EOF, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_program




    def program(self):

        localctx = CSlangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(CSlangParser.ID)
            self.state = 3
            self.match(CSlangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





