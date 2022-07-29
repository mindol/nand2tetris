import sys
from enum import Enum

class Command(Enum):
    A_COMMAND = 0
    C_COMMAND = 1
    L_COMMAND = 2

class Parser:
    commands = []
    current = ""
    index = 0
    
    def __init__(self, filename):
        with open(filename, 'r') as file:
            raw = file.readlines()
            for line in raw:
                p = "".join(line.split())   # remove all whitespaces
                a = p.split("//")[0]        # ignore comments
                if len(a) > 0:
                    self.commands.append(a)

    def hasMoreCommands(self):
        return self.index < len(self.commands)

    def advance(self):
        self.current = self.commands[self.index]
        self.index += 1

    def commandType(self):
        if self.current[0] == '@':
            return Command.A_COMMAND
        elif self.current[0] == '(':
            return Command.L_COMMAND
        else:
            return Command.C_COMMAND

    def symbol(self): # Only for A_COMMAND, L_COMMAND
        if self.commandType() == Command.A_COMMAND:
            return self.current[1:]
        else:
            return self.current[1:-1]

    def dest(self): # Only for C_COMMAND
        if '=' not in self.current:
            return "null0"
        else:
            return self.current.split('=')[0]

    def comp(self): # Only for C_COMMAND
        now = self.current
        if '=' in self.current:
            now = now.split('=')[1]
        if ';' in now:
            now = now.split(';')[0]
        return now

    def jump(self): # Only for C_COMMAND
        if ';' not in self.current:
            return "null"
        else:
            return self.current.split(';')[-1]

class Code:
    def dest(mnemonic):
        bit = ""
        for c in "ADM":
            if c in mnemonic:
                bit += '1'
            else:
                bit += '0'
        return bit

    def comp(mnemonic):
        bit = ""
        if 'M' in mnemonic:
            bit = "1"
            mnemonic = mnemonic.replace("M", "A")
        else:
            bit = "0"

        compInsts = {"0": "101010", "1": "111111", "-1": "111010", "D": "001100", "A": "110000", "!D": "001101",
                    "!A": "110001", "-D": "001111", "-A": "110011", "D+1": "011111", "A+1": "110111", "D-1": "001110",
                    "A-1": "110010", "D+A": "000010", "D-A": "010011", "A-D": "000111", "D&A": "000000", "D|A": "010101"}
        bit += compInsts[mnemonic]
        return bit

    def jump(mnemonic):
        jumpInsts = {"null": "000", "JGT": "001", "JEQ": "010", "JGE": "011", "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111"}
        bit = jumpInsts[mnemonic]
        return bit

class SymbolTable:
    def __init__(self):
        pass
    def addEntry(self, symbol, address):
        pass
    def contains(self, symbol):
        pass
    def getAddress(self, symbol):
        pass

def main():
    if len(sys.argv) < 2:
        print('Give an argument')
        sys.exit()
    elif len(sys.argv) > 2:
        print('Too many arguments')
        sys.exit()
    
    filename = sys.argv[1]
    p = Parser(filename)

    result = []
    while p.hasMoreCommands():
        p.advance()
        if p.commandType() == Command.C_COMMAND:
            (dest, comp, jump) = (p.dest(), p.comp(), p.jump())
            result.append('111' + Code.comp(comp) + Code.dest(dest) + Code.jump(jump))
        elif p.commandType() == Command.A_COMMAND:
            symbol = int(p.symbol())
            result.append('0' + '{:015b}'.format(symbol))

    filename = sys.argv[1].replace('.asm', '.hack')
    with open(filename, 'w') as file:
        for line in result:
            file.write(line + '\n')

    print('Successfully saved to', filename)

main()
        