@256    // Bootstrap Code
D=A
@SP
M=D
@SYS_INIT_MAY_NOT_RETURN_HERE    // Push(without modify SP) return address
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

@5    // ARG = SP - numArgs - 5
D=D-A
@ARG
M=D

@Sys.init    // Jump to Sys.init
0;JMP

(SYS_INIT_MAY_NOT_RETURN_HERE)
(Sys.init)
@4    // push 4
D=A
@SP
AM=M+1
A=A-1
M=D
@RETURN_ADDRESS_1_of_Main.fibonacci    // Push(without modify SP) return address
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

@6    // ARG = SP - numArgs - 5
D=D-A
@ARG
M=D

@Main.fibonacci    // Jump to Main.fibonacci
0;JMP

(RETURN_ADDRESS_1_of_Main.fibonacci)
(Sys.init$WHILE)
@Sys.init$WHILE
0;JMP
(Main.fibonacci)
@ARG    // push ARG 0
A=M
D=M
@SP
AM=M+1
A=A-1
M=D
@SP    // push 2
AM=M+1
A=A-1
MD=1
M=D+M
@SP    // lt
AM=M-1
D=M
A=A-1
D=M-D
@LT_0
D;JLT
@SP
A=M-1
M=0
@ENDLT_0
0;JMP
(LT_0)
@SP
A=M-1
M=-1
(ENDLT_0)
@SP    // if_goto Main.fibonacci$IF_TRUE
AM=M-1
D=M
@Main.fibonacci$IF_TRUE
D;JNE
@Main.fibonacci$IF_FALSE
0;JMP
(Main.fibonacci$IF_TRUE)
@ARG    // push ARG 0
A=M
D=M
@SP
AM=M+1
A=A-1
M=D
@5    // Save return address(located at LCL-5) at R13
D=A
@LCL
A=M-D
D=M
@R13
M=D
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
(Main.fibonacci$IF_FALSE)
@ARG    // push ARG 0
A=M
D=M
@SP
AM=M+1
A=A-1
M=D
@SP    // push 2
AM=M+1
A=A-1
MD=1
M=D+M
@SP    // sub
AM=M-1
D=M
A=A-1
M=M-D
@RETURN_ADDRESS_2_of_Main.fibonacci    // Push(without modify SP) return address
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

@6    // ARG = SP - numArgs - 5
D=D-A
@ARG
M=D

@Main.fibonacci    // Jump to Main.fibonacci
0;JMP

(RETURN_ADDRESS_2_of_Main.fibonacci)
@ARG    // push ARG 0
A=M
D=M
@SP
AM=M+1
A=A-1
M=D
@SP    // push 1
AM=M+1
A=A-1
M=1
@SP    // sub
AM=M-1
D=M
A=A-1
M=M-D
@RETURN_ADDRESS_3_of_Main.fibonacci    // Push(without modify SP) return address
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

@6    // ARG = SP - numArgs - 5
D=D-A
@ARG
M=D

@Main.fibonacci    // Jump to Main.fibonacci
0;JMP

(RETURN_ADDRESS_3_of_Main.fibonacci)
@SP    // add
AM=M-1
D=M
A=A-1
M=D+M
@5    // Save return address(located at LCL-5) at R13
D=A
@LCL
A=M-D
D=M
@R13
M=D
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
