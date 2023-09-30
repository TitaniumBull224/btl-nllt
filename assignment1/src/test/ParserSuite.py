import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_0(self):
        input = """class Program {
            var delta: [11]string = [1,2,3,4];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 200))

    def test_1(self):
        input = """class Program {
            const a, b, c: int = 3, 4, 6;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_2(self):
        input = """class Program{var  a, b, c, d: int = 3, 4, 6;}"""
        expect = "Error on line 1 col 44: ;"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_3(self):
        input = """class Program {
            func @main():int {}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_4(self):
        input = """class Program {
            var x: int = 65;
            func @fact(n: int):int {
                if n == 0 {return 1;}
                else {return n * @fact(n - 1);}
            }
            func  @inc( n, delta: int):void {
                n := n + delta;
                return n;
            }
            func @main():int {
                var delta: int = @fact(3);
                @inc(self.x, delta);
                io.@writeInt(self.x);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_5(self):
        input = """class Program {
            func @main():int {
                if {i := 0;} j > i {j := j - 1;} else {j := j + 1;}
                for i := 0;  i < 10;  i := 1 {
                    self.aPI := 3.14;
                    value := x.foo(5);
                    l[3] := value * 2;
                }
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
            var a: int = 5;
            func @increment():void {
                self.a := self.a + 1;
            }
            func @main():int {
                @increment();
                return self.a;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_10(self):
        input = """class Program {
            var a: int = 5;
            func @decrement():void {
                self.a := self.a - 1;
            }
            func @main():int {
                @decrement();
                return self.a;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_11(self):
        input = """class Program {
            var a: int = 5;
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
            var a: int = 5
        }"""
        expect = "Error on line 3 col 8: }"
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
                
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_16(self):
        input = """class Program {
            func @main():int {
                @increment();
                return self.a;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))
