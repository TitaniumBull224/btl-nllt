grammar CSlang;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: classdecllist EOF;
/*  
Parser rules
*/
// Class declaration
	classdecllist: classdecl classdecllist | classdecl;
	classdecl: CLASS (ID ARROW | ) ID LBR memberlist RBR;
	memberlist: member memberlist | ;
	member: attribute SM | method;
// Attribute declaration
	attribute: (VAR | CONST) (attlistdecl | attlistnodecl);
	attlistdecl: identifiers CM attlistdecl CM exprstr | identifiers COL atttyp DECLARE exprstr;
	attlistnodecl: identifiers CM attlistnodecl | identifiers COL atttyp;
	atttyp: (arraytyp | ) typ | classtyp;
	typ: INT | FLOAT | BOOL | STRING;
	arraytyp: LBK INT_LIT RBK;
	classtyp: NEW ID LPN RPN;
// Method declaration
	method
		: FUNC identifiers LPN (paramlist | ) RPN COL (typ | VOID) blockstmt 
		| FUNC CONSTRUCTOR LPN (paramlist | ) RPN blockstmt
		;
	paramlist: params CM paramlist | params COL typ;
	params: ID CM params | ID;
	blockstmt: LBR statements RBR;
	parenexpr: LPN expressions RPN;
// Expressions
	expressions: exprprime | ;
	exprprime: exprstr CM expressions | exprstr;

	exprstr: exprrel CONCATE exprrel | exprrel;
	exprrel: exprlog (EQ | NEQ | LT | LTEQ | GT | GTEQ) exprlog | exprlog;
	exprlog: exprlog (AND | OR) expradd | expradd;
	expradd: expradd (PLUS | MINUS) exprmul | exprmul;
	exprmul: exprmul (MUL | DIV_FLOAT | DIV_INT | MOD) exprnot | exprnot;
	exprnot: NEG exprnot | exprsign;
	exprsign: MINUS exprsign | exprindex;
	exprindex: exprinst LBK exprstr RBK | exprinst;
	exprinst
		: exprinst DOT ID (parenexpr | ) 
		| SELF DOT ID (parenexpr | )
		| exprstat
		;
	exprstat: ((ID | SELF) DOT | ) AT_ID (parenexpr | ) | exprobj;
	exprobj: NEW ID parenexpr | exprparen;
	exprparen: LPN exprstr RPN | identifiers | literals;

	identifiers: ID | AT_ID;
	literals: INT_LIT | FLOAT_LIT | boolliteral | STR_LIT | arrayliteral;

	arrayliteral: LBK (arrint | arrfloat | arrbool | arrstr) RBK;
	arrint: INT_LIT CM arrint | INT_LIT;
	arrfloat: FLOAT_LIT CM arrfloat | FLOAT_LIT;
	arrbool: boolliteral CM arrbool | boolliteral;
	arrstr: STR_LIT CM arrstr | STR_LIT;

	boolliteral: TRUE | FALSE;
// Statements
	statements: stmt statements | ;
	stmt
		: (VAR | CONST | ) stmtassign SM
		| IF (blockstmt | ) exprstr blockstmt (ELSE blockstmt | )
		| FOR stmtassign SM exprrel SM stmtassign blockstmt
		| BREAK SM
		| CONTINUE SM
		| RETURN (exprstr | ) SM
		| exprinst SM
		| attribute SM
		;
	stmtassign: lhs ASSIGN exprstr;
	lhs: lhs LBK exprstr RBK | lhsinst;
	lhsinst
		: lhsinst DOT ID (parenexpr | )
		| SELF DOT ID (parenexpr | )
		| lhsstat
		;
	lhsstat: ((ID | SELF) DOT | ) AT_ID (parenexpr | ) | lhsparen;
	lhsparen: LPN lhs RPN | identifiers;
/*  
Lexer tokens
*/
// Keywords
	BREAK: 'break';
	CONTINUE: 'continue';
	IF: 'if';
	ELSE: 'else';
	FOR: 'for';
	TRUE: 'true';
	FALSE: 'false';
	INT: 'int';
	FLOAT: 'float';
	BOOL: 'bool';
	STRING: 'string';
	RETURN: 'return';
	NULL: 'null';
	CLASS: 'class';
	CONSTRUCTOR: 'constructor';
	VAR: 'var';
	SELF: 'self';
	VOID: 'void';
	CONST: 'const';
	FUNC: 'func';
// Operators
	PLUS: '+';
	MINUS: '-';
	MUL: '*';
	DIV_FLOAT: '/';
	DIV_INT: '\\';
	MOD: '%';
	NEG: '!';
	AND: '&&';
	OR: '||';
	EQ: '==';
	NEQ: '!=';
	LT: '<';
	LTEQ: '<=';
	GT: '>';
	GTEQ: '>=';
	DECLARE: '=';
	ASSIGN: ':=';
	CONCATE: '^';
	ARROW: '<-';
	NEW: 'new';
// Separators
	LPN: '(';
	RPN: ')';
	LBK: '[';
	RBK: ']';
	LBR: '{';
	RBR: '}';
	DOT: '.';
	CM: ',';
	SM: ';';
	COL: ':';
// Literals
	INT_LIT: DIGIT+;
	FLOAT_LIT: DIGIT+ (FLOAT_DEC | FLOAT_EXP | FLOAT_DEC FLOAT_EXP);
	STR_LIT: '"' STR_CHAR* '"' {self.text = self.text[1:-1]};
// Comment
	BLOCK_COMMENT: '/*' .*? '*/' -> skip;
	LINE_COMMENT: '//' ~[\r\n]* -> skip;
// Identifiers
	ID: [a-zA-Z_] [a-zA-Z0-9_]*;
	AT_ID: '@' [a-zA-Z0-9_]+;
// fragment
	fragment FLOAT_DEC: DOT DIGIT*;
	fragment FLOAT_EXP: [eE] [-+]? DIGIT+;
	fragment DIGIT: [0-9];
	fragment STR_CHAR:  ~[\n\r\\"] | '\\' [btnfr"\\];
// EXCEPTION
	WS: [ \t\r\n]+ -> skip;
	UNCLOSE_STRING: '"' STR_CHAR* {self.text = self.text[1:]; raise UncloseString(self.text)};
	ILLEGAL_ESCAPE: '"' ('\\'[btnfr'\\] | ~[\n\r\\"])* ('\\'(~[btnfr'\\])) {self.text = self.text[1:]; raise IllegalEscape(self.text)};
	ERROR_CHAR: . {raise ErrorToken(self.text)};