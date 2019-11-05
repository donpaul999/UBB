;A byte string S is given. Build the string D whose elements represent the sum of each two consecutive bytes of S.

bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    S DB 1, 2, 3, 4, 5, 6
    len equ $-S
    d times len DB 0
    
; our code starts here
segment code use32 class=code
    start:
        mov ESI, 0
        repeat:
            mov AL, [S + ESI]
            inc ESI
            mov BL, [S + ESI]
            add AL, BL
            add AL, '0'
            mov [d + ESI], AL
        cmp ESI, len - 1
        jb repeat
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
