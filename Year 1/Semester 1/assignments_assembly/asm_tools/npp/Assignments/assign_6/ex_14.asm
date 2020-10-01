;Given an array S of doublewords, build the array of bytes D formed from bytes of doublewords sorted as unsigned numbers in ascending order.

bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    S DD 12345607h, 1A2B3C15h
    len equ $ - S
    d times len DB 0
    
; our code starts here
segment code use32 class=code
    start:
        mov ESI, S
        mov EDI, d
        mov ECX, len
        cld
        repeat:
            lodsb; AL <- [ESI]; ESI := ESI + 1
            stosb; AL <- [EDI]; EDI := EDI + 1
            loop repeat
        
        mov DX, 1 ; Bubble sort
        repeat1:
            cmp DX, 0
            je the_end
            mov DX, 0
            mov ESI, d
            mov ECX, len
            repeat2:
                mov AL, [ESI]
                cmp AL, [ESI + 1]
                jle next
                mov AH, [ESI + 1]
                mov BH, [ESI]
                mov [ESI + 1], BH
                mov [ESI], AH
                mov DX, 1
            next:
                inc ESI
                loop repeat2
                jmp repeat1             ;d DB 07h, 12h, 15h, 1Ah, 2Bh, 34h, 3Ch, 56h    
        the_end:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
