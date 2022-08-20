from misc import Ctype, ERROR

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
        elif command == "gt": # 10 insts if x>y, 12 insts otherwise
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
        elif command == "lt": # 10 insts if x<y, 12 insts otherwise
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
    
    def writePush(self, segment, index):
        res = ""
        abbr = {"local": "LCL", "argument": "ARG", "this": "THIS", "that": "THAT"}

        # [constant push]
        # 4 insts if constant = 0 or 1
        # 5 insts if constant = 2
        # 6 insts otherwise
        if segment == "constant": 
            if index == 0 or index == 1:
                res = "\n".join((
                    "@SP",
                    "AM=M+1",
                    "A=A-1",
                    "M={}".format(index)
                ))
            elif index == 2:
                res = "\n".join((
                    "@SP",
                    "AM=M+1",
                    "A=A-1",
                    "MD=1",
                    "M=D+M"
                ))
            else:
                res = "\n".join((
                    "@{}".format(index),
                    "D=A",
                    "@SP",
                    "AM=M+1",
                    "A=A-1",
                    "M=D"
                ))

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
            res += "\n" + "\n".join((
                "@SP",
                "AM=M+1",
                "A=A-1",
                "M=D"
            ))

        # [pointer, temp push]
        # 6 instructions
        elif segment in ["pointer", "temp"]:
            ptr = (3 if segment == "pointer" else 5) + index
            res += "\n".join((
                "@{}".format(ptr),
                "D=M",
                "@SP",
                "AM=M+1",
                "A=A-1",
                "M=D"
            ))
        
        # [static push]
        # 6 instructions
        elif segment == "static":
            res += "\n".join((
                "@{}.{}".format(self.filename, index),
                "D=M",
                "@SP",
                "AM=M+1",
                "A=A-1",
                "M=D"
            ))

        else:
            ERROR("[writePush] Unknown token:", segment)

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
                res = "\n".join((
                    "@{}".format(index),
                    "D=A",
                    "@{}".format(abbr[segment]),
                    "D=D+M",
                    "@R13",
                    "M=D",
                    "@SP",
                    "AM=M-1",
                    "D=M",
                    "@R13",
                    "A=M",
                    "M=D"
                ))

        # [pointer, temp pop]
        # 5 instructions
        elif segment in ["pointer", "temp"]:
            ptr = (3 if segment == "pointer" else 5) + index
            res = "\n".join((
                "@SP",
                "AM=M-1",
                "D=M",
                "@{}".format(ptr),
                "M=D"
            ))

        # [static pop]
        # 5 instructions
        elif segment == "static":
            res = "\n".join((
                "@SP",
                "AM=M-1",
                "D=M",
                "@{}.{}".format(self.filename, index),
                "M=D"
            ))

        else:
            ERROR("[writePop] Unknown token:", segment)

        self.file.write(res + "\n")

    def __del__(self):
        if self.file is not None:
            self.file.close()
            self.file = None