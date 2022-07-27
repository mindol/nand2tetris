class Parser:
    def __init__(self, filename):
        self.f = open(filename, 'r')
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
        print(self.f)
        self.f.close()

class Code:
    def dest(mnemonic):
        pass
    def comp(mnemonic):
        pass
    def jump(mnemonic):
        pass

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
    pass

main()
        