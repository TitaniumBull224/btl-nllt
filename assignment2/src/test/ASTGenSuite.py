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
                    ClassDecl(Id("testing"), []),
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
            class Child <- Parent {
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
            
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 311))

    def test12(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 312))

    def test13(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 313))

    def test14(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 314))

    def test15(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 315))

    def test16(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 316))

    def test17(self):
        input = r"""
            class main {

            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 317))

    def test18(self):
        input = r"""
            class main {

            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 318))

    def test19(self):
        input = r"""
            class main {

            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 319))

    def test20(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 320))

    def test21(self):
        input = r"""
            class main {
            
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 321))

    def test22(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 322))

    def test23(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 323))

    def test24(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 324))

    def test25(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 325))

    def test26(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 326))

    def test27(self):
        input = r"""
            class main {

            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 327))

    def test28(self):
        input = r"""
            class main {

            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 328))

    def test29(self):
        input = r"""
            class main {

            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 329))

    def test30(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 330))

    def test33(self):
        input = r"""
            class main {
            
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 331))

    def test32(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 332))

    def test33(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 333))

    def test34(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 334))

    def test35(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 335))

    def test36(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 336))

    def test37(self):
        input = r"""
            class main {

            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 337))

    def test38(self):
        input = r"""
            class main {

            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 338))

    def test39(self):
        input = r"""
            class main {

            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 339))

    def test40(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 340))

    def test41(self):
        input = r"""
            class main {
            
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 341))

    def test42(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 342))

    def test43(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 343))

    def test44(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 344))

    def test45(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 345))

    def test46(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 346))

    def test47(self):
        input = r"""
            class main {

            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 347))

    def test48(self):
        input = r"""
            class main {

            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 348))

    def test49(self):
        input = r"""
            class main {

            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 349))

    def test50(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 350))

    def test51(self):
        input = r"""
            class main {
            
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 351))

    def test52(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 352))

    def test53(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 353))

    def test54(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 354))

    def test55(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 355))

    def test56(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 356))

    def test57(self):
        input = r"""
            class main {

            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 357))

    def test58(self):
        input = r"""
            class main {

            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 358))

    def test59(self):
        input = r"""
            class main {

            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 359))

    def test60(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 360))

    def test61(self):
        input = r"""
            class main {
            
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 361))

    def test62(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 362))

    def test63(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 363))

    def test64(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 364))

    def test65(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 365))

    def test66(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 366))

    def test67(self):
        input = r"""
            class main {

            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 367))

    def test68(self):
        input = r"""
            class main {

            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 368))

    def test69(self):
        input = r"""
            class main {

            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 369))

    def test70(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 370))

    def test71(self):
        input = r"""
            class main {
            
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 371))

    def test72(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 372))

    def test73(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 373))

    def test74(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 374))

    def test75(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 375))

    def test76(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 376))

    def test77(self):
        input = r"""
            class main {

            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 377))

    def test78(self):
        input = r"""
            class main {

            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 378))

    def test79(self):
        input = r"""
            class main {

            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 379))

    def test80(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 380))

    def test81(self):
        input = r"""
            class main {
            
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 381))

    def test82(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 382))

    def test83(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 383))

    def test84(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 384))

    def test85(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 385))

    def test86(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 386))

    def test87(self):
        input = r"""
            class main {

            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 387))

    def test88(self):
        input = r"""
            class main {

            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 388))

    def test89(self):
        input = r"""
            class main {

            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 389))

    def test90(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 390))

    def test91(self):
        input = r"""
            class main {
            
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 391))

    def test92(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 392))

    def test93(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 393))

    def test94(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 394))

    def test95(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 395))

    def test96(self):
        input = r"""
            class main {
                
            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 396))

    def test97(self):
        input = r"""
            class main {

            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 397))

    def test98(self):
        input = r"""
            class main {

            }
        """
        expect = str(...)
        self.assertTrue(TestAST.test(input, expect, 398))

    def test99(self):
        input = r"""
            class Program {
                var x, y, z: int = 2, 2*4, 5%(6-2) + ab;
                func @fact(n: int):int {
                    if {i := 1;} n == 0 { Shape.lst.getSize(); }
                    else {return n * @fact(n - 1);}
                }
                func @inc( n, delta: int):void {
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
        expect = ...
        self.assertTrue(TestAST.test(input, expect, 399))
