(SimpleFunction.test)
@SP    // push 0
AM=M+1
A=A-1
M=0
@SP    // push 0
AM=M+1
A=A-1
M=0
@LCL    // push LCL 0
A=M
D=M
@SP
AM=M+1
A=A-1
M=D
@LCL    // push LCL 1
A=M+1
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
@SP    // not
A=M-1
M=!M
@ARG    // push ARG 0
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
@ARG    // push ARG 1
A=M+1
D=M
@SP
AM=M+1
A=A-1
M=D
@SP    // sub
AM=M-1
D=M
A=A-1
M=M-D
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
