import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_0(self):
        input = "class Program {//this is a line comment\n}"
        expected = "class,Program,{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 100))

    def test_1(self):
        input = "/*class Program {//this is a line comment\n}*/"
        expected = "<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 101))

    def test_2(self):
        input = "class /* Program <- */ A {}"
        expected = "class,A,{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 102))

    def test_3(self):
        input = (
            "var self.x := 1;/* This is a block comment, that\nmay span in many lines*/"
        )
        expected = "var,self,.,x,:=,1,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 103))

    def test_4(self):
        input = "var a: int = 5;//Hi\nreturn/* aosduhou, agat\nmasdgnwgnes*/;"
        expected = "var,a,:,int,=,5,;,return,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 104))

    def test_5(self):
        input = "/*//aw rgawrgasfgr awghat\nmawvrg liagres*/"
        expected = "<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 105))

    def test_6(self):
        input = "/*fawevfawgrg // hawaeagwrre */\n//awrrament so /* has nawrgawrh here"
        expected = "<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 106))

    def test_7(self):
        input = "@hako156"
        expected = "@hako156,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 107))

    def test_8(self):
        input = "@_"
        expected = "@_,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 108))

    def test_9(self):
        input = "__init__"
        expected = "__init__,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 109))

    def test_10(self):
        input = "trigger\r"
        expected = "trigger,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 110))

    def test_11(self):
        input = "continue"
        expected = "continue,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 111))

    def test_12(self):
        input = "<-"
        expected = "<-,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 112))

    def test_13(self):
        input = "."
        expected = ".,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 113))

    def test_14(self):
        input = "!"
        expected = "!,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 114))

    def test_15(self):
        input = "<="
        expected = "<=,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 115))

    def test_16(self):
        input = "562"
        expected = "562,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 116))

    def test_17(self):
        input = ".91385"
        expected = ".,91385,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 117))

    def test_18(self):
        input = "000000."
        expected = "000000.,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 118))

    def test_19(self):
        input = "00e00"
        expected = "00e00,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 119))

    def test_20(self):
        input = "01.e01"
        expected = "01.e01,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 120))

    def test_21(self):
        input = "e1"
        expected = "e1,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 121))

    def test_22(self):
        input = "32.E+9"
        expected = "32.E+9,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 122))

    def test_23(self):
        input = "e+03"
        expected = "e,+,03,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 123))

    def test_24(self):
        input = "E2e"
        expected = "E2e,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 124))

    def test_25(self):
        input = "00.00E-00"
        expected = "00.00E-00,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 125))

    def test_26(self):
        input = "4e"
        expected = "4,e,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 126))

    def test_27(self):
        input = "0.74E-2"
        expected = "0.74E-2,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 127))

    def test_28(self):
        input = "020e+-15"
        expected = "020,e,+,-,15,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 128))

    def test_29(self):
        input = "0E-0"
        expected = "0E-0,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 129))

    def test_30(self):
        input = "123E4.5"
        expected = "123E4,.,5,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 130))

    def test_31(self):
        input = "a := true"
        expected = "a,:=,true,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 131))

    def test_32(self):
        input = "self.a := false"
        expected = "self,.,a,:=,false,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 132))

    def test_33(self):
        input = "true"
        expected = "true,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 133))

    def test_34(self):
        input = '""'
        expected = ",<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 134))

    def test_35(self):
        input = '"kys\k Hi"'
        expected = "Illegal Escape In String: kys\k"
        self.assertTrue(TestLexer.test(input, expected, 135))

    def test_36(self):
        input = '"kys kek"'
        expected = "kys kek,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 136))

    def test_37(self):
        input = '"kys" "kek"'
        expected = "kys,kek,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 137))

    def test_38(self):
        input = 'foo("kys, wdhmbt!")'
        expected = "foo,(,kys, wdhmbt!,),<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 138))

    def test_39(self):
        input = '"ESL \w kys!"'
        expected = "Illegal Escape In String: ESL \w"
        self.assertTrue(TestLexer.test(input, expected, 139))

    def test_40(self):
        input = 'var str: string = "Where\'s Perry?"'
        expected = "var,str,:,string,=,Where's Perry?,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 140))

    def test_41(self):
        input = 'var str: string = "Where is Perry?"'
        expected = "var,str,:,string,=,Where is Perry?,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 141))

    def test_42(self):
        input = 'var str: string = "Where is Perry?'
        expected = "var,str,:,string,=,Unclosed String: Where is Perry?"
        self.assertTrue(TestLexer.test(input, expected, 142))

    def test_43(self):
        input = '"ESL\\s"'
        expected = "Illegal Escape In String: ESL\s"
        self.assertTrue(TestLexer.test(input, expected, 143))

    def test_44(self):
        input = '",./;\'www[666]!@#@!$"'
        expected = ",./;'www[666]!@#@!$,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 144))

    def test_45(self):
        input = '"Konnichiha\^"'
        expected = "Illegal Escape In String: Konnichiha\^"
        self.assertTrue(TestLexer.test(input, expected, 145))

    def test_46(self):
        input = '"Konnichiha$"'
        expected = "Konnichiha$,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 146))

    def test_47(self):
        input = '"Konnichiha\$"'
        expected = "Illegal Escape In String: Konnichiha\$"
        self.assertTrue(TestLexer.test(input, expected, 147))

    def test_48(self):
        input = '"ESL // kys"'
        expected = "ESL // kys,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 148))

    def test_49(self):
        input = '"ESL ^ kys"'
        expected = "ESL ^ kys,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 149))

    def test_50(self):
        input = '"ESL \& kys"'
        expected = "Illegal Escape In String: ESL \&"
        self.assertTrue(TestLexer.test(input, expected, 150))

    def test_51(self):
        input = '["a","b","c"]'
        expected = "[,a,,,b,,,c,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 151))

    def test_52(self):
        input = "[1,2,3]"
        expected = "[,1,,,2,,,3,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 152))

    def test_53(self):
        input = 'var kaela: [3]int = ["uuu",1,true]'
        expected = "var,kaela,:,[,3,],int,=,[,uuu,,,1,,,true,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 153))

    def test_54(self):
        input = '[["a", 1],"b","c","d"]'
        expected = "[,[,a,,,1,],,,b,,,c,,,d,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 154))

    def test_55(self):
        input = "[[1,2,3],4,5,6]"
        expected = "[,[,1,,,2,,,3,],,,4,,,5,,,6,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 155))

    def test_56(self):
        input = "[a,b],e]"
        expected = "[,a,,,b,],,,e,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 156))

    def test_57(self):
        input = "[new obj(),d],d]"
        expected = "[,new,obj,(,),,,d,],,,d,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 157))

    def test_58(self):
        input = '"new obj()"'
        expected = "new obj(),<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 158))

    def test_59(self):
        input = '""""'
        expected = ",,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 159))

    def test_60(self):
        input = "var aqua: float = 1E+3;"
        expected = "var,aqua,:,float,=,1E+3,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 160))

    def test_61(self):
        input = "[2e3, 4.1, 15e3]"
        expected = "[,2e3,,,4.1,,,15e3,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 161))

    def test_62(self):
        input = "kys\t"
        expected = "kys,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 162))

    def test_63(self):
        input = "4685759"
        expected = "4685759,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 163))

    def test_64(self):
        input = "000.000e+000"
        expected = "000.000e+000,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 164))

    def test_65(self):
        input = "class Omega\n {\n\tvar alpha: int = 563;\n}"
        expected = "class,Omega,{,var,alpha,:,int,=,563,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 165))

    def test_66(self):
        input = "class kink <- fetish {var fella: string;}"
        expected = "class,kink,<-,fetish,{,var,fella,:,string,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 166))

    def test_67(self):
        input = """func @main():int {
            self.x := @double(self.x);
            return self.x;
        }"""
        expected = "func,@main,(,),:,int,{,self,.,x,:=,@double,(,self,.,x,),;,return,self,.,x,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 167))

    def test_68(self):
        input = "continue;"
        expected = "continue,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 168))

    def test_69(self):
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
        expected = "class,Program,{,var,x,:,int,=,40,;,func,@quintuple,(,n,:,int,),:,int,{,return,n,*,5,;,},func,@main,(,),:,int,{,self,.,x,:=,@quintuple,(,self,.,x,),;,return,self,.,x,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 169))

    def test_70(self):
        input = '"ESL""'
        expected = "ESL,Unclosed String: "
        self.assertTrue(TestLexer.test(input, expected, 170))

    def test_71(self):
        input = "true == false"
        expected = "true,==,false,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 171))

    def test_72(self):
        input = "x % 2 != 1"
        expected = "x,%,2,!=,1,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 172))

    def test_73(self):
        input = "jork && true"
        expected = "jork,&&,true,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 173))

    def test_74(self):
        input = "jork &&& true"
        expected = "jork,&&,Error Token &"
        self.assertTrue(TestLexer.test(input, expected, 174))

    def test_75(self):
        input = "jork ||| true"
        expected = "jork,||,Error Token |"
        self.assertTrue(TestLexer.test(input, expected, 175))

    def test_76(self):
        input = "jork \\\ true"
        expected = "jork,\,\,true,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 176))

    def test_77(self):
        input = "jork != false"
        expected = "jork,!=,false,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 177))

    def test_78(self):
        input = "void"
        expected = "void,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 178))

    def test_79(self):
        input = """class Program {
            func constructor {
                break;
            }
        }"""
        expected = "class,Program,{,func,constructor,{,break,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 179))

    def test_80(self):
        input = """class Program {
            func @how(): void {
                if i % 5 != 2 && true {return;}
            }
        }"""
        expected = "class,Program,{,func,@how,(,),:,void,{,if,i,%,5,!=,2,&&,true,{,return,;,},},},<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 180))

    def test_81(self):
        input = """class Program {
            func @how(): void {
                if i > 2 {return;}
            }
        }"""
        expected = (
            "class,Program,{,func,@how,(,),:,void,{,if,i,>,2,{,return,;,},},},<EOF>"
        )
        self.assertTrue(TestLexer.test(input, expected, 181))

    def test_82(self):
        input = """class Program {
            func @how(): void {
                a.a.a();
            }
        }"""
        expected = "class,Program,{,func,@how,(,),:,void,{,a,.,a,.,a,(,),;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 182))

    def test_83(self):
        input = "1+2-3*4/5"
        expected = "1,+,2,-,3,*,4,/,5,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 183))

    def test_84(self):
        input = '"\#dead"'
        expected = "Illegal Escape In String: \#"
        self.assertTrue(TestLexer.test(input, expected, 184))

    def test_85(self):
        input = '"paranoid \Argg \getitout"'
        expected = "Illegal Escape In String: paranoid \A"
        self.assertTrue(TestLexer.test(input, expected, 185))

    def test_86(self):
        input = '"$$$"'
        expected = "$$$,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 186))

    def test_87(self):
        input = '"$"$$'
        expected = "$,Error Token $"
        self.assertTrue(TestLexer.test(input, expected, 187))

    def test_88(self):
        input = "$$$"
        expected = "Error Token $"
        self.assertTrue(TestLexer.test(input, expected, 188))

    def test_89(self):
        input = "\%"
        expected = "\,%,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 189))

    def test_90(self):
        input = '"\%"'
        expected = "Illegal Escape In String: \%"
        self.assertTrue(TestLexer.test(input, expected, 190))

    def test_91(self):
        input = """class Program {
            func @main():int {
                return !self.a;
            }
        }"""
        expected = (
            "class,Program,{,func,@main,(,),:,int,{,return,!,self,.,a,;,},},<EOF>"
        )
        self.assertTrue(TestLexer.test(input, expected, 191))

    def test_92(self):
        input = """class Program {
            const a: [789]int = [12];
        }"""
        expected = "class,Program,{,const,a,:,[,789,],int,=,[,12,],;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 192))

    def test_93(self):
        input = """func @main():int {
            self.x := @triple(self.x);
            return self.x;
        }"""
        expected = "func,@main,(,),:,int,{,self,.,x,:=,@triple,(,self,.,x,),;,return,self,.,x,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 193))

    def test_94(self):
        input = """func @main():int {
            var delta: [3]int = [fact(3), self.weird(), 1+2-3*4/5%6];
        }"""
        expected = "func,@main,(,),:,int,{,var,delta,:,[,3,],int,=,[,fact,(,3,),,,self,.,weird,(,),,,1,+,2,-,3,*,4,/,5,%,6,],;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 194))

    def test_95(self):
        input = """a: string = "haram"; //shinisokonai\n print a;"""
        expected = "a,:,string,=,haram,;,print,a,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 195))

    def test_96(self):
        input = "io.@writeInt(delta[2]);"
        expected = "io,.,@writeInt,(,delta,[,2,],),;,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 196))

    def test_97(self):
        input = """func @main():int {
            return (a ^ 34 + 24 - 624 && !37 || 54) * -34;
        }"""
        expected = "func,@main,(,),:,int,{,return,(,a,^,34,+,24,-,624,&&,!,37,||,54,),*,-,34,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 197))

    def test_98(self):
        input = """print "ESL \nkys"""
        expected = "print,Unclosed String: ESL "
        self.assertTrue(TestLexer.test(input, expected, 198))

    def test_99(self):
        input = """ print "ESL \\nkys" """
        expected = "print,ESL \\nkys,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 199))
