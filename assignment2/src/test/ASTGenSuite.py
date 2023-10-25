import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test0(self):
        input = r"""
            class main {
                
            }
            class sub {
            
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(Id("main"), []),
                    ClassDecl(Id("sub"), []),
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 300))

    def test1(self):
        input = r"""
            class main {
                var a:int;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [AttributeDecl(VarDecl(Id("a"), IntType(), None))],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 301))

    def test2(self):
        input = r"""
            class main {
                const a:int = 5;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [AttributeDecl(ConstDecl(Id("a"), IntType(), IntLiteral(5)))],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 302))

    def test3(self):
        input = r"""
            class main {
                func @main():void{
                    return;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("@main"),
                                [],
                                VoidType(),
                                Block([Return(None)]),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 303))

    def test4(self):
        input = r"""
            class main {
                func constructor(){
                    return;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("constructor"),
                                [],
                                VoidType(),
                                Block([Return(None)]),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 304))

    def test5(self):
        input = r"""
            class main {
                func @main():void{
                    return;
                }
                func constructor(){
                    return;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("@main"),
                                [],
                                VoidType(),
                                Block([Return(None)]),
                            ),
                            MethodDecl(
                                Id("constructor"),
                                [],
                                VoidType(),
                                Block([Return(None)]),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 305))

    def test6(self):
        input = r"""
            class main {
                var a:int;
                const b:int = 5;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(VarDecl(Id("a"), IntType(), None)),
                            AttributeDecl(ConstDecl(Id("b"), IntType(), IntLiteral(5))),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 306))

    def test7(self):
        input = r"""
            class main {
                var a:int;
                const b:int = 5;
            }
            class Secondary {
                func @main():void{
                    return;
                }
                func constructor(){
                    return;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(VarDecl(Id("a"), IntType(), None)),
                            AttributeDecl(ConstDecl(Id("b"), IntType(), IntLiteral(5))),
                        ],
                    ),
                    ClassDecl(
                        Id("Secondary"),
                        [
                            MethodDecl(
                                Id("@main"),
                                [],
                                VoidType(),
                                Block([Return(None)]),
                            ),
                            MethodDecl(
                                Id("constructor"),
                                [],
                                VoidType(),
                                Block([Return(None)]),
                            ),
                        ],
                    ),
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 307))

    def test8(self):
        input = r"""
            class Parent <- Child {
                var a:int;
                const b:int = 5;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Child"),
                        [
                            AttributeDecl(VarDecl(Id("a"), IntType(), None)),
                            AttributeDecl(ConstDecl(Id("b"), IntType(), IntLiteral(5))),
                        ],
                        Id("Parent"),
                    ),
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 308))

    def test9(self):
        input = r"""
            class main {
                func @main(a:int,b:float):void{
                    return;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("@main"),
                                [
                                    VarDecl(Id("a"), IntType(), None),
                                    VarDecl(Id("b"), FloatType(), None),
                                ],
                                VoidType(),
                                Block([Return(None)]),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 309))

    def test10(self):
        input = r"""
            class main {
                func @main(a:int,b:float):void{
                    if a > b {
                        return a;
                    }
                    else {
                        return b;
                    }
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("@main"),
                                [
                                    VarDecl(Id("a"), IntType(), None),
                                    VarDecl(Id("b"), FloatType(), None),
                                ],
                                VoidType(),
                                Block(
                                    [
                                        If(
                                            BinaryOp(">", Id("a"), Id("b")),
                                            Block([Return(Id("a"))]),
                                            None,
                                            Block([Return(Id("b"))]),
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 310))

    def test11(self):
        input = r"""
            class main {
                const a, b, c:float = 3.2, 20.5, 45.0;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                ConstDecl(Id("a"), FloatType(), FloatLiteral(3.2))
                            ),
                            AttributeDecl(
                                ConstDecl(Id("b"), FloatType(), FloatLiteral(20.5))
                            ),
                            AttributeDecl(
                                ConstDecl(Id("c"), FloatType(), FloatLiteral(45.0))
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 311))

    def test12(self):
        input = r"""
            class main {
                var a,b: [8]int = 2,3;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                VarDecl(Id("a"), ArrayType(8, IntType()), IntLiteral(2))
                            ),
                            AttributeDecl(
                                VarDecl(Id("b"), ArrayType(8, IntType()), IntLiteral(3))
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 312))

    def test13(self):
        input = r"""
            class main {
                func @test(a, b:int,t:[5]string):void {
                    break;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("@test"),
                                [
                                    VarDecl(Id("a"), IntType()),
                                    VarDecl(Id("b"), IntType()),
                                    VarDecl(Id("t"), ArrayType(5, StringType())),
                                ],
                                VoidType(),
                                Block([Break()]),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 313))

    def test14(self):
        input = r"""
            class main {
                const a:Shape = new Shape();
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                ConstDecl(
                                    Id("a"),
                                    ClassType(Id("Shape")),
                                    NewExpr(Id("Shape"), []),
                                )
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 314))

    def test15(self):
        input = r"""
            class main {
                var a:string = ("test"^"tmp")[0];
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                VarDecl(
                                    Id("a"),
                                    StringType(),
                                    ArrayCell(
                                        BinaryOp(
                                            "^",
                                            StringLiteral("test"),
                                            StringLiteral("tmp"),
                                        ),
                                        IntLiteral(0),
                                    ),
                                )
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 315))

    def test16(self):
        input = r"""
            class main {
                var a:bool = true;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                VarDecl(Id("a"), BoolType(), BooleanLiteral(True))
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 316))

    def test17(self):
        input = r"""
            class main {
                var a:float = 25.15e-1;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                VarDecl(Id("a"), FloatType(), FloatLiteral(25.15e-1))
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 317))

    def test18(self):
        input = r"""
            class main {
                const a:string = self.lst[5];
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                ConstDecl(
                                    Id("a"),
                                    StringType(),
                                    ArrayCell(
                                        FieldAccess(SelfLiteral(), Id("lst")),
                                        IntLiteral(5),
                                    ),
                                )
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 318))

    def test19(self):
        input = r"""
            class main {
                func test():void {
                    a := new X().b[0].c[1+2];
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("test"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        Assign(
                                            Id("a"),
                                            ArrayCell(
                                                FieldAccess(
                                                    ArrayCell(
                                                        FieldAccess(
                                                            NewExpr(Id("X"), []),
                                                            Id("b"),
                                                        ),
                                                        IntLiteral(0),
                                                    ),
                                                    Id("c"),
                                                ),
                                                BinaryOp(
                                                    "+", IntLiteral(1), IntLiteral(2)
                                                ),
                                            ),
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 319))

    def test20(self):
        input = r"""
            class main {
                var a:int = Animal.@b(1, 2, 3);
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                VarDecl(
                                    Id("a"),
                                    IntType(),
                                    CallExpr(
                                        Id("Animal"),
                                        Id("@b"),
                                        [IntLiteral(1), IntLiteral(2), IntLiteral(3)],
                                    ),
                                )
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 320))

    def test21(self):
        input = r"""
            class main {
                var a:string = k[0].b(4,8);
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                VarDecl(
                                    Id("a"),
                                    StringType(),
                                    CallExpr(
                                        ArrayCell(Id("k"), IntLiteral(0)),
                                        Id("b"),
                                        [IntLiteral(4), IntLiteral(8)],
                                    ),
                                )
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 321))

    def test22(self):
        input = r"""
            class main {
                var a:string = gen[0].name;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                VarDecl(
                                    Id("a"),
                                    StringType(),
                                    FieldAccess(
                                        ArrayCell(Id("gen"), IntLiteral(0)), Id("name")
                                    ),
                                )
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 322))

    def test23(self):
        input = r"""
            class main {
                var a:int = !!--anti;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                VarDecl(
                                    Id("a"),
                                    IntType(),
                                    UnaryOp(
                                        "!",
                                        UnaryOp(
                                            "!", UnaryOp("-", UnaryOp("-", Id("anti")))
                                        ),
                                    ),
                                )
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 323))

    def test24(self):
        input = r"""
            class main {
                var a:int = a \ b % c;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                VarDecl(
                                    Id("a"),
                                    IntType(),
                                    BinaryOp(
                                        "%", BinaryOp("\\", Id("a"), Id("b")), Id("c")
                                    ),
                                )
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 324))

    def test25(self):
        input = r"""
            class main {
                var a:bool = a && b || c;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                VarDecl(
                                    Id("a"),
                                    BoolType(),
                                    BinaryOp(
                                        "||", BinaryOp("&&", Id("a"), Id("b")), Id("c")
                                    ),
                                )
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 325))

    def test26(self):
        input = r"""
            class main {
                var a:int = null;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [AttributeDecl(VarDecl(Id("a"), IntType(), NullLiteral()))],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 326))

    def test27(self):
        input = r"""
            class main {
                func test():void {
                    a := 1;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("test"),
                                [],
                                VoidType(),
                                Block([Assign(Id("a"), IntLiteral(1))]),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 327))

    def test28(self):
        input = r"""
            class main {
                func test():void {
                    Vegi.aqua := 445;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("test"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        Assign(
                                            FieldAccess(Id("Vegi"), Id("aqua")),
                                            IntLiteral(445),
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 328))

    def test29(self):
        input = r"""
            class main {
                func test():void {
                    Oga.Vegi.aqua := 445;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("test"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        Assign(
                                            FieldAccess(
                                                FieldAccess(Id("Oga"), Id("Vegi")),
                                                Id("aqua"),
                                            ),
                                            IntLiteral(445),
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 329))

    def test30(self):
        input = r"""
            class main {
                func test():void {
                    Oga[420].Vegi.aqua := 445;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("test"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        Assign(
                                            FieldAccess(
                                                FieldAccess(
                                                    ArrayCell(
                                                        Id("Oga"), IntLiteral(420)
                                                    ),
                                                    Id("Vegi"),
                                                ),
                                                Id("aqua"),
                                            ),
                                            IntLiteral(445),
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 330))

    def test31(self):
        input = r"""
            class main {
                func test():void {
                    Anime.OP[1] := "Nightmare";
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("test"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        Assign(
                                            ArrayCell(
                                                FieldAccess(Id("Anime"), Id("OP")),
                                                IntLiteral(1),
                                            ),
                                            StringLiteral("Nightmare"),
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 331))

    def test32(self):
        input = r"""
            class main {
                func test():void {
                    if true {
                        return;
                    }
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("test"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        If(
                                            BooleanLiteral(True),
                                            Block([Return(None)]),
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 332))

    def test33(self):
        input = r"""
            class main {
                func test():int {
                    if true {
                        return 1;
                    }
                    else{
                        return 2;
                    }
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("test"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        If(
                                            BooleanLiteral(True),
                                            Block([Return(IntLiteral(1))]),
                                            None,
                                            Block([Return(IntLiteral(2))]),
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 333))

    def test34(self):
        input = r"""
            class main {
                func test():void {
                    if {t := 2;} true {
                        a := 1;
                    }
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("test"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        If(
                                            BooleanLiteral(True),
                                            Block([Assign(Id("a"), IntLiteral(1))]),
                                            Block([Assign(Id("t"), IntLiteral(2))]),
                                            None,
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 334))

    def test35(self):
        input = r"""
            class main {
                func test():void {
                    for i := 0; true; i := i + 1 {
                        a := a + 2;
                    }
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("test"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        For(
                                            Assign(Id("i"), IntLiteral(0)),
                                            BooleanLiteral(True),
                                            Assign(
                                                Id("i"),
                                                BinaryOp("+", Id("i"), IntLiteral(1)),
                                            ),
                                            Block(
                                                [
                                                    Assign(
                                                        Id("a"),
                                                        BinaryOp(
                                                            "+", Id("a"), IntLiteral(2)
                                                        ),
                                                    )
                                                ]
                                            ),
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 335))

    def test36(self):
        input = r"""
            class main {
                func test():void {
                    Aquapex.getLP();
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("test"),
                                [],
                                VoidType(),
                                Block([CallStmt(Id("Aquapex"), Id("getLP"), [])]),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 336))

    def test37(self):
        input = r"""
            class main {
                func test():void {
                    Aquapex.getLP(K, D);
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("test"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        CallStmt(
                                            Id("Aquapex"),
                                            Id("getLP"),
                                            [Id("K"), Id("D")],
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 337))

    def test38(self):
        input = r"""
            class main {
                func test():void {
                    Aquapex.getLP(@graph(gain));
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("test"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        CallStmt(
                                            Id("Aquapex"),
                                            Id("getLP"),
                                            [
                                                CallExpr(
                                                    None, Id("@graph"), [Id("gain")]
                                                )
                                            ],
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 338))

    def test39(self):
        input = r"""
            class main {
                func test():void {
                    @Aquapex.getLP(@graph(gain));
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("test"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        CallStmt(
                                            FieldAccess(None, Id("@Aquapex")),
                                            Id("getLP"),
                                            [
                                                CallExpr(
                                                    None, Id("@graph"), [Id("gain")]
                                                )
                                            ],
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 339))

    def test40(self):
        input = r"""
            class main {
                func test():void {
                    @Aquapex.getLP(gain.graph());
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("test"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        CallStmt(
                                            FieldAccess(None, Id("@Aquapex")),
                                            Id("getLP"),
                                            [CallExpr(Id("gain"), Id("graph"), [])],
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 340))

    def test41(self):
        input = r"""
            class main {
                func test():void {
                    const a, b: int = 420, 69;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("test"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        ConstDecl(Id("a"), IntType(), IntLiteral(420)),
                                        ConstDecl(Id("b"), IntType(), IntLiteral(69)),
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 341))

    def test42(self):
        input = r"""
            class main {
                func test():void {
                    var a,b:[3]Anime = [1, 2, 3], [4,5,6];
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("test"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("a"),
                                            ArrayType(3, ClassType(Id("Anime"))),
                                            ArrayLiteral(
                                                [
                                                    IntLiteral(1),
                                                    IntLiteral(2),
                                                    IntLiteral(3),
                                                ]
                                            ),
                                        ),
                                        VarDecl(
                                            Id("b"),
                                            ArrayType(3, ClassType(Id("Anime"))),
                                            ArrayLiteral(
                                                [
                                                    IntLiteral(4),
                                                    IntLiteral(5),
                                                    IntLiteral(6),
                                                ]
                                            ),
                                        ),
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 342))

    def test43(self):
        input = r"""class main {
            func test():void{
                why[5-x.how(exist && !exist)] := what[when[2+l]]+where;
            }
        }"""
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("test"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        Assign(
                                            ArrayCell(
                                                Id("why"),
                                                BinaryOp(
                                                    "-",
                                                    IntLiteral(5),
                                                    CallExpr(
                                                        Id("x"),
                                                        Id("how"),
                                                        [
                                                            BinaryOp(
                                                                "&&",
                                                                Id("exist"),
                                                                UnaryOp(
                                                                    "!",
                                                                    Id("exist"),
                                                                ),
                                                            )
                                                        ],
                                                    ),
                                                ),
                                            ),
                                            BinaryOp(
                                                "+",
                                                ArrayCell(
                                                    Id("what"),
                                                    ArrayCell(
                                                        Id("when"),
                                                        BinaryOp(
                                                            "+", IntLiteral(2), Id("l")
                                                        ),
                                                    ),
                                                ),
                                                Id("where"),
                                            ),
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 343))

    def test44(self):
        input = r"""
            class main {
                func test():void {
                    aqua.legend[0] := aqua.weapon()[1] + aqua.skill[2].getLvl();
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("test"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        Assign(
                                            ArrayCell(
                                                FieldAccess(Id("aqua"), Id("legend")),
                                                IntLiteral(0),
                                            ),
                                            BinaryOp(
                                                "+",
                                                ArrayCell(
                                                    CallExpr(
                                                        Id("aqua"), Id("weapon"), []
                                                    ),
                                                    IntLiteral(1),
                                                ),
                                                CallExpr(
                                                    ArrayCell(
                                                        FieldAccess(
                                                            Id("aqua"), Id("skill")
                                                        ),
                                                        IntLiteral(2),
                                                    ),
                                                    Id("getLvl"),
                                                    [],
                                                ),
                                            ),
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 344))

    def test45(self):
        input = r"""
            class main {
                func test():void {
                    if {x := 0;} y > x {y := y - 1;} else {y := y + 1;}
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("test"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        If(
                                            BinaryOp(">", Id("y"), Id("x")),
                                            Block(
                                                [
                                                    Assign(
                                                        Id("y"),
                                                        BinaryOp(
                                                            "-", Id("y"), IntLiteral(1)
                                                        ),
                                                    )
                                                ]
                                            ),
                                            Block([Assign(Id("x"), IntLiteral(0))]),
                                            Block(
                                                [
                                                    Assign(
                                                        Id("y"),
                                                        BinaryOp(
                                                            "+", Id("y"), IntLiteral(1)
                                                        ),
                                                    )
                                                ]
                                            ),
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 345))

    def test46(self):
        input = r"""
            class main {
                func test():void {
                    const n:int = 10;
                    for i := 0; i < n; i := i + 1 {
                        io.@print(i);
                    }
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("test"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        ConstDecl(Id("n"), IntType(), IntLiteral(10)),
                                        For(
                                            Assign(Id("i"), IntLiteral(0)),
                                            BinaryOp("<", Id("i"), Id("n")),
                                            Assign(
                                                Id("i"),
                                                BinaryOp("+", Id("i"), IntLiteral(1)),
                                            ),
                                            Block(
                                                [
                                                    CallStmt(
                                                        Id("io"),
                                                        Id("@print"),
                                                        [Id("i")],
                                                    )
                                                ]
                                            ),
                                        ),
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 346))

    def test47(self):
        input = r"""
            class main {
                func constructor() {
                    for i := 0; i < n; i := i + 1 {
                        if a[i] > k {break;}
                        a[i] := k - i;
                    }
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("constructor"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        For(
                                            Assign(Id("i"), IntLiteral(0)),
                                            BinaryOp("<", Id("i"), Id("n")),
                                            Assign(
                                                Id("i"),
                                                BinaryOp("+", Id("i"), IntLiteral(1)),
                                            ),
                                            Block(
                                                [
                                                    If(
                                                        BinaryOp(
                                                            ">",
                                                            ArrayCell(Id("a"), Id("i")),
                                                            Id("k"),
                                                        ),
                                                        Block([Break()]),
                                                        None,
                                                        None,
                                                    ),
                                                    Assign(
                                                        ArrayCell(Id("a"), Id("i")),
                                                        BinaryOp("-", Id("k"), Id("i")),
                                                    ),
                                                ]
                                            ),
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 347))

    def test48(self):
        input = r"""
            class main {
                func test():void {}
                func @error():bool {
                    return false;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(Id("test"), [], VoidType(), Block([])),
                            MethodDecl(
                                Id("@error"),
                                [],
                                BoolType(),
                                Block([Return(BooleanLiteral(False))]),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 348))

    def test49(self):
        input = r"""
            class main {
                const a:Anime = new Anime(44.5);
                func test():void{}
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                ConstDecl(
                                    Id("a"),
                                    ClassType(Id("Anime")),
                                    NewExpr(Id("Anime"), [FloatLiteral(44.5)]),
                                )
                            ),
                            MethodDecl(Id("test"), [], VoidType(), Block([])),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 349))

    def test50(self):
        input = r"""
            class main {
                func constructor(a,b,c: int) {}
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("constructor"),
                                [
                                    VarDecl(Id("a"), IntType()),
                                    VarDecl(Id("b"), IntType()),
                                    VarDecl(Id("c"), IntType()),
                                ],
                                VoidType(),
                                Block([]),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 350))

    def test51(self):
        input = r"""
            class main {
                func constructor(a,b: int, c: float) {}
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("constructor"),
                                [
                                    VarDecl(Id("a"), IntType()),
                                    VarDecl(Id("b"), IntType()),
                                    VarDecl(Id("c"), FloatType()),
                                ],
                                VoidType(),
                                Block([]),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 351))

    def test52(self):
        input = r"""
            class main {
                func constructor() {
                    for i := 0; i < n; i := i + 1 {
                        if a[i] > k {continue;}
                        a[i] := k * i;
                    }
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("constructor"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        For(
                                            Assign(Id("i"), IntLiteral(0)),
                                            BinaryOp("<", Id("i"), Id("n")),
                                            Assign(
                                                Id("i"),
                                                BinaryOp("+", Id("i"), IntLiteral(1)),
                                            ),
                                            Block(
                                                [
                                                    If(
                                                        BinaryOp(
                                                            ">",
                                                            ArrayCell(Id("a"), Id("i")),
                                                            Id("k"),
                                                        ),
                                                        Block([Continue()]),
                                                        None,
                                                        None,
                                                    ),
                                                    Assign(
                                                        ArrayCell(Id("a"), Id("i")),
                                                        BinaryOp("*", Id("k"), Id("i")),
                                                    ),
                                                ]
                                            ),
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 352))

    def test53(self):
        input = r"""
            class main {
                func constructor(a,b:Holo, c,d:Niji) {}
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("constructor"),
                                [
                                    VarDecl(Id("a"), ClassType(Id("Holo"))),
                                    VarDecl(Id("b"), ClassType(Id("Holo"))),
                                    VarDecl(Id("c"), ClassType(Id("Niji"))),
                                    VarDecl(Id("d"), ClassType(Id("Niji"))),
                                ],
                                VoidType(),
                                Block([]),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 353))

    def test54(self):
        input = r"""
            class main {
                var t:int = null;
                func constructor() {
                    var a:string = self.t;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(VarDecl(Id("t"), IntType(), NullLiteral())),
                            MethodDecl(
                                Id("constructor"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("a"),
                                            StringType(),
                                            FieldAccess(SelfLiteral(), Id("t")),
                                        )
                                    ]
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 354))

    def test55(self):
        input = r"""
            class main {
                func constructor() {
                    var a:string = "nijinigger";
                    for i := 1; false; i := true || i {
                        @hologod(a);
                    }
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("constructor"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("a"),
                                            StringType(),
                                            StringLiteral("nijinigger"),
                                        ),
                                        For(
                                            Assign(Id("i"), IntLiteral(1)),
                                            BooleanLiteral(False),
                                            Assign(
                                                Id("i"),
                                                BinaryOp(
                                                    "||", BooleanLiteral(True), Id("i")
                                                ),
                                            ),
                                            Block(
                                                [
                                                    CallStmt(
                                                        None, Id("@hologod"), [Id("a")]
                                                    )
                                                ]
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 355))

    def test56(self):
        input = r"""
            class main {
                func constructor() {
                    for i := 1; true; i := i + 1 {
                        return @hologod(a);
                    }
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("constructor"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        For(
                                            Assign(Id("i"), IntLiteral(1)),
                                            BooleanLiteral(True),
                                            Assign(
                                                Id("i"),
                                                BinaryOp("+", Id("i"), IntLiteral(1)),
                                            ),
                                            Block(
                                                [
                                                    Return(
                                                        CallExpr(
                                                            None,
                                                            Id("@hologod"),
                                                            [Id("a")],
                                                        )
                                                    )
                                                ]
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 356))

    def test57(self):
        input = r"""
            class main {
                func constructor() {
                    for i := 1; true; i := i + 1 {
                        for j := 1; true; j := j - 1 {
                            return i + j;
                        }
                    }
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("constructor"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        For(
                                            Assign(Id("i"), IntLiteral(1)),
                                            BooleanLiteral(True),
                                            Assign(
                                                Id("i"),
                                                BinaryOp("+", Id("i"), IntLiteral(1)),
                                            ),
                                            Block(
                                                [
                                                    For(
                                                        Assign(Id("j"), IntLiteral(1)),
                                                        BooleanLiteral(True),
                                                        Assign(
                                                            Id("j"),
                                                            BinaryOp(
                                                                "-",
                                                                Id("j"),
                                                                IntLiteral(1),
                                                            ),
                                                        ),
                                                        Block(
                                                            [
                                                                Return(
                                                                    BinaryOp(
                                                                        "+",
                                                                        Id("i"),
                                                                        Id("j"),
                                                                    )
                                                                )
                                                            ]
                                                        ),
                                                    )
                                                ]
                                            ),
                                        )
                                    ]
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 357))

    def test58(self):
        input = r"""
            class main {
                func constructor() {
                    if true {
                        for i := 1; true; i := i + 1 {
                            return i;
                        }
                    }
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("constructor"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        If(
                                            BooleanLiteral(True),
                                            Block(
                                                [
                                                    For(
                                                        Assign(Id("i"), IntLiteral(1)),
                                                        BooleanLiteral(True),
                                                        Assign(
                                                            Id("i"),
                                                            BinaryOp(
                                                                "+",
                                                                Id("i"),
                                                                IntLiteral(1),
                                                            ),
                                                        ),
                                                        Block([Return(Id("i"))]),
                                                    )
                                                ]
                                            ),
                                        )
                                    ]
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 358))

    def test59(self):
        input = r"""
            class main {
                func constructor() {
                    Hologod.Aqua.getSub();
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("constructor"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        CallStmt(
                                            FieldAccess(Id("Hologod"), Id("Aqua")),
                                            Id("getSub"),
                                            [],
                                        )
                                    ]
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 359))

    def test60(self):
        input = r"""
            class main {
                func constructor() {
                    @Hologod.Aqua.getSub();
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("constructor"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        CallStmt(
                                            FieldAccess(
                                                FieldAccess(None, Id("@Hologod")),
                                                Id("Aqua"),
                                            ),
                                            Id("getSub"),
                                            [],
                                        )
                                    ]
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 360))

    def test61(self):
        input = r"""
            class main {
                func constructor() {
                    Hologod[0].Aqua.getSub();
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("constructor"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        CallStmt(
                                            FieldAccess(
                                                ArrayCell(Id("Hologod"), IntLiteral(0)),
                                                Id("Aqua"),
                                            ),
                                            Id("getSub"),
                                            [],
                                        )
                                    ]
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 361))

    def test62(self):
        input = r"""
            class main {
                func constructor() {
                    Hologod.Aqua[0].getSub();
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("constructor"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        CallStmt(
                                            ArrayCell(
                                                FieldAccess(Id("Hologod"), Id("Aqua")),
                                                IntLiteral(0),
                                            ),
                                            Id("getSub"),
                                            [],
                                        )
                                    ]
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 362))

    def test63(self):
        input = r"""
            class main {
                func constructor() {
                    Hologod[0].Aqua[0].getSub();
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("constructor"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        CallStmt(
                                            ArrayCell(
                                                FieldAccess(
                                                    ArrayCell(
                                                        Id("Hologod"), IntLiteral(0)
                                                    ),
                                                    Id("Aqua"),
                                                ),
                                                IntLiteral(0),
                                            ),
                                            Id("getSub"),
                                            [],
                                        )
                                    ]
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 363))

    def test64(self):
        input = r"""
            class main {
                func constructor() {
                    Hologod[0] := a[0];
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("constructor"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        Assign(
                                            ArrayCell(
                                                Id("Hologod"),
                                                IntLiteral(0),
                                            ),
                                            ArrayCell(
                                                Id("a"),
                                                IntLiteral(0),
                                            ),
                                        )
                                    ]
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 364))

    def test65(self):
        input = r"""
            class main {
                func constructor() {
                    var Hologod: [1]int;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("constructor"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("Hologod"),
                                            ArrayType(1, IntType()),
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 365))

    def test66(self):
        input = r"""
            class main {
                func constructor() {
                    var Hologod: int = 1 + -2;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("constructor"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("Hologod"),
                                            IntType(),
                                            BinaryOp(
                                                "+",
                                                IntLiteral(1),
                                                UnaryOp("-", IntLiteral(2)),
                                            ),
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 366))

    def test67(self):
        input = r"""
            class main {
                func constructor() {
                    var Hologod: bool = a && !b;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("constructor"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("Hologod"),
                                            BoolType(),
                                            BinaryOp(
                                                "&&",
                                                Id("a"),
                                                UnaryOp("!", Id("b")),
                                            ),
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 367))

    def test68(self):
        input = r"""
            class main {
                func constructor() {
                    var Hologod: string = "a" + "b" ^ "c";
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("constructor"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("Hologod"),
                                            StringType(),
                                            BinaryOp(
                                                "^",
                                                BinaryOp(
                                                    "+",
                                                    StringLiteral("a"),
                                                    StringLiteral("b"),
                                                ),
                                                StringLiteral("c"),
                                            ),
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 368))

    def test69(self):
        input = r"""
            class main {
                func constructor() {
                    var Hologod: float = 1 - 2 / 3;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("constructor"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("Hologod"),
                                            FloatType(),
                                            BinaryOp(
                                                "-",
                                                IntLiteral(1),
                                                BinaryOp(
                                                    "/",
                                                    IntLiteral(2),
                                                    IntLiteral(3),
                                                ),
                                            ),
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 369))

    def test70(self):
        input = r"""
            class main {
                func constructor() {
                    self.Hologod().aqua();
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("constructor"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        CallStmt(
                                            CallExpr(SelfLiteral(), Id("Hologod"), []),
                                            Id("aqua"),
                                            [],
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 370))

    def test71(self):
        input = r"""
            class main {
                func constructor() {
                    self.Hologod()[0].aqua();
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("constructor"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        CallStmt(
                                            ArrayCell(
                                                CallExpr(
                                                    SelfLiteral(), Id("Hologod"), []
                                                ),
                                                IntLiteral(0),
                                            ),
                                            Id("aqua"),
                                            [],
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 371))

    def test72(self):
        input = r"""
            class main {
                func constructor() {
                    self.Hologod()[1+1].aqua();
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("constructor"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        CallStmt(
                                            ArrayCell(
                                                CallExpr(
                                                    SelfLiteral(), Id("Hologod"), []
                                                ),
                                                BinaryOp(
                                                    "+", IntLiteral(1), IntLiteral(1)
                                                ),
                                            ),
                                            Id("aqua"),
                                            [],
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 372))

    def test73(self):
        input = r"""
            class main {
                func constructor() {
                    self.Hologod()[@len(a)].aqua();
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("constructor"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        CallStmt(
                                            ArrayCell(
                                                CallExpr(
                                                    SelfLiteral(), Id("Hologod"), []
                                                ),
                                                CallExpr(None, Id("@len"), [Id("a")]),
                                            ),
                                            Id("aqua"),
                                            [],
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 373))

    def test74(self):
        input = r"""
            class main {
                func constructor() {
                    Hologod.aqua(@len(a));
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("constructor"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        CallStmt(
                                            Id("Hologod"),
                                            Id("aqua"),
                                            [
                                                CallExpr(None, Id("@len"), [Id("a")]),
                                            ],
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 374))

    def test75(self):
        input = r"""
            class main {
                var hologod:bool = !false;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                VarDecl(
                                    Id("hologod"),
                                    BoolType(),
                                    UnaryOp("!", BooleanLiteral(False)),
                                )
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 375))

    def test76(self):
        input = r"""
            class main {
                var hologod:bool = a != b;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                VarDecl(
                                    Id("hologod"),
                                    BoolType(),
                                    BinaryOp("!=", Id("a"), Id("b")),
                                )
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 376))

    def test77(self):
        input = r"""
            class main {
                var hologod:int = a \ b;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                VarDecl(
                                    Id("hologod"),
                                    IntType(),
                                    BinaryOp("\\", Id("a"), Id("b")),
                                )
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 377))

    def test78(self):
        input = r"""
            class main {
                var hologod:[3]int = [a, 1, a1];
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                VarDecl(
                                    Id("hologod"),
                                    ArrayType(3, IntType()),
                                    ArrayLiteral([Id("a"), IntLiteral(1), Id("a1")]),
                                )
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 378))

    def test79(self):
        input = r"""
            class main {
                var hologod:int = io.great;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                VarDecl(
                                    Id("hologod"),
                                    IntType(),
                                    FieldAccess(Id("io"), Id("great")),
                                )
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 379))

    def test80(self):
        input = r"""
            class main {
                var hologod:int = io.great();
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                VarDecl(
                                    Id("hologod"),
                                    IntType(),
                                    CallExpr(Id("io"), Id("great"), []),
                                )
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 380))

    def test81(self):
        input = r"""
            class main {
                var hologod:int = io.great().peak;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                VarDecl(
                                    Id("hologod"),
                                    IntType(),
                                    FieldAccess(
                                        CallExpr(Id("io"), Id("great"), []), Id("peak")
                                    ),
                                )
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 381))

    def test82(self):
        input = r"""
            class main {
                var hologod:int = io.great().peak[1];
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                VarDecl(
                                    Id("hologod"),
                                    IntType(),
                                    ArrayCell(
                                        FieldAccess(
                                            CallExpr(Id("io"), Id("great"), []),
                                            Id("peak"),
                                        ),
                                        IntLiteral(1),
                                    ),
                                )
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 382))

    def test83(self):
        input = r"""
            class main {
                var hologod:int = io.great().peak()[1];
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                VarDecl(
                                    Id("hologod"),
                                    IntType(),
                                    ArrayCell(
                                        CallExpr(
                                            CallExpr(Id("io"), Id("great"), []),
                                            Id("peak"),
                                            [],
                                        ),
                                        IntLiteral(1),
                                    ),
                                )
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 383))

    def test84(self):
        input = r"""
            class main {
                var hologod:int = io.great(a,b).peak()[1];
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                VarDecl(
                                    Id("hologod"),
                                    IntType(),
                                    ArrayCell(
                                        CallExpr(
                                            CallExpr(
                                                Id("io"),
                                                Id("great"),
                                                [Id("a"), Id("b")],
                                            ),
                                            Id("peak"),
                                            [],
                                        ),
                                        IntLiteral(1),
                                    ),
                                )
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 384))

    def test85(self):
        input = r"""
            class main {
                var hologod:bool = !a && b;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                VarDecl(
                                    Id("hologod"),
                                    BoolType(),
                                    BinaryOp("&&", UnaryOp("!", Id("a")), Id("b")),
                                )
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 385))

    def test86(self):
        input = r"""
            class main {
                var hologod:bool = !(a && b);
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                VarDecl(
                                    Id("hologod"),
                                    BoolType(),
                                    UnaryOp("!", BinaryOp("&&", Id("a"), Id("b"))),
                                )
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 386))

    def test87(self):
        input = r"""
            class main {
                var hologod:string = "onion" ^ "Aqua" + "=pred";
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                VarDecl(
                                    Id("hologod"),
                                    StringType(),
                                    BinaryOp(
                                        "^",
                                        StringLiteral("onion"),
                                        BinaryOp(
                                            "+",
                                            StringLiteral("Aqua"),
                                            StringLiteral("=pred"),
                                        ),
                                    ),
                                )
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 387))

    def test88(self):
        input = r"""
            class main {
                var hologod:string = ("onion" ^ "Aqua") + "=pred";
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                VarDecl(
                                    Id("hologod"),
                                    StringType(),
                                    BinaryOp(
                                        "+",
                                        BinaryOp(
                                            "^",
                                            StringLiteral("onion"),
                                            StringLiteral("Aqua"),
                                        ),
                                        StringLiteral("=pred"),
                                    ),
                                )
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 388))

    def test89(self):
        input = r"""
            class main {
                var hologod:float = a * b / c \ d % e;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            AttributeDecl(
                                VarDecl(
                                    Id("hologod"),
                                    FloatType(),
                                    BinaryOp(
                                        "%",
                                        BinaryOp(
                                            "\\",
                                            BinaryOp(
                                                "/",
                                                BinaryOp(
                                                    "*",
                                                    Id("a"),
                                                    Id("b"),
                                                ),
                                                Id("c"),
                                            ),
                                            Id("d"),
                                        ),
                                        Id("e"),
                                    ),
                                )
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 389))

    def test90(self):
        input = r"""
            class main {
                func max(arr:[10]int):int {
                    var max:int = arr[0];
                    for i:=1; i<10; i:=i+1 {
                        if arr[i] > max {
                            max := arr[i];
                        }
                    }
                    return max;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("max"),
                                [VarDecl(Id("arr"), ArrayType(10, IntType()), None)],
                                IntType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("max"),
                                            IntType(),
                                            ArrayCell(Id("arr"), IntLiteral(0)),
                                        ),
                                        For(
                                            Assign(Id("i"), IntLiteral(1)),
                                            BinaryOp("<", Id("i"), IntLiteral(10)),
                                            Assign(
                                                Id("i"),
                                                BinaryOp("+", Id("i"), IntLiteral(1)),
                                            ),
                                            Block(
                                                [
                                                    If(
                                                        BinaryOp(
                                                            ">",
                                                            ArrayCell(
                                                                Id("arr"), Id("i")
                                                            ),
                                                            Id("max"),
                                                        ),
                                                        Block(
                                                            [
                                                                Assign(
                                                                    Id("max"),
                                                                    ArrayCell(
                                                                        Id("arr"),
                                                                        Id("i"),
                                                                    ),
                                                                )
                                                            ]
                                                        ),
                                                    )
                                                ]
                                            ),
                                        ),
                                        Return(Id("max")),
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 390))

    def test91(self):
        input = r"""
            class main {
                func min(arr:[10]int):int {
                    var min:int = arr[0];
                    for i:=1; i<10; i:=i+1 {
                        if arr[i] < min {
                            min := arr[i];
                        }
                    }
                    return min;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("min"),
                                [VarDecl(Id("arr"), ArrayType(10, IntType()), None)],
                                IntType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("min"),
                                            IntType(),
                                            ArrayCell(Id("arr"), IntLiteral(0)),
                                        ),
                                        For(
                                            Assign(Id("i"), IntLiteral(1)),
                                            BinaryOp("<", Id("i"), IntLiteral(10)),
                                            Assign(
                                                Id("i"),
                                                BinaryOp("+", Id("i"), IntLiteral(1)),
                                            ),
                                            Block(
                                                [
                                                    If(
                                                        BinaryOp(
                                                            "<",
                                                            ArrayCell(
                                                                Id("arr"), Id("i")
                                                            ),
                                                            Id("min"),
                                                        ),
                                                        Block(
                                                            [
                                                                Assign(
                                                                    Id("min"),
                                                                    ArrayCell(
                                                                        Id("arr"),
                                                                        Id("i"),
                                                                    ),
                                                                )
                                                            ]
                                                        ),
                                                    )
                                                ]
                                            ),
                                        ),
                                        Return(Id("min")),
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 391))

    def test92(self):
        input = r"""
            class main {
                func prime(arr:[10]int):void {
                    for i := 0; i < 10; i := i + 1 {
                        if self.isPrime(arr[i]) {
                            @print(arr[i]);
                        }
                    }
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("prime"),
                                [VarDecl(Id("arr"), ArrayType(10, IntType()), None)],
                                VoidType(),
                                Block(
                                    [
                                        For(
                                            Assign(Id("i"), IntLiteral(0)),
                                            BinaryOp("<", Id("i"), IntLiteral(10)),
                                            Assign(
                                                Id("i"),
                                                BinaryOp("+", Id("i"), IntLiteral(1)),
                                            ),
                                            Block(
                                                [
                                                    If(
                                                        CallExpr(
                                                            SelfLiteral(),
                                                            Id("isPrime"),
                                                            [
                                                                ArrayCell(
                                                                    Id("arr"), Id("i")
                                                                )
                                                            ],
                                                        ),
                                                        Block(
                                                            [
                                                                CallStmt(
                                                                    None,
                                                                    Id("@print"),
                                                                    [
                                                                        ArrayCell(
                                                                            Id("arr"),
                                                                            Id("i"),
                                                                        )
                                                                    ],
                                                                )
                                                            ]
                                                        ),
                                                    )
                                                ]
                                            ),
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 392))

    def test93(self):
        input = r"""
            class main {
                func isPrime(a:int):bool {
                    if a < 2 {
                        return false;
                    }
                    for i := 2 ; i * i <= a; i := i + 1 {
                        if a % i == 0 {
                            return false;
                        }
                    }
                    return true;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("isPrime"),
                                [VarDecl(Id("a"), IntType(), None)],
                                BoolType(),
                                Block(
                                    [
                                        If(
                                            BinaryOp("<", Id("a"), IntLiteral(2)),
                                            Block([Return(BooleanLiteral(False))]),
                                        ),
                                        For(
                                            Assign(Id("i"), IntLiteral(2)),
                                            BinaryOp(
                                                "<=",
                                                BinaryOp("*", Id("i"), Id("i")),
                                                Id("a"),
                                            ),
                                            Assign(
                                                Id("i"),
                                                BinaryOp("+", Id("i"), IntLiteral(1)),
                                            ),
                                            Block(
                                                [
                                                    If(
                                                        BinaryOp(
                                                            "==",
                                                            BinaryOp(
                                                                "%", Id("a"), Id("i")
                                                            ),
                                                            IntLiteral(0),
                                                        ),
                                                        Block(
                                                            [
                                                                Return(
                                                                    BooleanLiteral(
                                                                        False
                                                                    )
                                                                )
                                                            ]
                                                        ),
                                                    )
                                                ]
                                            ),
                                        ),
                                        Return(BooleanLiteral(True)),
                                    ]
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 393))

    def test94(self):
        input = r"""
            class main {
                func fibo(n:int):int {
                    if n == 0 {
                        return 0;
                    }
                    if n == 1 {
                        return 1;
                    }
                    var a, b:int = 0, 1;
                    var c:int;
                    for i := 2; i <= n; i := i + 1 {
                        c := a + b;
                        a := b;
                        b := c;
                    }
                    return b;
                
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("fibo"),
                                [VarDecl(Id("n"), IntType(), None)],
                                IntType(),
                                Block(
                                    [
                                        If(
                                            BinaryOp("==", Id("n"), IntLiteral(0)),
                                            Block([Return(IntLiteral(0))]),
                                        ),
                                        If(
                                            BinaryOp("==", Id("n"), IntLiteral(1)),
                                            Block([Return(IntLiteral(1))]),
                                        ),
                                        VarDecl(Id("a"), IntType(), IntLiteral(0)),
                                        VarDecl(Id("b"), IntType(), IntLiteral(1)),
                                        VarDecl(Id("c"), IntType(), None),
                                        For(
                                            Assign(Id("i"), IntLiteral(2)),
                                            BinaryOp("<=", Id("i"), Id("n")),
                                            Assign(
                                                Id("i"),
                                                BinaryOp("+", Id("i"), IntLiteral(1)),
                                            ),
                                            Block(
                                                [
                                                    Assign(
                                                        Id("c"),
                                                        BinaryOp("+", Id("a"), Id("b")),
                                                    ),
                                                    Assign(Id("a"), Id("b")),
                                                    Assign(Id("b"), Id("c")),
                                                ]
                                            ),
                                        ),
                                        Return(Id("b")),
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 394))

    def test95(self):
        input = r"""
            class main {
                func reverse(str:string):void {
                    var len:int = str.length();
                    for i := len - 1; i >= 0; i := i - 1 {
                        @print(str[i]);
                    }
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("reverse"),
                                [VarDecl(Id("str"), StringType(), None)],
                                VoidType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("len"),
                                            IntType(),
                                            CallExpr(Id("str"), Id("length"), []),
                                        ),
                                        For(
                                            Assign(
                                                Id("i"),
                                                BinaryOp("-", Id("len"), IntLiteral(1)),
                                            ),
                                            BinaryOp(">=", Id("i"), IntLiteral(0)),
                                            Assign(
                                                Id("i"),
                                                BinaryOp("-", Id("i"), IntLiteral(1)),
                                            ),
                                            Block(
                                                [
                                                    CallStmt(
                                                        None,
                                                        Id("@print"),
                                                        [ArrayCell(Id("str"), Id("i"))],
                                                    ),
                                                ]
                                            ),
                                        ),
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 395))

    def test96(self):
        input = r"""
            class main {
                func reverse(arr:[5]string):void {
                    for i := 4; i >= 0; i := i - 1 {
                        @print(arr[i]);
                    }
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("reverse"),
                                [VarDecl(Id("arr"), ArrayType(5, StringType()), None)],
                                VoidType(),
                                Block(
                                    [
                                        For(
                                            Assign(Id("i"), IntLiteral(4)),
                                            BinaryOp(">=", Id("i"), IntLiteral(0)),
                                            Assign(
                                                Id("i"),
                                                BinaryOp("-", Id("i"), IntLiteral(1)),
                                            ),
                                            Block(
                                                [
                                                    CallStmt(
                                                        None,
                                                        Id("@print"),
                                                        [ArrayCell(Id("arr"), Id("i"))],
                                                    ),
                                                ]
                                            ),
                                        )
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 396))

    def test97(self):
        input = r"""
            class main {
                func sumArr(arr:[10]int):int {
                    var sum:int = 0;
                    for i := 0; i < 10; i := i + 1 {
                        sum := sum + arr[i];
                    }
                    return sum;
                }
            }

        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("sumArr"),
                                [VarDecl(Id("arr"), ArrayType(10, IntType()), None)],
                                IntType(),
                                Block(
                                    [
                                        VarDecl(Id("sum"), IntType(), IntLiteral(0)),
                                        For(
                                            Assign(Id("i"), IntLiteral(0)),
                                            BinaryOp("<", Id("i"), IntLiteral(10)),
                                            Assign(
                                                Id("i"),
                                                BinaryOp("+", Id("i"), IntLiteral(1)),
                                            ),
                                            Block(
                                                [
                                                    Assign(
                                                        Id("sum"),
                                                        BinaryOp(
                                                            "+",
                                                            Id("sum"),
                                                            ArrayCell(
                                                                Id("arr"), Id("i")
                                                            ),
                                                        ),
                                                    )
                                                ]
                                            ),
                                        ),
                                        Return(Id("sum")),
                                    ]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 397))

    def test98(self):
        input = r"""
            class main {
                func fact(n:int):int {
                    if n == 0 {
                        return 1;
                    }
                    else {
                        return n * self.fact(n - 1);
                    }
                }
                
                func @main():void {
                    var n:int;
                    n := 5;
                    @print(self.fact(n));
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("main"),
                        [
                            MethodDecl(
                                Id("fact"),
                                [VarDecl(Id("n"), IntType(), None)],
                                IntType(),
                                Block(
                                    [
                                        If(
                                            BinaryOp("==", Id("n"), IntLiteral(0)),
                                            Block([Return(IntLiteral(1))]),
                                            None,
                                            Block(
                                                [
                                                    Return(
                                                        BinaryOp(
                                                            "*",
                                                            Id("n"),
                                                            CallExpr(
                                                                SelfLiteral(),
                                                                Id("fact"),
                                                                [
                                                                    BinaryOp(
                                                                        "-",
                                                                        Id("n"),
                                                                        IntLiteral(1),
                                                                    )
                                                                ],
                                                            ),
                                                        )
                                                    )
                                                ]
                                            ),
                                        )
                                    ]
                                ),
                            ),
                            MethodDecl(
                                Id("@main"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        VarDecl(Id("n"), IntType(), None),
                                        Assign(Id("n"), IntLiteral(5)),
                                        CallStmt(
                                            None,
                                            Id("@print"),
                                            [
                                                CallExpr(
                                                    SelfLiteral(), Id("fact"), [Id("n")]
                                                )
                                            ],
                                        ),
                                    ]
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 398))

    def test99(self):
        input = r"""
            class Program {
                var x, y, z: int = -2, 2*4, 5%(6-2) + ab;
                func @fact(n: int):int {
                    if {i := 1;} n == 0 { Shape.lst.getSize(); }
                    else {return n * @fact(n - 1);}
                }
                func @inc(n, delta: int):int {
                    n := n + delta;
                    return n;
                }
                func @main():int {
                    var delta: int = @fact(3);
                    @inc(self.x, delta);
                    io.@writeInt(self.x);
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Program"),
                        [
                            AttributeDecl(
                                VarDecl(Id("x"), IntType(), UnaryOp("-", IntLiteral(2)))
                            ),
                            AttributeDecl(
                                VarDecl(
                                    Id("y"),
                                    IntType(),
                                    BinaryOp("*", IntLiteral(2), IntLiteral(4)),
                                )
                            ),
                            AttributeDecl(
                                VarDecl(
                                    Id("z"),
                                    IntType(),
                                    BinaryOp(
                                        "+",
                                        BinaryOp(
                                            "%",
                                            IntLiteral(5),
                                            BinaryOp("-", IntLiteral(6), IntLiteral(2)),
                                        ),
                                        Id("ab"),
                                    ),
                                )
                            ),
                            MethodDecl(
                                Id("@fact"),
                                [VarDecl(Id("n"), IntType(), None)],
                                IntType(),
                                Block(
                                    [
                                        If(
                                            BinaryOp("==", Id("n"), IntLiteral(0)),
                                            Block(
                                                [
                                                    CallStmt(
                                                        FieldAccess(
                                                            Id("Shape"), Id("lst")
                                                        ),
                                                        Id("getSize"),
                                                        [],
                                                    )
                                                ]
                                            ),
                                            Block([Assign(Id("i"), IntLiteral(1))]),
                                            Block(
                                                [
                                                    Return(
                                                        BinaryOp(
                                                            "*",
                                                            Id("n"),
                                                            CallExpr(
                                                                None,
                                                                Id("@fact"),
                                                                [
                                                                    BinaryOp(
                                                                        "-",
                                                                        Id("n"),
                                                                        IntLiteral(1),
                                                                    )
                                                                ],
                                                            ),
                                                        )
                                                    )
                                                ]
                                            ),
                                        )
                                    ]
                                ),
                            ),
                            MethodDecl(
                                Id("@inc"),
                                [
                                    VarDecl(Id("n"), IntType(), None),
                                    VarDecl(Id("delta"), IntType(), None),
                                ],
                                IntType(),
                                Block(
                                    [
                                        Assign(
                                            Id("n"), BinaryOp("+", Id("n"), Id("delta"))
                                        ),
                                        Return(Id("n")),
                                    ]
                                ),
                            ),
                            MethodDecl(
                                Id("@main"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("delta"),
                                            IntType(),
                                            CallExpr(
                                                None,
                                                Id("@fact"),
                                                [IntLiteral(3)],
                                            ),
                                        ),
                                        CallStmt(
                                            None,
                                            Id("@inc"),
                                            [
                                                FieldAccess(SelfLiteral(), Id("x")),
                                                Id("delta"),
                                            ],
                                        ),
                                        CallStmt(
                                            Id("io"),
                                            Id("@writeInt"),
                                            [FieldAccess(SelfLiteral(), Id("x"))],
                                        ),
                                    ]
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 399))
