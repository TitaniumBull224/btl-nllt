import sys
import os
from antlr4 import *

if not "./main/CSlang/parser/" in sys.path:
    sys.path.append("./main/CSlang/parser/")
if (
    os.path.isdir("../target/main/CSlang/parser")
    and not "../target/main/CSlang/parser/" in sys.path
):
    sys.path.append("../target/main/CSlang/parser/")
from CSlangLexer import CSlangLexer
from CSlangParser import CSlangParser
from CSlangVisitor import CSlangVisitor
from AST import *
from ASTGeneration import ASTGeneration


def generate_ast(input_str):
    input_stream = InputStream(input_str)
    lexer = CSlangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CSlangParser(stream)
    tree = parser.program()

    astgen = ASTGeneration()
    ast = astgen.visit(tree)

    return ast


input_str = r"""class Main {
    func @main(a:int,b:float):void{
        if a > b {
            return a;
        }
        else {
            return b;
        }
    }
}"""

ast = generate_ast(input_str)
print(ast)
