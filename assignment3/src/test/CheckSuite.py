import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    def test0(self):
        input = """
            class Program {
                func @main(): void {}
            }
            class a {}
            class b {}
            class a {}
        """
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test1(self):
        input = """
            class Program {}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test2(self):
        input = """
            class Program {
                func @main(): void {}
            }
            class a {}
            class b {}
            class b <- a {}
        """
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test3(self):
        input = """
            class Program {
                func @main(): void {}
            }
            class Program {
                func @main(): void {}
            }
        """
        expect = "Redeclared Class: Program"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test4(self):
        input = """
            class a {}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test5(self):
        input = """
            class Program {
                var a: int = 1;
                const a: float = 1.0;
                func @main(): void {}
            }
        """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test6(self):
        input = """
            class Program {
                var a, b: int = 1, 2;
                const b: float = 1.0;
                func @main(): void {}
            }
        """
        expect = "Redeclared Attribute: b"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test7(self):
        input = """
            class Program {
                var a: int = 1;
                func a(): int {}
                func @main(): void {}
            }
        """
        expect = "Redeclared Method: a"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test8(self):
        input = """
            class Program {
                func @main(): void {}
            }
            class Program <- a {
                func @main(): void {}
                var a, @main: int = 1, 2; 
            }
        """
        expect = "Redeclared Attribute: @main"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test9(self):
        input = """
            class Program {
                func @main(): void {}
                func hololive(member: string): int {}
                var member: int;
                const hololive: float;
            }
        """
        expect = "Redeclared Attribute: hololive"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test10(self):
        input = """
            class a {
                var b: int = 1;
            }
            class a <- Program {
                func @main(): void {}
                var b, c: float = 1.1, 1.2;
                const c: bool = true;
            }
        """
        expect = "Redeclared Attribute: c"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test11(self):
        input = """
            class Program {
                func @main(): void {}
                func a(b: int): int {}
                func a(c: float): float {}
            }
        """
        expect = "Redeclared Method: a"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test12(self):
        input = """
            class Program {
                func @main(): void {}
                var a: int = 1;
                func a(c: float): float {}
            }
        """
        expect = "Redeclared Method: a"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test13(self):
        input = """
            class Program {
                func @main(): void {}
                func constructor(a: float) {}
                func constructor(b: float) {}
                func @main(): void {}
            }
        """
        expect = "Redeclared Method: @main"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test14(self):
        input = """
            class Program {
                func @main(): void {}
                func main(): void {}
            }
            class io {}
        """
        expect = "Redeclared Class: io"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test15(self):
        input = """
            class Program {
                func @main(): void {}
            }
            class a {}
            class a <- a {}
        """
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test16(self):
        input = """
            class b {
                func @main(): void {}
            }
            class a {
                func @main(): void {}
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test17(self):
        input = """
            class program {
                func @main(): void {}
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test18(self):
        input = """
            class Program {
                func @Main(): void {}
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test19(self):
        input = """
            class Program {
                func main(): void {}
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 419))
