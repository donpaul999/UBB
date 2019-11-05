;Se da un sir de caractere S. Sa se construiasca sirul D care sa contina toate literele mici din sirul S.

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
    S DB 'a', 'A', 'b', 'B', '2', '%', 'x'
    len equ $-S
    d times len DB 0
    
; our code starts here
segment code use32 class=code
    start:
        mov ESI, -1
        repeat:
            inc ESI
            mov AL, [S+ESI]
            cmp AL, 'a'
            jb repeat
            cmp AL, 'z'
            ja repeat
            mov [d + ESI], AL
        cmp ESI, len
        jb repeat
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
