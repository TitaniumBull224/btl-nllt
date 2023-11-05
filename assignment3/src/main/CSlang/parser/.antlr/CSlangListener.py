# Generated from d:/Program/XAMPP/htdocs/btl-nllt/assignment3/src/main/CSlang/parser/CSlang.g4 by ANTLR 4.13.1
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


    # Enter a parse tree produced by CSlangParser#vardecl.
    def enterVardecl(self, ctx:CSlangParser.VardeclContext):
        pass

    # Exit a parse tree produced by CSlangParser#vardecl.
    def exitVardecl(self, ctx:CSlangParser.VardeclContext):
        pass


    # Enter a parse tree produced by CSlangParser#constdecl.
    def enterConstdecl(self, ctx:CSlangParser.ConstdeclContext):
        pass

    # Exit a parse tree produced by CSlangParser#constdecl.
    def exitConstdecl(self, ctx:CSlangParser.ConstdeclContext):
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


    # Enter a parse tree produced by CSlangParser#param.
    def enterParam(self, ctx:CSlangParser.ParamContext):
        pass

    # Exit a parse tree produced by CSlangParser#param.
    def exitParam(self, ctx:CSlangParser.ParamContext):
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


    # Enter a parse tree produced by CSlangParser#exprlist.
    def enterExprlist(self, ctx:CSlangParser.ExprlistContext):
        pass

    # Exit a parse tree produced by CSlangParser#exprlist.
    def exitExprlist(self, ctx:CSlangParser.ExprlistContext):
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


    # Enter a parse tree produced by CSlangParser#identifier.
    def enterIdentifier(self, ctx:CSlangParser.IdentifierContext):
        pass

    # Exit a parse tree produced by CSlangParser#identifier.
    def exitIdentifier(self, ctx:CSlangParser.IdentifierContext):
        pass


    # Enter a parse tree produced by CSlangParser#lit.
    def enterLit(self, ctx:CSlangParser.LitContext):
        pass

    # Exit a parse tree produced by CSlangParser#lit.
    def exitLit(self, ctx:CSlangParser.LitContext):
        pass


    # Enter a parse tree produced by CSlangParser#boollit.
    def enterBoollit(self, ctx:CSlangParser.BoollitContext):
        pass

    # Exit a parse tree produced by CSlangParser#boollit.
    def exitBoollit(self, ctx:CSlangParser.BoollitContext):
        pass


    # Enter a parse tree produced by CSlangParser#arraylit.
    def enterArraylit(self, ctx:CSlangParser.ArraylitContext):
        pass

    # Exit a parse tree produced by CSlangParser#arraylit.
    def exitArraylit(self, ctx:CSlangParser.ArraylitContext):
        pass


    # Enter a parse tree produced by CSlangParser#litlist.
    def enterLitlist(self, ctx:CSlangParser.LitlistContext):
        pass

    # Exit a parse tree produced by CSlangParser#litlist.
    def exitLitlist(self, ctx:CSlangParser.LitlistContext):
        pass


    # Enter a parse tree produced by CSlangParser#litprime.
    def enterLitprime(self, ctx:CSlangParser.LitprimeContext):
        pass

    # Exit a parse tree produced by CSlangParser#litprime.
    def exitLitprime(self, ctx:CSlangParser.LitprimeContext):
        pass


    # Enter a parse tree produced by CSlangParser#stmtlist.
    def enterStmtlist(self, ctx:CSlangParser.StmtlistContext):
        pass

    # Exit a parse tree produced by CSlangParser#stmtlist.
    def exitStmtlist(self, ctx:CSlangParser.StmtlistContext):
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


    # Enter a parse tree produced by CSlangParser#stmtinvoc.
    def enterStmtinvoc(self, ctx:CSlangParser.StmtinvocContext):
        pass

    # Exit a parse tree produced by CSlangParser#stmtinvoc.
    def exitStmtinvoc(self, ctx:CSlangParser.StmtinvocContext):
        pass


    # Enter a parse tree produced by CSlangParser#stmtinvocinst.
    def enterStmtinvocinst(self, ctx:CSlangParser.StmtinvocinstContext):
        pass

    # Exit a parse tree produced by CSlangParser#stmtinvocinst.
    def exitStmtinvocinst(self, ctx:CSlangParser.StmtinvocinstContext):
        pass


    # Enter a parse tree produced by CSlangParser#stmtinvocstat.
    def enterStmtinvocstat(self, ctx:CSlangParser.StmtinvocstatContext):
        pass

    # Exit a parse tree produced by CSlangParser#stmtinvocstat.
    def exitStmtinvocstat(self, ctx:CSlangParser.StmtinvocstatContext):
        pass


    # Enter a parse tree produced by CSlangParser#stmtdecl.
    def enterStmtdecl(self, ctx:CSlangParser.StmtdeclContext):
        pass

    # Exit a parse tree produced by CSlangParser#stmtdecl.
    def exitStmtdecl(self, ctx:CSlangParser.StmtdeclContext):
        pass



del CSlangParser