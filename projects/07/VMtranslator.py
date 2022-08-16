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
            return self.current[2]
        else:
            ERROR("[Parser::arg2] Called with wrong command type")

def main():
    if len(sys.argv) < 2:
        ERROR('[Arguments] Give an argument')
    elif len(sys.argv) > 2:
        ERROR('[Arguments] Too many arguments')
    arg = sys.argv[1]

    print(arg)
    p = Parser(arg)
    while p.hasMoreCommands():
        p.advance()
        print(p.current, p.commandType())

main()