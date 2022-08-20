import os, sys
from misc import Ctype, ERROR
from parser import Parser
from codewriter import CodeWriter

def main():
    if len(sys.argv) < 2:
        ERROR('[Arguments] Give an argument')
    elif len(sys.argv) > 2:
        ERROR('[Arguments] Too many arguments')

    arg = os.path.normpath(sys.argv[1])
    if not os.path.exists(arg):
        ERROR("[File] No such file or directory")

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
            ERROR("[Directory] Cannot find any .vm files in", arg)
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
            else:
                print("[command type] pass:", p.commandType)

if __name__ == "__main__":
    main()