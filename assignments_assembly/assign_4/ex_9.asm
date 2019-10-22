;Given the word A and the byte B, compute the doubleword C as follows:
;the bits 0-3 of C are the same as the bits 6-9 of A
;the bits 4-5 of C have the value 1
;the bits 6-7 of C are the same as the bits 1-2 of B
;the bits 8-23 of C are the same as the bits of A
;the bits 24-31 of C are the same as the bits of B

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
     a dw 0111011101010111b
     b db 10111110b
     c dd 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov AX, 0
        
        mov BX, [a]
        and BX, 00000000000000000000001111000000b
        mov CL, 6
        ror BX, CL
        or AX, BX
        
        or AX,00000000000000000000000000110000b
        
        mov BX, [b]
        and BX, 00000000000000000000000000000110b
        mov CL, 4
        rol BX, CL
        or AX, BX
        
        mov BX, [a]
        and BX, 00000000111111111111111100000000b
        or AX, BX
                
        mov BX, [b]
        and BX, 11111111000000000000000000000000b
        or AX, BX   ;AX = 110010111011101111101 (19777Dh)
        
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
