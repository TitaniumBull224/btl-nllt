grammar CSlang;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: ID EOF ;

ID: [a-z]+;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;