@ARG    // push ARG 1
A=M+1
D=M
@SP
AM=M+1
A=A-1
M=D
@SP    // pop pointer 1
AM=M-1
D=M
@4
M=D
@SP    // push 0
AM=M+1
A=A-1
M=0
@SP    // pop THAT 0
AM=M-1
D=M
@THAT
A=M
M=D
@SP    // push 1
AM=M+1
A=A-1
M=1
@SP    // pop THAT 1
AM=M-1
D=M
@THAT
A=M+1
M=D
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
@SP    // pop ARG 0
AM=M-1
D=M
@ARG
A=M
M=D
(MAIN_LOOP_START)
@ARG    // push ARG 0
A=M
D=M
@SP
AM=M+1
A=A-1
M=D
@SP    // if_goto COMPUTE_ELEMENT
AM=M-1
D=M
@COMPUTE_ELEMENT
D;JNE
@END_PROGRAM
0;JMP
(COMPUTE_ELEMENT)
@THAT    // push THAT 0
A=M
D=M
@SP
AM=M+1
A=A-1
M=D
@THAT    // push THAT 1
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
@2    // pop THAT 2
D=A
@THAT
D=D+M
@R13
M=D    // save addr at R13
@SP
AM=M-1
D=M
@R13
A=M
M=D
@4    // push pointer 1
D=M
@SP
AM=M+1
A=A-1
M=D
@SP    // push 1
AM=M+1
A=A-1
M=1
@SP    // add
AM=M-1
D=M
A=A-1
M=D+M
@SP    // pop pointer 1
AM=M-1
D=M
@4
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
@MAIN_LOOP_START
0;JMP
(END_PROGRAM)
