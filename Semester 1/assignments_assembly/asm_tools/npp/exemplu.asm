; asamblare 			nasm -fobj exemplu.asm
; linkeditare 			alink -oPE -subsys console -entry start exemplu.obj
; depanare  			ollydbg exemplu.exe
; programe necesare 	http://www.nasm.us + alink: alink.sourceforge.net/download.html + http://www.ollydbg.de

bits 32

global start
extern ExitProcess, printf
import ExitProcess kernel32.dll
import printf msvcrt.dll

segment code use32 class=CODE


start:
    mov AX, 86h
    cbw
    mov BL, 2
    div BL


segment data use32 class=DATA
    msg: db "Mesaj!", 13, 10, 0
    