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
@4000    // push 4000
D=A
@SP
AM=M+1
A=A-1
M=D
@SP    // pop pointer 0
AM=M-1
D=M
@3
M=D
@5000    // push 5000
D=A
@SP
AM=M+1
A=A-1
M=D
@SP    // pop pointer 1
AM=M-1
D=M
@4
M=D
@RETURN_ADDRESS_1_of_Sys.main    // Push(without modify SP) return address
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

@Sys.main    // Jump to Sys.main
0;JMP

(RETURN_ADDRESS_1_of_Sys.main)
@SP    // pop temp 1
AM=M-1
D=M
@6
M=D
(Sys.init$LOOP)
@Sys.init$LOOP
0;JMP
(Sys.main)
@SP
A=M
M=0
A=A+1
M=0
A=A+1
M=0
A=A+1
M=0
A=A+1
M=0
D=A+1
@SP
M=D
@4001    // push 4001
D=A
@SP
AM=M+1
A=A-1
M=D
@SP    // pop pointer 0
AM=M-1
D=M
@3
M=D
@5001    // push 5001
D=A
@SP
AM=M+1
A=A-1
M=D
@SP    // pop pointer 1
AM=M-1
D=M
@4
M=D
@200    // push 200
D=A
@SP
AM=M+1
A=A-1
M=D
@SP    // pop LCL 1
AM=M-1
D=M
@LCL
A=M+1
M=D
@40    // push 40
D=A
@SP
AM=M+1
A=A-1
M=D
@2    // pop LCL 2
D=A
@LCL
D=D+M
@R13
M=D    // save addr at R13
@SP
AM=M-1
D=M
@R13
A=M
M=D
@6    // push 6
D=A
@SP
AM=M+1
A=A-1
M=D
@3    // pop LCL 3
D=A
@LCL
D=D+M
@R13
M=D    // save addr at R13
@SP
AM=M-1
D=M
@R13
A=M
M=D
@123    // push 123
D=A
@SP
AM=M+1
A=A-1
M=D
@RETURN_ADDRESS_1_of_Sys.add12    // Push(without modify SP) return address
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

@Sys.add12    // Jump to Sys.add12
0;JMP

(RETURN_ADDRESS_1_of_Sys.add12)
@SP    // pop temp 0
AM=M-1
D=M
@5
M=D
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
@2    // push LCL 2
D=A
@LCL
A=D+M
D=M
@SP
AM=M+1
A=A-1
M=D
@3    // push LCL 3
D=A
@LCL
A=D+M
D=M
@SP
AM=M+1
A=A-1
M=D
@4    // push LCL 4
D=A
@LCL
A=D+M
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
@SP    // add
AM=M-1
D=M
A=A-1
M=D+M
@SP    // add
AM=M-1
D=M
A=A-1
M=D+M
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
(Sys.add12)
@4002    // push 4002
D=A
@SP
AM=M+1
A=A-1
M=D
@SP    // pop pointer 0
AM=M-1
D=M
@3
M=D
@5002    // push 5002
D=A
@SP
AM=M+1
A=A-1
M=D
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
@12    // push 12
D=A
@SP
AM=M+1
A=A-1
M=D
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
