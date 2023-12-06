import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test0(self):
        input = """
        class Program{
            const temp:[2]int = [6,7];
            func test(temp1,temp2:a):int{
                var a,b:int = s,temp1;
            }
            func @main():void{

            }
        }
        class a{
            const temp:int;
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Program"),
                        [
                            MethodDecl(
                                Id("@main"),
                                [],
                                VoidType(),
                                Block([]),
                            ),
                            AttributeDecl(VarDecl(Id("a"), VoidType())),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 300))
