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
    msg dd "Read a and b: ", 0
    _format2 dd "%x", 0
    _format dd "%d%d", 0
    a dd 0
    b dd 0
    c dd 2
    
    ; our code starts here
segment code use32 class=code
    start:
        ; ...
        push dword msg
        call [printf]
        add ESP, 4*1 ;clear stack
        
        push dword a
        push dword b
        push dword _format
        call [scanf]
        add ESP, 4*3 ;clear stack

        mov EDX, 0
        mov EAX, [a]
        add EAX, [b]
        div dword [c]
        
        push dword EAX
        push dword _format2
        call [printf]
        add ESP, 4*1
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
