from ctype import Ctype
from raw_arithmetic import Arithmetic
from raw_memoryaccess import MemoryAccess
from raw_controlflow import ControlFlow
from raw_functioncall import FunctionCall

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
            res = Arithmetic.add()
        elif command == "sub": # 5 instructions
            res = Arithmetic.sub()
        elif command == "neg": # 3 instructions
            res = Arithmetic.neg()
        elif command == "eq": # 8 insts if x=y, 11 insts otherwise
            res = Arithmetic.eq(self.label_count)
            self.label_count += 1
        elif command == "gt": # 10 insts if x>y, 12 insts otherwise
            res = Arithmetic.gt(self.label_count)
            self.label_count += 1
        elif command == "lt": # 10 insts if x<y, 12 insts otherwise
            res = Arithmetic.lt(self.label_count)
            self.label_count += 1
        elif command == "and": # 5 instructions
            res = Arithmetic._and()
        elif command == "or": # 5 instructions
            res = Arithmetic._or()
        elif command == "not": # 3 instructions
            res = Arithmetic._not()
        else:
            raise ValueError("[writeArithmetic] Unknown token: {}".format(command))
        
        self.file.write(res)
    
    def writePush(self, segment, index):
        res = ""
        abbr = {"local": "LCL", "argument": "ARG", "this": "THIS", "that": "THAT"}

        # [constant push]
        # 4 insts if constant = 0 or 1
        # 5 insts if constant = 2
        # 6 insts otherwise
        if segment == "constant": 
            if index == 0 or index == 1:
                res = MemoryAccess.push_constant_0_or_1(index)
            elif index == 2:
                res = MemoryAccess.push_constant_2()
            else:
                res = MemoryAccess.push_constant_greater_than_2(index)

        # [local, argument, this, that push] (indirect segments)
        # 7 insts if index = 0 or 1
        # 9 insts otherwise
        elif segment in abbr:
            if index == 0 or index == 1:
                res = MemoryAccess.push_indirect_segment_0_or_1(abbr[segment], index)
            else:
                res = MemoryAccess.push_indirect_segment_greater_than_1(abbr[segment], index)

        # [pointer, temp push]
        # 6 instructions
        elif segment == "pointer":
            res = MemoryAccess.push_pointer(index)
        elif segment == "temp":
            res = MemoryAccess.push_temp(index)

        # [static push]
        # 6 instructions
        elif segment == "static":
            res = MemoryAccess.push_static(self.filename, index)

        else:
            raise ValueError("[writePush] Unknown token: {}".format(segment))

        self.file.write(res)
    
    def writePop(self, segment, index):
        res = ""
        abbr = {"local": "LCL", "argument": "ARG", "this": "THIS", "that": "THAT"}

        # [constant pop]
        # no instructions.
        if segment == "constant":
            pass

        # [local, argument, this, that pop] (indirect segments)
        # 6 insts if index = 0, 1
        # 12 insts otherwise
        elif segment in abbr:
            if index == 0 or index == 1:
                res = MemoryAccess.pop_indirect_segment_0_or_1(abbr[segment], index)
            else:
                res = MemoryAccess.pop_indirect_segment_greater_than_1(abbr[segment], index)

        # [pointer, temp pop]
        # 5 instructions
        elif segment == "pointer":
            res = MemoryAccess.pop_pointer(index)
        elif segment == "temp":
            res = MemoryAccess.pop_temp(index)

        # [static pop]
        # 5 instructions
        elif segment == "static":
            res = MemoryAccess.pop_static(self.filename, index)

        else:
            raise ValueError("[writePop] Unknown token: {}".format(segment))

        self.file.write(res)

    def __del__(self):
        if self.file is not None:
            self.file.close()
            self.file = None