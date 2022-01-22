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

// Infinite loop
(INF_LOOP)
    @24576
    D=M
    @IF_PRESSED
    D;JNE
    // Not Pressed
    @16383
    D=A
    @i
    M=D
(NPLOOP)
    @24575
    D=D-A
    @INF_LOOP
    D;JGE
    @i
    AMD=M+1
    M=0
    @NPLOOP
    0;JMP

(IF_PRESSED)
    // Pressed
    @16383
    D=A
    @i
    M=D
(PLOOP)
    @24575
    D=D-A
    @INF_LOOP
    D;JGE
    @i
    AMD=M+1
    M=-1
    @PLOOP
    0;JMP
