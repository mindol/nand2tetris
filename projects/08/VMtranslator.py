import os, sys
from ctype import Ctype
from parser import Parser
from codewriter import CodeWriter

def main():
    if len(sys.argv) < 2:
        raise ValueError('[Arguments] Give an argument')
    elif len(sys.argv) > 2:
        raise ValueError('[Arguments] Too many arguments')

    arg = os.path.normpath(sys.argv[1])
    if not os.path.exists(arg):
        raise FileNotFoundError("[File] No such file or directory")

    vm_files = []
    output_filename = ""
    if os.path.isfile(arg): # got file
        vm_files.append(arg)
        if arg.endswith(".vm"):
            output_filename = arg.replace(".vm", ".asm")
        else:
            output_filename = arg + ".asm"
    else: # got directory
        for file in os.listdir(arg):
            if file.endswith(".vm"):
                vm_files.append(os.path.join(arg, file))
        if len(vm_files) == 0:
            raise FileNotFoundError("[Directory] Cannot find any .vm files in {}".format(arg))
        output_filename = os.path.join(arg, os.path.basename(arg) + ".asm")

    print("VM files:")
    for file in vm_files:
        print("\t" + file)
    print("Output:")
    print("\t" + output_filename)

    cw = CodeWriter(output_filename)
    for file in vm_files:
        cw.setFileName(os.path.basename(os.path.normpath(file)))
        p = Parser(file)
        while p.hasMoreCommands():
            p.advance()
            if p.commandType() == Ctype.C_ARITHMETIC:
                cw.writeArithmetic(p.current[0])
            elif p.commandType() == Ctype.C_PUSH:
                cw.writePush(p.arg1(), p.arg2())
            elif p.commandType() == Ctype.C_POP:
                cw.writePop(p.arg1(), p.arg2())
            elif p.commandType() == Ctype.C_LABEL:
                cw.writeLabel(p.arg1())
            elif p.commandType() == Ctype.C_GOTO:
                cw.writeGoto(p.arg1())
            elif p.commandType() == Ctype.C_IF:
                cw.writeIf(p.arg1())
            else:
                print("[command type] pass:", p.commandType)

if __name__ == "__main__":
    main()