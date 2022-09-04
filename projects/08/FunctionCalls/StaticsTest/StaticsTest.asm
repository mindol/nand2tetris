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
@6    // push 6
D=A
@SP
AM=M+1
A=A-1
M=D
@8    // push 8
D=A
@SP
AM=M+1
A=A-1
M=D
@RETURN_ADDRESS_1_of_Class1.set    // Push(without modify SP) return address
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

@7    // ARG = SP - numArgs - 5
D=D-A
@ARG
M=D

@Class1.set    // Jump to Class1.set
0;JMP

(RETURN_ADDRESS_1_of_Class1.set)
@SP    // pop temp 0
AM=M-1
D=M
@5
M=D
@23    // push 23
D=A
@SP
AM=M+1
A=A-1
M=D
@15    // push 15
D=A
@SP
AM=M+1
A=A-1
M=D
@RETURN_ADDRESS_1_of_Class2.set    // Push(without modify SP) return address
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

@7    // ARG = SP - numArgs - 5
D=D-A
@ARG
M=D

@Class2.set    // Jump to Class2.set
0;JMP

(RETURN_ADDRESS_1_of_Class2.set)
@SP    // pop temp 0
AM=M-1
D=M
@5
M=D
@RETURN_ADDRESS_1_of_Class1.get    // Push(without modify SP) return address
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

@Class1.get    // Jump to Class1.get
0;JMP

(RETURN_ADDRESS_1_of_Class1.get)
@RETURN_ADDRESS_1_of_Class2.get    // Push(without modify SP) return address
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

@Class2.get    // Jump to Class2.get
0;JMP

(RETURN_ADDRESS_1_of_Class2.get)
(Sys.init$WHILE)
@Sys.init$WHILE
0;JMP
(Class2.set)
@ARG    // push ARG 0
A=M
D=M
@SP
AM=M+1
A=A-1
M=D
@SP    // pop static
AM=M-1
D=M
@Class2.vm.0
M=D
@ARG    // push ARG 1
A=M+1
D=M
@SP
AM=M+1
A=A-1
M=D
@SP    // pop static
AM=M-1
D=M
@Class2.vm.1
M=D
@SP    // push 0
AM=M+1
A=A-1
M=0
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
(Class2.get)
@Class2.vm.0    // push static
D=M
@SP
AM=M+1
A=A-1
M=D
@Class2.vm.1    // push static
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
(Class1.set)
@ARG    // push ARG 0
A=M
D=M
@SP
AM=M+1
A=A-1
M=D
@SP    // pop static
AM=M-1
D=M
@Class1.vm.0
M=D
@ARG    // push ARG 1
A=M+1
D=M
@SP
AM=M+1
A=A-1
M=D
@SP    // pop static
AM=M-1
D=M
@Class1.vm.1
M=D
@SP    // push 0
AM=M+1
A=A-1
M=0
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
(Class1.get)
@Class1.vm.0    // push static
D=M
@SP
AM=M+1
A=A-1
M=D
@Class1.vm.1    // push static
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
