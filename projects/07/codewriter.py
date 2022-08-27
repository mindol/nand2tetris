from ctype import Ctype

class CodeWriter:
    def __init__(self, filename):
        self.file = open(filename, 'w')
        self.label_count = 0
        self.filename = None

    def setFileName(self, filename):
        self.filename = filename

    def writeArithmetic(self, command):
        res = ""

        if command == "add": # 5 instructions
            res = "\n".join("""
                @SP     AM=M-1  D=M
                A=A-1   M=D+M
            """.split())
        elif command == "sub": # 5 instructions
            res = "\n".join("""
                @SP     AM=M-1  D=M
                A=A-1   M=M-D
            """.split())
        elif command == "neg": # 3 instructions
            res = "\n".join("""
                @SP     A=M-1   M=-M
            """.split())
        elif command == "eq": # 8 insts if x=y, 11 insts otherwise
            res = "\n".join("""
                @SP     AM=M-1  D=M
                A=A-1   MD=M-D  M=!M
                @EQ_{0} D;JEQ
                @SP     A=M-1   M=0
                (EQ_{0})
            """.format(self.label_count).split())
            self.label_count += 1
        elif command == "gt": # 10 insts if x>y, 12 insts otherwise
            res = "\n".join("""
                @SP     AM=M-1  D=M
                A=A-1   D=M-D
                @GT_{0} D;JGT
                @SP     A=M-1   M=0
                @ENDGT_{0}  0;JMP
                (GT_{0})
                @SP     A=M-1   M=-1
                (ENDGT_{0})
            """.format(self.label_count).split())
            self.label_count += 1
        elif command == "lt": # 10 insts if x<y, 12 insts otherwise
            res = "\n".join("""
                @SP     AM=M-1  D=M
                A=A-1   D=M-D
                @LT_{0} D;JLT
                @SP     A=M-1   M=0
                @ENDLT_{0}  0;JMP
                (LT_{0})
                @SP     A=M-1   M=-1
                (ENDLT_{0})
            """.format(self.label_count).split())
            self.label_count += 1
        elif command == "and": # 5 instructions
            res = "\n".join("""
                @SP     AM=M-1  D=M
                A=A-1   M=D&M
            """.split())
        elif command == "or": # 5 instructions
            res = "\n".join("""
                @SP     AM=M-1  D=M
                A=A-1   M=D|M
            """.split())
        elif command == "not": # 3 instructions
            res = "\n".join("""
                @SP     A=M-1   M=!M
            """.split())
        else:
            raise ValueError("[writeArithmetic] Unknown token: {}".format(command))
        
        self.file.write(res + "\n")
    
    def writePush(self, segment, index):
        res = ""
        abbr = {"local": "LCL", "argument": "ARG", "this": "THIS", "that": "THAT"}

        # [constant push]
        # 4 insts if constant = 0 or 1
        # 5 insts if constant = 2
        # 6 insts otherwise
        if segment == "constant": 
            if index == 0 or index == 1:
                res = "\n".join("""
                    @SP     AM=M+1  A=A-1   M={}
                """.format(index).split())
            elif index == 2:
                res = "\n".join("""
                    @SP     AM=M+1  A=A-1
                    MD=1    M=D+M
                """.split())
            else:
                res = "\n".join("""
                    @{}     D=A
                    @SP     AM=M+1  A=A-1   M=D
                """.format(index).split())

        # [local, argument, this, that push]
        # 7 insts if index = 0 or 1
        # 9 insts otherwise
        elif segment in abbr:
            if index == 0 or index == 1:
                res = "\n".join((
                    "@{}".format(abbr[segment]),
                    "A=M" + ("" if index == 0 else "+1"),
                    "D=M"
                ))
            else:
                res = "\n".join((
                    "@{}".format(index),
                    "D=A",
                    "@{}".format(abbr[segment]),
                    "A=D+M",
                    "D=M"
                ))
            res += "\n" + "\n".join("""
                @SP     AM=M+1  A=A-1   M=D
            """.split())

        # [pointer, temp push]
        # 6 instructions
        elif segment in ["pointer", "temp"]:
            ptr = (3 if segment == "pointer" else 5) + index
            res = "\n".join("""
                @{}     D=M
                @SP     AM=M+1  A=A-1   M=D
            """.format(ptr).split())
        
        # [static push]
        # 6 instructions
        elif segment == "static":
            res = "\n".join("""
                @{}.{}  D=M
                @SP     AM=M+1  A=A-1   M=D
            """.format(self.filename, index).split())

        else:
            raise ValueError("[writePush] Unknown token: {}".format(segment))

        self.file.write(res + "\n")
    
    def writePop(self, segment, index):
        res = ""
        abbr = {"local": "LCL", "argument": "ARG", "this": "THIS", "that": "THAT"}

        # [constant pop]
        # no instructions.
        if segment == "constant":
            pass

        # [local, argument, this, that pop]
        # 6 insts if index = 0, 1
        # 12 insts otherwise
        elif segment in abbr:
            if index == 0 or index == 1:
                res = "\n".join((
                    "@SP",
                    "AM=M-1",
                    "D=M",
                    "@{}".format(abbr[segment]),
                    "A=M" + ("" if index == 0 else "+1"),
                    "M=D"
                ))
            else:
                res = "\n".join("""
                    @{}     D=A     @{}     D=D+M
                    @R13    M=D
                    @SP     AM=M-1  D=M
                    @R13    A=M     M=D
                """.format(index, abbr[segment]).split())

        # [pointer, temp pop]
        # 5 instructions
        elif segment in ["pointer", "temp"]:
            ptr = (3 if segment == "pointer" else 5) + index
            res = "\n".join("""
                @SP     AM=M-1  D=M
                @{}     M=D
            """.format(ptr).split())

        # [static pop]
        # 5 instructions
        elif segment == "static":
            res = "\n".join("""
                @SP     AM=M-1  D=M
                @{}.{}  M=D
            """.format(self.filename, index).split())

        else:
            raise ValueError("[writePop] Unknown token: {}".format(segment))

        self.file.write(res + "\n")

    def __del__(self):
        if self.file is not None:
            self.file.close()
            self.file = None