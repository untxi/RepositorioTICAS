 .MODEL SMALL      			; define un programa de 1 segmento
 .STACK 100h					; define una pila de 100H bytes
 .DATA						; define la sección de datos
   TiraNO           DB 'Hola mundo!', 0				; define un campo ´TiraNO´ que es una cadena con 12 bytes 
   TiraSi           DB 'dabalearrozalazorraelabad', 0
   MensajeSi        DB ' SI es', 10, 13, '$'
   MensajeNo        DB ' NO es', 10, 13, '$'

 .586								; arquitectura 586 o superior

 .CODE						; define la sección de código 

 Inicio:						; etiqueta
   MOV AX, @DATA                ; mueve la dirección del segmento de datos al AX
   MOV DS, AX
   LEA SI, TiraSI              	;        
   MOV DI, SI

   Ciclo1:
     CMP BYTE PTR [ DI ], 0            
     JE FinCiClo1
     INC DI                            
   JMP Ciclo1
   FinCiclo1:
   MOV BYTE PTR [ DI ], '$'            
   DEC DI                              
   LEA DX, TiraSI
   MOV AH, 09h                         
   INT 21h

   Ciclo2:
     CMP SI, DI
     JGE FinCiclo2Exito                
     MOV AL, [ SI ]                    
     CMP AL, [ DI ]                    
     JNE FinCiclo2Fallo
     INC SI                            
     DEC DI
   JMP Ciclo2
   FinCiclo2Exito:                     
     LEA DX, MensajeSi                 
     JMP FinCiclo2
   FinCiclo2Fallo:
     LEA DX, MensajeNo                 
   FinCiclo2:

   MOV AH, 09h                         
   INT 21h
   MOV AX, 4C00h                       
   INT 21h                             
 END Inicio