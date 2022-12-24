end :
    mov ebx, 0
    mov eax, 1
    int 0x80

section .text
    global _start

section .text
    _start:

    mov edx,len
    mov ecx,msg
    mov ebx, 1
    mov eax, 4
    int 0x80

    mov edx,len2
    mov ecx,msg2
    mov ebx, 1
    mov eax, 4
    int 0x80

    jp end


section .data
    
    msg db "some random Text bro", 0xa
    len equ $ - msg
    
    msg2 db "other random Text  bro", 0xa
    len2 equ $ - msg2