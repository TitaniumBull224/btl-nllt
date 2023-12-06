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
	classdecl: CLASS (ID LARROW)? ID LBR memberlist RBR;
	memberlist: member memberlist | ;
	member: attribute SM | method;
// Attribute declaration
	// attribute: (VAR | CONST) (attlistdecl | attlistnodecl);
	attribute: vardecl | constdecl;
	vardecl: VAR (attlistdecl | attlistnodecl);
	constdecl: CONST (attlistdecl | attlistnodecl);
	attlistdecl: identifier CM attlistdecl CM exprstr | identifier COL atttyp DECLARE exprstr;
	attlistnodecl: identifier CM attlistnodecl | identifier COL atttyp;
	atttyp: (LBK INTLIT RBK)? typ | VOID;
	typ: INT | FLOAT | BOOL | STRING | ID;
// Method declaration
	method
		: FUNC identifier LPN paramlist? RPN COL atttyp blockstmt 
		| FUNC CONSTRUCTOR LPN paramlist? RPN blockstmt
		;
	paramlist: params CM paramlist | params;
	params: param COL atttyp; 
	param: identifier CM param | identifier;

	blockstmt: LBR stmtlist RBR;
	parenexpr: LPN exprlist RPN;
// Expressions
	exprlist: exprprime | ;
	exprprime: exprstr CM exprprime | exprstr;

	exprstr: exprrel CONCATE exprrel | exprrel;
	exprrel: exprlog (EQ | NEQ | LT | LTEQ | GT | GTEQ) exprlog | exprlog;
	exprlog: exprlog (AND | OR) expradd | expradd;
	expradd: expradd (ADD | SUB) exprmul | exprmul;
	exprmul: exprmul (MUL | DIVFLOAT | DIVINT | MOD) exprnot | exprnot;
	exprnot: NEG exprnot | exprsign;
	exprsign: SUB exprsign | exprindex;
	exprindex: exprinst LBK exprstr RBK | exprinst;
	exprinst: exprinst (LBK exprstr RBK)? DOT ID parenexpr? | exprstat;
	exprstat: (ID DOT)? ATID parenexpr? | exprobj;
	exprobj: NEW ID parenexpr | exprparen;
	exprparen: LPN exprstr RPN | lit;
// Literals
	identifier: ID | ATID;
	lit: INTLIT | FLOATLIT | boollit | STRLIT | arraylit | NULL | SELF | identifier;
	boollit: TRUE | FALSE;
	arraylit: LBK litprime RBK;

	litlist: litprime | ;
	litprime: lit CM litprime | lit;
// Statements
	stmtlist: stmt stmtlist | ;
	stmt
		: IF blockstmt? exprstr blockstmt (ELSE blockstmt)?
		| FOR stmtassign SM exprstr SM stmtassign blockstmt
		| (VAR | CONST)? stmtassign SM
		| BREAK SM
		| CONTINUE SM
		| RETURN exprstr? SM
		| stmtinvoc SM
		| stmtdecl SM
		;
	stmtassign: lhs ASSIGN exprstr;
	lhs: lhsinst LBK exprstr RBK | lhsinst;
	lhsinst: lhsinst (LBK exprstr RBK)? DOT ID | lhsstat;
	lhsstat: (ID DOT)? ATID | lhsparen;
	lhsparen: LPN lhs RPN | SELF | identifier;

	stmtinvoc: stmtinvocinst | stmtinvocstat;
	stmtinvocinst: exprinst (LBK exprstr RBK)? DOT ID parenexpr;
	stmtinvocstat: (ID DOT)? ATID parenexpr;

	stmtdecl: vardecl | constdecl;
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
	ADD: '+';
	SUB: '-';
	MUL: '*';
	DIVFLOAT: '/';
	DIVINT: '\\';
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
	LARROW: '<-';
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
	INTLIT: DIGIT+;
	FLOATLIT: DIGIT+ (FLOAT_DEC | FLOAT_EXP | FLOAT_DEC FLOAT_EXP);
	STRLIT: '"' STR_CHAR* '"' {self.text = self.text[1:-1]};
// Comment
	BLOCK_COMMENT: '/*' .*? '*/' -> skip;
	LINE_COMMENT: '//' ~[\r\n]* -> skip;
// Identifiers
	ID: [a-zA-Z_] [a-zA-Z0-9_]*;
	ATID: '@' [a-zA-Z0-9_]+;
// fragment
	fragment FLOAT_DEC: DOT DIGIT*;
	fragment FLOAT_EXP: [eE] [-+]? DIGIT+;
	fragment DIGIT: [0-9];
	fragment STR_CHAR:  ~[\n\r\\"] | '\\' [btnfr"\\];
// EXCEPTION
	WS: [ \t\r\n]+ -> skip;
	UNCLOSE_STRING: '"' STR_CHAR* { self.text = self.text[1:]; raise UncloseString(self.text) };
	ILLEGAL_ESCAPE: '"' ('\\'[btnfr'\\] | ~[\n\r\\"])* ('\\'(~[btnfr'\\])) { self.text = self.text[1:]; raise IllegalEscape(self.text) };
	ERROR_CHAR: . { raise ErrorToken(self.text) };