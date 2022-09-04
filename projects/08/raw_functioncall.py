from textwrap import dedent
from raw_memoryaccess import MemoryAccess

class FunctionCall:
    
    # 4 * (numLocals) instructions
    def function_locals_4k(functionName, numLocals):
        res = '({})\n'.format(functionName)
        for _ in range(numLocals):
            res += MemoryAccess.push_constant_0_or_1(0)
        return res

    # 0 insts if numLocals = 0
    # 2 * (numLocals) + 4 insts otherwise
    def function_locals_2kp4(functionName, numLocals):
        res = '({})\n'.format(functionName)
        if numLocals > 0:
            res += dedent("""\
                @SP
                A=M
            """)
            for _ in range(numLocals - 1):
                res += dedent("""\
                    M=0
                    A=A+1
                """)
            res += dedent("""\
                M=0
                D=A+1
                @SP
                M=D
            """)

        return res

    # 35 instructions
    def call(functionName, numArgs, return_labelname):
        return dedent("""\
            @{0}    // Push(without modify SP) return address
            D=A
            @SP
            A=M
            M=D

            @LCL    // Push LCL
            D=M
            @SP
            AM=M+1
            M=D

            @ARG    // Push ARG
            D=M
            @SP
            AM=M+1
            M=D

            @THIS    // Push THIS
            D=M
            @SP
            AM=M+1
            M=D

            @THAT    // Push THAT
            D=M
            @SP
            AM=M+1
            M=D

            @SP    // Increment SP
            MD=M+1

            @LCL    // LCL = SP
            M=D

            @{2}    // ARG = SP - numArgs - 5
            D=D-A
            @ARG
            M=D

            @{1}    // Jump to {1}
            0;JMP

            ({0})
        """.format(return_labelname, functionName, numArgs + 5))

    # 7 instructions
    def _save_return_address_at_R13():
        return dedent("""\
            @5    // Save return address(located at LCL-5) at R13
            D=A
            @LCL
            A=M-D
            D=M
            @R13
            M=D
        """)
        return res

    # 39 instructions
    def _return():
        res = FunctionCall._save_return_address_at_R13()
        res += dedent("""\
            @SP    // Save return value
            A=M-1
            D=M
            @ARG
            A=M
            M=D
            D=A+1    // Set SP
            @SP
            M=D

            @LCL    // Set THAT
            AM=M-1
            D=M
            @THAT
            M=D

            @LCL    // Set THIS
            AM=M-1
            D=M
            @THIS
            M=D

            @LCL    // Set ARG
            AM=M-1
            D=M
            @ARG
            M=D

            @LCL    // Set LCL
            AM=M-1
            D=M
            @LCL
            M=D

            @R13    // Jump to return address
            A=M
            0;JMP
        """)

        return res
        

    