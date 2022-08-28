from textwrap import dedent

class MemoryAccess:

    def push_constant_0_or_1(value): # 4 instructions
        return dedent("""\
            @SP
            AM=M+1
            A=A-1
            M={}
        """.format(value))

    def push_constant_2(): # 5 instructions
        return dedent("""\
            @SP
            AM=M+1
            A=A-1
            MD=1
            M=D+M
        """)

    def push_constant_greater_than_2(value): # 6 instructions
        return dedent("""\
            @{}
            D=A
            @SP
            AM=M+1
            A=A-1
            M=D
        """.format(value))

    def push_pointer(index): # 6 instructions
        return dedent("""\
            @{}
            D=M
            @SP
            AM=M+1
            A=A-1
            M=D
        """.format(3 + index))

    def push_temp(index): # 6 instructions
        return dedent("""\
            @{}
            D=M
            @SP
            AM=M+1
            A=A-1
            M=D
        """.format(5 + index))

    def push_static(filename, index): # 6 instructions
        return dedent("""\
            @{}.{}
            D=M
            @SP
            AM=M+1
            A=A-1
            M=D
        """.format(filename, index))

    def push_indirect_segment_0_or_1(abbr, index): # 7 instructions
        return dedent("""\
            @{}
            A=M{}
            D=M
            @SP
            AM=M+1
            A=A-1
            M=D
        """.format(abbr, ("" if index == 0 else "+1")))
    
    def push_indirect_segment_greater_than_1(abbr, index): # 9 instructions
        return dedent("""\
            @{}
            D=A
            @{}
            A=D+M
            D=M
            @SP
            AM=M+1
            A=A-1
            M=D
        """.format(index, abbr))


    def pop_indirect_segment_0_or_1(abbr, index): # 6 instructions
        return dedent("""\
            @SP
            AM=M-1
            D=M
            @{}
            A=M{}
            M=D
        """.format(abbr, ("" if index == 0 else "+1")))

    def pop_indirect_segment_greater_than_1(abbr, index): # 12 instructions
        return dedent("""\
            @{}
            D=A
            @{}
            D=D+M
            @R13
            M=D
            @SP
            AM=M-1
            D=M
            @R13
            A=M
            M=D
        """.format(index, abbr))
    
    def pop_pointer(index): # 5 instructions
        return dedent("""\
            @SP
            AM=M-1
            D=M
            @{}
            M=D
        """.format(3 + index))

    def pop_temp(index): # 5 instructions
        return dedent("""\
            @SP
            AM=M-1
            D=M
            @{}
            M=D
        """.format(5 + index))

    def pop_static(filename, index): # 5 instructions
        return dedent("""\
            @SP
            AM=M-1
            D=M
            @{}.{}
            M=D
        """.format(filename, index))