from CSlangVisitor import CSlangVisitor
from CSlangParser import CSlangParser
from AST import *


class ASTGeneration(CSlangVisitor):
    # def visitProgram(self, ctx: CSlangParser.ProgramContext):
    #     return Program([self.visit(x) for x in ctx.classdecl()])

    # def visitClassdecl(self, ctx: CSlangParser.ClassdeclContext):
    #     return ClassDecl(Id(ctx.ID().getText()), [self.visit(x) for x in ctx.memdecl()])

    # def visitMemdecl(self, ctx: CSlangParser.MemdeclContext):
    #     return AttributeDecl(
    #         VarDecl(Id(ctx.ID().getText()), self.visit(ctx.cslangtype()))
    #     )

    # def visitCslangtype(self, ctx: CSlangParser.CslangtypeContext):
    #     return IntType() if ctx.INTTYPE() else VoidType()

    def visitProgram(self, ctx: CSlangParser.ProgramContext):
        return None

    def visitClassdecllist(self, ctx: CSlangParser.ClassdecllistContext):
        return None

    def visitClassdecl(self, ctx: CSlangParser.ClassdeclContext):
        return None

    def visitMemberlist(self, ctx: CSlangParser.MemberlistContext):
        return None

    def visitMember(self, ctx: CSlangParser.MemberContext):
        return None

    def visitAttribute(self, ctx: CSlangParser.AttributeContext):
        return None

    def visitAttlistdecl(self, ctx: CSlangParser.AttlistdeclContext):
        return None

    def visitAttlistnodecl(self, ctx: CSlangParser.AttlistnodeclContext):
        return None

    def visitAtttyp(self, ctx: CSlangParser.AtttypContext):
        return None

    def visitTyp(self, ctx: CSlangParser.TypContext):
        return None

    def visitMethod(self, ctx: CSlangParser.MethodContext):
        return None

    def visitParamlist(self, ctx: CSlangParser.ParamlistContext):
        return None

    def visitParams(self, ctx: CSlangParser.ParamsContext):
        return None

    def visitBlockstmt(self, ctx: CSlangParser.BlockstmtContext):
        return None

    def visitParenexpr(self, ctx: CSlangParser.ParenexprContext):
        return None

    def visitExprlist(self, ctx: CSlangParser.ExprlistContext):
        return None

    def visitExprprime(self, ctx: CSlangParser.ExprprimeContext):
        return None

    def visitExprstr(self, ctx: CSlangParser.ExprstrContext):
        return None

    def visitExprrel(self, ctx: CSlangParser.ExprrelContext):
        return None

    def visitExprlog(self, ctx: CSlangParser.ExprlogContext):
        return None

    def visitExpradd(self, ctx: CSlangParser.ExpraddContext):
        return None

    def visitExprmul(self, ctx: CSlangParser.ExprmulContext):
        return None

    def visitExprnot(self, ctx: CSlangParser.ExprnotContext):
        return None

    def visitExprsign(self, ctx: CSlangParser.ExprsignContext):
        return None

    def visitExprindex(self, ctx: CSlangParser.ExprindexContext):
        return None

    def visitExprinst(self, ctx: CSlangParser.ExprinstContext):
        return None

    def visitExprstat(self, ctx: CSlangParser.ExprstatContext):
        return None

    def visitExprobj(self, ctx: CSlangParser.ExprobjContext):
        return None

    def visitExprparen(self, ctx: CSlangParser.ExprparenContext):
        return None

    def visitIdentifier(self, ctx: CSlangParser.IdentifierContext):
        return None

    def visitLit(self, ctx: CSlangParser.LitContext):
        return None

    def visitBoollit(self, ctx: CSlangParser.BoollitContext):
        return None

    def visitArraylit(self, ctx: CSlangParser.ArraylitContext):
        return None

    def visitLitlist(self, ctx: CSlangParser.LitlistContext):
        return None

    def visitLitprime(self, ctx: CSlangParser.LitprimeContext):
        return None

    def visitStmtlist(self, ctx: CSlangParser.StmtlistContext):
        return None

    def visitStmt(self, ctx: CSlangParser.StmtContext):
        return None

    def visitStmtassign(self, ctx: CSlangParser.StmtassignContext):
        return None

    def visitLhs(self, ctx: CSlangParser.LhsContext):
        return None

    def visitLhsinst(self, ctx: CSlangParser.LhsinstContext):
        return None

    def visitLhsstat(self, ctx: CSlangParser.LhsstatContext):
        return None

    def visitLhsparen(self, ctx: CSlangParser.LhsparenContext):
        return None

    def visitStmtinvoc(self, ctx: CSlangParser.StmtinvocContext):
        return None

    def visitStmtinvocstat(self, ctx: CSlangParser.StmtinvocstatContext):
        return None
