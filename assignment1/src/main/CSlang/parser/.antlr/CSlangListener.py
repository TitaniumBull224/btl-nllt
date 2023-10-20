# Generated from d:/Program/XAMPP/htdocs/btl-nllt/assignment1/src/main/CSlang/parser/CSlang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CSlangParser import CSlangParser
else:
    from CSlangParser import CSlangParser

# This class defines a complete listener for a parse tree produced by CSlangParser.
class CSlangListener(ParseTreeListener):

    # Enter a parse tree produced by CSlangParser#program.
    def enterProgram(self, ctx:CSlangParser.ProgramContext):
        pass

    # Exit a parse tree produced by CSlangParser#program.
    def exitProgram(self, ctx:CSlangParser.ProgramContext):
        pass


    # Enter a parse tree produced by CSlangParser#classdecllist.
    def enterClassdecllist(self, ctx:CSlangParser.ClassdecllistContext):
        pass

    # Exit a parse tree produced by CSlangParser#classdecllist.
    def exitClassdecllist(self, ctx:CSlangParser.ClassdecllistContext):
        pass


    # Enter a parse tree produced by CSlangParser#classdecl.
    def enterClassdecl(self, ctx:CSlangParser.ClassdeclContext):
        pass

    # Exit a parse tree produced by CSlangParser#classdecl.
    def exitClassdecl(self, ctx:CSlangParser.ClassdeclContext):
        pass


    # Enter a parse tree produced by CSlangParser#memberlist.
    def enterMemberlist(self, ctx:CSlangParser.MemberlistContext):
        pass

    # Exit a parse tree produced by CSlangParser#memberlist.
    def exitMemberlist(self, ctx:CSlangParser.MemberlistContext):
        pass


    # Enter a parse tree produced by CSlangParser#member.
    def enterMember(self, ctx:CSlangParser.MemberContext):
        pass

    # Exit a parse tree produced by CSlangParser#member.
    def exitMember(self, ctx:CSlangParser.MemberContext):
        pass


    # Enter a parse tree produced by CSlangParser#attribute.
    def enterAttribute(self, ctx:CSlangParser.AttributeContext):
        pass

    # Exit a parse tree produced by CSlangParser#attribute.
    def exitAttribute(self, ctx:CSlangParser.AttributeContext):
        pass


    # Enter a parse tree produced by CSlangParser#attlistdecl.
    def enterAttlistdecl(self, ctx:CSlangParser.AttlistdeclContext):
        pass

    # Exit a parse tree produced by CSlangParser#attlistdecl.
    def exitAttlistdecl(self, ctx:CSlangParser.AttlistdeclContext):
        pass


    # Enter a parse tree produced by CSlangParser#attlistnodecl.
    def enterAttlistnodecl(self, ctx:CSlangParser.AttlistnodeclContext):
        pass

    # Exit a parse tree produced by CSlangParser#attlistnodecl.
    def exitAttlistnodecl(self, ctx:CSlangParser.AttlistnodeclContext):
        pass


    # Enter a parse tree produced by CSlangParser#atttyp.
    def enterAtttyp(self, ctx:CSlangParser.AtttypContext):
        pass

    # Exit a parse tree produced by CSlangParser#atttyp.
    def exitAtttyp(self, ctx:CSlangParser.AtttypContext):
        pass


    # Enter a parse tree produced by CSlangParser#typ.
    def enterTyp(self, ctx:CSlangParser.TypContext):
        pass

    # Exit a parse tree produced by CSlangParser#typ.
    def exitTyp(self, ctx:CSlangParser.TypContext):
        pass


    # Enter a parse tree produced by CSlangParser#arraytyp.
    def enterArraytyp(self, ctx:CSlangParser.ArraytypContext):
        pass

    # Exit a parse tree produced by CSlangParser#arraytyp.
    def exitArraytyp(self, ctx:CSlangParser.ArraytypContext):
        pass


    # Enter a parse tree produced by CSlangParser#classtyp.
    def enterClasstyp(self, ctx:CSlangParser.ClasstypContext):
        pass

    # Exit a parse tree produced by CSlangParser#classtyp.
    def exitClasstyp(self, ctx:CSlangParser.ClasstypContext):
        pass


    # Enter a parse tree produced by CSlangParser#method.
    def enterMethod(self, ctx:CSlangParser.MethodContext):
        pass

    # Exit a parse tree produced by CSlangParser#method.
    def exitMethod(self, ctx:CSlangParser.MethodContext):
        pass


    # Enter a parse tree produced by CSlangParser#paramlist.
    def enterParamlist(self, ctx:CSlangParser.ParamlistContext):
        pass

    # Exit a parse tree produced by CSlangParser#paramlist.
    def exitParamlist(self, ctx:CSlangParser.ParamlistContext):
        pass


    # Enter a parse tree produced by CSlangParser#params.
    def enterParams(self, ctx:CSlangParser.ParamsContext):
        pass

    # Exit a parse tree produced by CSlangParser#params.
    def exitParams(self, ctx:CSlangParser.ParamsContext):
        pass


    # Enter a parse tree produced by CSlangParser#blockstmt.
    def enterBlockstmt(self, ctx:CSlangParser.BlockstmtContext):
        pass

    # Exit a parse tree produced by CSlangParser#blockstmt.
    def exitBlockstmt(self, ctx:CSlangParser.BlockstmtContext):
        pass


    # Enter a parse tree produced by CSlangParser#parenexpr.
    def enterParenexpr(self, ctx:CSlangParser.ParenexprContext):
        pass

    # Exit a parse tree produced by CSlangParser#parenexpr.
    def exitParenexpr(self, ctx:CSlangParser.ParenexprContext):
        pass


    # Enter a parse tree produced by CSlangParser#expressions.
    def enterExpressions(self, ctx:CSlangParser.ExpressionsContext):
        pass

    # Exit a parse tree produced by CSlangParser#expressions.
    def exitExpressions(self, ctx:CSlangParser.ExpressionsContext):
        pass


    # Enter a parse tree produced by CSlangParser#exprprime.
    def enterExprprime(self, ctx:CSlangParser.ExprprimeContext):
        pass

    # Exit a parse tree produced by CSlangParser#exprprime.
    def exitExprprime(self, ctx:CSlangParser.ExprprimeContext):
        pass


    # Enter a parse tree produced by CSlangParser#exprstr.
    def enterExprstr(self, ctx:CSlangParser.ExprstrContext):
        pass

    # Exit a parse tree produced by CSlangParser#exprstr.
    def exitExprstr(self, ctx:CSlangParser.ExprstrContext):
        pass


    # Enter a parse tree produced by CSlangParser#exprrel.
    def enterExprrel(self, ctx:CSlangParser.ExprrelContext):
        pass

    # Exit a parse tree produced by CSlangParser#exprrel.
    def exitExprrel(self, ctx:CSlangParser.ExprrelContext):
        pass


    # Enter a parse tree produced by CSlangParser#exprlog.
    def enterExprlog(self, ctx:CSlangParser.ExprlogContext):
        pass

    # Exit a parse tree produced by CSlangParser#exprlog.
    def exitExprlog(self, ctx:CSlangParser.ExprlogContext):
        pass


    # Enter a parse tree produced by CSlangParser#expradd.
    def enterExpradd(self, ctx:CSlangParser.ExpraddContext):
        pass

    # Exit a parse tree produced by CSlangParser#expradd.
    def exitExpradd(self, ctx:CSlangParser.ExpraddContext):
        pass


    # Enter a parse tree produced by CSlangParser#exprmul.
    def enterExprmul(self, ctx:CSlangParser.ExprmulContext):
        pass

    # Exit a parse tree produced by CSlangParser#exprmul.
    def exitExprmul(self, ctx:CSlangParser.ExprmulContext):
        pass


    # Enter a parse tree produced by CSlangParser#exprnot.
    def enterExprnot(self, ctx:CSlangParser.ExprnotContext):
        pass

    # Exit a parse tree produced by CSlangParser#exprnot.
    def exitExprnot(self, ctx:CSlangParser.ExprnotContext):
        pass


    # Enter a parse tree produced by CSlangParser#exprsign.
    def enterExprsign(self, ctx:CSlangParser.ExprsignContext):
        pass

    # Exit a parse tree produced by CSlangParser#exprsign.
    def exitExprsign(self, ctx:CSlangParser.ExprsignContext):
        pass


    # Enter a parse tree produced by CSlangParser#exprindex.
    def enterExprindex(self, ctx:CSlangParser.ExprindexContext):
        pass

    # Exit a parse tree produced by CSlangParser#exprindex.
    def exitExprindex(self, ctx:CSlangParser.ExprindexContext):
        pass


    # Enter a parse tree produced by CSlangParser#exprinst.
    def enterExprinst(self, ctx:CSlangParser.ExprinstContext):
        pass

    # Exit a parse tree produced by CSlangParser#exprinst.
    def exitExprinst(self, ctx:CSlangParser.ExprinstContext):
        pass


    # Enter a parse tree produced by CSlangParser#exprstat.
    def enterExprstat(self, ctx:CSlangParser.ExprstatContext):
        pass

    # Exit a parse tree produced by CSlangParser#exprstat.
    def exitExprstat(self, ctx:CSlangParser.ExprstatContext):
        pass


    # Enter a parse tree produced by CSlangParser#exprobj.
    def enterExprobj(self, ctx:CSlangParser.ExprobjContext):
        pass

    # Exit a parse tree produced by CSlangParser#exprobj.
    def exitExprobj(self, ctx:CSlangParser.ExprobjContext):
        pass


    # Enter a parse tree produced by CSlangParser#exprparen.
    def enterExprparen(self, ctx:CSlangParser.ExprparenContext):
        pass

    # Exit a parse tree produced by CSlangParser#exprparen.
    def exitExprparen(self, ctx:CSlangParser.ExprparenContext):
        pass


    # Enter a parse tree produced by CSlangParser#identifiers.
    def enterIdentifiers(self, ctx:CSlangParser.IdentifiersContext):
        pass

    # Exit a parse tree produced by CSlangParser#identifiers.
    def exitIdentifiers(self, ctx:CSlangParser.IdentifiersContext):
        pass


    # Enter a parse tree produced by CSlangParser#literals.
    def enterLiterals(self, ctx:CSlangParser.LiteralsContext):
        pass

    # Exit a parse tree produced by CSlangParser#literals.
    def exitLiterals(self, ctx:CSlangParser.LiteralsContext):
        pass


    # Enter a parse tree produced by CSlangParser#arrayliteral.
    def enterArrayliteral(self, ctx:CSlangParser.ArrayliteralContext):
        pass

    # Exit a parse tree produced by CSlangParser#arrayliteral.
    def exitArrayliteral(self, ctx:CSlangParser.ArrayliteralContext):
        pass


    # Enter a parse tree produced by CSlangParser#arrint.
    def enterArrint(self, ctx:CSlangParser.ArrintContext):
        pass

    # Exit a parse tree produced by CSlangParser#arrint.
    def exitArrint(self, ctx:CSlangParser.ArrintContext):
        pass


    # Enter a parse tree produced by CSlangParser#arrfloat.
    def enterArrfloat(self, ctx:CSlangParser.ArrfloatContext):
        pass

    # Exit a parse tree produced by CSlangParser#arrfloat.
    def exitArrfloat(self, ctx:CSlangParser.ArrfloatContext):
        pass


    # Enter a parse tree produced by CSlangParser#arrbool.
    def enterArrbool(self, ctx:CSlangParser.ArrboolContext):
        pass

    # Exit a parse tree produced by CSlangParser#arrbool.
    def exitArrbool(self, ctx:CSlangParser.ArrboolContext):
        pass


    # Enter a parse tree produced by CSlangParser#arrstr.
    def enterArrstr(self, ctx:CSlangParser.ArrstrContext):
        pass

    # Exit a parse tree produced by CSlangParser#arrstr.
    def exitArrstr(self, ctx:CSlangParser.ArrstrContext):
        pass


    # Enter a parse tree produced by CSlangParser#boolliteral.
    def enterBoolliteral(self, ctx:CSlangParser.BoolliteralContext):
        pass

    # Exit a parse tree produced by CSlangParser#boolliteral.
    def exitBoolliteral(self, ctx:CSlangParser.BoolliteralContext):
        pass


    # Enter a parse tree produced by CSlangParser#statements.
    def enterStatements(self, ctx:CSlangParser.StatementsContext):
        pass

    # Exit a parse tree produced by CSlangParser#statements.
    def exitStatements(self, ctx:CSlangParser.StatementsContext):
        pass


    # Enter a parse tree produced by CSlangParser#stmt.
    def enterStmt(self, ctx:CSlangParser.StmtContext):
        pass

    # Exit a parse tree produced by CSlangParser#stmt.
    def exitStmt(self, ctx:CSlangParser.StmtContext):
        pass


    # Enter a parse tree produced by CSlangParser#stmtassign.
    def enterStmtassign(self, ctx:CSlangParser.StmtassignContext):
        pass

    # Exit a parse tree produced by CSlangParser#stmtassign.
    def exitStmtassign(self, ctx:CSlangParser.StmtassignContext):
        pass


    # Enter a parse tree produced by CSlangParser#lhs.
    def enterLhs(self, ctx:CSlangParser.LhsContext):
        pass

    # Exit a parse tree produced by CSlangParser#lhs.
    def exitLhs(self, ctx:CSlangParser.LhsContext):
        pass


    # Enter a parse tree produced by CSlangParser#lhsinst.
    def enterLhsinst(self, ctx:CSlangParser.LhsinstContext):
        pass

    # Exit a parse tree produced by CSlangParser#lhsinst.
    def exitLhsinst(self, ctx:CSlangParser.LhsinstContext):
        pass


    # Enter a parse tree produced by CSlangParser#lhsstat.
    def enterLhsstat(self, ctx:CSlangParser.LhsstatContext):
        pass

    # Exit a parse tree produced by CSlangParser#lhsstat.
    def exitLhsstat(self, ctx:CSlangParser.LhsstatContext):
        pass


    # Enter a parse tree produced by CSlangParser#lhsparen.
    def enterLhsparen(self, ctx:CSlangParser.LhsparenContext):
        pass

    # Exit a parse tree produced by CSlangParser#lhsparen.
    def exitLhsparen(self, ctx:CSlangParser.LhsparenContext):
        pass



del CSlangParser