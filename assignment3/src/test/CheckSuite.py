import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    def test0(self):
        input = """
        class Program {
            func @main():void{}
        }
        class a {}
        class b {}
        class a {}
        """
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test1(self):
        input = """
        class Program {
            func @main():void{}
        }
        class a {var a:int;var c:int;var c:int;}
        """
        expect = "Redeclared Attribute: c"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test2(self):
        input = Program(
            [ClassDecl(Id("a"), []), ClassDecl(Id("b"), []), ClassDecl(Id("a"), [])]
        )
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test3(self):
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
        expect = "Undeclared Identifier: s"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test4(self):
        input = Program(
            [
                ClassDecl(
                    Id("a"),
                    [
                        AttributeDecl(VarDecl(Id("a"), IntType())),
                        AttributeDecl(VarDecl(Id("c"), IntType())),
                        AttributeDecl(ConstDecl(Id("c"), IntType(), IntLiteral(2))),
                    ],
                )
            ]
        )
        expect = "Redeclared Attribute: c"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test5(self):
        input = """
        class Program {
            func @main():void{}
        }
        class a <- b {
            var a:int;
            var c:int;
        }
        """
        expect = "Undeclared Class: a"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test6(self):
        input = """
        class Program {
            func @main():void{}
        }
        class a{
            var a:string;
        }
        class a <- b {
            var a:int;
            const a:a;
            var c:int;
        }
        """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test7(self):
        input = """
        class Program {
            func @main():void{}
        }
        class abc{
            var s:string;
        }
        class abc <- b {
            var t:int;
            var c:Shape;
        }
        """
        expect = "Undeclared Class: Shape"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test8(self):
        input = """
        class Program {
            func @main():void{}
        }
        class a{
            var s:string;
        }
        class a <- b {
            var a:a;
            var c:Shape;
        }
        """
        expect = "Undeclared Class: Shape"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test9(self):
        input = """
        class Program {
            func @main():void{}
        }
        class a{
            var s:string;
            func temp():void{

            }
        }
        class a <- b {
            var a:a;
            func temp(i:int):void{

            }
            func temp():int{

            }
        }
        """
        expect = "Redeclared Method: temp"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test10(self):
        input = """
        class Program {
            func @main():void{}
        }
        class a{
            var s:string;
            func constructor(){

            }
        }
        class a <- io {
            var a:a;
            func temp():int{

            }
            func constructor(a:int){

            }
        }
        """
        expect = "Redeclared Class: io"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test11(self):
        input = """
        class a{
            var s:string;
            func constructor(b:int){

            }
        }
        class a <- b {
            var a:a;
            func temp():int{

            }
            func constructor(a:int){

            }
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test12(self):
        input = """
        class a{
            var s:string;
            func constructor(b:int){

            }
        }
        class a <- b {
            var a:a;
            func temp():int{

            }
            func constructor(a:int){

            }
        }
        class Program {
            var @main:int;
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test13(self):
        input = """
        class a{
            func @main():void{

            }
        }
        class a <- Program {

        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test14(self):
        input = Program([ClassDecl(Id("a"), [])])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test15(self):
        input = """
        class a{
            var s:string;
            func constructor(b:int){

            }
        }
        class a <- b {
            var a:a;
            func temp():int{

            }
            func constructor(a:int){

            }
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test16(self):
        input = """
        class a{
            var s:string;
            func constructor(b:int){

            }
        }
        class a <- b {
            var a:a;
            func temp():int{

            }
            func constructor(a:int){

            }
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test17(self):
        input = """
        class Program {
            func @main():void{}
        }
        class a{
            var s:string;
            func constructor(b:int){

            }
            func temp(a,b,c:bool):void{

            }
        }
        class a <- b {
            var a:a;
            func temp():int{

            }
            func temp(a:string):void{

            }
            func constructor(a:int){

            }
            func constructor(t,w:string){

            }
        }
        """
        expect = "Redeclared Method: temp"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test18(self):
        input = """
        class Program {
            func @main():void{}
        }
        class a{
            var s:string;
            func constructor(b:int){

            }
        }
        class a <- b {
            var a:a;
            func temp():int{

            }
            func constructor(a:int){

            }
        }
        class b <- c{
            var s:b;
            var s:int;
        }
        """
        expect = "Redeclared Attribute: s"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test19(self):
        input = """
        class Program {
            func @main():void{}
        }
        class a{
            var s:string;
            func constructor(b:int){

            }
        }
        class a <- b {
            var a:a;
            func temp():int{

            }
            func constructor(a:int){

            }
        }
        class b <- c{
            var t:int;
        }
        class c <- a{

        }
        """
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test20(self):
        input = """

        class a{
            func @main():void{

            }
        }
        class a <- Program{

        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test21(self):
        input = """
        class Program{
            func @main():void{

            }
            var a:[1]int = [true];
        }
        """
        expect = "Type Mismatch In Declaration: VarDecl(Id(a),ArrayType(1,IntType),[BooleanLit(True)])"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test22(self):
        input = """
        class Program{
            func @main():void{

            }
            var a:int = [true];
        }
        """
        expect = (
            "Type Mismatch In Declaration: VarDecl(Id(a),IntType,[BooleanLit(True)])"
        )
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test23(self):
        input = """
        class Program{
            func @main():void{

            }
            const @a:int = 2.0;
        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(@a),IntType,FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test24(self):
        input = """
        class Program{
            func @main():void{

            }
            var a:void;
        }
        """
        expect = "Type Mismatch In Declaration: VarDecl(Id(a),VoidType)"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test25(self):
        input = """
        class Program{
            func @main():void{

            }
            const a:[10]string;
        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(a),ArrayType(10,StringType),None)"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test26(self):
        input = """
        class Program{
            func @main():void{

            }
            const a: int = 1.2;
        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(a),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test27(self):
        input = """
        class Program{
            func @main():void{

            }
            const a:[2]bool = [true,true,2.0];
        }
        """
        expect = (
            "Illegal Array Literal: [BooleanLit(True),BooleanLit(True),FloatLit(2.0)]"
        )
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test28(self):
        input = """
        class Program{
            func test(t:int,t:[2]string):void{

            }
            func @main():void{

            }
        }
        """
        expect = "Redeclared Parameter: t"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test29(self):
        input = """
        class Program{
            var a:string = "22" ^ ["22"];
            func @main():void{

            }
        }
        """
        expect = (
            "Type Mismatch In Expression: BinaryOp(^,StringLit(22),[StringLit(22)])"
        )
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test30(self):
        input = """
        class Program{
            var t:string = "22";
            var a:string = self.t ^ self.t;
            func @main():void{

            }
            const ttemp:int;
        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(ttemp),IntType,None)"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test31(self):
        input = """
        class a{

        }
        class Program{
            var t:a = null;
            const a:a;
            func @main():void{

            }
        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(a),ClassType(Id(a)),None)"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test32(self):
        input = """
        class a{

        }
        class Program{
            var t:[2]a = [null,null];
            const a:a;
            func @main():void{

            }
        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(a),ClassType(Id(a)),None)"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test33(self):
        input = """
        class a{

        }
        class Program{
            var t:[1]a = [null,null];
            const a:a;
            func @main():void{

            }
        }
        """
        expect = "Type Mismatch In Declaration: VarDecl(Id(t),ArrayType(1,ClassType(Id(a))),[NullLiteral(),NullLiteral()])"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test34(self):
        input = """
        class Program{
            var t:bool = 2==true;
            const a:int;
            func @main():void{

            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,IntLit(2),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test35(self):
        input = """
        class Program{
            var t:bool = 2==5;
            const a:a;
            func @main():void{

            }
        }
        class a{

        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(a),ClassType(Id(a)),None)"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test36(self):
        input = """
        class Program{
            var t:bool = [true,false]==5;
            const a:a;
            func @main():void{

            }
        }
        class a{

        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,[BooleanLit(True),BooleanLit(False)],IntLit(5))"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test37(self):
        input = """
        class Program{
            var t:int = 1==5;
            const a:a;
            func @main():void{

            }
        }
        class a{

        }
        """
        expect = "Type Mismatch In Declaration: VarDecl(Id(t),IntType,BinaryOp(==,IntLit(1),IntLit(5)))"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test38(self):
        input = """
        class Program{
            var t:int = 1.0>5;
            const a:a;
            func @main():void{

            }
        }
        class a{

        }
        """
        expect = "Type Mismatch In Declaration: VarDecl(Id(t),IntType,BinaryOp(>,FloatLit(1.0),IntLit(5)))"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test39(self):
        input = """
        class Program{
            var t:int = 1.0>5.3;
            const a:a;
            func @main():void{

            }
        }
        class a{

        }
        """
        expect = "Type Mismatch In Declaration: VarDecl(Id(t),IntType,BinaryOp(>,FloatLit(1.0),FloatLit(5.3)))"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test40(self):
        input = """
        class Program{
            var t:bool = (2==5)||(5.3>1);
            const a:a;
            func @main():void{

            }
        }
        class a{

        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(a),ClassType(Id(a)),None)"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test41(self):
        input = """
        class Program{
            var t:int = 2+(5-6);
            const a:a;
            func @main():void{

            }
        }
        class a{

        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(a),ClassType(Id(a)),None)"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test42(self):
        input = """
        class Program{
            var t:int = 2-(5.2-6);
            const a:a;
            func @main():void{

            }
        }
        class a{

        }
        """
        expect = "Type Mismatch In Declaration: VarDecl(Id(t),IntType,BinaryOp(-,IntLit(2),BinaryOp(-,FloatLit(5.2),IntLit(6))))"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test43(self):
        input = """
        class Program{
            var t:bool = !!!(-2==5);
            const a:a;
            func @main():void{

            }
        }
        class a{

        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(a),ClassType(Id(a)),None)"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test44(self):
        input = """
        class Program{
            var t:float = [2.0,5.7,1e2][-2+3];
            const a:a;
            func @main():void{

            }
        }
        class a{

        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(a),ClassType(Id(a)),None)"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test45(self):
        input = """
        class Program{
            var t:float = [2.0,5.7,1e2][-2+3];
            const a:int = a.@a;
            func @main():void{

            }
        }
        class a{
            const @a:int = 2;
            var @t:string = "2";
            const t:void;
        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(t),VoidType,None)"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test46(self):
        input = """
        class Program{
            var @arr:[2]float = [2.5,3e-1];
            var t:float = @arr[1];
            const a:int = a.@a;
            func @main():void{

            }
        }
        class a{
            const @a:int = 2;
            var @t:string = "2";
            const t:void;
        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(t),VoidType,None)"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test47(self):
        input = """
        class Program{
            var @arr:[2]float = [2.5,3e-1];
            var t:float = @arr[1];
            const a:int = @test();
            func @test():void{

            }
            func @main():void{

            }
        }
        class a{
            const @a:int = 2;
            var @t:string = "2";
            const t:void;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(@test),[])"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test48(self):
        input = """
        class Program{
            var @arr:[2]float = [2.5,3e-1];
            var t:float = @arr[1];
            const a:int = self.ttt(2);
            func @test():void{

            }
            func ttt(id:int):int{

            }
            func @main():void{

            }
        }
        class a{
            const @a:int = 2;
            var @t:string = "2";
            const t:void;
        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(t),VoidType,None)"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test49(self):
        input = """
        class Program{
            var @arr:[2]float = [2.5,3e-1];
            var t:float = self.t;
            const a:int = self.ttt(2);
            func @test():void{

            }
            func ttt(id:int):int{

            }
            func @main():void{

            }
        }
        class a{
            const @a:int = 2;
            var @t:string = "2";
            const t:void;
        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(t),VoidType,None)"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test50(self):
        input = """
        class Program{
            var @arr:[2]float = [2.5,3e-1];
            var t:float = self.t;
            const a:int = self.ttt(2);
            func @test():void{

            }
            func ttt(id:float):int{

            }
            func @main():void{

            }
        }
        class a{
            const @a:int = 2;
            var @t:string = "2";
            const t:void;
        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(t),VoidType,None)"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test51(self):
        input = """
        class Program{
            var b_temp:b;
            const a_test:int = self.ttt(self.b_temp);
            func ttt(id:a):int{

            }
            func @main():void{

            }
        }
        class a{
            const @a:int = 2;
            var @t:string = "2";
            const t:void;
        }
        class a <- b{

        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(t),VoidType,None)"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test52(self):
        input = """
        class Program{
            const temp:a = new b(1,"1");
            func @main():void{

            }
        }
        class a{
            func constructor(t:int, s:string){

            }
        }
        class a<-b{
            func constructor(t:int, s:string){

            }
            const a:void;
        }

        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(a),VoidType,None)"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test53(self):
        input = """
        class Program{
            const temp:int = self.test(new b(2),new b(1));
            func test(temp1,temp2:a):int{

            }
            func @main():void{

            }
        }
        class a{
            func constructor(t:int, s:string){

            }
        }
        class a<-b{
            func constructor(a:int){

            }
            func constructor(t:int){

            }
            const a:void;
        }

        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(a),VoidType,None)"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test54(self):
        input = """
        class Program{
            const temp:a = new b(true);
            func test(temp1,temp2:a):int{

            }
            func @main():void{

            }
        }
        class a{
            func constructor(t:int, s:string){

            }
        }
        class a<-b{
            func constructor(){

            }
            func constructor(t:int){

            }
            func constructor(t:int, s:string){

            }
            const a:void;
        }

        """
        expect = "Type Mismatch In Expression: NewExpr(Id(b),[BooleanLit(True)])"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test55(self):
        input = """
        class Program{
            const temp:[2]int = [6,7];
            func test(temp1,temp2:a):int{

            }
            func @main():void{

            }
        }
        class a{
            func constructor(t:int, s:string){

            }
        }
        class a<-b{
            func constructor(){

            }
            func constructor(t:int){

            }
            func constructor(t:int, s:string){

            }
            const a:void;
        }

        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(a),VoidType,None)"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test56(self):
        input = """
        class Program{
            const temp:[2]int = [6,7];
            func test(temp1,temp2:a):int{
                var b_1:b;
                var b_2:b;
                const c:[2]a = [b_1,b_2];
            }
            func @main():void{

            }
        }
        class a{
            func constructor(t:int, s:string){

            }
        }
        class a<-b{
            func constructor(){

            }
            func constructor(t:int){

            }
            func constructor(t:int, s:string){

            }
            const a:void;
        }

        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(a),VoidType,None)"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test57(self):
        input = """
        class Program{
            const temp:[2]int = [6,7];
            func test(temp1,temp2:a):int{
                var  a,b:float=3.0,4.e-3;
                var  d:[5]int=[5,3,6,3,1];
                const s:string = "anv";
                const c:int =  5;
                if {b :=  b+1;} b>c {io.@writeInt(d[c]);} else {io.@writeFloat(b);}
            }
            func @main():void{

            }
        }
        class a{
            const temp:int;
        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test58(self):
        input = """
        class Program{
            const temp:[2]int = [6,7];
            func test(temp1,temp2:a):int{
                var a,b:Shape;
            }
            func @main():void{

            }
        }
        class a{
            const temp:int;
        }
        """
        expect = "Undeclared Class: Shape"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test59(self):
        input = """
        class Program{
            const temp:[2]int = [6,7];
            func test(temp1,temp2:a):int{
                var a,b:int = new Shape(),new Shape();
            }
            func @main():void{

            }
        }
        class a{
            const temp:int;
        }
        """
        expect = "Undeclared Class: Shape"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test60(self):
        input = """
        class Program{
            const temp:[2]int = [6,7];
            func test(temp1,temp2:Shape):int{
                var a,b:int = new Shape(),new Shape();
            }
            func @main():void{

            }
        }
        class a{
            const temp:int;
        }
        """
        expect = "Undeclared Class: Shape"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test61(self):
        input = """
        class Program{
            const temp:[2]int = [6,7];
            func test(temp1,temp2:a):int{
                var a,b:int = self.t,self.t2s;
            }
            func @main():void{

            }
        }
        class a{
            const temp:int;
        }
        """
        expect = "Undeclared Attribute: t"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test62(self):
        input = """
        class Program{
            const temp:[2]int = [6,7];
            func test(temp1,temp2:a):int{
                var a,b:int = self.t(),self.t2s;
            }
            func @main():void{

            }
        }
        class a{
            const temp:int;
        }
        """
        expect = "Undeclared Method: t"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test63(self):
        input = """
        class Program{
            var a:int = 5;
            func test(temp1,temp2:a):int{
                var a:int = 2;
                if{a:=2;} 1>2.0 {const a:bool = false;} else {var u:bool = a;}
            }
            func @main():void{

            }
        }
        class a{
            const temp:int;
        }
        """
        expect = "Type Mismatch In Declaration: VarDecl(Id(u),BoolType,Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test64(self):
        input = """
        class Program{
            var a:int = 5;
            func test(temp1,temp2:a):int{
                var a:int = 2;
            }
            func @main():void{
                var temp1:b;
                var temp2:b;
                var temp3:[2]a = [temp1,temp2];
            }
        }
        class a{
            const temp:int;
        }
        class a <- b{

        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test65(self):
        input = """
        class Program{
            var a:int = 5;
            func test(temp1,temp2:a):int{
                var a:int = 2;
            }
            func @main():void{
                var temp1:b;
                var temp2:b;
                var i:int = 2;
                for i:=0 ; i<10 ; i:=i+1{
                    io.@writeInt(i);
                }
            }
        }
        class a{
            const temp:int;
        }
        class a <- b{

        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test66(self):
        input = """
        class Program{
            var a:int = 5;
            func test(temp1,temp2:a):int{
                var a:int = 2;
            }
            func @main():void{
                var temp1:b;
                var temp2:b;
                const i:int = 2;
                for i:=0 ; i<10 ; i:=i+1{
                    io.@writeInt(i);
                }
            }
        }
        class a{
            const temp:int;
        }
        class a <- b{

        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(i),IntLit(0))"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test67(self):
        input = """
        class Program{
            var a:int = 5;
            func test(temp1,temp2:a):int{
                var a:int = 2;
            }
            func @main():void{
                var temp1:b;
                var temp2:b;
                var i:int = 2;
                for i:=0 ; i<10 ; i:=i+1{
                    io.writeInt(i);
                }
            }
        }
        class a{
            const temp:int;
        }
        class a <- b{

        }
        """
        expect = "Undeclared Identifier: io"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test68(self):
        input = """
        class Program{
            var a:int = 5;
            func test(temp1,temp2:a):int{
                var a:int = 2;
            }
            func @main():void{
                var temp1:b;
                var temp2:b;
                var i:int = 2;
                for i:=0 ; i<10 ; i:=i+1{
                    io.@writeInt(i);
                    continue;
                }
            }
        }
        class a{
            const temp:int;
        }
        class a <- b{

        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test69(self):
        input = """
        class Program{
            var a:int = 5;
            func test(temp1,temp2:a):int{
                var a:int = 2;
            }
            func @main():void{
                var temp1:b;
                var temp2:b;
                var i:int = 2;
                continue;
                for i:=0 ; i<10 ; i:=i+1{
                    io.@writeInt(i);
                }
            }
        }
        class a{
            const temp:int;
        }
        class a <- b{

        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test70(self):
        input = """
        class Program{
            var a:int = 5;
            func test(temp1,temp2:a):int{
                var a:int = 2;
            }
            func @main():void{
                var temp1:b;
                var temp2:b;
                var i:int = 2;
                for i:=0 ; i<10 ; i:=i+1{
                    io.@writeInt(i);
                    break;
                }
            }
        }
        class a{
            const temp:int;
        }
        class a <- b{

        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test71(self):
        input = """
        class Program{
            var a:int = 5;
            func test(temp1,temp2:a):int{
                var a:int = 2;
            }
            func @main():void{
                var temp1:b;
                var temp2:b;
                var i:int = 2;
                break;
                for i:=0 ; i<10 ; i:=i+1{
                    io.@writeInt(i);
                    break;
                }
            }
        }
        class a{
            const temp:int;
        }
        class a <- b{

        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test72(self):
        input = """
        class Program{
            var a:int = 5;
            func test(temp1,temp2:a):int{
                var a:int = 2;
            }
            func @main():void{
                var temp1:b;
                var temp2:b;
                var i:int = 2;
                for i:=0 ; i<10 ; i:=i+1{
                    io.@writeInt(i);
                    return;
                    break;
                }
            }
        }
        class a{
            const temp:int;
        }
        class a <- b{

        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test73(self):
        input = """
        class Program{
            var a:int = 5;
            func test(temp1,temp2:a):int{
                var a:int = 2;
            }
            func @main():void{
                var temp1:b;
                var temp2:b;
                var i:int = 2;
                for i:=0 ; i<10 ; i:=i+1{
                    io.@writeInt(i);
                    return null;
                    break;
                }
            }
        }
        class a{
            const temp:int;
        }
        class a <- b{

        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test74(self):
        input = """
        class Program{
            var a:int = 5;
            func test(temp1,temp2:a):int{
                var a:int = 2;
            }
            func @main():void{
                var temp1:b;
                var temp2:b;
                var i:int = 2;
                for i:=0 ; i<10 ; i:=i+1{
                    io.@writeInt(i);
                    return 1;
                    break;
                }
            }
        }
        class a{
            const temp:int;
        }
        class a <- b{

        }
        """
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test75(self):
        input = """
        class Program{
            var a:int = 5;
            func test(temp1,temp2:a):float{
                var a:int = 2;
                return a;
            }
            func @main():void{
                var temp1:b;
                var temp2:b;
                var i:int = 2;
                for i:=0 ; i<10 ; i:=i+1{
                    io.@writeInt(i);
                    return;
                    break;
                }
            }
        }
        class a{
            const temp:int;
        }
        class a <- b{

        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test76(self):
        input = """
        class Program{
            var a:int = 5;
            func test(temp1,temp2:a):b{
                var a:int = 2;
                return null;
            }
            func @main():void{
                var temp1:b;
                var temp2:b;
                var i:int = 2;
                for i:=0 ; i<10 ; i:=i+1{
                    io.@writeInt(i);
                    return;
                    break;
                }
            }
        }
        class a{
            const temp:int;
        }
        class a <- b{

        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test77(self):
        input = """
        class Program{
            var a:int = 5;
            func test(temp1,temp2:a):a{
                var a:int = 2;
                const temp:b = new b();
                return temp;
            }
            func @main():void{
                var temp1:b;
                var temp2:b;
                var i:int = 2;
                for i:=0 ; i<10 ; i:=i+1{
                    io.@writeInt(i);
                    return;
                    break;
                }
            }
        }
        class a{
            const temp:int;
        }
        class a <- b{
            func constructor(){

            }
        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test78(self):
        input = """
        class Program{
            var a:int = 5;
            func test(temp1,temp2:a):bool{
                return 2==5;
            }
            func @main():void{
            }
        }
        class a{
            const temp:int;
        }
        class a <- b{
            func constructor(){

            }
        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test79(self):
        input = """
        class Program{
            var a:int = 5;
            func test(temp1,temp2:a):void{
                var a:int = 2;
                const temp:b = new b();
                return temp;
            }
            func @main():void{
                var temp1:b;
                var temp2:b;
                var i:int = 2;
                for i:=0 ; i<10 ; i:=i+1{
                    io.@writeInt(i);
                    return;
                    break;
                }
            }
        }
        class a{
            const temp:int;
        }
        class a <- b{
            func constructor(){

            }
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(temp))"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test80(self):
        input = """
        class Program{
            var a:int = 5;
            func test(temp1,temp2:a):int{
                var a:int = 2;
                const temp:b = new b();
                return 1+3+self.a;
            }
            func @main():void{
                var temp1:b;
                var temp2:b;
                var i:int = 2;
                for i:=0 ; i<10 ; i:=i+1{
                    io.@writeInt(i);
                    return;
                    break;
                }
            }
        }
        class a{
            const temp:int;
        }
        class a <- b{
            func constructor(){

            }
        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test81(self):
        input = """
        class Program{
            var a:int = 5;
            func test(temp1,temp2:a):a{
                var a:int = 2;
                return self.test(new a(),new a());
            }
            func @main():void{
            }
        }
        class a{
            const temp:int;
            func constructor(){}
        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test82(self):
        input = """
        class Program{
            func @main():void{
                const a:int = 1.2;
            }
            const temp:int;
        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(a),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test83(self):
        input = """
        class Program{
            func @main():void{
                const b: float;
            }
            const temp:int;
        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(b),FloatType,None)"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test84(self):
        input = """
        class Program{
            func @main():void{
                var c: void;
            }
            const temp:int;
        }
        """
        expect = "Type Mismatch In Declaration: VarDecl(Id(c),VoidType)"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test85(self):
        input = """
        class Program{
            func @main():void{
                const temp:a = new a(5,new b());
            }
            const temp:int;
        }
        class a{
            func constructor(a:int,t:a){

            }
        }
        class a <- b{
            func constructor(){}
        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test86(self):
        input = """
        class Program{
            func @main():void{
                const temp:a = new a(5,new b());
            }
            const temp:int;
        }
        class a{
            func constructor(a:int,t:a){

            }
        }
        class a <- b{
            func constructor(){}
        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test87(self):
        input = """
        class Program{
            var a:int = 2;
            func @main():void{
                var c: int = (1+2).t;
            }
            const temp:int;
        }
        """
        expect = "Type Mismatch In Expression: FieldAccess(BinaryOp(+,IntLit(1),IntLit(2)),Id(t))"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test88(self):
        input = """
        class Program{
            var a:int = 2;
            func @main():void{
                var c: int = null.t;
            }
            const temp:int;
        }
        """
        expect = "Type Mismatch In Expression: FieldAccess(NullLiteral(),Id(t))"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test89(self):
        input = """
        class Program{
            var a:int = 2;
            func @main():void{
                var c: int = self.temp.t;
            }
            const temp:int;
        }
        """
        expect = "Type Mismatch In Expression: FieldAccess(FieldAccess(Self(),Id(temp)),Id(t))"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test90(self):
        input = """
        class Program{
            var a:int = 2;
            func test():void{}
            func @main():void{
                self.test();
            }
            const temp:int;
        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test91(self):
        input = """
        class Program{
            var a:int = 2;
            func test():int{}
            func @main():void{
                self.test();
            }
            const temp:int;
        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test92(self):
        input = """
        class Program{
            var a:int = 2;
            func @test():void{}
            func @main():void{
                @test();
            }
            const temp:int;
        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test93(self):
        input = """
        class Program{
            var a:int = 2;
            func @test():float{}
            func @main():void{
            }
            const temp:int;
        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test94(self):
        input = """
        class Program{
            func @main():void{
                var arr:[2]int = [2,5];
                io.@writeFloat(arr[0]);
            }
            const temp:int;
        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test95(self):
        input = """
        class Program{
            var arr:[2]int = [2,5];
            func @main():void{
                io.@writeFloat(self.arr[0]);
            }
            const temp:int;
        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test96(self):
        input = """
        class Program{
            var arr:[2]int = [2,5];
            func @main():void{
                io.@writeFloat(("2w4"^"23")[0]);
            }
            const temp:int;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(BinaryOp(^,StringLit(2w4),StringLit(23)),IntLit(0))"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test97(self):
        input = """
        class Program{
            func @main():void{
                var arr:[2]int = [2,5];
                io.@writeFloat(arr[arr[0]]);
            }
            const temp:int;
        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test98(self):
        input = """
        class Program{
            func @main():void{
                var arr:[2]int = [2,5];
                io.@writeFloat(arr[arr[1]+5]);
            }
            const temp:int;
        }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test99(self):
        input = """
        class Program{
            func @main():void{
                var arr:[2]int = [2,5];
                io.@writeFloat(arr["24"]);
            }
            const temp:int;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(arr),StringLit(24))"
        self.assertTrue(TestChecker.test(input, expect, 499))
