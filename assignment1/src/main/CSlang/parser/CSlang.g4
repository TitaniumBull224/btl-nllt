grammar CSlang;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}
/*
program: ID EOF ;

ID: [a-z]+;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
*/
// Parser rules
program: ID EOF;

// Lexer rules

// 1. Characters set
fragment CHAR:   [a-zA-Z0-9_];
WS : [ \t\b\f\r\n]+ -> skip ; // skip blank, tab, backspace, formfeed, carriage return, newline
// 2. Comment
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT:  '//' ~[\r\n]* -> skip;

// 3. Identifiers
ID: [a-zA-Z_] CHAR*;
AT_ID: '@' CHAR+;

// 4. Keywords
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

// 5. Operators
PLUS: '+';
MINUS: '-';
STAR: '*';
SLASH: '/';
BACKSLASH: '\\';
BANG: '!';
ANDAND: '&&';
OROR: '||';
EQEQ: '==';
EQ: '=';
BANGEQ: '!=';
LT: '<';
LTEQ: '<=';
GT: '>';
GTEQ: '>=';
COLONEQ: ':=';
CARET: '^';
NEW: 'new';
PERCENT: '%';

// 6. Separators
LPAREN: '(';
RPAREN: ')';
LBRACK: '[';
RBRACK: ']';
DOT: '.';
COMMA: ',';
SEMI: ';';
COLON: ':';
LBRACE: '{';
RBRACE: '}';

// 7. Literals

// EXCEPTION
ERROR_TOKEN: . {raise Exception("ERROR_TOKEN")};
UNCLOSE_STRING: '"' ~[\r\n]* {raise Exception("UNCLOSE_STRING")};
ILLEGAL_ESCAPE: '\\' ~[btnfr"'\\] {raise Exception("ILLEGAL_ESCAPE")};