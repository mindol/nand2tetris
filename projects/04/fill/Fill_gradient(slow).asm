// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// init r, c, rm, cr, cd = 0
    @r
    M=0
    @c
    M=0
    @rm
    M=0
    @cr
    M=0
    @cd
    M=0

// RAM[24 ~ 39] has 2^0 ~ 2^15
    @j
    M=1
    @23
    D=A
    @k
    M=D
    @i
    MD=0 // i=0, j=1, k=23
(LOOP1)
    @16
    D=D-A
    @LOOP1_END
    D;JGE
    @j
    D=M
    M=D+M
    @k
    AM=M+1
    M=D    
    @i
    MD=M+1
    @LOOP1
    0;JMP
(LOOP1_END)

// RAM[40 ~ 55] has (~2^0) ~ (~2^15)
    @39
    D=A    
    @j
    M=D
    @23
    D=A
    @k
    M=D
    @i
    MD=0 // i=0, j=39, k=23
(LOOP2)
    @16
    D=D-A
    @LOOP2_END
    D;JGE
    D=-1
    @k
    AM=M+1
    D=D-M
    @j
    AM=M+1
    M=D
    @i
    MD=M+1
    @LOOP2
    0;JMP
(LOOP2_END)

// Infinite loop
(INF_LOOP)
    @24576
    D=M
    @IF_PRESSED
    D;JNE
    // Not Pressed
    @16384
    D=A
    @rm
    D=D+M
    @cd
    D=D+M
    @j
    M=D // j=16384+rm+cd
    @40
    D=A
    @cr
    A=D+M
    D=M // D=RAM[40+cr]
    @j
    A=M
    M=D&M // RAM[j] &= RAM[40+cr] (Erase)
    
    @r
    D=M
    @P1
    D;JNE
    @c
    D=M
    @P1
    D;JNE
    @PFIN  // r=0 and c=0 then do nothing.
    0;JMP    
(P1)
    @cr
    D=M
    @P1E
    D;JNE
    @15
    D=A
    @cr
    M=D
    @cd
    M=M-1
    @P2
    0;JMP
(P1E)
    @cr
    M=M-1
(P2)
    @c
    D=M
    @P2E
    D;JNE
    @511
    D=A
    @c
    M=D
    @31
    D=A
    @cd
    M=D
    @r
    M=M-1
    @32
    D=A
    @rm
    M=M-D
    @PFIN
    0;JMP
(P2E)
    @c
    M=M-1
(PFIN)
    @IF_END
    0;JMP

(IF_PRESSED)
    // Pressed
    @16384
    D=A
    @rm
    D=D+M
    @cd
    D=D+M
    @j
    M=D // j=16384+rm+cd
    @24
    D=A
    @cr
    A=D+M
    D=M // D=RAM[24+cr]
    @j
    A=M
    M=D|M // RAM[j] |= RAM[24+cr] (Fill)
    
    @255
    D=A
    @r
    D=D-M
    @N1
    D;JNE
    @255
    D=A
    @c
    D=D-M
    @N1
    D;JNE
    @NFIN // r=255 and c=255 then do nothing.
    0;JMP
(N1)
    @15
    D=A
    @cr
    D=D-M
    @N1E
    D;JNE
    @cr
    M=0
    @cd
    M=M+1
    @N2
    0;JMP
(N1E)
    @cr
    M=M+1
(N2)
    @511
    D=A
    @c
    D=D-M
    @N2E
    D;JNE
    @c
    M=0
    @cd
    M=0
    @r
    M=M+1
    @32
    D=A
    @rm
    M=M+D
    @NFIN
    0;JMP
(N2E)
    @c
    M=M+1
(NFIN)

(IF_END)
    @INF_LOOP
    0;JMP
