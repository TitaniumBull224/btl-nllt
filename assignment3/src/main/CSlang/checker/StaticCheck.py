from AST import *
from Visitor import *
from Utils import Utils, MType
from StaticError import *
from functools import reduce
from typing import Dict, List
import copy
from enum import Enum
import logging


class Kind(Enum):
    MUTABLE = "mutable"
    IMMUTABLE = "immutable"
    METHOD = "method"
    INSTANCE = "instance"
    STATIC = "static"
    VAR = "var"
    CONST = "const"


class ExpUtils:
    @staticmethod
    def isNaNType(expType):
        return type(expType) not in [IntType, FloatType]

    @staticmethod
    def isNotAccess(expType):
        return type(expType) not in [CallExpr, FieldAccess, CallStmt]

    # env {Class}
    # Class "id" : (parentId, {Var / Const / Method})
    # Var "id" : (Kind.MUTABLE, Type)
    # Const "id" : (Kind.IMMUTABLE, Type)
    # Method "id" : (Kind.METHOD, Type, Dict)
    def printEnv(env: Dict):
        for id, value in env.items():
            parent, memberList = value
            print(f"{id}: {parent} [")
            for memberId, memberVal in memberList.items():
                print(f"{memberId}: {type(memberVal[1])}")
            print("]")

    def findMember(self, classId: str, memberId: str, env):
        it = classId
        while env.get(it) is not None:
            classEnv = env.get(it)
            if memberId in classEnv[1].keys():
                return True
            if classEnv[0] == None:
                return False
            it = classEnv[0]
        return False


class GetEnv(BaseVisitor, Utils):
    def __init__(self):
        self.globalEnv = {}

    def visitProgram(self, ast: Program, o: object):
        self.globalEnv = o
        return reduce(lambda x, y: self.visit(y, x), ast.decl, o)

    # Class "id" : (parentId, {Var / Const / Method})
    def visitClassDecl(self, ast: ClassDecl, o: object):
        env = o
        id = ast.classname.name
        parentId = ast.parentname.name if ast.parentname else None
        if env.get(id) is not None:
            raise Redeclared(Class(), id)
        env[id] = (parentId, reduce(lambda x, y: self.visit(y, x), ast.memlist, {}))
        return env

    def visitAttributeDecl(self, ast: AttributeDecl, o: object):
        env = o
        return (
            self.visit(ast.decl, env)
            if type(ast.decl) is ConstDecl
            else self.visit(ast.decl, (Attribute(), env))
        )

    # Var "id" : (Kind.MUTABLE, Type)
    def visitVarDecl(self, ast: VarDecl, o: object):
        kind, env = o
        id = ast.variable.name
        if env.get(id) is not None:
            raise Redeclared(kind, id)

        env[id] = (Kind.MUTABLE, self.visit(ast.varType, env))  # kind, type
        return env

    # Const "id" : (Kind.IMMUTABLE, Type)
    def visitConstDecl(self, ast: ConstDecl, o: object):
        env = o
        id = ast.constant.name
        if env.get(id) is not None:
            raise Redeclared(Attribute(), id)
        env[id] = (Kind.IMMUTABLE, self.visit(ast.constType, env))  # kind, type
        return env

    # Method "id" : (Kind.METHOD, Type, Dict)
    def visitMethodDecl(self, ast: MethodDecl, o: object):
        env = o
        id = ast.name.name
        if env.get(id) is not None and id != "constructor":
            raise Redeclared(Method(), id)
        param = reduce(lambda x, y: self.visit(y, (Parameter(), x)), ast.param, {})

        env[id] = (
            Kind.METHOD,
            self.visit(ast.returnType, env),
            param,
        )  # kind, type, Dict
        return env

    def visitIntType(self, ast: IntType, o: object):
        return ast

    def visitFloatType(self, ast: FloatType, o: object):
        return ast

    def visitBoolType(self, ast: BoolType, o: object):
        return ast

    def visitStringType(self, ast: StringType, o: object):
        return ast

    def visitVoidType(self, ast: VoidType, o: object):
        return ast

    def visitArrayType(self, ast: ArrayType, o: object):
        return ast

    def visitClassType(self, ast: ClassType, o: object):
        return ast


class StaticChecker(BaseVisitor, Utils):
    def __init__(self, ast):
        self.ast = ast
        self.io = {
            "io": (
                None,
                {
                    "@readInt": (Kind.METHOD, IntType(), {}),
                    "@writeInt": (
                        Kind.METHOD,
                        VoidType(),
                        {"anArg": (Kind.MUTABLE, IntType())},
                    ),
                    "@readFloat": (Kind.METHOD, FloatType(), {}),
                    "@writeFloat": (
                        Kind.METHOD,
                        VoidType(),
                        {"anArg": (Kind.MUTABLE, FloatType())},
                    ),
                    "@readBool": (Kind.METHOD, BoolType(), {}),
                    "@writeBool": (
                        Kind.METHOD,
                        VoidType(),
                        {"anArg": (Kind.MUTABLE, BoolType())},
                    ),
                    "@readStr": (Kind.METHOD, StringType(), {}),
                    "@writeStr": (
                        Kind.METHOD,
                        VoidType(),
                        {"anArg": (Kind.MUTABLE, StringType())},
                    ),
                },
            )
        }

    def check(self):
        self.visit(self.ast, self.io)
        return []

    def visitProgram(self, ast: Program, o: object):
        env = GetEnv().visit(ast, o)
        if env.get("Program") is None:
            raise NoEntryPoint()
        if env["Program"][1].get("@main") is None:
            raise NoEntryPoint()
        if env["Program"][1]["@main"][0] != Kind.METHOD:
            raise NoEntryPoint()
        for x in ast.decl:
            self.visit(x, env)
        return env

    def visitClassDecl(self, ast: ClassDecl, o: object):
        env = {}
        env["global"] = o
        env["current"] = ast.classname.name
        if ast.parentname is not None:
            parId = ast.parentname.name
            if env["global"].get(parId) is None:
                raise Undeclared(Class(), parId)
            env["parent"] = parId
        else:
            env["parent"] = None
        return reduce(lambda x, y: self.visit(y, x), ast.memlist, env)

    def visitMethodDecl(self, ast: MethodDecl, o: object):
        env = {}
        env["global"] = o["global"]
        env["local"] = [{}]
        env["current"] = o["current"]
        env["parent"] = o["parent"]
        env["return"] = self.visit(ast.returnType, env)
        env["inLoop"] = False
        env["isParam"] = True
        env = reduce(lambda x, y: self.visit(y, x), ast.param, env)
        env["isParam"] = False
        return reduce(lambda x, y: self.visit(y, x), ast.body.stmt, env)

    def visitAttributeDecl(self, ast: AttributeDecl, o: object):
        env = o
        return self.visit(ast.decl, env)

    def visitVarDecl(self, ast: VarDecl, o: object):
        env = o
        kind = Variable()
        if env.get("isParam") is not None and env["isParam"]:
            kind = Parameter()
        id = ast.variable.name
        varTyp = self.visit(ast.varType, env)
        if type(varTyp) is VoidType:
            raise TypeMismatchInDeclaration(ast)
        if ast.varInit is not None:
            valueKind, valueTyp = self.visit(ast.varInit, env)
            if type(valueTyp) is not NullLiteral:
                if type(valueTyp) is not type(varTyp):
                    raise TypeMismatchInDeclaration(ast)
                if type(valueTyp) is ArrayType and type(varTyp) is ArrayType:
                    if valueTyp.size != varTyp.size:
                        raise TypeMismatchInDeclaration(ast)
                    if type(valueTyp.eleType) is not NullLiteral:
                        if type(valueTyp.eleType) is not type(varTyp.eleType):
                            raise TypeMismatchInDeclaration(ast)

            elif type(varTyp) is not ClassType:
                raise TypeMismatchInDeclaration(ast)

        if env.get("local") is not None:
            if env["local"][0].get(id) is not None:
                raise Redeclared(kind, id)
            env["local"][0][id] = (Kind.VAR, varTyp)
        return env

    def visitConstDecl(self, ast: ConstDecl, o: object):
        env = o
        id = ast.constant.name
        constTyp = self.visit(ast.constType, env)
        if ast.value is None:
            raise TypeMismatchInDeclaration(ast)
        valueKind, valueTyp = self.visit(ast.value, env)
        if type(valueTyp) is not type(constTyp):
            raise TypeMismatchInDeclaration(ast)
        if type(valueTyp) is ArrayType and type(constTyp) is ArrayType:
            if valueTyp.size != constTyp.size:
                raise TypeMismatchInDeclaration(ast)
            if type(valueTyp.eleType) is not type(constTyp.eleType):
                raise TypeMismatchInDeclaration(ast)
        if env.get("local") is not None:
            if env["local"][0].get(id) is not None:
                raise Redeclared(Constant(), id)
            env["local"][0][id] = (Kind.CONST, constTyp)
        return env

    def visitBlock(self, ast: Block, o):
        oEnv = o
        env = {}
        env["global"] = oEnv["global"]
        env["local"] = [{}] + oEnv["local"]
        env["current"] = oEnv["current"]
        env["parent"] = oEnv["parent"]
        env["return"] = oEnv["return"]
        env["inLoop"] = oEnv["inLoop"]
        return reduce(lambda x, y: self.visit(y, x), ast.stmt, env)

    # STATEMENT
    def visitAssign(self, ast: Assign, o: object):
        env = o
        lhsKind, lhsTyp = self.visit(ast.lhs, env)
        expKind, expTyp = self.visit(ast.exp, env)

        if lhsKind in [Kind.CONST, Kind.IMMUTABLE]:
            raise CannotAssignToConstant(ast)
        if lhsKind in [Kind.MUTABLE, Kind.IMMUTABLE, Kind.METHOD]:
            if ExpUtils.isNotAccess(ast.lhs):
                raise Undeclared(Identifier(), ast.lhs.name)
        if expKind in [Kind.MUTABLE, Kind.IMMUTABLE, Kind.METHOD]:
            if ExpUtils.isNotAccess(ast.exp):
                raise Undeclared(Identifier(), ast.exp.name)
        if type(lhsTyp) is VoidType:
            raise TypeMismatchInStatement(ast)
        if isinstance(lhsTyp, ArrayType) and isinstance(expTyp, ArrayType):
            if lhsTyp.size != expTyp.size:
                raise TypeMismatchInStatement(ast)
            if type(lhsTyp.eleType) is not type(expTyp.eleType):
                if not (
                    type(lhsTyp.eleType) is FloatType
                    and type(expTyp.eleType) is IntType
                ):
                    raise TypeMismatchInStatement(ast)
        if not (
            (type(lhsTyp) is type(expTyp))
            or (type(lhsTyp) is FloatType and type(expTyp) is IntType)
        ):
            raise TypeMismatchInStatement(ast)
        return env

    def visitIf(self, ast: If, o: object):
        env = o
        condKind, condTyp = self.visit(ast.expr, env)
        if condKind in [Kind.MUTABLE, Kind.IMMUTABLE, Kind.METHOD]:
            if ExpUtils.isNotAccess(ast.expr):
                raise Undeclared(Identifier(), ast.expr.name)
        if type(condTyp) is not BoolType:
            raise TypeMismatchInStatement(ast)
        if ast.preStmt is not None:
            self.visit(ast.preStmt, env)
        self.visit(ast.thenStmt, env)
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, env)
        return env

    def visitFor(self, ast: For, o: object):
        env = o
        env = self.visit(ast.initStmt, env)

        condKind, condTyp = self.visit(ast.expr, env)
        if type(condTyp) is not BoolType:
            raise TypeMismatchInStatement(ast)

        env = self.visit(ast.postStmt, env)
        env["inLoop"] = True
        env = self.visit(ast.loop, env)
        env["inLoop"] = False
        return env

    def visitContinue(self, ast: Continue, o: object):
        env = o
        if not env["inLoop"]:
            raise MustInLoop(ast)
        return env

    def visitBreak(self, ast: Break, o: object):
        env = o
        if not env["inLoop"]:
            raise MustInLoop(ast)
        return env

    def visitReturn(self, ast: Return, o: object):
        env = o
        if ast.expr is not None:
            retKind, retTyp = self.visit(ast.expr, o)
            if retKind in [Kind.MUTABLE, Kind.IMMUTABLE, Kind.METHOD]:
                if ExpUtils.isNotAccess(ast.expr):
                    raise Undeclared(Identifier(), ast.expr.name)
        else:
            retTyp = VoidType()
        if type(env["return"]) is not type(retTyp):
            if not (type(env["return"]) is FloatType and type(retTyp) is IntType):
                if not (
                    type(env["return"]) in [ClassType, VoidType]
                    and type(retTyp) is NullLiteral
                ):
                    raise TypeMismatchInStatement(ast)

        return env

    def visitCallStmt(self, ast: CallStmt, o: object):
        env = o
        id = ast.method.name
        classId = ""
        if id[0] == "@":
            # Static handling
            if ast.obj is None or type(ast.obj) is SelfLiteral:
                classId = env["current"]
            elif type(ast.obj) is Id:
                classId = ast.obj.name
            else:
                raise TypeMismatchInExpression(ast)
        else:
            # Instance handling
            classKind, classTyp = self.visit(ast.obj, env)
            if type(classTyp) is ClassType:
                classId = classTyp.classname.name
            elif type(classTyp) is SelfLiteral:
                classId = env["current"]
            else:
                raise TypeMismatchInExpression(ast)

        if env["global"].get(classId) is None:
            raise Undeclared(Class(), classId)
        if env["global"][classId][1].get(id) is None:
            raise Undeclared(Method(), id)
        # env["global"] = {classId: (parent, {id:(kind,typ,{(kind,typ)})})}
        medKind, medTyp, medParams = env["global"][classId][1][id]
        if len(medParams) != len(ast.param):
            raise TypeMismatchInExpression(ast)
        valParTyp = reduce(lambda x, y: x + [self.visit(y, env)[1]], ast.param, [])
        medParTyp = [typ for kind, typ in medParams.values()]
        for x, y in zip(valParTyp, medParTyp):
            if not (
                type(x) is type(y) or (type(x) is IntType and type(y) is FloatType)
            ):
                raise TypeMismatchInExpression(ast)
        return env

    # EXPRESSION
    def visitBinaryOp(self, ast: BinaryOp, o: object):
        env = o
        lKind, lTyp = self.visit(ast.left, env)
        rKind, rTyp = self.visit(ast.right, env)
        if lKind in [Kind.MUTABLE, Kind.IMMUTABLE, Kind.METHOD]:
            if ExpUtils.isNotAccess(ast.left):
                raise Undeclared(Identifier(), ast.left.name)
        if rKind in [Kind.MUTABLE, Kind.IMMUTABLE, Kind.METHOD]:
            if ExpUtils.isNotAccess(ast.right):
                raise Undeclared(Identifier(), ast.right.name)
        op = str(ast.op)
        if op in ["+", "-", "*"]:
            if ExpUtils.isNaNType(lTyp) or ExpUtils.isNaNType(rTyp):
                raise TypeMismatchInExpression(ast)
            if type(lTyp) is FloatType or type(rTyp) is FloatType:
                return (None, FloatType())
            return (None, IntType())
        if op in ["/"]:
            if ExpUtils.isNaNType(lTyp) or ExpUtils.isNaNType(rTyp):
                raise TypeMismatchInExpression(ast)
            return (None, FloatType())
        if op in ["\\", "%"]:
            if not (type(lTyp) is type(rTyp) is IntType):
                raise TypeMismatchInExpression(ast)
            return (None, IntType())
        if op in ["==", "!="]:
            if type(lTyp) is type(rTyp) and type(lTyp) in [IntType, BoolType]:
                return (None, BoolType())
            raise TypeMismatchInExpression(ast)
        if op in [">", "<", ">=", "<="]:
            if ExpUtils.isNaNType(lTyp) or ExpUtils.isNaNType(rTyp):
                raise TypeMismatchInExpression(ast)
            return (None, BoolType())
        if op in ["&&", "||"]:
            if type(lTyp) is type(rTyp) and type(lTyp) is BoolType:
                return (None, BoolType())
            raise TypeMismatchInExpression(ast)
        if op in ["^"]:
            if type(lTyp) is type(rTyp) and type(lTyp) is StringType:
                return (None, StringType())
            raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast: UnaryOp, o: object):
        env = o
        expKind, expTyp = self.visit(ast.body, env)
        if expKind in [Kind.MUTABLE, Kind.IMMUTABLE, Kind.METHOD]:
            if ExpUtils.isNotAccess(ast.body):
                raise Undeclared(Identifier(), ast.body.name)
        op = str(ast.op)
        if op in ["-"]:
            if ExpUtils.isNaNType(expTyp):
                raise TypeMismatchInExpression(ast)
        if op in ["!"]:
            if type(expTyp) is not BoolType:
                raise TypeMismatchInExpression(ast)
        return (None, expTyp)

    def visitArrayCell(self, ast: ArrayCell, o: object):
        env = o
        arrKind, arrTyp = self.visit(ast.arr, env)
        idxKind, idxTyp = self.visit(ast.idx, env)
        if type(idxTyp) is not IntType or type(arrTyp) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        return (None, arrTyp.eleType)

    def visitCallExpr(self, ast: CallExpr, o: object):
        env = o
        id = ast.method.name
        classId = ""
        if id[0] == "@":
            # Static handling
            if ast.obj is None or type(ast.obj) is SelfLiteral:
                classId = env["current"]
            elif type(ast.obj) is Id:
                classId = ast.obj.name
            else:
                raise TypeMismatchInExpression(ast)
        else:
            # Instance handling
            classKind, classTyp = self.visit(ast.obj, env)
            if type(classTyp) is ClassType:
                classId = classTyp.classname.name
            elif type(classTyp) is SelfLiteral:
                classId = env["current"]
            else:
                raise TypeMismatchInExpression(ast)

        if env["global"].get(classId) is None:
            raise Undeclared(Class(), classId)
        if env["global"][classId][1].get(id) is None:
            raise Undeclared(Method(), id)
        # env["global"] = {classId: (parent, {id:(kind,typ,{(kind,typ)})})}
        medKind, medTyp, medParams = env["global"][classId][1][id]
        if type(medTyp) is VoidType:
            raise TypeMismatchInExpression(ast)
        if len(medParams) != len(ast.param):
            raise TypeMismatchInExpression(ast)
        valParTyp = reduce(lambda x, y: x + [self.visit(y, env)[1]], ast.param, [])
        medParTyp = [typ for kind, typ in medParams.values()]
        for x, y in zip(valParTyp, medParTyp):
            if not (
                type(x) is type(y) or (type(x) is IntType and type(y) is FloatType)
            ):
                raise TypeMismatchInExpression(ast)
        return (None, medTyp)

    def visitFieldAccess(self, ast: FieldAccess, o: object):
        env = o
        id = ast.fieldname.name
        classId = ""
        if id[0] == "@":
            # Static handling
            if ast.obj is None or type(ast.obj) is SelfLiteral:
                classId = env["current"]
            elif type(ast.obj) is Id:
                classId = ast.obj.name
            else:
                raise TypeMismatchInExpression(ast)
        else:
            # Instance handling
            classKind, classTyp = self.visit(ast.obj, env)
            if type(classTyp) is ClassType:
                classId = classTyp.classname.name
            elif type(classTyp) is SelfLiteral:
                classId = env["current"]
            else:
                raise TypeMismatchInExpression(ast)

        if env["global"].get(classId) is None:
            raise Undeclared(Class(), classId)
        if env["global"][classId][1].get(id) is None:
            raise Undeclared(Attribute(), id)
        # env["global"] = {classId: (parent, {id:(kind,typ)})}
        attKind, attTyp = env["global"][classId][1][id]
        if type(attTyp) is VoidType:
            raise TypeMismatchInExpression(ast)
        return (None, attTyp)

    def visitNewExpr(self, ast: NewExpr, o: object):
        env = o
        id = ast.classname.name
        if env["global"].get(id) is None:
            raise Undeclared(Class(), id)
        if "constructor" in env["global"][id][1]:
            conParams = env["global"][id][1]["constructor"][2]
        else:
            raise Undeclared(Method(), "constructor")
        paramCall = reduce(lambda x, y: x + [self.visit(y, env)], ast.param, [])
        conParams = list(conParams.values())
        if len(paramCall) != len(conParams):
            raise TypeMismatchInExpression(ast)
        for x, y in zip(paramCall, conParams):
            if not (
                type(x[1]) is type(y[1])
                or (type(x[1]) is FloatType and type(y[1]) is IntType)
            ):
                raise TypeMismatchInExpression(ast)
        return (None, ClassType(ast.classname))

    # TYPE
    def visitIntType(self, ast: IntType, o: object):
        return ast

    def visitFloatType(self, ast: FloatType, o: object):
        return ast

    def visitBoolType(self, ast: BoolType, o: object):
        return ast

    def visitStringType(self, ast: StringType, o: object):
        return ast

    def visitVoidType(self, ast: VoidType, o: object):
        return ast

    def visitArrayType(self, ast: ArrayType, o: object):
        return ast

    def visitClassType(self, ast: ClassType, o: object):
        env = o
        id = ast.classname.name
        if env["global"].get(id) is None:
            raise Undeclared(Class(), id)
        return ast

    # LITERAL
    def visitId(self, ast: Id, o: object):
        env = o
        id = ast.name
        if env.get("local") is not None:
            for local in env["local"]:
                if id in local:
                    return local[id]
        it = env["current"]
        while env["global"].get(it) is not None:
            classEnv = env["global"].get(it)
            if id in classEnv[1].keys():
                return env["global"][it][1][id]
            if classEnv[0] == None:
                raise Undeclared(Identifier(), id)
            it = classEnv[0]
        raise Undeclared(Identifier(), id)

    def visitIntLiteral(self, ast: IntLiteral, o: object):
        return (None, IntType())

    def visitFloatLiteral(self, ast: FloatLiteral, o: object):
        return (None, FloatType())

    def visitBooleanLiteral(self, ast: BooleanLiteral, o: object):
        return (None, BoolType())

    def visitStringLiteral(self, ast: StringLiteral, o: object):
        return (None, StringType())

    def visitNullLiteral(self, ast: NullLiteral, o: object):
        return (None, NullLiteral())

    def visitSelfLiteral(self, ast: SelfLiteral, o: object):
        return (None, SelfLiteral())

    def visitArrayLiteral(self, ast: ArrayLiteral, o: object):
        env = o
        EleList = reduce(lambda x, y: x + [self.visit(y, env)], ast.value, [])
        arrTyp = EleList[0][1]
        for ElementTyp in EleList:
            if type(ElementTyp[1]) is not type(arrTyp):
                raise IllegalArrayLiteral(ast)
        return (None, ArrayType(len(EleList), arrTyp))
