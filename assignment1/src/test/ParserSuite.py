import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_0(self):
        input = """class Program {
            var alpha: [5]int = [1,2,3,4,5];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 200))

    def test_1(self):
        input = """class Program {
            const first, second, third: int = 3, 4, 6;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_2(self):
        input = """class Program <- Nogood {
            var  one, two, three: int = 4, 5, 6, 7;
        }"""
        expect = "Error on line 2 col 47: ,"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_3(self):
        input = """class Program {
            func @main():int {}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_4(self):
        input = """class Program {
            func @main():int {
                var delta: [3]int = [fact(3), self.weird(), 1+2-3*4/5%6];
            }
        }"""
        expect = "Error on line 3 col 37: fact"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_5(self):
        input = """class Program {
            func @main():int {
                io.@writeInt(delta[2]);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_6(self):
        input = """class Program {
            func @main():int {
                for i := 0;  i < 10;  i := 1 {
                    if {j := 5;} j > i {j := j - 1; continue;} else {j := j + 1; break;}
                    return i * j + 3;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_7(self):
        input = """class Program {
            var [3]a: int = [1.2, 1, 3];
        }"""
        expect = "Error on line 2 col 16: ["
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_8(self):
        input = """class Program {
            var a: [5]int = [1,2,3,4,5];
            func @main():int {
                return self.a[2];
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_9(self):
        input = """class Program {
            func @increment():void {
                so.a := self.a + 1;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_10(self):
        input = """class Program {
            func @decrement():void {
                self.a := 12.b;
            }
        }"""
        expect = "Error on line 3 col 29: b"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_11(self):
        input = """class Program {
            func @multiply(n: int):void {
                self.a := self.a * n;
            }
            func @main():int {
                @multiply(2);
                return self.a;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_12(self):
        input = """class Program {
            // whatisthis\t\q\e\p\'\"fq
            var a: int = "hello";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_13(self):
        input = """class Program {
            var a: [2]int = [5];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_14(self):
        input = """class Program {
            func @main():int {
                return (a ^ 34 + 24 - 624 && !37 || 54) * -34;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_15(self):
        input = """class Program {
            func @main():void {
                i := self;
            }
        }"""
        expect = "Error on line 3 col 25: ;"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_16(self):
        input = """class Program {
            func @main():int {
                self.b := self.@e + a * (1 + io.h[2-(5+u)/3]);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_17(self):
        input = """class Program {
            func @main():int {
                for i := 3 + 5; i >= i + 2; i := i - 1 {
                    @lol(13);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_18(self):
        input = """class Program {
            func @main():int {
                return self.a;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_19(self):
        input = """class Program {
            var a: int = 5;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_20(self):
        input = """class Program {
            func @main():int {
                return self.a + 5;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_21(self):
        input = """class Program {
            func @main():int {
                return self.a - 5;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_22(self):
        input = """class Program {
            func @main():int {
                return self.a * 5;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_23(self):
        input = """class Program {
            func @main():int {
                return self.a / 5;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_24(self):
        input = """class Program {
            func @main():int {
                return self.a % 5;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_25(self):
        input = """class Program {
            func @main():int {
                return -self.a;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_26(self):
        input = """class Program {
            func @main():int {
                return !self.a;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_27(self):
        input = """class Program {
            func @main():int {
                return self.a && 5;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_28(self):
        input = """class Program {
            // This is a comment
            /* This is a
            block comment */
            var x: string = "whatever \\t";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_29(self):
        input = """class Program {
            var x: int = 10;
            func @double(n: int):int {
                return n * 2;
            }
            func @main():int {
                self.x := @double(self.x);
                return self.x;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_29(self):
        input = """class Program {
            const a: [789]int = [12];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_30(self):
        input = """class Program {
            var @ma : [2]int;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_31(self):
        input = """class Program {
            var @ma := 123;
        }"""
        expect = "Error on line 2 col 20: :="
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_32(self):
        input = """class Program {
            func abd(): void {}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_33(self):
        input = """class Program {
            var x: int = 20;
            func @triple(n: int):int {
                return n * 3;
            }
            func @main():int {
                self.x := @triple(self.x);
                return self.x;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_34(self):
        input = """class Program {
            var x: int = 30;
            func @quadruple(n: int):int {
                return n * 4;
            }
            func @main():int {
                self.x := @quadruple(self.x);
                return self.x;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_35(self):
        input = """class Program {
            const a: [123]int = [45];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_36(self):
        input = """class Program {
            var @mb : [3]int;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_37(self):
        input = """class Program {
            var @mc := 456;
        }"""
        expect = "Error on line 2 col 20: :="
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_38(self):
        input = """class Program {
            func cde(): void {}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_39(self):
        input = """class Program {
            var x: int = 40;
            func @quintuple(n: int):int {
                return n * 5;
            }
            func @main():int {
                self.x := @quintuple(self.x);
                return self.x;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_40(self):
        input = """class Program {
            var x: int = 50;
            func @sextuple(n: int):int {
                return n * 6;
            }
            func @main():int {
                self.x := @sextuple(self.x);
                return self.x;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_41(self):
        input = """class Program {
            func @how(): void {
                a.a.a();
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_42(self):
        input = """class Program {
            func @how(): void {
                a;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_43(self):
        input = """class Program {
            func @how(): void {
                if i > 2 {return;}
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_44(self):
        input = """class Program {
            func @how(): void {
                self := self + 1;
            }
        }"""
        expect = "Error on line 3 col 21: :="
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_45(self):
        input = """class Program {
            func @how(): void {
                const n, t, r: [3]int = [1, 2], [4, 2], [5, 9];
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_46(self):
        input = """class Program {
            func @how(): void {
                const n, t, r: string = abc^@aou, "[4,\\" 2]", "\\\\what\\t";
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_47(self):
        input = """class Program {
            func @how(): void {
                if i % 5 != 2 && true {return;}
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_48(self):
        input = """class Program {
            func @how(): void {
                if i % 5 == 2 && 3 != 2 {return;}
            }
        }"""
        expect = "Error on line 3 col 35: !="
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_49(self):
        input = """class Program {
            var x: int = 10;
            func @main():int {
                if self.x > 5 {return self.x;}
                else {return 0;}
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_50(self):
        input = """class Program {
            var x: int = 10;
            func @main():int {
                for i := 0; i < self.x; i := i + 1 {
                    return i;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_51(self):
        input = """class Program {
            var x: int = 10;
            func @main():int {
                if self.x > 0 {
                    self.x := self.x - 1;
                }
                return self.x;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_52(self):
        input = """class Program {
            var x: int = 10;
            func @main():int {
                do {
                    self.x := self.x - 1;
                } while self.x > 0;
                return self.x;
            }
        }"""
        expect = "Error on line 4 col 19: {"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_53(self):
        input = """class Program {
            func @main():void {
                var int x = 23;
            }
        }"""
        expect = "Error on line 3 col 20: int"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_54(self):
        input = """class Program {
            func @main():void {
                const x := 10;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_55(self):
        input = """class Program {
            func @main():void {
                if true return;
            }
        }"""
        expect = "Error on line 3 col 24: return"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_56(self):
        input = """class Program {
            func @main():void {
                for i := 0; i < 10; i := i + 1 {return i := 1;}
            }
        }"""
        expect = "Error on line 3 col 57: :="
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_57(self):
        input = """class Program {
            func @main():void {
                break a;
            }
        }"""
        expect = "Error on line 3 col 22: a"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_58(self):
        input = """class Program {
            func @main():void {
                continue;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_59(self):
        input = """class Program {
            func @main():void {
                return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_60(self):
        input = """class Program {
            func @main():void {
                self.x := 10;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_61(self):
        input = """class Program {
            var x: int := ;
        }"""
        expect = "Error on line 2 col 23: :="
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_62(self):
        input = """class Program {
            func @main():void {
                for i := ; i < 10; i := i + 1 {return;}
            }
        }"""
        expect = "Error on line 3 col 25: ;"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_63(self):
        input = """func @main(): void {
            var x: int = 10;
        }"""
        expect = "Error on line 1 col 0: func"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_64(self):
        input = """Program {
            func @main():void {
                const x: int = 10;
            }
        }"""
        expect = "Error on line 1 col 0: Program"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_65(self):
        input = """class Program {
            func @main():void {
                else {return;}
            }
        }"""
        expect = "Error on line 3 col 16: else"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_66(self):
        input = """class Program {
            func @main():void {
                for i := 0; i < 10; i := i + 1 {return;} else {return;};
            }
        }"""
        expect = "Error on line 3 col 57: else"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_67(self):
        input = """class Program {
            func @main():void {
                while true {return;}
                else {return;}
            }
        }"""
        expect = "Error on line 3 col 22: true"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_68(self):
        input = """class Program {
            func @main():void {
                do {return;} while true;
                else {return;}
            }
        }"""
        expect = "Error on line 3 col 19: {"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_69(self):
        input = """class Program {
            func constructor {
                break;
            }
        }"""
        expect = "Error on line 2 col 29: {"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_70(self):
        input = """class Program {
            return 0;
        }"""
        expect = "Error on line 2 col 12: return"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_71(self):
        input = """class Program {
            break;
        }"""
        expect = "Error on line 2 col 12: break"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_72(self):
        input = """class Program {
            func @main():void {
                assert(x > 0);
                return x;
            }
        }"""
        expect = "Error on line 3 col 22: ("
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_73(self):
        input = """class Program {
            func @main():void {
                var a: [3]int = [[23], 4, 5]
            }
        }"""
        expect = "Error on line 3 col 33: ["
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_74(self):
        input = """class Program {
            func @main():void {
                var a: [3]int = [23, , 5];
            }
        }"""
        expect = "Error on line 3 col 37: ,"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_75(self):
        input = """class Program {
            func @main():void {
                var a: int = 5 + ;
            }
        }"""
        expect = "Error on line 3 col 33: ;"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_76(self):
        input = """class Program {
            func @main():void {
                var a: int = 5 - ;
            }
        }"""
        expect = "Error on line 3 col 33: ;"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_77(self):
        input = """class Program {
            func @main():void {
                var a: int = 5 * ;
            }
        }"""
        expect = "Error on line 3 col 33: ;"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_78(self):
        input = """class Program {
            func @main():void {
                var a: int = 5 / ;
            }
        }"""
        expect = "Error on line 3 col 33: ;"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_79(self):
        input = """class Program {
            func @main():void {
                var a: int = 5 % ;
            }
        }"""
        expect = "Error on line 3 col 33: ;"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_80(self):
        input = """class Program {
            func @main():void {
                var a: int = - ;
            }
        }"""
        expect = "Error on line 3 col 31: ;"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_81(self):
        input = """class Program {
            func @main():void {
                var a: int = ! ;
            }
        }"""
        expect = "Error on line 3 col 31: ;"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_82(self):
        input = """class Program {
            func @main():void {
                var a: int = && true;
            }
        }"""
        expect = "Error on line 3 col 29: &&"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_83(self):
        input = """class Program {
            func @main():void {
                var a: int = || false;
            }
        }"""
        expect = "Error on line 3 col 29: ||"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_84(self):
        input = """class Program {
            func @main():void {
                var a: int = == true;
            }
        }"""
        expect = "Error on line 3 col 29: =="
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_85(self):
        input = """class Program {
            func @main():void {
                var a: int = < 5;
            }
        }"""
        expect = "Error on line 3 col 29: <"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_86(self):
        input = """class Program {
            func @main():void {
                var a: int = > 5;
            }
        }"""
        expect = "Error on line 3 col 29: >"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_87(self):
        input = """class Program {
            func @main():void {
                var a: int = <= 5;
            }
        }"""
        expect = "Error on line 3 col 29: <="
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_88(self):
        input = """class Program {
            func @main():void {
                var a: int = >= 5;
            }
        }"""
        expect = "Error on line 3 col 29: >="
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_89(self):
        input = """class Program {
            func @main():void {
                var a: int = != true;
            }
        }"""
        expect = "Error on line 3 col 29: !="
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_90(self):
        input = """class Program {
            func @main():void {
                var a: int = == ;
            }
        }"""
        expect = "Error on line 3 col 29: =="
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_91(self):
        input = """class Program {
            func @main():void {
                var a: int = && ;
            }
        }"""
        expect = "Error on line 3 col 29: &&"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_92(self):
        input = """class Program {
            func @main():void {
                var a: int = || ;
            }
        }"""
        expect = "Error on line 3 col 29: ||"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_93(self):
        input = """class Program {
            func @main():void {
                var a: int = ! ;
            }
        }"""
        expect = "Error on line 3 col 31: ;"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_94(self):
        input = """class Program {
            func @main():void {
                var a: int = - ;
            }
        }"""
        expect = "Error on line 3 col 31: ;"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_95(self):
        input = """class Program {
            func @main():void {
                if {return;}
            }
        }"""
        expect = "Error on line 4 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_96(self):
        input = """class Program {
            func @main():void {
                if false return;
            }
        }"""
        expect = "Error on line 3 col 25: return"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_97(self):
        input = """class Program {
            func @main():void {
                for i := 0; i < 10; i := i + 1 return;
            }
        }"""
        expect = "Error on line 3 col 47: return"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_98(self):
        input = """class Program {
            func @main():void {
                for i := 10; i > 0; i { return };
            }
        }"""
        expect = "Error on line 3 col 38: {"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_99(self):
        input = """class Program {
            func @main():void {
                if true {return;} else return;
            }
        }"""
        expect = "Error on line 3 col 39: return"
        self.assertTrue(TestParser.test(input, expect, 299))
