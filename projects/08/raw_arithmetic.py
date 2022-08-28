from textwrap import dedent

class Arithmetic:

    def add(): # 5 instructions
        return dedent("""\
            @SP
            AM=M-1
            D=M
            A=A-1
            M=D+M
        """)
    
    def sub(): # 5 instructions
        return dedent("""\
            @SP
            AM=M-1
            D=M
            A=A-1
            M=M-D
        """)

    def neg(): # 3 instructions
        return dedent("""\
            @SP
            A=M-1
            M=-M
        """)

    def eq(label_count): # 8 insts if x=y, 11 insts otherwise
        return dedent("""\
            @SP
            AM=M-1
            D=M
            A=A-1
            MD=M-D
            M=!M
            @EQ_{0}
            D;JEQ
            @SP
            A=M-1
            M=0
            (EQ_{0})
        """.format(label_count))

    def gt(label_count): # 10 insts if x>y, 12 insts otherwise
        return dedent("""\
            @SP
            AM=M-1
            D=M
            A=A-1
            D=M-D
            @GT_{0}
            D;JGT
            @SP
            A=M-1
            M=0
            @ENDGT_{0}
            0;JMP
            (GT_{0})
            @SP
            A=M-1
            M=-1
            (ENDGT_{0})
        """.format(label_count))
    
    def lt(label_count): # 10 insts if x<y, 12 insts otherwise
        return dedent("""\
            @SP
            AM=M-1
            D=M
            A=A-1
            D=M-D
            @LT_{0}
            D;JLT
            @SP
            A=M-1
            M=0
            @ENDLT_{0}
            0;JMP
            (LT_{0})
            @SP
            A=M-1
            M=-1
            (ENDLT_{0})
        """.format(label_count))
    
    def _and(): # 5 instructions
        return dedent("""\
            @SP
            AM=M-1
            D=M
            A=A-1
            M=D&M
        """)
    
    def _or(): # 5 instructions
        return dedent("""\
            @SP
            AM=M-1
            D=M
            A=A-1
            M=D|M
        """)
    
    def _not(): # 3 instructions
        return dedent("""\
            @SP
            A=M-1
            M=!M
        """)