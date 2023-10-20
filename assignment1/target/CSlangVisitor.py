# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CSlangParser import CSlangParser
else:
    from CSlangParser import CSlangParser

# This class defines a complete generic visitor for a parse tree produced by CSlangParser.

class CSlangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSlangParser#program.
    def visitProgram(self, ctx:CSlangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#classdecllist.
    def visitClassdecllist(self, ctx:CSlangParser.ClassdecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#classdecl.
    def visitClassdecl(self, ctx:CSlangParser.ClassdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#memberlist.
    def visitMemberlist(self, ctx:CSlangParser.MemberlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#member.
    def visitMember(self, ctx:CSlangParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attribute.
    def visitAttribute(self, ctx:CSlangParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attlistdecl.
    def visitAttlistdecl(self, ctx:CSlangParser.AttlistdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attlistnodecl.
    def visitAttlistnodecl(self, ctx:CSlangParser.AttlistnodeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#atttyp.
    def visitAtttyp(self, ctx:CSlangParser.AtttypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#typ.
    def visitTyp(self, ctx:CSlangParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#arraytyp.
    def visitArraytyp(self, ctx:CSlangParser.ArraytypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#classtyp.
    def visitClasstyp(self, ctx:CSlangParser.ClasstypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#method.
    def visitMethod(self, ctx:CSlangParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#paramlist.
    def visitParamlist(self, ctx:CSlangParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#params.
    def visitParams(self, ctx:CSlangParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#blockstmt.
    def visitBlockstmt(self, ctx:CSlangParser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#parenexpr.
    def visitParenexpr(self, ctx:CSlangParser.ParenexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expressions.
    def visitExpressions(self, ctx:CSlangParser.ExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exprprime.
    def visitExprprime(self, ctx:CSlangParser.ExprprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exprstr.
    def visitExprstr(self, ctx:CSlangParser.ExprstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exprrel.
    def visitExprrel(self, ctx:CSlangParser.ExprrelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exprlog.
    def visitExprlog(self, ctx:CSlangParser.ExprlogContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expradd.
    def visitExpradd(self, ctx:CSlangParser.ExpraddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exprmul.
    def visitExprmul(self, ctx:CSlangParser.ExprmulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exprnot.
    def visitExprnot(self, ctx:CSlangParser.ExprnotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exprsign.
    def visitExprsign(self, ctx:CSlangParser.ExprsignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exprindex.
    def visitExprindex(self, ctx:CSlangParser.ExprindexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exprinst.
    def visitExprinst(self, ctx:CSlangParser.ExprinstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exprstat.
    def visitExprstat(self, ctx:CSlangParser.ExprstatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exprobj.
    def visitExprobj(self, ctx:CSlangParser.ExprobjContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exprparen.
    def visitExprparen(self, ctx:CSlangParser.ExprparenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#identifiers.
    def visitIdentifiers(self, ctx:CSlangParser.IdentifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#literals.
    def visitLiterals(self, ctx:CSlangParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#arrayliteral.
    def visitArrayliteral(self, ctx:CSlangParser.ArrayliteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#arrint.
    def visitArrint(self, ctx:CSlangParser.ArrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#arrfloat.
    def visitArrfloat(self, ctx:CSlangParser.ArrfloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#arrbool.
    def visitArrbool(self, ctx:CSlangParser.ArrboolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#arrstr.
    def visitArrstr(self, ctx:CSlangParser.ArrstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#boolliteral.
    def visitBoolliteral(self, ctx:CSlangParser.BoolliteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#statements.
    def visitStatements(self, ctx:CSlangParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#stmt.
    def visitStmt(self, ctx:CSlangParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#stmtassign.
    def visitStmtassign(self, ctx:CSlangParser.StmtassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#lhs.
    def visitLhs(self, ctx:CSlangParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#lhsinst.
    def visitLhsinst(self, ctx:CSlangParser.LhsinstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#lhsstat.
    def visitLhsstat(self, ctx:CSlangParser.LhsstatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#lhsparen.
    def visitLhsparen(self, ctx:CSlangParser.LhsparenContext):
        return self.visitChildren(ctx)



del CSlangParser