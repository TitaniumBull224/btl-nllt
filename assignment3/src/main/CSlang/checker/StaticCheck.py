from AST import *
from Visitor import *
from Utils import Utils, MType
from StaticError import *
from functools import reduce
from typing import Dict, List
import copy


class Env:
    def __str__(self):
        pass


class MemberEnv(Env):
    def __init__(self, typ: Type, isMu: bool):
        self.typ = typ
        self.isMu = isMu

    # def __str__(self):
    #     return (
    #         "MemberEnv(" + str(self.typ) + ", " + "Mutable"
    #         if self.isMu
    #         else "Immutable" + ")"
    #     )


class AttributeEnv(MemberEnv):
    def __init__(self, typ: Type, isMu: bool):
        super().__init__(typ, isMu)

    # def __str__(self):
    #     return (
    #         "AttributeEnv(" + str(self.typ) + ", " + "Mutable"
    #         if self.isMu
    #         else "Immutable" + ")"
    #     )


class MethodEnv(MemberEnv):
    def __init__(self, typ: Type, body: Dict):
        self.typ = typ
        self.isMu = False
        self.body = body

    # def __str__(self):
    #     return (
    #         "MethodEnv(" + str(self.typ) + ", " + "Mutable"
    #         if self.isMu
    #         else "Immutable" + str(self.body) + ")"
    #     )


class ClassEnv(Env):
    def __init__(self, parent: str, member: Dict):
        self.parent = parent
        self.member = member

    # def __str__(self):
    #     return "ClassEnv(" + self.parent + ", " + str(self.member) + ")"


class GetEnv(BaseVisitor, Utils):
    def visitProgram(self, ast: Program, o: object):
        o = reduce(lambda prev, curr: self.visit(curr, prev), ast.decl, o)
        return o

    def visitClassDecl(self, ast: ClassDecl, o: object):
        id = ast.classname.name
        parentId = ast.parentname.name if ast.parentname else None

        if o.get(id) is not None:
            raise Redeclared(Class(), id)

        env = reduce(lambda prev, curr: self.visit(curr, prev), ast.memlist, {})
        o[id] = ClassEnv(parentId, env)
        return o

    def visitAttributeDecl(self, ast: AttributeDecl, o: object):
        o = self.visit(ast.decl, o)
        return o

    def visitVarDecl(self, ast: VarDecl, o: object):
        id = ast.variable.name

        if o.get(id) is not None:
            raise Redeclared(Attribute(), id)

        o[id] = AttributeEnv(ast.varType, True)
        return o

    def visitConstDecl(self, ast: ConstDecl, o: object):
        id = ast.constant.name

        if o.get(id) is not None:
            raise Redeclared(Attribute(), id)

        o[id] = AttributeEnv(ast.constType, False)
        return o

    def visitMethodDecl(self, ast: MethodDecl, o: object):
        id = ast.name.name

        if o.get(id) is not None:
            raise Redeclared(Method(), id)
        body = {}

        for param in ast.param:
            if body.get(param.variable.name) is not None:
                raise Redeclared(Parameter(), param.variable.name)
            body[param.variable.name] = AttributeEnv(param.varType, True)
            if "constructor" in id:
                id += str(param.varType).replace("Type", "")

        if id == "constructor":
            id += "Default"

        for stmt in ast.body.stmt:
            if type(stmt) is VarDecl:
                if body.get(stmt.variable.name) is not None:
                    raise Redeclared(Variable(), stmt.variable.name)
                body[stmt.variable.name] = AttributeEnv(stmt.varType, True)

            if type(stmt) is ConstDecl:
                if body.get(stmt.constant.name) is not None:
                    raise Redeclared(Constant(), stmt.constant.name)
                body[stmt.constant.name] = AttributeEnv(stmt.constType, False)

        o[id] = MethodEnv(ast.returnType, body)
        return o


class EnvScope:
    def __init__(self, ast: Program, o: object):
        self.env = GetEnv().visit(ast, o)

    def searchGlobal(self, classId: str):
        if self.env.get(classId) is None:
            return False
        return True

    def searchCLassScope(self, classId: str, memberId: str):
        it = classId
        while self.env.get(it) is not None:
            classEnv = self.env.get(it)
            if memberId in classEnv.member.keys():
                return True
            if classEnv.parent == None:
                return False
            it = classEnv.parent
        return False

    def searchMethodScope(self):
        return True

    def searchStmtScope(self):
        return True


class StaticChecker(BaseVisitor, Utils):
    def __init__(self, ast):
        self.ast = ast
        self.io = {
            "io": ClassEnv(
                None,
                {
                    "@readInt": MethodEnv(IntType(), {}),
                    "@writeIntLn": MethodEnv(VoidType(), {"anArg": IntType()}),
                    "@readFloat": MethodEnv(FloatType(), {}),
                    "@writeFloatLn": MethodEnv(VoidType(), {"anArg": FloatType()}),
                    "@readBool": MethodEnv(BoolType(), {}),
                    "@writeBoolLn": MethodEnv(VoidType(), {"anArg": BoolType()}),
                    "@readStr": MethodEnv(StringType(), {}),
                    "@writeStrLn": MethodEnv(VoidType(), {"anArg": StringType()}),
                },
            )
        }

    def check(self):
        self.visit(self.ast, self.io)
        return []

    def visitProgram(self, ast: Program, o: object):
        o = EnvScope(ast, o)
        if o.searchCLassScope("Program", "@main") == False:
            raise NoEntryPoint()
        return o
