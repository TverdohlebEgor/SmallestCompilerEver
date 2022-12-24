import subprocess


def compileAndRun(outputAsm):
    subprocess.run(["nasm","-felf64",f"{outputAsm}.asm"])
    subprocess.run(["ld","-o",outputAsm,f"{outputAsm}.o"])
    subprocess.run(["rm",f"{outputAsm}.o"])
    subprocess.run([f"./{outputAsm}"])

def writePrint(fl,text = "Hello, world!"):
    fl.write("section .text\n")
    fl.write("    global _start\n\n")

    fl.write("section .data\n")
    fl.write(f"    msg db \"{text}\", 0xa\n")
    fl.write("    len equ $ - msg\n\n")

    fl.write("section .text\n")
    fl.write("    _start:\n\n")

    fl.write("    mov edx,len\n")
    fl.write("    mov ecx,msg\n")
    fl.write("    mov ebx, 1\n")
    fl.write("    mov eax, 4\n")
    fl.write("    int 0x80\n\n")
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
    
    with open(f"{outputFileName}.asm","w") as fl:
        writePrint(fl,"Hello, world!")
    
    compileAndRun(outputFileName)

if __name__ == "__main__":
    main()