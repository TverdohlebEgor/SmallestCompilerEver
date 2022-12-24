import subprocess


def compileAndRun(outputAsm):
    subprocess.run(["nasm","-felf64",f"{outputAsm}.asm"])
    subprocess.run(["ld","-o",outputAsm,f"{outputAsm}.o"])
    subprocess.run(["rm",f"{outputAsm}.o"])
    subprocess.run([f"./{outputAsm}"])

def writePrint(fl , text : list):
    fl.write("section .text\n")
    fl.write("    global _start\n\n")

    fl.write("section .data\n")

    for x in range(len(text)):
        fl.write(f"    msg{x} db \"{text[x]}\", 0xa\n")
        fl.write(f"    len{x} equ $ - msg{x}\n\n")

    fl.write("section .text\n")
    fl.write("    _start:\n\n")

    for x in range(len(text)):
        fl.write(f"    mov edx,len{x}\n")
        fl.write(f"    mov ecx,msg{x}\n")
        fl.write( "    mov ebx, 1\n")
        fl.write( "    mov eax, 4\n")
        fl.write( "    int 0x80\n\n")


    fl.write("    jp end\n")


    fl.write("end :\n\n")

    fl.write("    mov ebx, 0\n")
    fl.write("    mov eax, 1\n")
    fl.write("    int 0x80\n")

def main():
    outputFileName = "output"
    inputFileName = "fileInput.lm"

    linesOfCode = []

    with open(inputFileName, "r") as fl:
        linesOfCode = fl.read().split(";")
        linesOfCode = list(map(lambda x : x.strip("\n"),linesOfCode))
    
    printableStuff = []

    for ind,string in enumerate(linesOfCode):
        if string[:8] == "printman":
            if(string[9] != '\"' or string[-2] != '\"'):
                print(string,string[9],string[-2])
                raise Exception(f"Error ->  you can't print a non string object line {ind+1}")
            printableStuff.append(string[10 : -2])

    with open(f"{outputFileName}.asm","w") as fl:
        writePrint(fl,printableStuff)
    
    compileAndRun(outputFileName)

if __name__ == "__main__":
    main()