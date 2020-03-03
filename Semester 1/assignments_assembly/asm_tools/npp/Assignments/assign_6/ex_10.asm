;Given an array A of words, build two arrays of bytes:  
;- array B1 contains as elements the higher part of the words from A
;- array B2 contains as elements the lower part of the words from A

bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    A DW 2345h, 0A5h, 368h, 3990h
    len equ ($-A)/2
    B1 times len DB 0
    B2 times len DB 0

; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;lower parts
        mov ESI, A
        mov EDI, B2
        mov ECX, len
        cld
        repeat:
            lodsw ;AX <- [ESI], ESI += 2
            stosb
            loop repeat
        ;higher parts
        mov ESI, A
        mov ECX, len
        mov EDI, B1
        repeat1:
            lodsw; AX <- [ESI], ESI += 2, high byte in AH
            mov AL, AH
            stosb; AL ->[EDI], EDI++
            loop repeat1
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
