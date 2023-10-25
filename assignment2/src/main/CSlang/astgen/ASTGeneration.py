from CSlangVisitor import CSlangVisitor
from CSlangParser import CSlangParser
from AST import *


class ASTGeneration(CSlangVisitor):
    def visitProgram(self, ctx: CSlangParser.ProgramContext):
        return Program(self.visit(ctx.classdecllist()))

    # Class declaration
    def visitClassdecllist(self, ctx: CSlangParser.ClassdecllistContext):
        return (
            [self.visit(ctx.classdecl())] + self.visit(ctx.classdecllist())
            if ctx.classdecllist()
            else [self.visit(ctx.classdecl())]
        )

    def visitClassdecl(self, ctx: CSlangParser.ClassdeclContext):
        return ClassDecl(
            Id(ctx.ID(1).getText()) if ctx.LARROW() else Id(ctx.ID(0).getText()),
            self.visit(ctx.memberlist()),
            Id(ctx.ID(0).getText()) if ctx.LARROW() else None,
        )

    def visitMemberlist(self, ctx: CSlangParser.MemberlistContext):
        return (
            self.visit(ctx.member()) + self.visit(ctx.memberlist())
            if ctx.memberlist()
            else []
        )

    def visitMember(self, ctx: CSlangParser.MemberContext):
        return (
            self.visit(ctx.attribute())
            if ctx.attribute()
            else [self.visit(ctx.method())]
        )

    # Attribute declaration
    def visitAttribute(self, ctx: CSlangParser.AttributeContext):
        att = (
            self.visit(ctx.vardecl()) if ctx.vardecl() else self.visit(ctx.constdecl())
        )
        return [AttributeDecl(x) for x in att]

    def visitVardecl(self, ctx: CSlangParser.VardeclContext):
        node = ctx.attlistdecl() if ctx.attlistdecl() else ctx.attlistnodecl()
        return [VarDecl(*x) for x in self.visit(node)]

    def visitConstdecl(self, ctx: CSlangParser.ConstdeclContext):
        node = ctx.attlistdecl() if ctx.attlistdecl() else ctx.attlistnodecl()
        return [ConstDecl(*x) for x in self.visit(node)]

    def visitAttlistdecl(self, ctx: CSlangParser.AttlistdeclContext):
        ids, exprs = [], []
        while ctx.attlistdecl():
            ids.append(self.visit(ctx.identifier()))
            exprs.insert(0, self.visit(ctx.exprstr()))
            ctx = ctx.attlistdecl()

        ids.append(self.visit(ctx.identifier()))
        exprs.insert(0, self.visit(ctx.exprstr()))
        typ = self.visit(ctx.atttyp())
        return [(id, typ, expr) for id, expr in zip(ids, exprs)]

    def visitAttlistnodecl(self, ctx: CSlangParser.AttlistnodeclContext):
        ids = []
        while ctx.attlistnodecl():
            ids.append(self.visit(ctx.identifier()))
            ctx = ctx.attlistnodecl()

        ids.append(self.visit(ctx.identifier()))
        typ = self.visit(ctx.atttyp())
        return [(id, typ, None) for id in ids]

    def visitAtttyp(self, ctx: CSlangParser.AtttypContext):
        return (
            ArrayType(int(ctx.INTLIT().getText()), self.visit(ctx.typ()))
            if ctx.INTLIT()
            else self.visit(ctx.typ())
        )

    def visitTyp(self, ctx: CSlangParser.TypContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOL():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        elif ctx.ID():
            return ClassType(Id(ctx.ID().getText()))

    # Method declaration
    def visitMethod(self, ctx: CSlangParser.MethodContext):
        id = (
            self.visit(ctx.identifier())
            if ctx.identifier()
            else Id(ctx.CONSTRUCTOR().getText())
        )
        typ = (
            self.visit(ctx.atttyp())
            if ctx.identifier() and ctx.atttyp()
            else VoidType()
        )
        return MethodDecl(
            id,
            self.visit(ctx.paramlist()) if ctx.paramlist() else [],
            typ,
            self.visit(ctx.blockstmt()),
        )

    def visitParamlist(self, ctx: CSlangParser.ParamlistContext):
        return (
            self.visit(ctx.params()) + self.visit(ctx.paramlist())
            if ctx.paramlist()
            else self.visit(ctx.params())
        )

    def visitParams(self, ctx: CSlangParser.ParamsContext):
        return [VarDecl(x, self.visit(ctx.atttyp())) for x in self.visit(ctx.param())]

    def visitParam(self, ctx: CSlangParser.ParamContext):
        return (
            [self.visit(ctx.identifier())] + self.visit(ctx.param())
            if ctx.param()
            else [self.visit(ctx.identifier())]
        )

    def visitBlockstmt(self, ctx: CSlangParser.BlockstmtContext):
        return Block(self.visit(ctx.stmtlist()))

    def visitParenexpr(self, ctx: CSlangParser.ParenexprContext):
        return self.visit(ctx.exprlist())

    # Expressions
    def visitExprlist(self, ctx: CSlangParser.ExprlistContext):
        return self.visit(ctx.exprprime()) if ctx.exprprime() else []

    def visitExprprime(self, ctx: CSlangParser.ExprprimeContext):
        return (
            [self.visit(ctx.exprstr())] + self.visit(ctx.exprprime())
            if ctx.exprprime()
            else [self.visit(ctx.exprstr())]
        )

    def visitExprstr(self, ctx: CSlangParser.ExprstrContext):
        return (
            BinaryOp(
                ctx.getChild(1).getText(),
                self.visit(ctx.exprrel(0)),
                self.visit(ctx.exprrel(1)),
            )
            if ctx.getChildCount() == 3
            else self.visit(ctx.exprrel(0))
        )

    def visitExprrel(self, ctx: CSlangParser.ExprrelContext):
        return (
            BinaryOp(
                ctx.getChild(1).getText(),
                self.visit(ctx.exprlog(0)),
                self.visit(ctx.exprlog(1)),
            )
            if ctx.getChildCount() == 3
            else self.visit(ctx.exprlog(0))
        )

    def visitExprlog(self, ctx: CSlangParser.ExprlogContext):
        return (
            BinaryOp(
                ctx.getChild(1).getText(),
                self.visit(ctx.exprlog()),
                self.visit(ctx.expradd()),
            )
            if ctx.getChildCount() == 3
            else self.visit(ctx.expradd())
        )

    def visitExpradd(self, ctx: CSlangParser.ExpraddContext):
        return (
            BinaryOp(
                ctx.getChild(1).getText(),
                self.visit(ctx.expradd()),
                self.visit(ctx.exprmul()),
            )
            if ctx.getChildCount() == 3
            else self.visit(ctx.exprmul())
        )

    def visitExprmul(self, ctx: CSlangParser.ExprmulContext):
        return (
            BinaryOp(
                ctx.getChild(1).getText(),
                self.visit(ctx.exprmul()),
                self.visit(ctx.exprnot()),
            )
            if ctx.getChildCount() == 3
            else self.visit(ctx.exprnot())
        )

    def visitExprnot(self, ctx: CSlangParser.ExprnotContext):
        return (
            UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.exprnot()))
            if ctx.getChildCount() == 2
            else self.visit(ctx.exprsign())
        )

    def visitExprsign(self, ctx: CSlangParser.ExprsignContext):
        return (
            UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.exprsign()))
            if ctx.getChildCount() == 2
            else self.visit(ctx.exprindex())
        )

    def visitExprindex(self, ctx: CSlangParser.ExprindexContext):
        return (
            ArrayCell(self.visit(ctx.exprinst()), self.visit(ctx.exprstr()))
            if ctx.getChildCount() == 4
            else self.visit(ctx.exprinst())
        )

    def visitExprinst(self, ctx: CSlangParser.ExprinstContext):
        num = ctx.getChildCount()
        exprinst = self.visit(ctx.exprinst()) if ctx.exprinst() else None
        if num in [7, 4]:
            return CallExpr(
                ArrayCell(exprinst, self.visit(ctx.exprstr()))
                if num == 7
                else exprinst,
                Id(ctx.ID().getText()),
                self.visit(ctx.parenexpr()),
            )
        elif num in [6, 3]:
            return FieldAccess(
                ArrayCell(exprinst, self.visit(ctx.exprstr()))
                if num == 6
                else exprinst,
                Id(ctx.ID().getText()),
            )
        else:
            return self.visit(ctx.exprstat())

    def visitExprstat(self, ctx: CSlangParser.ExprstatContext):
        return (
            self.visit(ctx.statpart()) if ctx.statpart() else self.visit(ctx.exprobj())
        )

    def visitExprobj(self, ctx: CSlangParser.ExprobjContext):
        return (
            NewExpr(
                Id(ctx.ID().getText()),
                self.visit(ctx.parenexpr()),
            )
            if ctx.NEW()
            else self.visit(ctx.exprparen())
        )

    def visitExprparen(self, ctx: CSlangParser.ExprparenContext):
        return self.visit(ctx.exprstr()) if ctx.LPN() else self.visit(ctx.lit())

    def visitStatpart(self, ctx: CSlangParser.StatpartContext):
        id = Id(ctx.ID().getText()) if ctx.ID() else None
        atid = Id(ctx.ATID().getText())
        return (
            CallExpr(id, atid, self.visit(ctx.parenexpr()))
            if ctx.parenexpr()
            else FieldAccess(id, atid)
        )

    # Literals
    def visitIdentifier(self, ctx: CSlangParser.IdentifierContext):
        return Id(ctx.getText())

    def visitLit(self, ctx: CSlangParser.LitContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.boollit():
            return self.visit(ctx.boollit())
        elif ctx.STRLIT():
            return StringLiteral(str(ctx.STRLIT().getText()))
        elif ctx.arraylit():
            return self.visit(ctx.arraylit())
        elif ctx.NULL():
            return NullLiteral()
        elif ctx.SELF():
            return SelfLiteral()
        elif ctx.identifier():
            return self.visit(ctx.identifier())

    def visitBoollit(self, ctx: CSlangParser.BoollitContext):
        return BooleanLiteral(True if ctx.TRUE() else False)

    def visitArraylit(self, ctx: CSlangParser.ArraylitContext):
        return ArrayLiteral(self.visit(ctx.litprime()))

    def visitLitlist(self, ctx: CSlangParser.LitlistContext):
        return self.visit(ctx.litprime()) if ctx.litprime() else []

    def visitLitprime(self, ctx: CSlangParser.LitprimeContext):
        return (
            [self.visit(ctx.lit())] + self.visit(ctx.litprime())
            if ctx.litprime()
            else [self.visit(ctx.lit())]
        )

    # Statements
    def visitStmtlist(self, ctx: CSlangParser.StmtlistContext):
        return (
            self.visit(ctx.stmt()) + self.visit(ctx.stmtlist())
            if ctx.stmtlist()
            else []
        )

    def visitStmt(self, ctx: CSlangParser.StmtContext):
        if ctx.IF():
            index_map = {6: (1, 0, 2), 5: (0, -1, 1), 4: (1, 0, -1)}
            thenIn, preIn, elseIn = index_map.get(ctx.getChildCount(), (0, -1, -1))
            return [
                If(
                    self.visit(ctx.exprstr()),
                    self.visit(ctx.blockstmt(thenIn)),
                    self.visit(ctx.blockstmt(preIn)) if preIn != -1 else None,
                    self.visit(ctx.blockstmt(elseIn)) if elseIn != -1 else None,
                )
            ]
        elif ctx.FOR():
            return [
                For(
                    self.visit(ctx.stmtassign(0)),
                    self.visit(ctx.exprstr()),
                    self.visit(ctx.stmtassign(1)),
                    self.visit(ctx.blockstmt(0)),
                )
            ]
        elif ctx.stmtassign():
            return [self.visit(ctx.stmtassign(0))]
        elif ctx.BREAK():
            return [Break()]
        elif ctx.CONTINUE():
            return [Continue()]
        elif ctx.RETURN():
            return [Return(self.visit(ctx.exprstr()) if ctx.exprstr() else None)]
        elif ctx.stmtinvoc():
            return [self.visit(ctx.stmtinvoc())]
        else:
            return self.visit(ctx.stmtdecl())

    def visitStmtassign(self, ctx: CSlangParser.StmtassignContext):
        return Assign(self.visit(ctx.lhs()), self.visit(ctx.exprstr()))

    def visitLhs(self, ctx: CSlangParser.LhsContext):
        return (
            ArrayCell(self.visit(ctx.lhs()), self.visit(ctx.exprstr()))
            if ctx.getChildCount() == 4
            else self.visit(ctx.lhsinst())
        )

    def visitLhsinst(self, ctx: CSlangParser.LhsinstContext):
        num = ctx.getChildCount()
        lhsinst = self.visit(ctx.lhsinst()) if ctx.lhsinst() else None

        if num in [7, 4]:
            return CallExpr(
                ArrayCell(lhsinst, self.visit(ctx.exprstr())) if num == 7 else lhsinst,
                Id(ctx.ID().getText()),
                self.visit(ctx.parenexpr()),
            )
        elif num in [6, 3]:
            return FieldAccess(
                ArrayCell(lhsinst, self.visit(ctx.exprstr())) if num == 6 else lhsinst,
                Id(ctx.ID().getText()),
            )
        else:
            return self.visit(ctx.lhsstat())

    def visitLhsstat(self, ctx: CSlangParser.LhsstatContext):
        return (
            self.visit(ctx.statpart()) if ctx.statpart() else self.visit(ctx.lhsparen())
        )

    def visitLhsparen(self, ctx: CSlangParser.LhsparenContext):
        if ctx.lhs():
            return self.visit(ctx.lhs())
        elif ctx.SELF():
            return SelfLiteral()
        else:
            return self.visit(ctx.identifier())

    def visitStmtinvoc(self, ctx: CSlangParser.StmtinvocContext):
        return (
            self.visit(ctx.stmtinvocinst())
            if ctx.stmtinvocinst()
            else self.visit(ctx.stmtinvocstat())
        )

    def visitStmtinvocinst(self, ctx: CSlangParser.StmtinvocinstContext):
        return CallStmt(
            ArrayCell(self.visit(ctx.exprinst()), self.visit(ctx.exprstr()))
            if ctx.exprstr()
            else self.visit(ctx.exprinst()),
            Id(ctx.ID().getText()),
            self.visit(ctx.parenexpr()),
        )

    def visitStmtinvocstat(self, ctx: CSlangParser.StmtinvocstatContext):
        return CallStmt(
            Id(ctx.ID().getText()) if ctx.ID() else None,
            Id(ctx.ATID().getText()),
            self.visit(ctx.parenexpr()),
        )

    def visitStmtdecl(self, ctx: CSlangParser.StmtdeclContext):
        return (
            self.visit(ctx.vardecl()) if ctx.vardecl() else self.visit(ctx.constdecl())
        )
