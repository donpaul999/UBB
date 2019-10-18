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
		a DD 6
		b DB 5
		c DB 15
		d DB 5
		x DQ 41
		
	; our code starts here
	segment code use32 class=code
		start:
			; ...
			mov AL, [b] ;AL := b
			mul AL	; AX := AL*AL = b * b
			mov BX, AX ; BX := AX = b * b
			
			mov AL, [c]	; AL := c
			mov AH, 0	; AX := c
			div byte [d]	;AL := c/d, AH := c % d

			mov AH, 0	; AX := AL = c/d
			sub BX, AX 	; BX := BX - AX = b * b - c / d
			add BX, 2	; BX := BX + 2 = b * b - c / d + 2
		
			mov EAX, dword [x]	
			mov EDX, dword [x + 4]	; EDX:EAX := x
			
			add EAX, 7
			adc EDX, 0	; EDX:EAX := x + 7
			
            push 0
			push BX
			pop ECX	;ECX := CX= b*b -c/d+2
			
			div ECX ; EDX := EDX % ECX, EAX := EAX/ ECX
			
			mov EBX, [a]	;EBX := a
			sub EBX, EAX	;EBX := EBX - EAX
                            ;EBX := 4
			
			
			; exit(0)
			push    dword 0      ; push the parameter for exit onto the stack
			call    [exit]       ; call exit to terminate the program
