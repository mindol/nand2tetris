from textwrap import dedent

class MemoryAccess:

    def push_constant_0_or_1(value): # 4 instructions
        return dedent("""\
            @SP    // push {0}
            AM=M+1
            A=A-1
            M={0}
        """.format(value))

    def push_constant_2(): # 5 instructions
        return dedent("""\
            @SP    // push 2
            AM=M+1
            A=A-1
            MD=1
            M=D+M
        """)

    def push_constant_greater_than_2(value): # 6 instructions
        return dedent("""\
            @{0}    // push {0}
            D=A
            @SP
            AM=M+1
            A=A-1
            M=D
        """.format(value))

    def push_pointer(index): # 6 instructions
        return dedent("""\
            @{0}    // push pointer {1}
            D=M
            @SP
            AM=M+1
            A=A-1
            M=D
        """.format(3 + index, index))

    def push_temp(index): # 6 instructions
        return dedent("""\
            @{0}    // push temp {1}
            D=M
            @SP
            AM=M+1
            A=A-1
            M=D
        """.format(5 + index, index))

    def push_static(filename, index): # 6 instructions
        return dedent("""\
            @{}.{}    // push static
            D=M
            @SP
            AM=M+1
            A=A-1
            M=D
        """.format(filename, index))

    def push_indirect_segment_0_or_1(abbr, index): # 7 instructions
        return dedent("""\
            @{0}    // push {0} {2}
            A=M{1}
            D=M
            @SP
            AM=M+1
            A=A-1
            M=D
        """.format(abbr, ("" if index == 0 else "+1"), index))
    
    def push_indirect_segment_greater_than_1(abbr, index): # 9 instructions
        return dedent("""\
            @{0}    // push {1} {2}
            D=A
            @{1}
            A=D+M
            D=M
            @SP
            AM=M+1
            A=A-1
            M=D
        """.format(index, abbr, index))


    def pop_indirect_segment_0_or_1(abbr, index): # 6 instructions
        return dedent("""\
            @SP    // pop {0} {2}
            AM=M-1
            D=M
            @{0}
            A=M{1}
            M=D
        """.format(abbr, ("" if index == 0 else "+1"), index))

    def pop_indirect_segment_greater_than_1(abbr, index): # 12 instructions
        return dedent("""\
            @{0}    // pop {1} {0}
            D=A
            @{1}
            D=D+M
            @R13
            M=D    // save addr at R13
            @SP
            AM=M-1
            D=M
            @R13
            A=M
            M=D
        """.format(index, abbr))
    
    def pop_pointer(index): # 5 instructions
        return dedent("""\
            @SP    // pop pointer {1}
            AM=M-1
            D=M
            @{0}
            M=D
        """.format(3 + index, index))

    def pop_temp(index): # 5 instructions
        return dedent("""\
            @SP    // pop temp {1}
            AM=M-1
            D=M
            @{0}
            M=D
        """.format(5 + index, index))

    def pop_static(filename, index): # 5 instructions
        return dedent("""\
            @SP    // pop static
            AM=M-1
            D=M
            @{}.{}
            M=D
        """.format(filename, index))