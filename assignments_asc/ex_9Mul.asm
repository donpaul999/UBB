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
    a DB 6
    b DB 5
    c DW 10
    e DD 15
    x DQ 12
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov AX, [c]
        mov DX, 128
        mul DX
        mov BL, [a]
        mov BH, 0
        sub BL, [b]
        add BX, AX 
        mov AX, BX
        mov CL, [a]
        add CL, [b]
        div CL
        add AX, [e]
        sub AX, [x] ;AH = 5 AL = 119
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
