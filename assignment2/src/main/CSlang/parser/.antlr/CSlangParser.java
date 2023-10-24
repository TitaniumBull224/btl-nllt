// Generated from d:/Program/XAMPP/htdocs/btl-nllt/assignment2/src/main/CSlang/parser/CSlang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class CSlangParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		BREAK=1, CONTINUE=2, IF=3, ELSE=4, FOR=5, TRUE=6, FALSE=7, INT=8, FLOAT=9, 
		BOOL=10, STRING=11, RETURN=12, NULL=13, CLASS=14, CONSTRUCTOR=15, VAR=16, 
		SELF=17, VOID=18, CONST=19, FUNC=20, ADD=21, SUB=22, MUL=23, DIVFLOAT=24, 
		DIVINT=25, MOD=26, NEG=27, AND=28, OR=29, EQ=30, NEQ=31, LT=32, LTEQ=33, 
		GT=34, GTEQ=35, DECLARE=36, ASSIGN=37, CONCATE=38, LARROW=39, NEW=40, 
		LPN=41, RPN=42, LBK=43, RBK=44, LBR=45, RBR=46, DOT=47, CM=48, SM=49, 
		COL=50, INTLIT=51, FLOATLIT=52, STRLIT=53, BLOCK_COMMENT=54, LINE_COMMENT=55, 
		ID=56, ATID=57, WS=58, UNCLOSE_STRING=59, ILLEGAL_ESCAPE=60, ERROR_CHAR=61;
	public static final int
		RULE_program = 0, RULE_classdecllist = 1, RULE_classdecl = 2, RULE_memberlist = 3, 
		RULE_member = 4, RULE_attribute = 5, RULE_vardecl = 6, RULE_constdecl = 7, 
		RULE_attlistdecl = 8, RULE_attlistnodecl = 9, RULE_atttyp = 10, RULE_typ = 11, 
		RULE_method = 12, RULE_paramlist = 13, RULE_params = 14, RULE_param = 15, 
		RULE_blockstmt = 16, RULE_parenexpr = 17, RULE_exprlist = 18, RULE_exprprime = 19, 
		RULE_exprstr = 20, RULE_exprrel = 21, RULE_exprlog = 22, RULE_expradd = 23, 
		RULE_exprmul = 24, RULE_exprnot = 25, RULE_exprsign = 26, RULE_exprindex = 27, 
		RULE_exprinst = 28, RULE_exprstat = 29, RULE_exprobj = 30, RULE_exprparen = 31, 
		RULE_statpart = 32, RULE_identifier = 33, RULE_lit = 34, RULE_boollit = 35, 
		RULE_arraylit = 36, RULE_litlist = 37, RULE_litprime = 38, RULE_stmtlist = 39, 
		RULE_stmt = 40, RULE_stmtassign = 41, RULE_lhs = 42, RULE_lhsinst = 43, 
		RULE_lhsstat = 44, RULE_lhsparen = 45, RULE_stmtinvoc = 46, RULE_stmtinvocinst = 47, 
		RULE_stmtinvocstat = 48, RULE_stmtdecl = 49;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "classdecllist", "classdecl", "memberlist", "member", "attribute", 
			"vardecl", "constdecl", "attlistdecl", "attlistnodecl", "atttyp", "typ", 
			"method", "paramlist", "params", "param", "blockstmt", "parenexpr", "exprlist", 
			"exprprime", "exprstr", "exprrel", "exprlog", "expradd", "exprmul", "exprnot", 
			"exprsign", "exprindex", "exprinst", "exprstat", "exprobj", "exprparen", 
			"statpart", "identifier", "lit", "boollit", "arraylit", "litlist", "litprime", 
			"stmtlist", "stmt", "stmtassign", "lhs", "lhsinst", "lhsstat", "lhsparen", 
			"stmtinvoc", "stmtinvocinst", "stmtinvocstat", "stmtdecl"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'break'", "'continue'", "'if'", "'else'", "'for'", "'true'", "'false'", 
			"'int'", "'float'", "'bool'", "'string'", "'return'", "'null'", "'class'", 
			"'constructor'", "'var'", "'self'", "'void'", "'const'", "'func'", "'+'", 
			"'-'", "'*'", "'/'", "'\\'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", 
			"'<'", "'<='", "'>'", "'>='", "'='", "':='", "'^'", "'<-'", "'new'", 
			"'('", "')'", "'['", "']'", "'{'", "'}'", "'.'", "','", "';'", "':'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", "INT", 
			"FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", 
			"VAR", "SELF", "VOID", "CONST", "FUNC", "ADD", "SUB", "MUL", "DIVFLOAT", 
			"DIVINT", "MOD", "NEG", "AND", "OR", "EQ", "NEQ", "LT", "LTEQ", "GT", 
			"GTEQ", "DECLARE", "ASSIGN", "CONCATE", "LARROW", "NEW", "LPN", "RPN", 
			"LBK", "RBK", "LBR", "RBR", "DOT", "CM", "SM", "COL", "INTLIT", "FLOATLIT", 
			"STRLIT", "BLOCK_COMMENT", "LINE_COMMENT", "ID", "ATID", "WS", "UNCLOSE_STRING", 
			"ILLEGAL_ESCAPE", "ERROR_CHAR"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "CSlang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public CSlangParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public ClassdecllistContext classdecllist() {
			return getRuleContext(ClassdecllistContext.class,0);
		}
		public TerminalNode EOF() { return getToken(CSlangParser.EOF, 0); }
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(100);
			classdecllist();
			setState(101);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ClassdecllistContext extends ParserRuleContext {
		public ClassdeclContext classdecl() {
			return getRuleContext(ClassdeclContext.class,0);
		}
		public ClassdecllistContext classdecllist() {
			return getRuleContext(ClassdecllistContext.class,0);
		}
		public ClassdecllistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classdecllist; }
	}

	public final ClassdecllistContext classdecllist() throws RecognitionException {
		ClassdecllistContext _localctx = new ClassdecllistContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_classdecllist);
		try {
			setState(107);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(103);
				classdecl();
				setState(104);
				classdecllist();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(106);
				classdecl();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ClassdeclContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(CSlangParser.CLASS, 0); }
		public List<TerminalNode> ID() { return getTokens(CSlangParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(CSlangParser.ID, i);
		}
		public TerminalNode LBR() { return getToken(CSlangParser.LBR, 0); }
		public MemberlistContext memberlist() {
			return getRuleContext(MemberlistContext.class,0);
		}
		public TerminalNode RBR() { return getToken(CSlangParser.RBR, 0); }
		public TerminalNode LARROW() { return getToken(CSlangParser.LARROW, 0); }
		public ClassdeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classdecl; }
	}

	public final ClassdeclContext classdecl() throws RecognitionException {
		ClassdeclContext _localctx = new ClassdeclContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_classdecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(109);
			match(CLASS);
			setState(112);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				setState(110);
				match(ID);
				setState(111);
				match(LARROW);
				}
				break;
			}
			setState(114);
			match(ID);
			setState(115);
			match(LBR);
			setState(116);
			memberlist();
			setState(117);
			match(RBR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MemberlistContext extends ParserRuleContext {
		public MemberContext member() {
			return getRuleContext(MemberContext.class,0);
		}
		public MemberlistContext memberlist() {
			return getRuleContext(MemberlistContext.class,0);
		}
		public MemberlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_memberlist; }
	}

	public final MemberlistContext memberlist() throws RecognitionException {
		MemberlistContext _localctx = new MemberlistContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_memberlist);
		try {
			setState(123);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
			case CONST:
			case FUNC:
				enterOuterAlt(_localctx, 1);
				{
				setState(119);
				member();
				setState(120);
				memberlist();
				}
				break;
			case RBR:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MemberContext extends ParserRuleContext {
		public AttributeContext attribute() {
			return getRuleContext(AttributeContext.class,0);
		}
		public TerminalNode SM() { return getToken(CSlangParser.SM, 0); }
		public MethodContext method() {
			return getRuleContext(MethodContext.class,0);
		}
		public MemberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_member; }
	}

	public final MemberContext member() throws RecognitionException {
		MemberContext _localctx = new MemberContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_member);
		try {
			setState(129);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
			case CONST:
				enterOuterAlt(_localctx, 1);
				{
				setState(125);
				attribute();
				setState(126);
				match(SM);
				}
				break;
			case FUNC:
				enterOuterAlt(_localctx, 2);
				{
				setState(128);
				method();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AttributeContext extends ParserRuleContext {
		public VardeclContext vardecl() {
			return getRuleContext(VardeclContext.class,0);
		}
		public ConstdeclContext constdecl() {
			return getRuleContext(ConstdeclContext.class,0);
		}
		public AttributeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attribute; }
	}

	public final AttributeContext attribute() throws RecognitionException {
		AttributeContext _localctx = new AttributeContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_attribute);
		try {
			setState(133);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(131);
				vardecl();
				}
				break;
			case CONST:
				enterOuterAlt(_localctx, 2);
				{
				setState(132);
				constdecl();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VardeclContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(CSlangParser.VAR, 0); }
		public AttlistdeclContext attlistdecl() {
			return getRuleContext(AttlistdeclContext.class,0);
		}
		public AttlistnodeclContext attlistnodecl() {
			return getRuleContext(AttlistnodeclContext.class,0);
		}
		public VardeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vardecl; }
	}

	public final VardeclContext vardecl() throws RecognitionException {
		VardeclContext _localctx = new VardeclContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_vardecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(135);
			match(VAR);
			setState(138);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				{
				setState(136);
				attlistdecl();
				}
				break;
			case 2:
				{
				setState(137);
				attlistnodecl();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConstdeclContext extends ParserRuleContext {
		public TerminalNode CONST() { return getToken(CSlangParser.CONST, 0); }
		public AttlistdeclContext attlistdecl() {
			return getRuleContext(AttlistdeclContext.class,0);
		}
		public AttlistnodeclContext attlistnodecl() {
			return getRuleContext(AttlistnodeclContext.class,0);
		}
		public ConstdeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constdecl; }
	}

	public final ConstdeclContext constdecl() throws RecognitionException {
		ConstdeclContext _localctx = new ConstdeclContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_constdecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(140);
			match(CONST);
			setState(143);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				{
				setState(141);
				attlistdecl();
				}
				break;
			case 2:
				{
				setState(142);
				attlistnodecl();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AttlistdeclContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public List<TerminalNode> CM() { return getTokens(CSlangParser.CM); }
		public TerminalNode CM(int i) {
			return getToken(CSlangParser.CM, i);
		}
		public AttlistdeclContext attlistdecl() {
			return getRuleContext(AttlistdeclContext.class,0);
		}
		public ExprstrContext exprstr() {
			return getRuleContext(ExprstrContext.class,0);
		}
		public TerminalNode COL() { return getToken(CSlangParser.COL, 0); }
		public AtttypContext atttyp() {
			return getRuleContext(AtttypContext.class,0);
		}
		public TerminalNode DECLARE() { return getToken(CSlangParser.DECLARE, 0); }
		public AttlistdeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attlistdecl; }
	}

	public final AttlistdeclContext attlistdecl() throws RecognitionException {
		AttlistdeclContext _localctx = new AttlistdeclContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_attlistdecl);
		try {
			setState(157);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(145);
				identifier();
				setState(146);
				match(CM);
				setState(147);
				attlistdecl();
				setState(148);
				match(CM);
				setState(149);
				exprstr();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(151);
				identifier();
				setState(152);
				match(COL);
				setState(153);
				atttyp();
				setState(154);
				match(DECLARE);
				setState(155);
				exprstr();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AttlistnodeclContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode CM() { return getToken(CSlangParser.CM, 0); }
		public AttlistnodeclContext attlistnodecl() {
			return getRuleContext(AttlistnodeclContext.class,0);
		}
		public TerminalNode COL() { return getToken(CSlangParser.COL, 0); }
		public AtttypContext atttyp() {
			return getRuleContext(AtttypContext.class,0);
		}
		public AttlistnodeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attlistnodecl; }
	}

	public final AttlistnodeclContext attlistnodecl() throws RecognitionException {
		AttlistnodeclContext _localctx = new AttlistnodeclContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_attlistnodecl);
		try {
			setState(167);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(159);
				identifier();
				setState(160);
				match(CM);
				setState(161);
				attlistnodecl();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(163);
				identifier();
				setState(164);
				match(COL);
				setState(165);
				atttyp();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AtttypContext extends ParserRuleContext {
		public TypContext typ() {
			return getRuleContext(TypContext.class,0);
		}
		public TerminalNode LBK() { return getToken(CSlangParser.LBK, 0); }
		public TerminalNode INTLIT() { return getToken(CSlangParser.INTLIT, 0); }
		public TerminalNode RBK() { return getToken(CSlangParser.RBK, 0); }
		public AtttypContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atttyp; }
	}

	public final AtttypContext atttyp() throws RecognitionException {
		AtttypContext _localctx = new AtttypContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_atttyp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(172);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LBK) {
				{
				setState(169);
				match(LBK);
				setState(170);
				match(INTLIT);
				setState(171);
				match(RBK);
				}
			}

			setState(174);
			typ();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(CSlangParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(CSlangParser.FLOAT, 0); }
		public TerminalNode BOOL() { return getToken(CSlangParser.BOOL, 0); }
		public TerminalNode STRING() { return getToken(CSlangParser.STRING, 0); }
		public TerminalNode ID() { return getToken(CSlangParser.ID, 0); }
		public TypContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typ; }
	}

	public final TypContext typ() throws RecognitionException {
		TypContext _localctx = new TypContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_typ);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(176);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 72057594037931776L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MethodContext extends ParserRuleContext {
		public TerminalNode FUNC() { return getToken(CSlangParser.FUNC, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode LPN() { return getToken(CSlangParser.LPN, 0); }
		public TerminalNode RPN() { return getToken(CSlangParser.RPN, 0); }
		public TerminalNode COL() { return getToken(CSlangParser.COL, 0); }
		public BlockstmtContext blockstmt() {
			return getRuleContext(BlockstmtContext.class,0);
		}
		public AtttypContext atttyp() {
			return getRuleContext(AtttypContext.class,0);
		}
		public TerminalNode VOID() { return getToken(CSlangParser.VOID, 0); }
		public ParamlistContext paramlist() {
			return getRuleContext(ParamlistContext.class,0);
		}
		public TerminalNode CONSTRUCTOR() { return getToken(CSlangParser.CONSTRUCTOR, 0); }
		public MethodContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method; }
	}

	public final MethodContext method() throws RecognitionException {
		MethodContext _localctx = new MethodContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_method);
		int _la;
		try {
			setState(200);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(178);
				match(FUNC);
				setState(179);
				identifier();
				setState(180);
				match(LPN);
				setState(182);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ID || _la==ATID) {
					{
					setState(181);
					paramlist();
					}
				}

				setState(184);
				match(RPN);
				setState(185);
				match(COL);
				setState(188);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case INT:
				case FLOAT:
				case BOOL:
				case STRING:
				case LBK:
				case ID:
					{
					setState(186);
					atttyp();
					}
					break;
				case VOID:
					{
					setState(187);
					match(VOID);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(190);
				blockstmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(192);
				match(FUNC);
				setState(193);
				match(CONSTRUCTOR);
				setState(194);
				match(LPN);
				setState(196);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ID || _la==ATID) {
					{
					setState(195);
					paramlist();
					}
				}

				setState(198);
				match(RPN);
				setState(199);
				blockstmt();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamlistContext extends ParserRuleContext {
		public ParamsContext params() {
			return getRuleContext(ParamsContext.class,0);
		}
		public TerminalNode CM() { return getToken(CSlangParser.CM, 0); }
		public ParamlistContext paramlist() {
			return getRuleContext(ParamlistContext.class,0);
		}
		public ParamlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paramlist; }
	}

	public final ParamlistContext paramlist() throws RecognitionException {
		ParamlistContext _localctx = new ParamlistContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_paramlist);
		try {
			setState(207);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(202);
				params();
				setState(203);
				match(CM);
				setState(204);
				paramlist();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(206);
				params();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamsContext extends ParserRuleContext {
		public ParamContext param() {
			return getRuleContext(ParamContext.class,0);
		}
		public TerminalNode COL() { return getToken(CSlangParser.COL, 0); }
		public AtttypContext atttyp() {
			return getRuleContext(AtttypContext.class,0);
		}
		public ParamsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_params; }
	}

	public final ParamsContext params() throws RecognitionException {
		ParamsContext _localctx = new ParamsContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_params);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(209);
			param();
			setState(210);
			match(COL);
			setState(211);
			atttyp();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode CM() { return getToken(CSlangParser.CM, 0); }
		public ParamContext param() {
			return getRuleContext(ParamContext.class,0);
		}
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_param);
		try {
			setState(218);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(213);
				identifier();
				setState(214);
				match(CM);
				setState(215);
				param();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(217);
				identifier();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockstmtContext extends ParserRuleContext {
		public TerminalNode LBR() { return getToken(CSlangParser.LBR, 0); }
		public StmtlistContext stmtlist() {
			return getRuleContext(StmtlistContext.class,0);
		}
		public TerminalNode RBR() { return getToken(CSlangParser.RBR, 0); }
		public BlockstmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_blockstmt; }
	}

	public final BlockstmtContext blockstmt() throws RecognitionException {
		BlockstmtContext _localctx = new BlockstmtContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_blockstmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(220);
			match(LBR);
			setState(221);
			stmtlist();
			setState(222);
			match(RBR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParenexprContext extends ParserRuleContext {
		public TerminalNode LPN() { return getToken(CSlangParser.LPN, 0); }
		public ExprlistContext exprlist() {
			return getRuleContext(ExprlistContext.class,0);
		}
		public TerminalNode RPN() { return getToken(CSlangParser.RPN, 0); }
		public ParenexprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parenexpr; }
	}

	public final ParenexprContext parenexpr() throws RecognitionException {
		ParenexprContext _localctx = new ParenexprContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_parenexpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(224);
			match(LPN);
			setState(225);
			exprlist();
			setState(226);
			match(RPN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprlistContext extends ParserRuleContext {
		public ExprprimeContext exprprime() {
			return getRuleContext(ExprprimeContext.class,0);
		}
		public ExprlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprlist; }
	}

	public final ExprlistContext exprlist() throws RecognitionException {
		ExprlistContext _localctx = new ExprlistContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_exprlist);
		try {
			setState(230);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TRUE:
			case FALSE:
			case NULL:
			case SELF:
			case SUB:
			case NEG:
			case NEW:
			case LPN:
			case LBK:
			case INTLIT:
			case FLOATLIT:
			case STRLIT:
			case ID:
			case ATID:
				enterOuterAlt(_localctx, 1);
				{
				setState(228);
				exprprime();
				}
				break;
			case RPN:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprprimeContext extends ParserRuleContext {
		public ExprstrContext exprstr() {
			return getRuleContext(ExprstrContext.class,0);
		}
		public TerminalNode CM() { return getToken(CSlangParser.CM, 0); }
		public ExprprimeContext exprprime() {
			return getRuleContext(ExprprimeContext.class,0);
		}
		public ExprprimeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprprime; }
	}

	public final ExprprimeContext exprprime() throws RecognitionException {
		ExprprimeContext _localctx = new ExprprimeContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_exprprime);
		try {
			setState(237);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(232);
				exprstr();
				setState(233);
				match(CM);
				setState(234);
				exprprime();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(236);
				exprstr();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprstrContext extends ParserRuleContext {
		public List<ExprrelContext> exprrel() {
			return getRuleContexts(ExprrelContext.class);
		}
		public ExprrelContext exprrel(int i) {
			return getRuleContext(ExprrelContext.class,i);
		}
		public TerminalNode CONCATE() { return getToken(CSlangParser.CONCATE, 0); }
		public ExprstrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprstr; }
	}

	public final ExprstrContext exprstr() throws RecognitionException {
		ExprstrContext _localctx = new ExprstrContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_exprstr);
		try {
			setState(244);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(239);
				exprrel();
				setState(240);
				match(CONCATE);
				setState(241);
				exprrel();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(243);
				exprrel();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprrelContext extends ParserRuleContext {
		public List<ExprlogContext> exprlog() {
			return getRuleContexts(ExprlogContext.class);
		}
		public ExprlogContext exprlog(int i) {
			return getRuleContext(ExprlogContext.class,i);
		}
		public TerminalNode EQ() { return getToken(CSlangParser.EQ, 0); }
		public TerminalNode NEQ() { return getToken(CSlangParser.NEQ, 0); }
		public TerminalNode LT() { return getToken(CSlangParser.LT, 0); }
		public TerminalNode LTEQ() { return getToken(CSlangParser.LTEQ, 0); }
		public TerminalNode GT() { return getToken(CSlangParser.GT, 0); }
		public TerminalNode GTEQ() { return getToken(CSlangParser.GTEQ, 0); }
		public ExprrelContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprrel; }
	}

	public final ExprrelContext exprrel() throws RecognitionException {
		ExprrelContext _localctx = new ExprrelContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_exprrel);
		int _la;
		try {
			setState(251);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(246);
				exprlog(0);
				setState(247);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 67645734912L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(248);
				exprlog(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(250);
				exprlog(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprlogContext extends ParserRuleContext {
		public ExpraddContext expradd() {
			return getRuleContext(ExpraddContext.class,0);
		}
		public ExprlogContext exprlog() {
			return getRuleContext(ExprlogContext.class,0);
		}
		public TerminalNode AND() { return getToken(CSlangParser.AND, 0); }
		public TerminalNode OR() { return getToken(CSlangParser.OR, 0); }
		public ExprlogContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprlog; }
	}

	public final ExprlogContext exprlog() throws RecognitionException {
		return exprlog(0);
	}

	private ExprlogContext exprlog(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprlogContext _localctx = new ExprlogContext(_ctx, _parentState);
		ExprlogContext _prevctx = _localctx;
		int _startState = 44;
		enterRecursionRule(_localctx, 44, RULE_exprlog, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(254);
			expradd(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(261);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExprlogContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_exprlog);
					setState(256);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(257);
					_la = _input.LA(1);
					if ( !(_la==AND || _la==OR) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(258);
					expradd(0);
					}
					} 
				}
				setState(263);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpraddContext extends ParserRuleContext {
		public ExprmulContext exprmul() {
			return getRuleContext(ExprmulContext.class,0);
		}
		public ExpraddContext expradd() {
			return getRuleContext(ExpraddContext.class,0);
		}
		public TerminalNode ADD() { return getToken(CSlangParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(CSlangParser.SUB, 0); }
		public ExpraddContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expradd; }
	}

	public final ExpraddContext expradd() throws RecognitionException {
		return expradd(0);
	}

	private ExpraddContext expradd(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpraddContext _localctx = new ExpraddContext(_ctx, _parentState);
		ExpraddContext _prevctx = _localctx;
		int _startState = 46;
		enterRecursionRule(_localctx, 46, RULE_expradd, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(265);
			exprmul(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(272);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExpraddContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expradd);
					setState(267);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(268);
					_la = _input.LA(1);
					if ( !(_la==ADD || _la==SUB) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(269);
					exprmul(0);
					}
					} 
				}
				setState(274);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprmulContext extends ParserRuleContext {
		public ExprnotContext exprnot() {
			return getRuleContext(ExprnotContext.class,0);
		}
		public ExprmulContext exprmul() {
			return getRuleContext(ExprmulContext.class,0);
		}
		public TerminalNode MUL() { return getToken(CSlangParser.MUL, 0); }
		public TerminalNode DIVFLOAT() { return getToken(CSlangParser.DIVFLOAT, 0); }
		public TerminalNode DIVINT() { return getToken(CSlangParser.DIVINT, 0); }
		public TerminalNode MOD() { return getToken(CSlangParser.MOD, 0); }
		public ExprmulContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprmul; }
	}

	public final ExprmulContext exprmul() throws RecognitionException {
		return exprmul(0);
	}

	private ExprmulContext exprmul(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprmulContext _localctx = new ExprmulContext(_ctx, _parentState);
		ExprmulContext _prevctx = _localctx;
		int _startState = 48;
		enterRecursionRule(_localctx, 48, RULE_exprmul, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(276);
			exprnot();
			}
			_ctx.stop = _input.LT(-1);
			setState(283);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExprmulContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_exprmul);
					setState(278);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(279);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 125829120L) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(280);
					exprnot();
					}
					} 
				}
				setState(285);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprnotContext extends ParserRuleContext {
		public TerminalNode NEG() { return getToken(CSlangParser.NEG, 0); }
		public ExprnotContext exprnot() {
			return getRuleContext(ExprnotContext.class,0);
		}
		public ExprsignContext exprsign() {
			return getRuleContext(ExprsignContext.class,0);
		}
		public ExprnotContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprnot; }
	}

	public final ExprnotContext exprnot() throws RecognitionException {
		ExprnotContext _localctx = new ExprnotContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_exprnot);
		try {
			setState(289);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NEG:
				enterOuterAlt(_localctx, 1);
				{
				setState(286);
				match(NEG);
				setState(287);
				exprnot();
				}
				break;
			case TRUE:
			case FALSE:
			case NULL:
			case SELF:
			case SUB:
			case NEW:
			case LPN:
			case LBK:
			case INTLIT:
			case FLOATLIT:
			case STRLIT:
			case ID:
			case ATID:
				enterOuterAlt(_localctx, 2);
				{
				setState(288);
				exprsign();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprsignContext extends ParserRuleContext {
		public TerminalNode SUB() { return getToken(CSlangParser.SUB, 0); }
		public ExprsignContext exprsign() {
			return getRuleContext(ExprsignContext.class,0);
		}
		public ExprindexContext exprindex() {
			return getRuleContext(ExprindexContext.class,0);
		}
		public ExprsignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprsign; }
	}

	public final ExprsignContext exprsign() throws RecognitionException {
		ExprsignContext _localctx = new ExprsignContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_exprsign);
		try {
			setState(294);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SUB:
				enterOuterAlt(_localctx, 1);
				{
				setState(291);
				match(SUB);
				setState(292);
				exprsign();
				}
				break;
			case TRUE:
			case FALSE:
			case NULL:
			case SELF:
			case NEW:
			case LPN:
			case LBK:
			case INTLIT:
			case FLOATLIT:
			case STRLIT:
			case ID:
			case ATID:
				enterOuterAlt(_localctx, 2);
				{
				setState(293);
				exprindex();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprindexContext extends ParserRuleContext {
		public ExprinstContext exprinst() {
			return getRuleContext(ExprinstContext.class,0);
		}
		public TerminalNode LBK() { return getToken(CSlangParser.LBK, 0); }
		public ExprstrContext exprstr() {
			return getRuleContext(ExprstrContext.class,0);
		}
		public TerminalNode RBK() { return getToken(CSlangParser.RBK, 0); }
		public ExprindexContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprindex; }
	}

	public final ExprindexContext exprindex() throws RecognitionException {
		ExprindexContext _localctx = new ExprindexContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_exprindex);
		try {
			setState(302);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,25,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(296);
				exprinst(0);
				setState(297);
				match(LBK);
				setState(298);
				exprstr();
				setState(299);
				match(RBK);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(301);
				exprinst(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprinstContext extends ParserRuleContext {
		public ExprstatContext exprstat() {
			return getRuleContext(ExprstatContext.class,0);
		}
		public ExprinstContext exprinst() {
			return getRuleContext(ExprinstContext.class,0);
		}
		public TerminalNode DOT() { return getToken(CSlangParser.DOT, 0); }
		public TerminalNode ID() { return getToken(CSlangParser.ID, 0); }
		public TerminalNode LBK() { return getToken(CSlangParser.LBK, 0); }
		public ExprstrContext exprstr() {
			return getRuleContext(ExprstrContext.class,0);
		}
		public TerminalNode RBK() { return getToken(CSlangParser.RBK, 0); }
		public ParenexprContext parenexpr() {
			return getRuleContext(ParenexprContext.class,0);
		}
		public ExprinstContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprinst; }
	}

	public final ExprinstContext exprinst() throws RecognitionException {
		return exprinst(0);
	}

	private ExprinstContext exprinst(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprinstContext _localctx = new ExprinstContext(_ctx, _parentState);
		ExprinstContext _prevctx = _localctx;
		int _startState = 56;
		enterRecursionRule(_localctx, 56, RULE_exprinst, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(305);
			exprstat();
			}
			_ctx.stop = _input.LT(-1);
			setState(321);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,28,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExprinstContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_exprinst);
					setState(307);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(312);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==LBK) {
						{
						setState(308);
						match(LBK);
						setState(309);
						exprstr();
						setState(310);
						match(RBK);
						}
					}

					setState(314);
					match(DOT);
					setState(315);
					match(ID);
					setState(317);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
					case 1:
						{
						setState(316);
						parenexpr();
						}
						break;
					}
					}
					} 
				}
				setState(323);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,28,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprstatContext extends ParserRuleContext {
		public StatpartContext statpart() {
			return getRuleContext(StatpartContext.class,0);
		}
		public ExprobjContext exprobj() {
			return getRuleContext(ExprobjContext.class,0);
		}
		public ExprstatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprstat; }
	}

	public final ExprstatContext exprstat() throws RecognitionException {
		ExprstatContext _localctx = new ExprstatContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_exprstat);
		try {
			setState(326);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,29,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(324);
				statpart();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(325);
				exprobj();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprobjContext extends ParserRuleContext {
		public TerminalNode NEW() { return getToken(CSlangParser.NEW, 0); }
		public TerminalNode ID() { return getToken(CSlangParser.ID, 0); }
		public ParenexprContext parenexpr() {
			return getRuleContext(ParenexprContext.class,0);
		}
		public ExprparenContext exprparen() {
			return getRuleContext(ExprparenContext.class,0);
		}
		public ExprobjContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprobj; }
	}

	public final ExprobjContext exprobj() throws RecognitionException {
		ExprobjContext _localctx = new ExprobjContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_exprobj);
		try {
			setState(332);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NEW:
				enterOuterAlt(_localctx, 1);
				{
				setState(328);
				match(NEW);
				setState(329);
				match(ID);
				setState(330);
				parenexpr();
				}
				break;
			case TRUE:
			case FALSE:
			case NULL:
			case SELF:
			case LPN:
			case LBK:
			case INTLIT:
			case FLOATLIT:
			case STRLIT:
			case ID:
			case ATID:
				enterOuterAlt(_localctx, 2);
				{
				setState(331);
				exprparen();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprparenContext extends ParserRuleContext {
		public TerminalNode LPN() { return getToken(CSlangParser.LPN, 0); }
		public ExprstrContext exprstr() {
			return getRuleContext(ExprstrContext.class,0);
		}
		public TerminalNode RPN() { return getToken(CSlangParser.RPN, 0); }
		public LitContext lit() {
			return getRuleContext(LitContext.class,0);
		}
		public ExprparenContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprparen; }
	}

	public final ExprparenContext exprparen() throws RecognitionException {
		ExprparenContext _localctx = new ExprparenContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_exprparen);
		try {
			setState(339);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LPN:
				enterOuterAlt(_localctx, 1);
				{
				setState(334);
				match(LPN);
				setState(335);
				exprstr();
				setState(336);
				match(RPN);
				}
				break;
			case TRUE:
			case FALSE:
			case NULL:
			case SELF:
			case LBK:
			case INTLIT:
			case FLOATLIT:
			case STRLIT:
			case ID:
			case ATID:
				enterOuterAlt(_localctx, 2);
				{
				setState(338);
				lit();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatpartContext extends ParserRuleContext {
		public TerminalNode ATID() { return getToken(CSlangParser.ATID, 0); }
		public TerminalNode ID() { return getToken(CSlangParser.ID, 0); }
		public TerminalNode DOT() { return getToken(CSlangParser.DOT, 0); }
		public ParenexprContext parenexpr() {
			return getRuleContext(ParenexprContext.class,0);
		}
		public StatpartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statpart; }
	}

	public final StatpartContext statpart() throws RecognitionException {
		StatpartContext _localctx = new StatpartContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_statpart);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(343);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(341);
				match(ID);
				setState(342);
				match(DOT);
				}
			}

			setState(345);
			match(ATID);
			setState(347);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,33,_ctx) ) {
			case 1:
				{
				setState(346);
				parenexpr();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdentifierContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(CSlangParser.ID, 0); }
		public TerminalNode ATID() { return getToken(CSlangParser.ATID, 0); }
		public IdentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifier; }
	}

	public final IdentifierContext identifier() throws RecognitionException {
		IdentifierContext _localctx = new IdentifierContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_identifier);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(349);
			_la = _input.LA(1);
			if ( !(_la==ID || _la==ATID) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LitContext extends ParserRuleContext {
		public TerminalNode INTLIT() { return getToken(CSlangParser.INTLIT, 0); }
		public TerminalNode FLOATLIT() { return getToken(CSlangParser.FLOATLIT, 0); }
		public BoollitContext boollit() {
			return getRuleContext(BoollitContext.class,0);
		}
		public TerminalNode STRLIT() { return getToken(CSlangParser.STRLIT, 0); }
		public ArraylitContext arraylit() {
			return getRuleContext(ArraylitContext.class,0);
		}
		public TerminalNode NULL() { return getToken(CSlangParser.NULL, 0); }
		public TerminalNode SELF() { return getToken(CSlangParser.SELF, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public LitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lit; }
	}

	public final LitContext lit() throws RecognitionException {
		LitContext _localctx = new LitContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_lit);
		try {
			setState(359);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTLIT:
				enterOuterAlt(_localctx, 1);
				{
				setState(351);
				match(INTLIT);
				}
				break;
			case FLOATLIT:
				enterOuterAlt(_localctx, 2);
				{
				setState(352);
				match(FLOATLIT);
				}
				break;
			case TRUE:
			case FALSE:
				enterOuterAlt(_localctx, 3);
				{
				setState(353);
				boollit();
				}
				break;
			case STRLIT:
				enterOuterAlt(_localctx, 4);
				{
				setState(354);
				match(STRLIT);
				}
				break;
			case LBK:
				enterOuterAlt(_localctx, 5);
				{
				setState(355);
				arraylit();
				}
				break;
			case NULL:
				enterOuterAlt(_localctx, 6);
				{
				setState(356);
				match(NULL);
				}
				break;
			case SELF:
				enterOuterAlt(_localctx, 7);
				{
				setState(357);
				match(SELF);
				}
				break;
			case ID:
			case ATID:
				enterOuterAlt(_localctx, 8);
				{
				setState(358);
				identifier();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoollitContext extends ParserRuleContext {
		public TerminalNode TRUE() { return getToken(CSlangParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(CSlangParser.FALSE, 0); }
		public BoollitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boollit; }
	}

	public final BoollitContext boollit() throws RecognitionException {
		BoollitContext _localctx = new BoollitContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_boollit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(361);
			_la = _input.LA(1);
			if ( !(_la==TRUE || _la==FALSE) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArraylitContext extends ParserRuleContext {
		public TerminalNode LBK() { return getToken(CSlangParser.LBK, 0); }
		public LitprimeContext litprime() {
			return getRuleContext(LitprimeContext.class,0);
		}
		public TerminalNode RBK() { return getToken(CSlangParser.RBK, 0); }
		public ArraylitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arraylit; }
	}

	public final ArraylitContext arraylit() throws RecognitionException {
		ArraylitContext _localctx = new ArraylitContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_arraylit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(363);
			match(LBK);
			setState(364);
			litprime();
			setState(365);
			match(RBK);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LitlistContext extends ParserRuleContext {
		public LitprimeContext litprime() {
			return getRuleContext(LitprimeContext.class,0);
		}
		public LitlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_litlist; }
	}

	public final LitlistContext litlist() throws RecognitionException {
		LitlistContext _localctx = new LitlistContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_litlist);
		try {
			setState(369);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TRUE:
			case FALSE:
			case NULL:
			case SELF:
			case LBK:
			case INTLIT:
			case FLOATLIT:
			case STRLIT:
			case ID:
			case ATID:
				enterOuterAlt(_localctx, 1);
				{
				setState(367);
				litprime();
				}
				break;
			case EOF:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LitprimeContext extends ParserRuleContext {
		public LitContext lit() {
			return getRuleContext(LitContext.class,0);
		}
		public TerminalNode CM() { return getToken(CSlangParser.CM, 0); }
		public LitprimeContext litprime() {
			return getRuleContext(LitprimeContext.class,0);
		}
		public LitprimeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_litprime; }
	}

	public final LitprimeContext litprime() throws RecognitionException {
		LitprimeContext _localctx = new LitprimeContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_litprime);
		try {
			setState(376);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,36,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(371);
				lit();
				setState(372);
				match(CM);
				setState(373);
				litprime();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(375);
				lit();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StmtlistContext extends ParserRuleContext {
		public StmtContext stmt() {
			return getRuleContext(StmtContext.class,0);
		}
		public StmtlistContext stmtlist() {
			return getRuleContext(StmtlistContext.class,0);
		}
		public StmtlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmtlist; }
	}

	public final StmtlistContext stmtlist() throws RecognitionException {
		StmtlistContext _localctx = new StmtlistContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_stmtlist);
		try {
			setState(382);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BREAK:
			case CONTINUE:
			case IF:
			case FOR:
			case TRUE:
			case FALSE:
			case RETURN:
			case NULL:
			case VAR:
			case SELF:
			case CONST:
			case NEW:
			case LPN:
			case LBK:
			case INTLIT:
			case FLOATLIT:
			case STRLIT:
			case ID:
			case ATID:
				enterOuterAlt(_localctx, 1);
				{
				setState(378);
				stmt();
				setState(379);
				stmtlist();
				}
				break;
			case RBR:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StmtContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(CSlangParser.IF, 0); }
		public ExprstrContext exprstr() {
			return getRuleContext(ExprstrContext.class,0);
		}
		public List<BlockstmtContext> blockstmt() {
			return getRuleContexts(BlockstmtContext.class);
		}
		public BlockstmtContext blockstmt(int i) {
			return getRuleContext(BlockstmtContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(CSlangParser.ELSE, 0); }
		public TerminalNode FOR() { return getToken(CSlangParser.FOR, 0); }
		public List<StmtassignContext> stmtassign() {
			return getRuleContexts(StmtassignContext.class);
		}
		public StmtassignContext stmtassign(int i) {
			return getRuleContext(StmtassignContext.class,i);
		}
		public List<TerminalNode> SM() { return getTokens(CSlangParser.SM); }
		public TerminalNode SM(int i) {
			return getToken(CSlangParser.SM, i);
		}
		public TerminalNode VAR() { return getToken(CSlangParser.VAR, 0); }
		public TerminalNode CONST() { return getToken(CSlangParser.CONST, 0); }
		public TerminalNode BREAK() { return getToken(CSlangParser.BREAK, 0); }
		public TerminalNode CONTINUE() { return getToken(CSlangParser.CONTINUE, 0); }
		public TerminalNode RETURN() { return getToken(CSlangParser.RETURN, 0); }
		public StmtinvocContext stmtinvoc() {
			return getRuleContext(StmtinvocContext.class,0);
		}
		public StmtdeclContext stmtdecl() {
			return getRuleContext(StmtdeclContext.class,0);
		}
		public StmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt; }
	}

	public final StmtContext stmt() throws RecognitionException {
		StmtContext _localctx = new StmtContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_stmt);
		int _la;
		try {
			setState(423);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,42,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(384);
				match(IF);
				setState(386);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==LBR) {
					{
					setState(385);
					blockstmt();
					}
				}

				setState(388);
				exprstr();
				setState(389);
				blockstmt();
				setState(392);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ELSE) {
					{
					setState(390);
					match(ELSE);
					setState(391);
					blockstmt();
					}
				}

				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(394);
				match(FOR);
				setState(395);
				stmtassign();
				setState(396);
				match(SM);
				setState(397);
				exprstr();
				setState(398);
				match(SM);
				setState(399);
				stmtassign();
				setState(400);
				blockstmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(403);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==VAR || _la==CONST) {
					{
					setState(402);
					_la = _input.LA(1);
					if ( !(_la==VAR || _la==CONST) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
				}

				setState(405);
				stmtassign();
				setState(406);
				match(SM);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(408);
				match(BREAK);
				setState(409);
				match(SM);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(410);
				match(CONTINUE);
				setState(411);
				match(SM);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(412);
				match(RETURN);
				setState(414);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 231947475576037568L) != 0)) {
					{
					setState(413);
					exprstr();
					}
				}

				setState(416);
				match(SM);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(417);
				stmtinvoc();
				setState(418);
				match(SM);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(420);
				stmtdecl();
				setState(421);
				match(SM);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StmtassignContext extends ParserRuleContext {
		public LhsContext lhs() {
			return getRuleContext(LhsContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(CSlangParser.ASSIGN, 0); }
		public ExprstrContext exprstr() {
			return getRuleContext(ExprstrContext.class,0);
		}
		public StmtassignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmtassign; }
	}

	public final StmtassignContext stmtassign() throws RecognitionException {
		StmtassignContext _localctx = new StmtassignContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_stmtassign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(425);
			lhs(0);
			setState(426);
			match(ASSIGN);
			setState(427);
			exprstr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LhsContext extends ParserRuleContext {
		public LhsinstContext lhsinst() {
			return getRuleContext(LhsinstContext.class,0);
		}
		public LhsContext lhs() {
			return getRuleContext(LhsContext.class,0);
		}
		public TerminalNode LBK() { return getToken(CSlangParser.LBK, 0); }
		public ExprstrContext exprstr() {
			return getRuleContext(ExprstrContext.class,0);
		}
		public TerminalNode RBK() { return getToken(CSlangParser.RBK, 0); }
		public LhsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lhs; }
	}

	public final LhsContext lhs() throws RecognitionException {
		return lhs(0);
	}

	private LhsContext lhs(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		LhsContext _localctx = new LhsContext(_ctx, _parentState);
		LhsContext _prevctx = _localctx;
		int _startState = 84;
		enterRecursionRule(_localctx, 84, RULE_lhs, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(430);
			lhsinst(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(439);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,43,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new LhsContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_lhs);
					setState(432);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(433);
					match(LBK);
					setState(434);
					exprstr();
					setState(435);
					match(RBK);
					}
					} 
				}
				setState(441);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,43,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LhsinstContext extends ParserRuleContext {
		public LhsstatContext lhsstat() {
			return getRuleContext(LhsstatContext.class,0);
		}
		public LhsinstContext lhsinst() {
			return getRuleContext(LhsinstContext.class,0);
		}
		public TerminalNode DOT() { return getToken(CSlangParser.DOT, 0); }
		public TerminalNode ID() { return getToken(CSlangParser.ID, 0); }
		public TerminalNode LBK() { return getToken(CSlangParser.LBK, 0); }
		public ExprstrContext exprstr() {
			return getRuleContext(ExprstrContext.class,0);
		}
		public TerminalNode RBK() { return getToken(CSlangParser.RBK, 0); }
		public ParenexprContext parenexpr() {
			return getRuleContext(ParenexprContext.class,0);
		}
		public LhsinstContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lhsinst; }
	}

	public final LhsinstContext lhsinst() throws RecognitionException {
		return lhsinst(0);
	}

	private LhsinstContext lhsinst(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		LhsinstContext _localctx = new LhsinstContext(_ctx, _parentState);
		LhsinstContext _prevctx = _localctx;
		int _startState = 86;
		enterRecursionRule(_localctx, 86, RULE_lhsinst, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(443);
			lhsstat();
			}
			_ctx.stop = _input.LT(-1);
			setState(459);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,46,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new LhsinstContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_lhsinst);
					setState(445);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(450);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==LBK) {
						{
						setState(446);
						match(LBK);
						setState(447);
						exprstr();
						setState(448);
						match(RBK);
						}
					}

					setState(452);
					match(DOT);
					setState(453);
					match(ID);
					setState(455);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,45,_ctx) ) {
					case 1:
						{
						setState(454);
						parenexpr();
						}
						break;
					}
					}
					} 
				}
				setState(461);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,46,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LhsstatContext extends ParserRuleContext {
		public StatpartContext statpart() {
			return getRuleContext(StatpartContext.class,0);
		}
		public LhsparenContext lhsparen() {
			return getRuleContext(LhsparenContext.class,0);
		}
		public LhsstatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lhsstat; }
	}

	public final LhsstatContext lhsstat() throws RecognitionException {
		LhsstatContext _localctx = new LhsstatContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_lhsstat);
		try {
			setState(464);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,47,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(462);
				statpart();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(463);
				lhsparen();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LhsparenContext extends ParserRuleContext {
		public TerminalNode LPN() { return getToken(CSlangParser.LPN, 0); }
		public LhsContext lhs() {
			return getRuleContext(LhsContext.class,0);
		}
		public TerminalNode RPN() { return getToken(CSlangParser.RPN, 0); }
		public TerminalNode SELF() { return getToken(CSlangParser.SELF, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public LhsparenContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lhsparen; }
	}

	public final LhsparenContext lhsparen() throws RecognitionException {
		LhsparenContext _localctx = new LhsparenContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_lhsparen);
		try {
			setState(472);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LPN:
				enterOuterAlt(_localctx, 1);
				{
				setState(466);
				match(LPN);
				setState(467);
				lhs(0);
				setState(468);
				match(RPN);
				}
				break;
			case SELF:
				enterOuterAlt(_localctx, 2);
				{
				setState(470);
				match(SELF);
				}
				break;
			case ID:
			case ATID:
				enterOuterAlt(_localctx, 3);
				{
				setState(471);
				identifier();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StmtinvocContext extends ParserRuleContext {
		public StmtinvocinstContext stmtinvocinst() {
			return getRuleContext(StmtinvocinstContext.class,0);
		}
		public StmtinvocstatContext stmtinvocstat() {
			return getRuleContext(StmtinvocstatContext.class,0);
		}
		public StmtinvocContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmtinvoc; }
	}

	public final StmtinvocContext stmtinvoc() throws RecognitionException {
		StmtinvocContext _localctx = new StmtinvocContext(_ctx, getState());
		enterRule(_localctx, 92, RULE_stmtinvoc);
		try {
			setState(476);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,49,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(474);
				stmtinvocinst();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(475);
				stmtinvocstat();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StmtinvocinstContext extends ParserRuleContext {
		public ExprinstContext exprinst() {
			return getRuleContext(ExprinstContext.class,0);
		}
		public TerminalNode DOT() { return getToken(CSlangParser.DOT, 0); }
		public TerminalNode ID() { return getToken(CSlangParser.ID, 0); }
		public ParenexprContext parenexpr() {
			return getRuleContext(ParenexprContext.class,0);
		}
		public TerminalNode LBK() { return getToken(CSlangParser.LBK, 0); }
		public ExprstrContext exprstr() {
			return getRuleContext(ExprstrContext.class,0);
		}
		public TerminalNode RBK() { return getToken(CSlangParser.RBK, 0); }
		public StmtinvocinstContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmtinvocinst; }
	}

	public final StmtinvocinstContext stmtinvocinst() throws RecognitionException {
		StmtinvocinstContext _localctx = new StmtinvocinstContext(_ctx, getState());
		enterRule(_localctx, 94, RULE_stmtinvocinst);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(478);
			exprinst(0);
			setState(483);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LBK) {
				{
				setState(479);
				match(LBK);
				setState(480);
				exprstr();
				setState(481);
				match(RBK);
				}
			}

			setState(485);
			match(DOT);
			setState(486);
			match(ID);
			setState(487);
			parenexpr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StmtinvocstatContext extends ParserRuleContext {
		public TerminalNode ATID() { return getToken(CSlangParser.ATID, 0); }
		public ParenexprContext parenexpr() {
			return getRuleContext(ParenexprContext.class,0);
		}
		public TerminalNode ID() { return getToken(CSlangParser.ID, 0); }
		public TerminalNode DOT() { return getToken(CSlangParser.DOT, 0); }
		public StmtinvocstatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmtinvocstat; }
	}

	public final StmtinvocstatContext stmtinvocstat() throws RecognitionException {
		StmtinvocstatContext _localctx = new StmtinvocstatContext(_ctx, getState());
		enterRule(_localctx, 96, RULE_stmtinvocstat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(491);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(489);
				match(ID);
				setState(490);
				match(DOT);
				}
			}

			setState(493);
			match(ATID);
			setState(494);
			parenexpr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StmtdeclContext extends ParserRuleContext {
		public VardeclContext vardecl() {
			return getRuleContext(VardeclContext.class,0);
		}
		public ConstdeclContext constdecl() {
			return getRuleContext(ConstdeclContext.class,0);
		}
		public StmtdeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmtdecl; }
	}

	public final StmtdeclContext stmtdecl() throws RecognitionException {
		StmtdeclContext _localctx = new StmtdeclContext(_ctx, getState());
		enterRule(_localctx, 98, RULE_stmtdecl);
		try {
			setState(498);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(496);
				vardecl();
				}
				break;
			case CONST:
				enterOuterAlt(_localctx, 2);
				{
				setState(497);
				constdecl();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 22:
			return exprlog_sempred((ExprlogContext)_localctx, predIndex);
		case 23:
			return expradd_sempred((ExpraddContext)_localctx, predIndex);
		case 24:
			return exprmul_sempred((ExprmulContext)_localctx, predIndex);
		case 28:
			return exprinst_sempred((ExprinstContext)_localctx, predIndex);
		case 42:
			return lhs_sempred((LhsContext)_localctx, predIndex);
		case 43:
			return lhsinst_sempred((LhsinstContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean exprlog_sempred(ExprlogContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expradd_sempred(ExpraddContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean exprmul_sempred(ExprmulContext _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean exprinst_sempred(ExprinstContext _localctx, int predIndex) {
		switch (predIndex) {
		case 3:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean lhs_sempred(LhsContext _localctx, int predIndex) {
		switch (predIndex) {
		case 4:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean lhsinst_sempred(LhsinstContext _localctx, int predIndex) {
		switch (predIndex) {
		case 5:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001=\u01f5\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0002\"\u0007\"\u0002"+
		"#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007&\u0002\'\u0007\'\u0002"+
		"(\u0007(\u0002)\u0007)\u0002*\u0007*\u0002+\u0007+\u0002,\u0007,\u0002"+
		"-\u0007-\u0002.\u0007.\u0002/\u0007/\u00020\u00070\u00021\u00071\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0003\u0001l\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0003"+
		"\u0002q\b\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003|\b"+
		"\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004\u0082"+
		"\b\u0004\u0001\u0005\u0001\u0005\u0003\u0005\u0086\b\u0005\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0003\u0006\u008b\b\u0006\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0003\u0007\u0090\b\u0007\u0001\b\u0001\b\u0001\b\u0001\b"+
		"\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003"+
		"\b\u009e\b\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0003\t\u00a8\b\t\u0001\n\u0001\n\u0001\n\u0003\n\u00ad\b\n\u0001\n"+
		"\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0003"+
		"\f\u00b7\b\f\u0001\f\u0001\f\u0001\f\u0001\f\u0003\f\u00bd\b\f\u0001\f"+
		"\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0003\f\u00c5\b\f\u0001\f\u0001"+
		"\f\u0003\f\u00c9\b\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0003\r\u00d0"+
		"\b\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u00db\b\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0003\u0012\u00e7\b\u0012\u0001"+
		"\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0003\u0013\u00ee"+
		"\b\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0003"+
		"\u0014\u00f5\b\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0003\u0015\u00fc\b\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0001\u0016\u0005\u0016\u0104\b\u0016\n\u0016\f\u0016"+
		"\u0107\t\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0005\u0017\u010f\b\u0017\n\u0017\f\u0017\u0112\t\u0017\u0001"+
		"\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0005"+
		"\u0018\u011a\b\u0018\n\u0018\f\u0018\u011d\t\u0018\u0001\u0019\u0001\u0019"+
		"\u0001\u0019\u0003\u0019\u0122\b\u0019\u0001\u001a\u0001\u001a\u0001\u001a"+
		"\u0003\u001a\u0127\b\u001a\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b"+
		"\u0001\u001b\u0001\u001b\u0003\u001b\u012f\b\u001b\u0001\u001c\u0001\u001c"+
		"\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c"+
		"\u0003\u001c\u0139\b\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0003\u001c"+
		"\u013e\b\u001c\u0005\u001c\u0140\b\u001c\n\u001c\f\u001c\u0143\t\u001c"+
		"\u0001\u001d\u0001\u001d\u0003\u001d\u0147\b\u001d\u0001\u001e\u0001\u001e"+
		"\u0001\u001e\u0001\u001e\u0003\u001e\u014d\b\u001e\u0001\u001f\u0001\u001f"+
		"\u0001\u001f\u0001\u001f\u0001\u001f\u0003\u001f\u0154\b\u001f\u0001 "+
		"\u0001 \u0003 \u0158\b \u0001 \u0001 \u0003 \u015c\b \u0001!\u0001!\u0001"+
		"\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0003\"\u0168"+
		"\b\"\u0001#\u0001#\u0001$\u0001$\u0001$\u0001$\u0001%\u0001%\u0003%\u0172"+
		"\b%\u0001&\u0001&\u0001&\u0001&\u0001&\u0003&\u0179\b&\u0001\'\u0001\'"+
		"\u0001\'\u0001\'\u0003\'\u017f\b\'\u0001(\u0001(\u0003(\u0183\b(\u0001"+
		"(\u0001(\u0001(\u0001(\u0003(\u0189\b(\u0001(\u0001(\u0001(\u0001(\u0001"+
		"(\u0001(\u0001(\u0001(\u0001(\u0003(\u0194\b(\u0001(\u0001(\u0001(\u0001"+
		"(\u0001(\u0001(\u0001(\u0001(\u0001(\u0003(\u019f\b(\u0001(\u0001(\u0001"+
		"(\u0001(\u0001(\u0001(\u0001(\u0003(\u01a8\b(\u0001)\u0001)\u0001)\u0001"+
		")\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0005*\u01b6"+
		"\b*\n*\f*\u01b9\t*\u0001+\u0001+\u0001+\u0001+\u0001+\u0001+\u0001+\u0001"+
		"+\u0003+\u01c3\b+\u0001+\u0001+\u0001+\u0003+\u01c8\b+\u0005+\u01ca\b"+
		"+\n+\f+\u01cd\t+\u0001,\u0001,\u0003,\u01d1\b,\u0001-\u0001-\u0001-\u0001"+
		"-\u0001-\u0001-\u0003-\u01d9\b-\u0001.\u0001.\u0003.\u01dd\b.\u0001/\u0001"+
		"/\u0001/\u0001/\u0001/\u0003/\u01e4\b/\u0001/\u0001/\u0001/\u0001/\u0001"+
		"0\u00010\u00030\u01ec\b0\u00010\u00010\u00010\u00011\u00011\u00031\u01f3"+
		"\b1\u00011\u0000\u0006,.08TV2\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010"+
		"\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,.02468:<>@BDFHJLNPR"+
		"TVXZ\\^`b\u0000\b\u0002\u0000\b\u000b88\u0001\u0000\u001e#\u0001\u0000"+
		"\u001c\u001d\u0001\u0000\u0015\u0016\u0001\u0000\u0017\u001a\u0001\u0000"+
		"89\u0001\u0000\u0006\u0007\u0002\u0000\u0010\u0010\u0013\u0013\u0204\u0000"+
		"d\u0001\u0000\u0000\u0000\u0002k\u0001\u0000\u0000\u0000\u0004m\u0001"+
		"\u0000\u0000\u0000\u0006{\u0001\u0000\u0000\u0000\b\u0081\u0001\u0000"+
		"\u0000\u0000\n\u0085\u0001\u0000\u0000\u0000\f\u0087\u0001\u0000\u0000"+
		"\u0000\u000e\u008c\u0001\u0000\u0000\u0000\u0010\u009d\u0001\u0000\u0000"+
		"\u0000\u0012\u00a7\u0001\u0000\u0000\u0000\u0014\u00ac\u0001\u0000\u0000"+
		"\u0000\u0016\u00b0\u0001\u0000\u0000\u0000\u0018\u00c8\u0001\u0000\u0000"+
		"\u0000\u001a\u00cf\u0001\u0000\u0000\u0000\u001c\u00d1\u0001\u0000\u0000"+
		"\u0000\u001e\u00da\u0001\u0000\u0000\u0000 \u00dc\u0001\u0000\u0000\u0000"+
		"\"\u00e0\u0001\u0000\u0000\u0000$\u00e6\u0001\u0000\u0000\u0000&\u00ed"+
		"\u0001\u0000\u0000\u0000(\u00f4\u0001\u0000\u0000\u0000*\u00fb\u0001\u0000"+
		"\u0000\u0000,\u00fd\u0001\u0000\u0000\u0000.\u0108\u0001\u0000\u0000\u0000"+
		"0\u0113\u0001\u0000\u0000\u00002\u0121\u0001\u0000\u0000\u00004\u0126"+
		"\u0001\u0000\u0000\u00006\u012e\u0001\u0000\u0000\u00008\u0130\u0001\u0000"+
		"\u0000\u0000:\u0146\u0001\u0000\u0000\u0000<\u014c\u0001\u0000\u0000\u0000"+
		">\u0153\u0001\u0000\u0000\u0000@\u0157\u0001\u0000\u0000\u0000B\u015d"+
		"\u0001\u0000\u0000\u0000D\u0167\u0001\u0000\u0000\u0000F\u0169\u0001\u0000"+
		"\u0000\u0000H\u016b\u0001\u0000\u0000\u0000J\u0171\u0001\u0000\u0000\u0000"+
		"L\u0178\u0001\u0000\u0000\u0000N\u017e\u0001\u0000\u0000\u0000P\u01a7"+
		"\u0001\u0000\u0000\u0000R\u01a9\u0001\u0000\u0000\u0000T\u01ad\u0001\u0000"+
		"\u0000\u0000V\u01ba\u0001\u0000\u0000\u0000X\u01d0\u0001\u0000\u0000\u0000"+
		"Z\u01d8\u0001\u0000\u0000\u0000\\\u01dc\u0001\u0000\u0000\u0000^\u01de"+
		"\u0001\u0000\u0000\u0000`\u01eb\u0001\u0000\u0000\u0000b\u01f2\u0001\u0000"+
		"\u0000\u0000de\u0003\u0002\u0001\u0000ef\u0005\u0000\u0000\u0001f\u0001"+
		"\u0001\u0000\u0000\u0000gh\u0003\u0004\u0002\u0000hi\u0003\u0002\u0001"+
		"\u0000il\u0001\u0000\u0000\u0000jl\u0003\u0004\u0002\u0000kg\u0001\u0000"+
		"\u0000\u0000kj\u0001\u0000\u0000\u0000l\u0003\u0001\u0000\u0000\u0000"+
		"mp\u0005\u000e\u0000\u0000no\u00058\u0000\u0000oq\u0005\'\u0000\u0000"+
		"pn\u0001\u0000\u0000\u0000pq\u0001\u0000\u0000\u0000qr\u0001\u0000\u0000"+
		"\u0000rs\u00058\u0000\u0000st\u0005-\u0000\u0000tu\u0003\u0006\u0003\u0000"+
		"uv\u0005.\u0000\u0000v\u0005\u0001\u0000\u0000\u0000wx\u0003\b\u0004\u0000"+
		"xy\u0003\u0006\u0003\u0000y|\u0001\u0000\u0000\u0000z|\u0001\u0000\u0000"+
		"\u0000{w\u0001\u0000\u0000\u0000{z\u0001\u0000\u0000\u0000|\u0007\u0001"+
		"\u0000\u0000\u0000}~\u0003\n\u0005\u0000~\u007f\u00051\u0000\u0000\u007f"+
		"\u0082\u0001\u0000\u0000\u0000\u0080\u0082\u0003\u0018\f\u0000\u0081}"+
		"\u0001\u0000\u0000\u0000\u0081\u0080\u0001\u0000\u0000\u0000\u0082\t\u0001"+
		"\u0000\u0000\u0000\u0083\u0086\u0003\f\u0006\u0000\u0084\u0086\u0003\u000e"+
		"\u0007\u0000\u0085\u0083\u0001\u0000\u0000\u0000\u0085\u0084\u0001\u0000"+
		"\u0000\u0000\u0086\u000b\u0001\u0000\u0000\u0000\u0087\u008a\u0005\u0010"+
		"\u0000\u0000\u0088\u008b\u0003\u0010\b\u0000\u0089\u008b\u0003\u0012\t"+
		"\u0000\u008a\u0088\u0001\u0000\u0000\u0000\u008a\u0089\u0001\u0000\u0000"+
		"\u0000\u008b\r\u0001\u0000\u0000\u0000\u008c\u008f\u0005\u0013\u0000\u0000"+
		"\u008d\u0090\u0003\u0010\b\u0000\u008e\u0090\u0003\u0012\t\u0000\u008f"+
		"\u008d\u0001\u0000\u0000\u0000\u008f\u008e\u0001\u0000\u0000\u0000\u0090"+
		"\u000f\u0001\u0000\u0000\u0000\u0091\u0092\u0003B!\u0000\u0092\u0093\u0005"+
		"0\u0000\u0000\u0093\u0094\u0003\u0010\b\u0000\u0094\u0095\u00050\u0000"+
		"\u0000\u0095\u0096\u0003(\u0014\u0000\u0096\u009e\u0001\u0000\u0000\u0000"+
		"\u0097\u0098\u0003B!\u0000\u0098\u0099\u00052\u0000\u0000\u0099\u009a"+
		"\u0003\u0014\n\u0000\u009a\u009b\u0005$\u0000\u0000\u009b\u009c\u0003"+
		"(\u0014\u0000\u009c\u009e\u0001\u0000\u0000\u0000\u009d\u0091\u0001\u0000"+
		"\u0000\u0000\u009d\u0097\u0001\u0000\u0000\u0000\u009e\u0011\u0001\u0000"+
		"\u0000\u0000\u009f\u00a0\u0003B!\u0000\u00a0\u00a1\u00050\u0000\u0000"+
		"\u00a1\u00a2\u0003\u0012\t\u0000\u00a2\u00a8\u0001\u0000\u0000\u0000\u00a3"+
		"\u00a4\u0003B!\u0000\u00a4\u00a5\u00052\u0000\u0000\u00a5\u00a6\u0003"+
		"\u0014\n\u0000\u00a6\u00a8\u0001\u0000\u0000\u0000\u00a7\u009f\u0001\u0000"+
		"\u0000\u0000\u00a7\u00a3\u0001\u0000\u0000\u0000\u00a8\u0013\u0001\u0000"+
		"\u0000\u0000\u00a9\u00aa\u0005+\u0000\u0000\u00aa\u00ab\u00053\u0000\u0000"+
		"\u00ab\u00ad\u0005,\u0000\u0000\u00ac\u00a9\u0001\u0000\u0000\u0000\u00ac"+
		"\u00ad\u0001\u0000\u0000\u0000\u00ad\u00ae\u0001\u0000\u0000\u0000\u00ae"+
		"\u00af\u0003\u0016\u000b\u0000\u00af\u0015\u0001\u0000\u0000\u0000\u00b0"+
		"\u00b1\u0007\u0000\u0000\u0000\u00b1\u0017\u0001\u0000\u0000\u0000\u00b2"+
		"\u00b3\u0005\u0014\u0000\u0000\u00b3\u00b4\u0003B!\u0000\u00b4\u00b6\u0005"+
		")\u0000\u0000\u00b5\u00b7\u0003\u001a\r\u0000\u00b6\u00b5\u0001\u0000"+
		"\u0000\u0000\u00b6\u00b7\u0001\u0000\u0000\u0000\u00b7\u00b8\u0001\u0000"+
		"\u0000\u0000\u00b8\u00b9\u0005*\u0000\u0000\u00b9\u00bc\u00052\u0000\u0000"+
		"\u00ba\u00bd\u0003\u0014\n\u0000\u00bb\u00bd\u0005\u0012\u0000\u0000\u00bc"+
		"\u00ba\u0001\u0000\u0000\u0000\u00bc\u00bb\u0001\u0000\u0000\u0000\u00bd"+
		"\u00be\u0001\u0000\u0000\u0000\u00be\u00bf\u0003 \u0010\u0000\u00bf\u00c9"+
		"\u0001\u0000\u0000\u0000\u00c0\u00c1\u0005\u0014\u0000\u0000\u00c1\u00c2"+
		"\u0005\u000f\u0000\u0000\u00c2\u00c4\u0005)\u0000\u0000\u00c3\u00c5\u0003"+
		"\u001a\r\u0000\u00c4\u00c3\u0001\u0000\u0000\u0000\u00c4\u00c5\u0001\u0000"+
		"\u0000\u0000\u00c5\u00c6\u0001\u0000\u0000\u0000\u00c6\u00c7\u0005*\u0000"+
		"\u0000\u00c7\u00c9\u0003 \u0010\u0000\u00c8\u00b2\u0001\u0000\u0000\u0000"+
		"\u00c8\u00c0\u0001\u0000\u0000\u0000\u00c9\u0019\u0001\u0000\u0000\u0000"+
		"\u00ca\u00cb\u0003\u001c\u000e\u0000\u00cb\u00cc\u00050\u0000\u0000\u00cc"+
		"\u00cd\u0003\u001a\r\u0000\u00cd\u00d0\u0001\u0000\u0000\u0000\u00ce\u00d0"+
		"\u0003\u001c\u000e\u0000\u00cf\u00ca\u0001\u0000\u0000\u0000\u00cf\u00ce"+
		"\u0001\u0000\u0000\u0000\u00d0\u001b\u0001\u0000\u0000\u0000\u00d1\u00d2"+
		"\u0003\u001e\u000f\u0000\u00d2\u00d3\u00052\u0000\u0000\u00d3\u00d4\u0003"+
		"\u0014\n\u0000\u00d4\u001d\u0001\u0000\u0000\u0000\u00d5\u00d6\u0003B"+
		"!\u0000\u00d6\u00d7\u00050\u0000\u0000\u00d7\u00d8\u0003\u001e\u000f\u0000"+
		"\u00d8\u00db\u0001\u0000\u0000\u0000\u00d9\u00db\u0003B!\u0000\u00da\u00d5"+
		"\u0001\u0000\u0000\u0000\u00da\u00d9\u0001\u0000\u0000\u0000\u00db\u001f"+
		"\u0001\u0000\u0000\u0000\u00dc\u00dd\u0005-\u0000\u0000\u00dd\u00de\u0003"+
		"N\'\u0000\u00de\u00df\u0005.\u0000\u0000\u00df!\u0001\u0000\u0000\u0000"+
		"\u00e0\u00e1\u0005)\u0000\u0000\u00e1\u00e2\u0003$\u0012\u0000\u00e2\u00e3"+
		"\u0005*\u0000\u0000\u00e3#\u0001\u0000\u0000\u0000\u00e4\u00e7\u0003&"+
		"\u0013\u0000\u00e5\u00e7\u0001\u0000\u0000\u0000\u00e6\u00e4\u0001\u0000"+
		"\u0000\u0000\u00e6\u00e5\u0001\u0000\u0000\u0000\u00e7%\u0001\u0000\u0000"+
		"\u0000\u00e8\u00e9\u0003(\u0014\u0000\u00e9\u00ea\u00050\u0000\u0000\u00ea"+
		"\u00eb\u0003&\u0013\u0000\u00eb\u00ee\u0001\u0000\u0000\u0000\u00ec\u00ee"+
		"\u0003(\u0014\u0000\u00ed\u00e8\u0001\u0000\u0000\u0000\u00ed\u00ec\u0001"+
		"\u0000\u0000\u0000\u00ee\'\u0001\u0000\u0000\u0000\u00ef\u00f0\u0003*"+
		"\u0015\u0000\u00f0\u00f1\u0005&\u0000\u0000\u00f1\u00f2\u0003*\u0015\u0000"+
		"\u00f2\u00f5\u0001\u0000\u0000\u0000\u00f3\u00f5\u0003*\u0015\u0000\u00f4"+
		"\u00ef\u0001\u0000\u0000\u0000\u00f4\u00f3\u0001\u0000\u0000\u0000\u00f5"+
		")\u0001\u0000\u0000\u0000\u00f6\u00f7\u0003,\u0016\u0000\u00f7\u00f8\u0007"+
		"\u0001\u0000\u0000\u00f8\u00f9\u0003,\u0016\u0000\u00f9\u00fc\u0001\u0000"+
		"\u0000\u0000\u00fa\u00fc\u0003,\u0016\u0000\u00fb\u00f6\u0001\u0000\u0000"+
		"\u0000\u00fb\u00fa\u0001\u0000\u0000\u0000\u00fc+\u0001\u0000\u0000\u0000"+
		"\u00fd\u00fe\u0006\u0016\uffff\uffff\u0000\u00fe\u00ff\u0003.\u0017\u0000"+
		"\u00ff\u0105\u0001\u0000\u0000\u0000\u0100\u0101\n\u0002\u0000\u0000\u0101"+
		"\u0102\u0007\u0002\u0000\u0000\u0102\u0104\u0003.\u0017\u0000\u0103\u0100"+
		"\u0001\u0000\u0000\u0000\u0104\u0107\u0001\u0000\u0000\u0000\u0105\u0103"+
		"\u0001\u0000\u0000\u0000\u0105\u0106\u0001\u0000\u0000\u0000\u0106-\u0001"+
		"\u0000\u0000\u0000\u0107\u0105\u0001\u0000\u0000\u0000\u0108\u0109\u0006"+
		"\u0017\uffff\uffff\u0000\u0109\u010a\u00030\u0018\u0000\u010a\u0110\u0001"+
		"\u0000\u0000\u0000\u010b\u010c\n\u0002\u0000\u0000\u010c\u010d\u0007\u0003"+
		"\u0000\u0000\u010d\u010f\u00030\u0018\u0000\u010e\u010b\u0001\u0000\u0000"+
		"\u0000\u010f\u0112\u0001\u0000\u0000\u0000\u0110\u010e\u0001\u0000\u0000"+
		"\u0000\u0110\u0111\u0001\u0000\u0000\u0000\u0111/\u0001\u0000\u0000\u0000"+
		"\u0112\u0110\u0001\u0000\u0000\u0000\u0113\u0114\u0006\u0018\uffff\uffff"+
		"\u0000\u0114\u0115\u00032\u0019\u0000\u0115\u011b\u0001\u0000\u0000\u0000"+
		"\u0116\u0117\n\u0002\u0000\u0000\u0117\u0118\u0007\u0004\u0000\u0000\u0118"+
		"\u011a\u00032\u0019\u0000\u0119\u0116\u0001\u0000\u0000\u0000\u011a\u011d"+
		"\u0001\u0000\u0000\u0000\u011b\u0119\u0001\u0000\u0000\u0000\u011b\u011c"+
		"\u0001\u0000\u0000\u0000\u011c1\u0001\u0000\u0000\u0000\u011d\u011b\u0001"+
		"\u0000\u0000\u0000\u011e\u011f\u0005\u001b\u0000\u0000\u011f\u0122\u0003"+
		"2\u0019\u0000\u0120\u0122\u00034\u001a\u0000\u0121\u011e\u0001\u0000\u0000"+
		"\u0000\u0121\u0120\u0001\u0000\u0000\u0000\u01223\u0001\u0000\u0000\u0000"+
		"\u0123\u0124\u0005\u0016\u0000\u0000\u0124\u0127\u00034\u001a\u0000\u0125"+
		"\u0127\u00036\u001b\u0000\u0126\u0123\u0001\u0000\u0000\u0000\u0126\u0125"+
		"\u0001\u0000\u0000\u0000\u01275\u0001\u0000\u0000\u0000\u0128\u0129\u0003"+
		"8\u001c\u0000\u0129\u012a\u0005+\u0000\u0000\u012a\u012b\u0003(\u0014"+
		"\u0000\u012b\u012c\u0005,\u0000\u0000\u012c\u012f\u0001\u0000\u0000\u0000"+
		"\u012d\u012f\u00038\u001c\u0000\u012e\u0128\u0001\u0000\u0000\u0000\u012e"+
		"\u012d\u0001\u0000\u0000\u0000\u012f7\u0001\u0000\u0000\u0000\u0130\u0131"+
		"\u0006\u001c\uffff\uffff\u0000\u0131\u0132\u0003:\u001d\u0000\u0132\u0141"+
		"\u0001\u0000\u0000\u0000\u0133\u0138\n\u0002\u0000\u0000\u0134\u0135\u0005"+
		"+\u0000\u0000\u0135\u0136\u0003(\u0014\u0000\u0136\u0137\u0005,\u0000"+
		"\u0000\u0137\u0139\u0001\u0000\u0000\u0000\u0138\u0134\u0001\u0000\u0000"+
		"\u0000\u0138\u0139\u0001\u0000\u0000\u0000\u0139\u013a\u0001\u0000\u0000"+
		"\u0000\u013a\u013b\u0005/\u0000\u0000\u013b\u013d\u00058\u0000\u0000\u013c"+
		"\u013e\u0003\"\u0011\u0000\u013d\u013c\u0001\u0000\u0000\u0000\u013d\u013e"+
		"\u0001\u0000\u0000\u0000\u013e\u0140\u0001\u0000\u0000\u0000\u013f\u0133"+
		"\u0001\u0000\u0000\u0000\u0140\u0143\u0001\u0000\u0000\u0000\u0141\u013f"+
		"\u0001\u0000\u0000\u0000\u0141\u0142\u0001\u0000\u0000\u0000\u01429\u0001"+
		"\u0000\u0000\u0000\u0143\u0141\u0001\u0000\u0000\u0000\u0144\u0147\u0003"+
		"@ \u0000\u0145\u0147\u0003<\u001e\u0000\u0146\u0144\u0001\u0000\u0000"+
		"\u0000\u0146\u0145\u0001\u0000\u0000\u0000\u0147;\u0001\u0000\u0000\u0000"+
		"\u0148\u0149\u0005(\u0000\u0000\u0149\u014a\u00058\u0000\u0000\u014a\u014d"+
		"\u0003\"\u0011\u0000\u014b\u014d\u0003>\u001f\u0000\u014c\u0148\u0001"+
		"\u0000\u0000\u0000\u014c\u014b\u0001\u0000\u0000\u0000\u014d=\u0001\u0000"+
		"\u0000\u0000\u014e\u014f\u0005)\u0000\u0000\u014f\u0150\u0003(\u0014\u0000"+
		"\u0150\u0151\u0005*\u0000\u0000\u0151\u0154\u0001\u0000\u0000\u0000\u0152"+
		"\u0154\u0003D\"\u0000\u0153\u014e\u0001\u0000\u0000\u0000\u0153\u0152"+
		"\u0001\u0000\u0000\u0000\u0154?\u0001\u0000\u0000\u0000\u0155\u0156\u0005"+
		"8\u0000\u0000\u0156\u0158\u0005/\u0000\u0000\u0157\u0155\u0001\u0000\u0000"+
		"\u0000\u0157\u0158\u0001\u0000\u0000\u0000\u0158\u0159\u0001\u0000\u0000"+
		"\u0000\u0159\u015b\u00059\u0000\u0000\u015a\u015c\u0003\"\u0011\u0000"+
		"\u015b\u015a\u0001\u0000\u0000\u0000\u015b\u015c\u0001\u0000\u0000\u0000"+
		"\u015cA\u0001\u0000\u0000\u0000\u015d\u015e\u0007\u0005\u0000\u0000\u015e"+
		"C\u0001\u0000\u0000\u0000\u015f\u0168\u00053\u0000\u0000\u0160\u0168\u0005"+
		"4\u0000\u0000\u0161\u0168\u0003F#\u0000\u0162\u0168\u00055\u0000\u0000"+
		"\u0163\u0168\u0003H$\u0000\u0164\u0168\u0005\r\u0000\u0000\u0165\u0168"+
		"\u0005\u0011\u0000\u0000\u0166\u0168\u0003B!\u0000\u0167\u015f\u0001\u0000"+
		"\u0000\u0000\u0167\u0160\u0001\u0000\u0000\u0000\u0167\u0161\u0001\u0000"+
		"\u0000\u0000\u0167\u0162\u0001\u0000\u0000\u0000\u0167\u0163\u0001\u0000"+
		"\u0000\u0000\u0167\u0164\u0001\u0000\u0000\u0000\u0167\u0165\u0001\u0000"+
		"\u0000\u0000\u0167\u0166\u0001\u0000\u0000\u0000\u0168E\u0001\u0000\u0000"+
		"\u0000\u0169\u016a\u0007\u0006\u0000\u0000\u016aG\u0001\u0000\u0000\u0000"+
		"\u016b\u016c\u0005+\u0000\u0000\u016c\u016d\u0003L&\u0000\u016d\u016e"+
		"\u0005,\u0000\u0000\u016eI\u0001\u0000\u0000\u0000\u016f\u0172\u0003L"+
		"&\u0000\u0170\u0172\u0001\u0000\u0000\u0000\u0171\u016f\u0001\u0000\u0000"+
		"\u0000\u0171\u0170\u0001\u0000\u0000\u0000\u0172K\u0001\u0000\u0000\u0000"+
		"\u0173\u0174\u0003D\"\u0000\u0174\u0175\u00050\u0000\u0000\u0175\u0176"+
		"\u0003L&\u0000\u0176\u0179\u0001\u0000\u0000\u0000\u0177\u0179\u0003D"+
		"\"\u0000\u0178\u0173\u0001\u0000\u0000\u0000\u0178\u0177\u0001\u0000\u0000"+
		"\u0000\u0179M\u0001\u0000\u0000\u0000\u017a\u017b\u0003P(\u0000\u017b"+
		"\u017c\u0003N\'\u0000\u017c\u017f\u0001\u0000\u0000\u0000\u017d\u017f"+
		"\u0001\u0000\u0000\u0000\u017e\u017a\u0001\u0000\u0000\u0000\u017e\u017d"+
		"\u0001\u0000\u0000\u0000\u017fO\u0001\u0000\u0000\u0000\u0180\u0182\u0005"+
		"\u0003\u0000\u0000\u0181\u0183\u0003 \u0010\u0000\u0182\u0181\u0001\u0000"+
		"\u0000\u0000\u0182\u0183\u0001\u0000\u0000\u0000\u0183\u0184\u0001\u0000"+
		"\u0000\u0000\u0184\u0185\u0003(\u0014\u0000\u0185\u0188\u0003 \u0010\u0000"+
		"\u0186\u0187\u0005\u0004\u0000\u0000\u0187\u0189\u0003 \u0010\u0000\u0188"+
		"\u0186\u0001\u0000\u0000\u0000\u0188\u0189\u0001\u0000\u0000\u0000\u0189"+
		"\u01a8\u0001\u0000\u0000\u0000\u018a\u018b\u0005\u0005\u0000\u0000\u018b"+
		"\u018c\u0003R)\u0000\u018c\u018d\u00051\u0000\u0000\u018d\u018e\u0003"+
		"(\u0014\u0000\u018e\u018f\u00051\u0000\u0000\u018f\u0190\u0003R)\u0000"+
		"\u0190\u0191\u0003 \u0010\u0000\u0191\u01a8\u0001\u0000\u0000\u0000\u0192"+
		"\u0194\u0007\u0007\u0000\u0000\u0193\u0192\u0001\u0000\u0000\u0000\u0193"+
		"\u0194\u0001\u0000\u0000\u0000\u0194\u0195\u0001\u0000\u0000\u0000\u0195"+
		"\u0196\u0003R)\u0000\u0196\u0197\u00051\u0000\u0000\u0197\u01a8\u0001"+
		"\u0000\u0000\u0000\u0198\u0199\u0005\u0001\u0000\u0000\u0199\u01a8\u0005"+
		"1\u0000\u0000\u019a\u019b\u0005\u0002\u0000\u0000\u019b\u01a8\u00051\u0000"+
		"\u0000\u019c\u019e\u0005\f\u0000\u0000\u019d\u019f\u0003(\u0014\u0000"+
		"\u019e\u019d\u0001\u0000\u0000\u0000\u019e\u019f\u0001\u0000\u0000\u0000"+
		"\u019f\u01a0\u0001\u0000\u0000\u0000\u01a0\u01a8\u00051\u0000\u0000\u01a1"+
		"\u01a2\u0003\\.\u0000\u01a2\u01a3\u00051\u0000\u0000\u01a3\u01a8\u0001"+
		"\u0000\u0000\u0000\u01a4\u01a5\u0003b1\u0000\u01a5\u01a6\u00051\u0000"+
		"\u0000\u01a6\u01a8\u0001\u0000\u0000\u0000\u01a7\u0180\u0001\u0000\u0000"+
		"\u0000\u01a7\u018a\u0001\u0000\u0000\u0000\u01a7\u0193\u0001\u0000\u0000"+
		"\u0000\u01a7\u0198\u0001\u0000\u0000\u0000\u01a7\u019a\u0001\u0000\u0000"+
		"\u0000\u01a7\u019c\u0001\u0000\u0000\u0000\u01a7\u01a1\u0001\u0000\u0000"+
		"\u0000\u01a7\u01a4\u0001\u0000\u0000\u0000\u01a8Q\u0001\u0000\u0000\u0000"+
		"\u01a9\u01aa\u0003T*\u0000\u01aa\u01ab\u0005%\u0000\u0000\u01ab\u01ac"+
		"\u0003(\u0014\u0000\u01acS\u0001\u0000\u0000\u0000\u01ad\u01ae\u0006*"+
		"\uffff\uffff\u0000\u01ae\u01af\u0003V+\u0000\u01af\u01b7\u0001\u0000\u0000"+
		"\u0000\u01b0\u01b1\n\u0002\u0000\u0000\u01b1\u01b2\u0005+\u0000\u0000"+
		"\u01b2\u01b3\u0003(\u0014\u0000\u01b3\u01b4\u0005,\u0000\u0000\u01b4\u01b6"+
		"\u0001\u0000\u0000\u0000\u01b5\u01b0\u0001\u0000\u0000\u0000\u01b6\u01b9"+
		"\u0001\u0000\u0000\u0000\u01b7\u01b5\u0001\u0000\u0000\u0000\u01b7\u01b8"+
		"\u0001\u0000\u0000\u0000\u01b8U\u0001\u0000\u0000\u0000\u01b9\u01b7\u0001"+
		"\u0000\u0000\u0000\u01ba\u01bb\u0006+\uffff\uffff\u0000\u01bb\u01bc\u0003"+
		"X,\u0000\u01bc\u01cb\u0001\u0000\u0000\u0000\u01bd\u01c2\n\u0002\u0000"+
		"\u0000\u01be\u01bf\u0005+\u0000\u0000\u01bf\u01c0\u0003(\u0014\u0000\u01c0"+
		"\u01c1\u0005,\u0000\u0000\u01c1\u01c3\u0001\u0000\u0000\u0000\u01c2\u01be"+
		"\u0001\u0000\u0000\u0000\u01c2\u01c3\u0001\u0000\u0000\u0000\u01c3\u01c4"+
		"\u0001\u0000\u0000\u0000\u01c4\u01c5\u0005/\u0000\u0000\u01c5\u01c7\u0005"+
		"8\u0000\u0000\u01c6\u01c8\u0003\"\u0011\u0000\u01c7\u01c6\u0001\u0000"+
		"\u0000\u0000\u01c7\u01c8\u0001\u0000\u0000\u0000\u01c8\u01ca\u0001\u0000"+
		"\u0000\u0000\u01c9\u01bd\u0001\u0000\u0000\u0000\u01ca\u01cd\u0001\u0000"+
		"\u0000\u0000\u01cb\u01c9\u0001\u0000\u0000\u0000\u01cb\u01cc\u0001\u0000"+
		"\u0000\u0000\u01ccW\u0001\u0000\u0000\u0000\u01cd\u01cb\u0001\u0000\u0000"+
		"\u0000\u01ce\u01d1\u0003@ \u0000\u01cf\u01d1\u0003Z-\u0000\u01d0\u01ce"+
		"\u0001\u0000\u0000\u0000\u01d0\u01cf\u0001\u0000\u0000\u0000\u01d1Y\u0001"+
		"\u0000\u0000\u0000\u01d2\u01d3\u0005)\u0000\u0000\u01d3\u01d4\u0003T*"+
		"\u0000\u01d4\u01d5\u0005*\u0000\u0000\u01d5\u01d9\u0001\u0000\u0000\u0000"+
		"\u01d6\u01d9\u0005\u0011\u0000\u0000\u01d7\u01d9\u0003B!\u0000\u01d8\u01d2"+
		"\u0001\u0000\u0000\u0000\u01d8\u01d6\u0001\u0000\u0000\u0000\u01d8\u01d7"+
		"\u0001\u0000\u0000\u0000\u01d9[\u0001\u0000\u0000\u0000\u01da\u01dd\u0003"+
		"^/\u0000\u01db\u01dd\u0003`0\u0000\u01dc\u01da\u0001\u0000\u0000\u0000"+
		"\u01dc\u01db\u0001\u0000\u0000\u0000\u01dd]\u0001\u0000\u0000\u0000\u01de"+
		"\u01e3\u00038\u001c\u0000\u01df\u01e0\u0005+\u0000\u0000\u01e0\u01e1\u0003"+
		"(\u0014\u0000\u01e1\u01e2\u0005,\u0000\u0000\u01e2\u01e4\u0001\u0000\u0000"+
		"\u0000\u01e3\u01df\u0001\u0000\u0000\u0000\u01e3\u01e4\u0001\u0000\u0000"+
		"\u0000\u01e4\u01e5\u0001\u0000\u0000\u0000\u01e5\u01e6\u0005/\u0000\u0000"+
		"\u01e6\u01e7\u00058\u0000\u0000\u01e7\u01e8\u0003\"\u0011\u0000\u01e8"+
		"_\u0001\u0000\u0000\u0000\u01e9\u01ea\u00058\u0000\u0000\u01ea\u01ec\u0005"+
		"/\u0000\u0000\u01eb\u01e9\u0001\u0000\u0000\u0000\u01eb\u01ec\u0001\u0000"+
		"\u0000\u0000\u01ec\u01ed\u0001\u0000\u0000\u0000\u01ed\u01ee\u00059\u0000"+
		"\u0000\u01ee\u01ef\u0003\"\u0011\u0000\u01efa\u0001\u0000\u0000\u0000"+
		"\u01f0\u01f3\u0003\f\u0006\u0000\u01f1\u01f3\u0003\u000e\u0007\u0000\u01f2"+
		"\u01f0\u0001\u0000\u0000\u0000\u01f2\u01f1\u0001\u0000\u0000\u0000\u01f3"+
		"c\u0001\u0000\u0000\u00005kp{\u0081\u0085\u008a\u008f\u009d\u00a7\u00ac"+
		"\u00b6\u00bc\u00c4\u00c8\u00cf\u00da\u00e6\u00ed\u00f4\u00fb\u0105\u0110"+
		"\u011b\u0121\u0126\u012e\u0138\u013d\u0141\u0146\u014c\u0153\u0157\u015b"+
		"\u0167\u0171\u0178\u017e\u0182\u0188\u0193\u019e\u01a7\u01b7\u01c2\u01c7"+
		"\u01cb\u01d0\u01d8\u01dc\u01e3\u01eb\u01f2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}