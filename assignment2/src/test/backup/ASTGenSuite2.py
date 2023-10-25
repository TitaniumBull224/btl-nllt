import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):

    # def test_simple_program(self):
    #     """Simple program: class main {} """
    #     input = """class main {}"""
    #     expect = str(Program([ClassDecl(Id("main"),[])]))
    #     self.assertTrue(TestAST.test(input,expect,300))

    # def test_class_with_one_decl_program(self):
    #     """More complex program"""
    #     input = """class main {
    #         var a:int;
    #     }"""
    #     expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType()))])]))
    #     self.assertTrue(TestAST.test(input,expect,301))
    
    # def test_class_with_two_decl_program(self):
    #     """More complex program"""
    #     input = """class main {
    #         var a:int;
    #         var b:int;
    #     }"""
    #     expect = str(Program([ClassDecl(Id("main"),
    #         [AttributeDecl(VarDecl(Id("a"),IntType())),
    #          AttributeDecl(VarDecl(Id("b"),IntType()))])]))
    #     self.assertTrue(TestAST.test(input,expect,302))
    
    def test_simple_program(self):
        """Simple program: class main {} """
        input = """class main {} class testing{}"""
        expect = str(Program([ClassDecl(Id("main"),[]),ClassDecl(Id("testing"),[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_class_with_one_decl_program(self):
        """More complex program"""
        input = """class main {
            var a:int;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_class_with_two_decl_program(self):
        """More complex program"""
        input = """class main {
            var a,t:int;
            var b:int;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(VarDecl(Id("a"),IntType())),
             AttributeDecl(VarDecl(Id("t"),IntType())),
             AttributeDecl(VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_const_values(self):
        """More complex program"""
        input = """class main {
            const a,b: [5]int = 5,6;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(ConstDecl(Id("a"),ArrayType(5,IntType()),IntLiteral(5))),
             AttributeDecl(ConstDecl(Id("b"),ArrayType(5,IntType()),IntLiteral(6)))])]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_var_values(self):
        """More complex program"""
        input = """class main {
            var a,b: [5]int = 5,6;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(VarDecl(Id("a"),ArrayType(5,IntType()),IntLiteral(5))),
             AttributeDecl(VarDecl(Id("b"),ArrayType(5,IntType()),IntLiteral(6)))])]))
        self.assertTrue(TestAST.test(input,expect,304))

    def test_var_no_value(self):
        """More complex program"""
        input = """class main {
            var a,b: [5]int;
            const c: string = 5;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(VarDecl(Id("a"),ArrayType(5,IntType()))),
             AttributeDecl(VarDecl(Id("b"),ArrayType(5,IntType()))),
             AttributeDecl(ConstDecl(Id("c"),StringType(),IntLiteral(5)))])]))
        self.assertTrue(TestAST.test(input,expect,305))

    def test_func_add(self):
        """More complex program"""
        input = """class main {
            func @test(a, b:int,t:[5]string):void{
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("@test"),
                    [
                        VarDecl(Id("a"),IntType()),
                        VarDecl(Id("b"),IntType()),
                        VarDecl(Id("t"),ArrayType(5,StringType()))
                    ],
                    VoidType(),
                    Block([])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,306))
    
    def test_func_no_param(self):
        """More complex program"""
        input = """class main {
            func @test():Shape{
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("@test"),
                    [
                        
                    ],
                    ClassType(Id("Shape")),
                    Block([])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,307))
    
    def test_type_int(self):
        """More complex program"""
        input = """class main {
            var a:int;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(VarDecl(Id("a"),IntType()))
             ])]))
        self.assertTrue(TestAST.test(input,expect,308))
    
    def test_type_string(self):
        """More complex program"""
        input = """class main {
            const a:string = "22";
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(ConstDecl(Id("a"),StringType(),StringLiteral("22")))
             ])]))
        self.assertTrue(TestAST.test(input,expect,309))
    
    def test_type_ID(self):
        """More complex program"""
        input = """class main {
            const a:Shape = "22";
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(ConstDecl(Id("a"),ClassType(Id("Shape")),StringLiteral("22")))
             ])]))
        self.assertTrue(TestAST.test(input,expect,310))
   
    def test_arr_type(self):
        """More complex program"""
        input = """class main {
            const a:[5]Shape = "22";
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(ConstDecl(Id("a"),ArrayType(5,ClassType(Id("Shape"))),StringLiteral("22")))
             ])]))
        self.assertTrue(TestAST.test(input,expect,311))

    def test_func_return_void(self):
        """More complex program"""
        input = """class main {
            func test():void{
                return;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("test"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        Return(None)
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,312))
    
    def test_func_return_int(self):
        """More complex program"""
        input = """class main {
            func test():void{
                return 5;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("test"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        Return(IntLiteral(5))
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,313))

    def test_concat(self):
        """More complex program"""
        input = """class main {
            var a:string = "2"^"5";
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    BinaryOp("^",StringLiteral("2"),StringLiteral("5"))
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,314))
    
    def test_expr1(self):
        """More complex program"""
        input = """class main {
            var a:string = "2";
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    StringLiteral("2")
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,315))
    
    def test_eqop(self):
        """More complex program"""
        input = """class main {
            var a:string = et == 69;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    BinaryOp("==",Id("et"),IntLiteral(69))
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,316))
    
    def test_noteqop(self):
        """More complex program"""
        input = """class main {
            var a:string = t != 6;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    BinaryOp("!=",Id("t"),IntLiteral(6))
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,317))
    
    def test_less_lesseq(self):
        """More complex program"""
        input = """class main {
            var a:string = t < 5;
            var b:string = t <= 5;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    BinaryOp("<",Id("t"),IntLiteral(5))
                )),
                AttributeDecl(VarDecl(
                    Id("b"),
                    StringType(),
                    BinaryOp("<=",Id("t"),IntLiteral(5))
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,318))

    def test_lar_lareq(self):
        """More complex program"""
        input = """class main {
            var a:string = t > 5;
            var b:string = t >= 5;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    BinaryOp(">",Id("t"),IntLiteral(5))
                )),
                AttributeDecl(VarDecl(
                    Id("b"),
                    StringType(),
                    BinaryOp(">=",Id("t"),IntLiteral(5))
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,319))
    
    def test_log_op(self):
        """More complex program"""
        input = """class main {
            var a:string = a && b || c;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    BinaryOp(
                        "||",
                        BinaryOp("&&",Id("a"),Id("b")),
                        Id("c")
                    )
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,320))
    
    def test_final_expr(self):
        """More complex program"""
        input = """class main {
            var a:string = a;
        }"""
        expect =str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    Id("a")
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,321))
    
    def test_expr3(self):
        """More complex program"""
        input = """class main {
            var a:string = a + b -c;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    BinaryOp(
                        "-",
                        BinaryOp("+",Id("a"),Id("b")),
                        Id("c")
                    )
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,322))
    
    def test_expr4_1(self):
        """More complex program"""
        input = """class main {
            var a:string = a *b /c;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    BinaryOp(
                        "/",
                        BinaryOp("*",Id("a"),Id("b")),
                        Id("c")
                    )
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,323))
    
    def test_expr4_2(self):
        """More complex program"""
        input = r"""class main {
            var a:string = a \ b % c;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    BinaryOp(
                        "%",
                        BinaryOp("\\",Id("a"),Id("b")),
                        Id("c")
                    )
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,324))
    
    def test_expr5(self):
        """More complex program"""
        input = r"""class main {
            var a:string = !!a;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    UnaryOp(
                        "!",
                        UnaryOp(
                            "!",Id("a")
                        )
                    )
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,325))
    
    def test_expr6(self):
        """More complex program"""
        input = r"""class main {
            var a:string = --a;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    UnaryOp(
                        "-",
                        UnaryOp(
                            "-",Id("a")
                        )
                    )
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,326))
    
    def test_expr5_6(self):
        """More complex program"""
        input = r"""class main {
            var a:string = !!--a;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    UnaryOp(
                        "!",
                        UnaryOp(
                            "!",
                            UnaryOp(
                                "-",
                                UnaryOp(
                                    "-",
                                    Id("a")
                                )
                            )
                        )
                    )
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,327))

    def test_expr7(self):
        """More complex program"""
        input = r"""class main {
            var a:string = a[2];
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    ArrayCell(
                        Id("a"),
                        IntLiteral(2)
                    )
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,328))
    
    def test_expr8_access_LSRS(self):
        """More complex program"""
        input = r"""class main {
            var a:string = a[2].t;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    FieldAccess(
                        ArrayCell(
                            Id("a"),
                            IntLiteral(2)
                        ),
                        Id("t")
                    )
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,329))
    
    def test_expr8_access(self):
        """More complex program"""
        input = r"""class main {
            var a:string = a.t;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    FieldAccess(
                        Id("a"),
                        Id("t")
                    )
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,330))
    
    def test_expr8_invoc_LSRS(self):
        """More complex program"""
        input = r"""class main {
            var a:string = a[2].t(1,2);
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    CallExpr(
                        ArrayCell(
                            Id("a"),
                            IntLiteral(2)
                        ),
                        Id("t"),
                        [
                            IntLiteral(1),
                            IntLiteral(2)
                        ]
                    )
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,331))
    
    def test_expr8_invoc(self):
        """More complex program"""
        input = r"""class main {
            var a:string = a.t(1,2);
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    CallExpr(
                        Id("a"),
                        Id("t"),
                        [
                            IntLiteral(1),
                            IntLiteral(2)
                        ]
                    )
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,332))
    
    def test_expr9_dot_access(self):
        """More complex program"""
        input = r"""class main {
            var a:string = Shape.@a;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    FieldAccess(
                        Id("Shape"),
                        Id("@a")
                    )
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,333))

    def test_expr9_nodot_access(self):
        """More complex program"""
        input = r"""class main {
            var a:string = @a;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    FieldAccess(
                        None,
                        Id("@a")
                    )
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,334))
    
    def test_expr9_nodot_invoc(self):
        """More complex program"""
        input = r"""class main {
            var a:string = @a(2,5,6);
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    CallExpr(
                        None,
                        Id("@a"),
                        [
                            IntLiteral(2),
                            IntLiteral(5),
                            IntLiteral(6)
                        ]
                    )
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,335))
    
    def test_expr9_dot_invoc(self):
        """More complex program"""
        input = r"""class main {
            var a:string = Shape.@a(2,5,6);
        }"""
        expect =  str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    CallExpr(
                        Id("Shape"),
                        Id("@a"),
                        [
                            IntLiteral(2),
                            IntLiteral(5),
                            IntLiteral(6)
                        ]
                    )
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,336))
    
    def test_expr10(self):
        """More complex program"""
        input = r"""class main {
            var a:string = new Shape()[2];
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    ArrayCell(
                        NewExpr(
                            Id("Shape"),
                            []
                        ),
                        IntLiteral(2)
                    )
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,337))
    
    def test_expr_parent(self):
        """More complex program"""
        input = r"""class main {
            var a:string = ("temp"^"temp")[2];
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    ArrayCell(
                        BinaryOp(
                            "^",
                            StringLiteral("temp"),
                            StringLiteral("temp")
                        ),
                        IntLiteral(2)
                    )
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,338))
    
    def test_bool_lit(self):
        """More complex program"""
        input = r"""class main {
            var a:string = true;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    BooleanLiteral(True)
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,339))
    
    def test_float_lit(self):
        """More complex program"""
        input = r"""class main {
            var a:string = 2.4e5;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    FloatLiteral(2.4e5)
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,340))
    
    def test_self_lit(self):
        """More complex program"""
        input = r"""class main {
            var a:string = self.t[2];
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    ArrayCell(
                        FieldAccess(
                            SelfLiteral(),
                            Id("t")
                        ),
                        IntLiteral(2)
                    )
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,341))
    
    def test_null_lit(self):
        """More complex program"""
        input = r"""class main {
            var a:string = null;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    NullLiteral()
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,342))

    def test_id_lit(self):
        """More complex program"""
        input = r"""class main {
            var a:string = awdwa;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    Id("awdwa")
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,343))
    
    def test_ass_stmt(self):
        """More complex program"""
        input = r"""class main {
            func test():void{
                a:=2;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("test"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        Assign(
                            Id("a"),
                            IntLiteral(2)
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,344))
    
    def test_ass_stmt_advanced(self):
        """More complex program"""
        input = r"""class main {
            func test():void{
                a:=new X().a[2].t[5+2];
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("test"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        Assign(
                            Id("a"),
                            ArrayCell(
                                FieldAccess(
                                    ArrayCell(
                                        FieldAccess(
                                            NewExpr(
                                                Id("X"),
                                                []
                                            ),
                                            Id("a")
                                        ),
                                        IntLiteral(2)
                                    ),
                                    Id("t")
                                ),
                                BinaryOp("+",IntLiteral(5),IntLiteral(2))
                            )
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,345))

    def test_ass_stmt_attr(self):
        """More complex program"""
        input = r"""class main {
            func test():void{
                Shape.a := 2;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("test"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        Assign(
                            FieldAccess(
                                Id("Shape"),
                                Id("a")
                            ),
                            IntLiteral(2)
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,346))
    
    def test_ass_stmt_attr_arr(self):
        """More complex program"""
        input = r"""class main {
            func test():void{
                Shape[2].a := 2;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("test"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        Assign(
                            FieldAccess(
                                ArrayCell(
                                    Id("Shape"),
                                    IntLiteral(2)
                                ),
                                Id("a")
                            ),
                            IntLiteral(2)
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,347))

    def test_ass_stmt_arr(self):
        """More complex program"""
        input = r"""class main {
            func test():void{
                a[2]:= 2;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("test"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        Assign(
                            ArrayCell(
                                Id("a"),
                                IntLiteral(2)
                            ),
                            IntLiteral(2)
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,348))
    
    def test_ass_stmt_combined(self):
        """More complex program"""
        input = r"""class main {
            func test():void{
                Shape.a[2]:= 2;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("test"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        Assign(
                            ArrayCell(
                                FieldAccess(
                                    Id("Shape"),
                                    Id("a")
                                ),
                                IntLiteral(2)
                            ),
                            IntLiteral(2)
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,349))
    
    def test_if_stmt_no_pre_no_else(self):
        """More complex program"""
        input = r"""class main {
            func test():void{
                if true {
                    a:=1;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("test"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        If(
                            BooleanLiteral(True),
                            Block([
                                Assign(Id("a"),IntLiteral(1))
                            ])
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,350))
    
    def test_ifstmt_no_pre(self):
        """More complex program"""
        input = r"""class main {
            func test():void{
                if true {
                    a:=1;
                }
                else{
                
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("test"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        If(
                            BooleanLiteral(True),
                            Block([
                                Assign(Id("a"),IntLiteral(1))
                            ]),
                            None,
                            Block(
                                []
                            )
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,351))
    
    def test_if_stmt_pre_else(self):
        """More complex program"""
        input = r"""class main {
            func test():void{
                if {t:=2;} true {
                    a:=1;
                }
                else{
                
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("test"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        If(
                            BooleanLiteral(True),
                            Block([
                                Assign(Id("a"),IntLiteral(1))
                            ]),
                            Block(
                                [Assign(Id("t"),IntLiteral(2))]
                            ),
                            Block(
                                []
                            )
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,352))
    
    def test_for(self):
        """More complex program"""
        input = r"""class Main {
            func @main():void{
                for i:=1; true; i:=i+1{
                    a:=2+a;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Main"),
            [
                MethodDecl(
                    Id("@main"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        For(
                            Assign(Id("i"),IntLiteral(1)),
                            BooleanLiteral(True),
                            Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                            Block(
                                [
                                    Assign(Id("a"),BinaryOp(
                                        "+",IntLiteral(2),Id("a")
                                    ))
                                ]
                            )
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,353))
    
    def test_invocstmt(self):
        """More complex program"""
        input = r"""class Main1 {
            func test1():void{
                Shape.@getLength();
            }
        }"""
        expect = str(Program([ClassDecl(Id("Main1"),
            [
                MethodDecl(
                    Id("test1"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        CallStmt(
                            Id("Shape"),
                            Id("@getLength"),
                            []
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,354))
    
    def test_invocstmt_withparam(self):
        """More complex program"""
        input = r"""class Main1 {
            func test1():void{
                Shape.@getLength(5);
            }
        }"""
        expect = str(Program([ClassDecl(Id("Main1"),
            [
                MethodDecl(
                    Id("test1"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        CallStmt(
                            Id("Shape"),
                            Id("@getLength"),
                            [
                                IntLiteral(5)
                            ]
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,355))

    def test_invoc_stmt_withinvocparam(self):
        """More complex program"""
        input = r"""class Main1 {
            func test1():void{
                Shape.@getLength(Shape.getIndex());
            }
        }"""
        expect = str(Program([ClassDecl(Id("Main1"),
            [
                MethodDecl(
                    Id("test1"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        CallStmt(
                            Id("Shape"),
                            Id("@getLength"),
                            [
                                CallExpr(
                                    Id("Shape"),
                                    Id("getIndex"),
                                    []
                                )
                            ]
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,356))
    
    def test_invoc_stmt_with_static_invocparam(self):
        """More complex program"""
        """More complex program"""
        input = r"""class Main1 {
            func test1():void{
                Shape.@getLength(@getIndex());
            }
        }"""
        expect = str(Program([ClassDecl(Id("Main1"),
            [
                MethodDecl(
                    Id("test1"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        CallStmt(
                            Id("Shape"),
                            Id("@getLength"),
                            [
                                CallExpr(
                                    None,
                                    Id("@getIndex"),
                                    []
                                )
                            ]
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,357))
    
    def test_invoc_stmt_with_static_invocparam(self):
        """More complex program"""
        """More complex program"""
        input = r"""class Main {
            func @main():void{
                Shape.@getLength(@getIndex());
            }
        }"""
        expect = str(Program([ClassDecl(Id("Main"),
            [
                MethodDecl(
                    Id("@main"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        CallStmt(
                            Id("Shape"),
                            Id("@getLength"),
                            [
                                CallExpr(
                                    None,
                                    Id("@getIndex"),
                                    []
                                )
                            ]
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,357))

    def test_invoc_stmt_complex(self):
        """More complex program"""
        input = r"""class Main {
            func @main():void{
                Shape.length.getLength();
            }
        }"""
        expect = str(Program([ClassDecl(Id("Main"),
            [
                MethodDecl(
                    Id("@main"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        CallStmt(
                            FieldAccess(Id("Shape"),Id("length")),
                            Id("getLength"),
                            []
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,358))
    
    def test_invoc_stmt_complex2(self):
        """More complex program"""
        input = r"""class Main {
            func @main():void{
                Shape[0].length.getLength();
            }
        }"""
        expect = str(Program([ClassDecl(Id("Main"),
            [
                MethodDecl(
                    Id("@main"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        CallStmt(
                            FieldAccess(ArrayCell(Id("Shape"),IntLiteral(0)),Id("length")),
                            Id("getLength"),
                            []
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,359))
    
    def test_invoc_stmt_complex3(self):
        """More complex program"""
        input = r"""class Main {
            func @main():void{
                Shape.@getLength(a.getIndex());
            }
        }"""
        expect = str(Program([ClassDecl(Id("Main"),
            [
                MethodDecl(
                    Id("@main"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        CallStmt(
                            Id("Shape"),
                            Id("@getLength"),
                            [
                                CallExpr(
                                    Id("a"),Id("getIndex"),[]
                                )
                            ]
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,360))
    
    def test_static_invoc_stmt_params(self):
        """More complex program"""
        input = r"""class Main {
            func @main():void{
                @getArea(2,6);
            }
        }"""
        expect = str(Program([ClassDecl(Id("Main"),
            [
                MethodDecl(
                    Id("@main"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        CallStmt(
                            None,
                            Id("@getArea"),
                            [
                                IntLiteral(2),
                                IntLiteral(6)
                            ]
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,361))
    
    def test_static_invoc_stmt_params2(self):
        """More complex program"""
        input = r"""class Main {
            func @main():void{
                @getLength(a.getIndex());
            }
        }"""
        expect = str(Program([ClassDecl(Id("Main"),
            [
                MethodDecl(
                    Id("@main"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        CallStmt(
                            None,
                            Id("@getLength"),
                            [
                                CallExpr(
                                    Id("a"),Id("getIndex"),[]
                                )
                            ]
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,362))
    
    def test_inheritance(self):
        """More complex program"""
        input = """class object<-main{ const x, y, z: int = 1, 2, 3; var a, b: float;}"""
        expect = str(
            Program(
                [
                    ClassDecl(Id("main"),[
                        AttributeDecl(
                            ConstDecl(Id("x"),IntType(),IntLiteral(1))
                        ),
                        AttributeDecl(
                            ConstDecl(Id("y"),IntType(),IntLiteral(2))
                        ),
                        AttributeDecl(
                            ConstDecl(Id("z"),IntType(),IntLiteral(3))
                        ),
                        AttributeDecl(
                            VarDecl(Id("a"),FloatType())
                        ),
                        AttributeDecl(
                            VarDecl(Id("b"),FloatType())
                        )
                    ],Id("object"))
                ]
            )
        )
        self.assertTrue(TestAST.test(input,expect,363))
    
    def test_decl_stmt_var_decl_complex1(self):
        """More complex program"""
        input = """class Main {
            func test():void{
                var a:[2]int = [1,2];
            }
        }"""
        expect = str(Program([ClassDecl(Id("Main"),
            [
                MethodDecl(
                    Id("test"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        VarDecl(
                            Id("a"),
                            ArrayType(2,IntType()),
                            ArrayLiteral([IntLiteral(1),IntLiteral(2)])
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,364))
    
    def test_decl_stmt_var_decl_complex2(self):
        """More complex program"""
        input = """class Main {
            func test():void{
                var a:[2]Shape = ["square","rectangle"];
            }
        }"""
        expect = str(Program([ClassDecl(Id("Main"),
            [
                MethodDecl(
                    Id("test"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        VarDecl(
                            Id("a"),
                            ArrayType(2,ClassType(Id("Shape"))),
                            ArrayLiteral([StringLiteral('square'),StringLiteral("rectangle")])
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,365))
    
    def test_index_op_complex(self):
        """More complex program"""
        input = r"""class main {
            func test():void{
                var a: int = n[b[2]]+3;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("test"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        VarDecl(
                            Id("a"),
                            IntType(),
                            BinaryOp(
                                "+",
                                ArrayCell(
                                Id("n"),
                                ArrayCell(
                                    Id("b"),
                                    IntLiteral(2)
                                )
                                ),
                                IntLiteral(3)
                            )
                            
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,366))
    
    def test_index_op_complex2(self):
        """More complex program"""
        input = r"""class main {
            func test():void{
                x.b[3+x.foo(2)] := x.m()[3];
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("test"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        Assign(
                            ArrayCell(
                                FieldAccess(
                                Id("x"),
                                Id("b")),
                                BinaryOp("+",IntLiteral(3),CallExpr(Id("x"),Id("foo"),[IntLiteral(2)]))
                            ),
                            ArrayCell(
                                CallExpr(
                                    Id("x"),
                                    Id("m"),
                                    []
                                ),
                                IntLiteral(3)
                            )
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,367))
    
    def test_sample_if_stmt(self):
        """More complex program"""
        input = r"""class Main {
            func @main():void{
                if {i := 1;} j > i {j := j - 1;} else {j := j + 1;}
            }
        }"""
        expect = str(Program([ClassDecl(Id("Main"),
            [
                MethodDecl(
                    Id("@main"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        If(
                            BinaryOp(">",Id("j"),Id("i")),
                            Block([
                                Assign(
                                    Id("j"),
                                    BinaryOp("-",Id("j"),IntLiteral(1))
                                )
                            ]),
                            Block([
                                Assign(
                                    Id("i"),
                                    IntLiteral(1)
                                )
                            ]),
                            Block([
                                Assign(
                                    Id("j"),
                                    BinaryOp("+",Id("j"),IntLiteral(1))
                                )
                               
                            ])
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,368))
    
    def test_sample_if_stmt_no_pre(self):
        """More complex program"""
        input = r"""class Main {
            func @main():void{
                if j < i {j := j - 1;} else {j := j + 1;}
            }
        }"""
        expect = str(Program([ClassDecl(Id("Main"),
            [
                MethodDecl(
                    Id("@main"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        If(

                            BinaryOp("<",Id("j"),Id("i")),
                            Block([
                                Assign(
                                    Id("j"),
                                    BinaryOp("-",Id("j"),IntLiteral(1))
                                )
                            ]),
                            None,                    
                            Block([
                                Assign(
                                    Id("j"),
                                    BinaryOp("+",Id("j"),IntLiteral(1))
                                )
                               
                            ])
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,369))
    
    def test_sample_if_stmt_no_pre_no_else(self):
        """More complex program"""
        input = r"""class Main {
            func @main():void{
                if j < i {j := j - 1;}
            }
        }"""
        expect = str(Program([ClassDecl(Id("Main"),
            [
                MethodDecl(
                    Id("@main"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        If(
                            BinaryOp("<",Id("j"),Id("i")),
                            Block([
                                Assign(
                                    Id("j"),
                                    BinaryOp("-",Id("j"),IntLiteral(1))
                                )
                            ]),
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,370))
    
    def test_sample_if_stmt_no_else(self):
        """More complex program"""
        input = r"""class Main {
            func @main():void{
                if {i := 1;} j > i {j := j - 1;}
            }
        }"""
        expect = str(Program([ClassDecl(Id("Main"),
            [
                MethodDecl(
                    Id("@main"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        If(
                            BinaryOp(">",Id("j"),Id("i")),
                            Block([
                                Assign(
                                    Id("j"),
                                    BinaryOp("-",Id("j"),IntLiteral(1))
                                )
                            ]),
                            Block([
                                Assign(
                                    Id("i"),
                                    IntLiteral(1)
                                )
                            ]),
                        
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,371))
    
    def test_sample_for_stmt(self):
        """More complex program"""
        input = r"""class Main {
            func @main():void{
                for j := 0; j < 10; j := j + 1 {
                    io.@writeInt(j);
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Main"),
            [
                MethodDecl(
                    Id("@main"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        For(
                            Assign(
                                Id("j"),
                                IntLiteral(0)
                            ),
                            BinaryOp("<",Id("j"),IntLiteral(10)),
                            Assign(
                                Id("j"),
                                BinaryOp("+",Id("j"),IntLiteral(1))
                            ),
                            Block([
                                CallStmt(
                                    Id("io"),
                                    Id("@writeInt"),
                                    [Id("j")]
                                )
                            ])
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,372))
    
    def test_sample_for_stmt_with_continue(self):
        """More complex program"""
        input = r"""class Main {
            func @main():void{
                for j := 0; j < 10; j := j + 1 {
                    io.@writeInt(j);
                    continue;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Main"),
            [
                MethodDecl(
                    Id("@main"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        For(
                            Assign(
                                Id("j"),
                                IntLiteral(0)
                            ),
                            BinaryOp("<",Id("j"),IntLiteral(10)),
                            Assign(
                                Id("j"),
                                BinaryOp("+",Id("j"),IntLiteral(1))
                            ),
                            Block([
                                CallStmt(
                                    Id("io"),
                                    Id("@writeInt"),
                                    [Id("j")]
                                ),
                                Continue()
                            ])
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,373))
    
    def test_sample_for_stmt_with_break(self):
        """More complex program"""
        input = r"""class Main {
            func @main():void{
                for j := 0; j < 10; j := j + 1 {
                    io.@writeInt(j);
                    break;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Main"),
            [
                MethodDecl(
                    Id("@main"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        For(
                            Assign(
                                Id("j"),
                                IntLiteral(0)
                            ),
                            BinaryOp("<",Id("j"),IntLiteral(10)),
                            Assign(
                                Id("j"),
                                BinaryOp("+",Id("j"),IntLiteral(1))
                            ),
                            Block([
                                CallStmt(
                                    Id("io"),
                                    Id("@writeInt"),
                                    [Id("j")]
                                ),
                                Break()
                            ])
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,374))
    
    def test_sample_for_stmt_with_if(self):
        """More complex program"""
        input = r"""class Main {
            func @main():void{
                for j := 0; j < 10; j := j + 1 {
                    io.@writeInt(j);
                    if j == 3 {break;}
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Main"),
            [
                MethodDecl(
                    Id("@main"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        For(
                            Assign(
                                Id("j"),
                                IntLiteral(0)
                            ),
                            BinaryOp("<",Id("j"),IntLiteral(10)),
                            Assign(
                                Id("j"),
                                BinaryOp("+",Id("j"),IntLiteral(1))
                            ),
                            Block([
                                CallStmt(
                                    Id("io"),
                                    Id("@writeInt"),
                                    [Id("j")]
                                ),
                                If(
                                    BinaryOp("==", Id("j"), IntLiteral(3)),
                                    Block([Break()])
                                )
                            ])
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,375))
    
    def test_multi_member(self):
        """More complex program"""
        input = r"""class main {
            func test1():void{}
            func test2():int{
                return 10;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("test1"),
                    [],
                    VoidType(),
                    Block([])
                ),
                MethodDecl(
                    Id("test2"),
                    [],
                    IntType(),
                    Block([
                        Return(IntLiteral(10))
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,376))
    
    def test_multi_member2(self):
        """More complex program"""
        input = r"""class Main {
            const a:Shape = new Shape(4,6);
            func main():void{}
        }"""
        expect = str(Program([ClassDecl(Id("Main"),
            [
                AttributeDecl(ConstDecl(Id("a"),ClassType(Id("Shape")),NewExpr(Id("Shape"),[IntLiteral(4),IntLiteral(6)]))),
                MethodDecl(Id("main"),[],VoidType(),Block([]))
            ])]))
        self.assertTrue(TestAST.test(input,expect,377))
    
    def test_multi_member3(self):
        """More complex program"""
        input = r"""class Main {
            const a:[3]string = ["square","rectangle","triangle"];
            func main():void{}
        }"""
        expect = str(Program([ClassDecl(Id("Main"),
            [
                AttributeDecl(ConstDecl(Id("a"),ArrayType(3,StringType()),ArrayLiteral([StringLiteral("square"),StringLiteral("rectangle"),StringLiteral("triangle")]))),
                MethodDecl(Id("main"),[],VoidType(),Block([]))
            ])]))
        self.assertTrue(TestAST.test(input,expect,378))
    
    def test_multi_member4(self):
        """More complex program"""
        input = """class Main {
            const a:[3]bool = [true,false,true];
            func main():void{}
        }"""
        expect = str(Program([ClassDecl(Id("Main"),
            [
                AttributeDecl(ConstDecl(Id("a"),ArrayType(3,BoolType()),ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False),BooleanLiteral(True)]))),
                MethodDecl(Id("main"),[],VoidType(),Block([]))
            ])]))
        self.assertTrue(TestAST.test(input,expect,379))
    
    def test_multi_member5(self):
        """More complex program"""
        input = """class Main {
            const a:[3]float = [1.09,1.0E-3,6.90];
            func main():void{}
        }"""
        expect = str(Program([ClassDecl(Id("Main"),
            [
                AttributeDecl(ConstDecl(Id("a"),ArrayType(3,FloatType()),ArrayLiteral([FloatLiteral(1.09),FloatLiteral(1.0E-3),FloatLiteral(6.90)]))),
                MethodDecl(Id("main"),[],VoidType(),Block([]))
            ])]))
        self.assertTrue(TestAST.test(input,expect,380))

    def test_multi_members_constr(self):
        """More complex program"""
        input = r"""class main {
            func constructor(a:int, name:string){}
            func constructor(){}
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("constructor"),
                    [
                        VarDecl(Id("a"),IntType()),
                        VarDecl(Id("name"),StringType())
                    ],
                    VoidType(),
                    Block([])
                ),
                MethodDecl(
                    Id("constructor"),
                    [],
                    VoidType(),
                    Block([
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,381))
    
    def test_constr_multi_param(self):
        """More complex program"""
        input = r"""class main {
            var c: int;
            func constructor(a:int, b:string){
                c := a;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(Id("c"),IntType(),None)),
                MethodDecl(
                    Id("constructor"),
                    [
                        VarDecl(Id("a"),IntType()),
                        VarDecl(Id("b"),StringType())
                    ],
                    VoidType(),
                    Block([
                        Assign(
                            Id("c"), Id("a")
                        )
                    ])
                ),
            ])]))
        self.assertTrue(TestAST.test(input,expect,382))
    
    def test_constr_multi_param_together(self):
        """More complex program"""
        input = r"""class main {
            func constructor(ac,bd:int){}
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("constructor"),
                    [
                        VarDecl(Id("ac"),IntType()),
                        VarDecl(Id("bd"),IntType())
                    ],
                    VoidType(),
                    Block([])
                ),
            ])]))
        self.assertTrue(TestAST.test(input,expect,383))
    
    def test_func_complex_param_together_ind(self):
        """More complex program"""
        input = r"""class main {
            func constructor(ax,bg:float, c:ShapeS){}
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("constructor"),
                    [
                        VarDecl(Id("ax"),FloatType()),
                        VarDecl(Id("bg"),FloatType()),
                        VarDecl(Id("c"),ClassType(Id("ShapeS")))
                    ],
                    VoidType(),
                    Block([])
                ),
            ])]))
        self.assertTrue(TestAST.test(input,expect,384))
    
    def test_block_null_self(self):
        """More complex program"""
        input = r"""class main {
            var c: int;
            var d: int;
            func constructor(a:int, b:string){
                self.c := a;
                self.d := null;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(Id("c"),IntType(),None)),
                AttributeDecl(VarDecl(Id("d"),IntType(),None)),
                MethodDecl(
                    Id("constructor"),
                    [
                        VarDecl(Id("a"),IntType()),
                        VarDecl(Id("b"),StringType())
                    ],
                    VoidType(),
                    Block([
                        Assign(
                            FieldAccess(SelfLiteral(),Id("c")),Id("a")
                            
                        ),
                        Assign(
                            FieldAccess(SelfLiteral(),Id("d")),NullLiteral()
                            
                        )
                        
                    ])
                ),
            ])]))
        self.assertTrue(TestAST.test(input,expect,385))

    def test_block_for_in_for(self):
        """More complex program"""
        input = r"""class Main {
            func constructor(){
                for i:=0;false;i:=true{
                    for j:=i;true;j:=j+i{
                    
                    }
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Main"),
            [
                MethodDecl(
                    Id("constructor"),
                    [
                    ],
                    VoidType(),
                    Block([
                        For(
                            Assign(
                                Id("i"),
                                IntLiteral(0)
                            ),
                            BooleanLiteral(False),
                            Assign(
                                Id("i"),
                                BooleanLiteral(True)
                            ),
                            Block([
                                For(
                                    Assign(
                                        Id("j"),
                                        Id("i")
                                    ),
                                    BooleanLiteral(True),
                                    Assign(
                                        Id("j"),
                                        BinaryOp("+",Id("j"),Id("i"))
                                    ),
                                    Block([])
                                )
                            ])
                        )
                    ])
                ),
            ])]))
        self.assertTrue(TestAST.test(input,expect,386))
    
    def test_block_if_in_if(self):
        """More complex program"""
        input = r"""class main {
            func constructor(){
                if false{
                    if true{
                        return "HelloWorld";
                    }
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("constructor"),
                    [
                    ],
                    VoidType(),
                    Block([
                        If(
                            BooleanLiteral(False),
                            Block([
                                If(
                                    BooleanLiteral(True),
                                    Block([
                                        Return(StringLiteral("HelloWorld"))
                                    ])
                                )
                            ])
                        )
                    ])
                ),
            ])]))
        self.assertTrue(TestAST.test(input,expect,387))
    
    def test_block_complex_for_for(self):
        """More complex program"""
        input = r"""class main {
            func constructor(){
                for i:=1;false;i:=3{
                    for j:=1;true;j:=4{
                        return j%3;
                    }
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("constructor"),
                    [
                    ],
                    VoidType(),
                    Block([
                        For(
                            Assign(
                                Id("i"),
                                IntLiteral(1)
                            ),
                            BooleanLiteral(False),
                            Assign(
                                Id("i"),
                                IntLiteral(3)
                            ),
                            Block([
                                For(
                                    Assign(
                                        Id("j"),
                                        IntLiteral(1)
                                    ),
                                    BooleanLiteral(True),
                                    Assign(
                                        Id("j"),
                                        IntLiteral(4)
                                    ),
                                    Block([
                                        Return(BinaryOp("%",Id("j"),IntLiteral(3)))
                                    ])
                                )
                            ])
                        )
                    ])
                ),
            ])]))
        self.assertTrue(TestAST.test(input,expect,388))
    
    def test_random1(self):
        """More complex program"""
        input = r"""class main {
            const a,b:int;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(ConstDecl(Id("a"),IntType(),None)),
                AttributeDecl(ConstDecl(Id("b"),IntType(),None))
            ])]))
        self.assertTrue(TestAST.test(input,expect,389))

    def test_random2(self):
        """More complex program"""
        input = r"""class Main {
            const a:bool = ("god" == "dog");
        }"""
        expect = str(Program([ClassDecl(Id("Main"),
            [
                AttributeDecl(
                    ConstDecl(
                        Id("a"),
                        BoolType(),
                        BinaryOp("==",StringLiteral("god"),StringLiteral("dog")),
                    )
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,390))

    def test_random3(self):
        """More complex program"""
        input = r"""class main {
            const a:int = 3 + -6;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(
                    ConstDecl(
                        Id("a"),
                        IntType(),
                        BinaryOp(
                            "+",
                            IntLiteral(3),
                            UnaryOp("-",IntLiteral(6))
                        )
                    )
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,391))

    def test_random4(self):
        """More complex program"""
        input = r"""class main {
            const a:int = 6*3 + 2;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(
                    ConstDecl(
                        Id("a"),
                        IntType(),
                        BinaryOp(
                            "+",
                            BinaryOp("*",IntLiteral(6),IntLiteral(3)),
                            IntLiteral(2)
                        )
                    )
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,392))
    
    def test_random5(self):
        """More complex program"""
        input = r"""class main {
            const a:Shape = (Shape1+Shape2).get();
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(
                    ConstDecl(
                        Id("a"),
                        ClassType(Id("Shape")),
                        CallExpr(
                            BinaryOp("+",Id("Shape1"),Id("Shape2")),
                            Id("get"),
                            []
                        )
                    )
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,393))

    def test_random6(self):
        """More complex program"""
        input = r"""class Main {
            func @main():void{
                @Shape.length.getLength();
            }
        }"""
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Main"),
                        [
                            MethodDecl(
                                Id("@main"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        CallStmt(
                                            FieldAccess(
                                                FieldAccess(None, Id("@Shape")), 
                                                Id("length")
                                            ),
                                            Id("getLength"),
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
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_random7(self):
        """More complex program"""
        input = r"""class main {
            const a:int = (2+3)*90+(60-3);
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(
                    ConstDecl(
                        Id("a"),
                        IntType(),
                        BinaryOp(
                            "+",
                            BinaryOp(
                                "*",
                                BinaryOp(
                                    "+",
                                    IntLiteral(2),
                                    IntLiteral(3)
                                ),
                                IntLiteral(90)

                            ),
                            BinaryOp(
                                "-",
                                IntLiteral(60),
                                IntLiteral(3)
                            )
                        )
                    )
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,395))

    
    def test_random8(self):
        """More complex program"""
        input = r"""class main {
            const a:int = (2+3)*90+(60- -3);
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(
                    ConstDecl(
                        Id("a"),
                        IntType(),
                        BinaryOp(
                            "+",
                            BinaryOp(
                                "*",
                                BinaryOp(
                                    "+",
                                    IntLiteral(2),
                                    IntLiteral(3)
                                ),
                                IntLiteral(90)

                            ),
                            BinaryOp(
                                "-",
                                IntLiteral(60),
                                UnaryOp("-",IntLiteral(3))
                            )
                        )
                    )
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,396))
    
    def test_random9(self):
        """More complex program"""
        input = r"""class main {
            const a:bool = ("a"=="a") && ("b" == 0);
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(
                    ConstDecl(
                        Id("a"),
                        BoolType(),
                        BinaryOp(
                            "&&",
                            BinaryOp(
                                "==",
                                StringLiteral("a"),
                                StringLiteral("a"),

                            ),
                            BinaryOp(
                                "==",
                                StringLiteral("b"),
                                IntLiteral(0)
                            )
                        )
                    )
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,397))
    
    def test_random9(self):
        """More complex program"""
        input = r"""class main {
            const a:Temp = new Temp(33);
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(
                    ConstDecl(
                        Id("a"),
                        ClassType(Id("Temp")),
                        NewExpr(Id("Temp"),[IntLiteral(33)])
                    )
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,398))
    
    def test_random10(self):
        """More complex program"""
        input = r"""class main {
            const a:Temp = new Temp(33);
            func constructor() {
                var b: int;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(
                    ConstDecl(
                        Id("a"),
                        ClassType(Id("Temp")),
                        NewExpr(Id("Temp"),[IntLiteral(33)])
                    )
                ),
                MethodDecl(
                    Id("constructor"),[],VoidType(),Block([
                        VarDecl(Id("b"),IntType(),None)
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,399))
    
    def test_random11(self):
        """More complex program"""
        input = r"""class main {
            const a:Temp = new Temp(33);
            func constructor() {
                var b: int;
            }
            func constructor(a: Temp) {
                var b: Temp = a;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(
                    ConstDecl(
                        Id("a"),
                        ClassType(Id("Temp")),
                        NewExpr(Id("Temp"),[IntLiteral(33)])
                    )
                ),
                MethodDecl(
                    Id("constructor"),[],VoidType(),Block([
                        VarDecl(Id("b"),IntType(),None)
                    ])
                ),
                MethodDecl(
                    Id("constructor"),[VarDecl(Id("a"),ClassType(Id("Temp")))],VoidType(),Block([
                        VarDecl(Id("b"),ClassType(Id("Temp")),Id("a"))
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,400))