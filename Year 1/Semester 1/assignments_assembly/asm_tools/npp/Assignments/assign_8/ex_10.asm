bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf, scanf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf msvcrt.dll
import scanf  msvcrt.dll
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    msg dd "Read n: ", 0
    _format2 dd "%x", 0
    _format dd "%d", 0
    n dd 0

; our code starts here
segment code use32 class=code
    start:
        ; ...
        push dword msg
        call [printf]
        add ESP, 4*1 ;clear stack
        
        push dword n
        push dword _format
        call [scanf]
        add ESP, 4*2 ;clear stack

        
        push dword [n]
        push dword _format2
        call [printf]
        add ESP, 4*1
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
