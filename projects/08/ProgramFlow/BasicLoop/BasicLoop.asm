@SP    // push 0
AM=M+1
A=A-1
M=0
@SP    // pop LCL 0
AM=M-1
D=M
@LCL
A=M
M=D
(LOOP_START)
@ARG    // push ARG 0
A=M
D=M
@SP
AM=M+1
A=A-1
M=D
@LCL    // push LCL 0
A=M
D=M
@SP
AM=M+1
A=A-1
M=D
@SP    // add
AM=M-1
D=M
A=A-1
M=D+M
@SP    // pop LCL 0
AM=M-1
D=M
@LCL
A=M
M=D
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
@SP    // pop ARG 0
AM=M-1
D=M
@ARG
A=M
M=D
@ARG    // push ARG 0
A=M
D=M
@SP
AM=M+1
A=A-1
M=D
@SP    // if_goto LOOP_START
AM=M-1
D=M
@LOOP_START
D;JNE
@LCL    // push LCL 0
A=M
D=M
@SP
AM=M+1
A=A-1
M=D
