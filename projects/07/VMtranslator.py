import sys
from enum import Enum

class Ctype(Enum):
    C_ARITHMETIC = 0
    C_PUSH = 1
    C_POP = 2
    C_LABEL = 3
    C_GOTO = 4
    C_IF = 5
    C_FUNCTION = 6
    C_RETURN = 7
    C_CALL = 8

def ERROR(*argv):
    print(*argv)
    sys.exit()

class Parser:
    def __init__(self, filename):
        self.commands = []
        self.current = None
        self.index = 0

        with open(filename, 'r') as file:
            raw = file.readlines()
            for line in raw:
                tokens = line.split("//")[0].split()
                if len(tokens) > 0:
                    self.commands.append(tokens)

    def hasMoreCommands(self):
        return self.index < len(self.commands)

    def advance(self):
        self.current = self.commands[self.index]
        self.index += 1

    # Only deals with arithmetic and memory access commands in project 7
    def commandType(self):
        opcode = self.current[0]
        if opcode in ["add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"]:
            return Ctype.C_ARITHMETIC
        elif opcode == "push":
            return Ctype.C_PUSH
        elif opcode == "pop":
            return Ctype.C_POP
        else:
            ERROR("[Parser::commandType] Unknown token:", opcode)

    def arg1(self):
        ctype = self.commandType()
        if ctype == Ctype.C_ARITHMETIC:
            return self.current[0]
        elif ctype == Ctype.C_RETURN:
            ERROR("[Parser::arg1] Called with C_RETURN command")
        else:
            return self.current[1]

    def arg2(self):
        ctype = self.commandType()
        if ctype in [Ctype.C_PUSH, Ctype.C_POP, Ctype.C_FUNCTION, Ctype.C_CALL]:
            return int(self.current[2])
        else:
            ERROR("[Parser::arg2] Called with wrong command type")

class CodeWriter:
    def __init__(self):
        self.file = None
        self.label_count = 0

    def setFileName(self, filename):
        self.file = open(filename, 'w')

    def writeArithmetic(self, command):
        res = ""
        if command == "add": # 5 instructions
            res = "\n".join((
                "@SP",
                "AM=M-1",
                "D=M",
                "A=A-1",
                "M=D+M",
            ))
        elif command == "sub": # 5 instructions
            res = "\n".join((
                "@SP",
                "AM=M-1",
                "D=M",
                "A=A-1",
                "M=M-D",
            ))
        elif command == "neg": # 3 instructions
            res = "\n".join((
                "@SP",
                "A=M-1",
                "M=-M",
            ))
        elif command == "eq": # 8 insts if x=y, 11 insts otherwise
            res = "\n".join((
                "@SP",
                "AM=M-1",
                "D=M",
                "A=A-1",
                "MD=M-D",
                "M=!M",
                "@EQ_{}".format(self.label_count),
                "D;JEQ",
                "@SP",
                "A=M-1",
                "M=0",
                "(EQ_{})".format(self.label_count),
            ))
            self.label_count += 1
        elif command == "gt": # 10 insts if x=y, 12 insts otherwise
            res = "\n".join((
                "@SP",
                "AM=M-1",
                "D=M",
                "A=A-1",
                "D=M-D",
                "@GT_{}".format(self.label_count),
                "D;JGT",
                "@SP",
                "A=M-1",
                "M=0",
                "@ENDGT_{}".format(self.label_count),
                "0;JMP",
                "(GT_{})".format(self.label_count),
                "@SP",
                "A=M-1",
                "M=-1",
                "(ENDGT_{})".format(self.label_count),
            ))
            self.label_count += 1
        elif command == "lt": # 10 insts if x=y, 12 insts otherwise
            res = "\n".join((
                "@SP",
                "AM=M-1",
                "D=M",
                "A=A-1",
                "D=M-D",
                "@LT_{}".format(self.label_count),
                "D;JLT",
                "@SP",
                "A=M-1",
                "M=0",
                "@ENDLT_{}".format(self.label_count),
                "0;JMP",
                "(LT_{})".format(self.label_count),
                "@SP",
                "A=M-1",
                "M=-1",
                "(ENDLT_{})".format(self.label_count),
            ))
            self.label_count += 1
        elif command == "and": # 5 instructions
            res = "\n".join((
                "@SP",
                "AM=M-1",
                "D=M",
                "A=A-1",
                "M=D&M",
            ))
        elif command == "or": # 5 instructions
            res = "\n".join((
                "@SP",
                "AM=M-1",
                "D=M",
                "A=A-1",
                "M=D|M",
            ))
        elif command == "not": # 3 instructions
            res = "\n".join((
                "@SP",
                "A=M-1",
                "M=!M",
            ))
        else:
            ERROR("[writeArithmetic] Unknown token:", command)
        
        self.file.write(res + "\n")

    def writePushPop(self, command, segment, index):
        res = ""
        if segment == "constant": # 6 instructions constant push
            res = "\n".join((
                "@{}".format(index),
                "D=A",
                "@SP",
                "AM=M+1",
                "A=A-1",
                "M=D"
            ))
        else:
            ERROR("[writePushPop] Unknown token:", segment)

        self.file.write(res + "\n")

    def __del__(self):
        if self.file is not None:
            self.file.close()
            self.file = None

def main():
    if len(sys.argv) < 2:
        ERROR('[Arguments] Give an argument')
    elif len(sys.argv) > 2:
        ERROR('[Arguments] Too many arguments')
    arg = sys.argv[1]

    print(arg)
    p = Parser(arg)

    path = arg.split("/")
    path[-1] = path[-1].replace(".vm", ".asm")
    print("/".join(path))
    cw = CodeWriter()
    cw.setFileName("/".join(path))
    
    while p.hasMoreCommands():
        p.advance()
        if p.commandType() == Ctype.C_ARITHMETIC:
            cw.writeArithmetic(p.current[0])
        elif p.commandType() == Ctype.C_PUSH:
            cw.writePushPop(p.commandType(), p.arg1(), p.arg2())

main()