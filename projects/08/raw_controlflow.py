from textwrap import dedent

class ControlFlow:
    
    def label(labelname): # 0 instructions
        return dedent("""\
            ({})
        """.format(labelname))

    def goto(labelname): # 2 instructions
        return dedent("""\
            @{}
            0;JMP
        """.format(labelname))
    
    def if_goto(labelname): # 5 instructions
        return dedent("""\
            @SP    // if_goto {0}
            AM=M-1
            D=M
            @{0}
            D;JNE
        """.format(labelname))