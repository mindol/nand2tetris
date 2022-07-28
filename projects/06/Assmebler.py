import sys

class Parser:
    commands = []
    
    def __init__(self, filename):
        try:
            self.file = open(filename, 'r')
        except:
            print('Error during file opening')
            raise
        rawInput = self.file.readlines()

        #for line in rawInput:
        #    a = list(map(str.strip, line.split("//")))
        #    print(a)

    def hasMoreCommands(self):
        pass 
    def advance(self):
        pass
    def commandType(self):
        pass
    def symbol(self):
        pass
    def dest(self):
        pass
    def comp(self):
        pass
    def jump(self):
        pass
    def __del__(self):
        try:
            self.file.close()
        except:
            pass

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

main()
        