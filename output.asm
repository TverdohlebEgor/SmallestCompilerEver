section .text
    global _start

section .data
    msg0 db "Look here man i'm the best", 0xa
    len0 equ $ - msg0

    msg1 db "HAHAHHAHAHAHAHAHAHAHAH", 0xa
    len1 equ $ - msg1

    msg2 db "+++", 0xa
    len2 equ $ - msg2

section .text
    _start:

    mov edx,len0
    mov ecx,msg0
    mov ebx, 1
    mov eax, 4
    int 0x80

    mov edx,len1
    mov ecx,msg1
    mov ebx, 1
    mov eax, 4
    int 0x80

    mov edx,len2
    mov ecx,msg2
    mov ebx, 1
    mov eax, 4
    int 0x80

    jp end
end :

    mov ebx, 0
    mov eax, 1
    int 0x80
