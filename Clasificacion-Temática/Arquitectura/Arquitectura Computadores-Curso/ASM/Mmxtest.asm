;--------------------------------------------------------------------------
; El siguiente programa es para determinar si la m†quina en la cual es
;  ejecutado posee tecnolog°a MMX en el procesador                                                                         
;--------------------------------------------------------------------------                                                                           
        .model small
        .stack 100h
        .586
                                                                   
        .data                                                      
                                                                   
        l1      db  '    ‹‹     ‹‹  ‹‹     ‹‹  ‹‹     ‹‹           $'
        l2      db  '     €ﬂ‹ ‹ﬂ€    €ﬂ‹ ‹ﬂ€     ﬂ‹ ‹ﬂ             $'
        l3      db  '     €  €  €    €  €  €       €               $'
        l4      db  '     €     €    €     €     ‹ﬂ ﬂ‹    TESTER   $'
        l5      db  '    ﬂﬂ     ﬂﬂ  ﬂﬂ     ﬂﬂ  ﬂﬂ     ﬂﬂ           $'
        l6      db  'ƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒ $'
        l7      db  '  Verificando presencia de MMX                $'
        l8      db  '         Salado!, su computadora no           $'
        l9      db  '         Genial!, su computadora s°           $'
        lA      db  '             tiene tecnolog°a MMX             $'
        lB      db  '  MMX-Technology Tester por (c)Esteban Arias  $'
        lC      db '          Presione ESC para terminar           $'
                                                                   
        .code                                                      
                                                                   
Inicio:                                                            
        mov ax,@data                                               
        mov ds,ax                                                  
                                                                   
        mov bh,03h       ; Color                                   
        call Limpiar_Pantalla                                      
        mov bl,009h     ; Color                                    
        call Pantalla                                              
                                                                   
        mov eax,1                                                  
        CPUID
        test edx,00800000h                                         
        jz      Not_Found                                          
        jnz     MMX_Technology_Found                
                                                    
Not_Found:                                          
        mov dx,0D13h
        call Cursor
        lea dx,l8       ; l°nea 8
        call Mostrar
        jmp Concluir
                                
MMX_Technology_Found:        
        mov dx,0D13h
        call Cursor              
        lea dx,l9       ; l°nea 9
        call Mostrar              
        jmp Concluir         
                             
Concluir: ; Devuelve el control al DOS, termina el programa
        mov dx,0E13h
        call Cursor               
        lea dx,lA       ; l°nea 10
        call Mostrar              
        mov dx,1013h              
        call Cursor               
        lea dx,l6       ; l°nea 6 
        call Mostrar              
        mov dx,1213h              
        call Cursor               
        lea dx,lB       ; l°nea 11
        call Mostrar
        mov dx,1713h
        call Cursor 
        lea dx,lC       ; l°nea 12
        call Mostrar
        mov dx,0D1Bh
        call Cursor
        
Espere:
        mov ah,10h    	; Lectura de tecla
        int 16h                                  
                                                 
        cmp ah,01h	; Compara con Esc (Salir)
        je Final                                 
        jmp Espere
                  
Final:            
        mov bh,07h       ; Color
        call Limpiar_Pantalla
        mov ax,4C00h
        int 21h                   
                  
;--- Procedimiento para limpiar la pantalla                    
Limpiar_Pantalla proc near                 
        mov ax,0600h     ; Solicitud de recorrido de pantalla
        mov cx,0000      ; De 00,00                 
        mov dx,184fh     ; A 24,79                  
        int 10h     
Limpiar_Pantalla endp        
         
;--- Procedimiento para cambiar color del texto ---
Color proc near
        call Cursor     ; Ubicar el cursor
        mov ah,09h
        mov al,'-'                
        mov bh,00h
        int 10h         ; Establecer el color
        ret        
Color endp       
         
;--- Procedimiento para ubicar el cursor ---                               
Cursor  proc near                     
        mov ah,02h      ; Solicitud de ubicaci¢n del cursor
        mov bh,00       ; P†gina 0    
        int 10h                       
        ret                           
Cursor  endp                          
                                                                           
;--- Procedimiento para mostrar datos en pantalla ---                      
Mostrar proc near                     
        mov ah,09h      ; Solicitud de despliegue en pantalla
        int 21h         ; Llama al DOS
        ret      
Mostrar endp      
                                  
;--- Procedimiento para crear la presentaci¢n ---                 
Pantalla proc near
        mov dx,0313h    ; Posici¢n
        mov cx,45       ; Espacio
        call color   
        mov dx,0313h              
        call Cursor  
        lea dx,l1       ; l°nea 1
        call Mostrar
                   
        mov dx,0413h    ; Posici¢n
        mov cx,45       ; Espacio
        call color   
        mov dx,0413h
        call Cursor  
        lea dx,l2       ; l°nea 2
        call Mostrar
                   
        mov dx,0513h    ; Posici¢n
        mov cx,45       ; Espacio 
        call color   
        mov dx,0513h
        call Cursor  
        lea dx,l3       ; l°nea 3
        call Mostrar             
                                  
        mov dx,0613h    ; Posici¢n
        mov cx,45       ; Espacio
        call color               
        mov dx,0613h
        call Cursor              
        lea dx,l4       ; l°nea 4
        call Mostrar
                   
        mov dx,0713h    ; Posici¢n
        mov cx,45       ; Espacio
        call color               
        mov dx,0713h
        call Cursor              
        lea dx,l5       ; l°nea 5 
        call Mostrar             
                                 
        mov dx,0813h    ; Posici¢n
        mov bl,00Bh     ; Color
        mov cx,45       ; Espacio
        call color                
        mov dx,0813h           
        call Cursor               
        lea dx,l6       ; l°nea 6 
        call Mostrar              
                                  
        mov dx,0B13h              
        call Cursor               
        lea dx,l7       ; l°nea 7 
        call Mostrar              
                                  
        mov dx,0D13h    ; Posici¢n
        mov bl,00Bh     ; Color
        mov cx,45       ; Espacio
        call color 
        mov dx,0E13h    ; Posici¢n
        mov bl,00Bh     ; Color           
        mov cx,45       ; Espacio         
        call color                        
        mov dx,1013h    ; Posici¢n        
        mov bl,00Bh     ; Color   
        mov cx,45       ; Espacio 
        call color 
        mov dx,1213h    ; Posici¢n
        mov bl,009h     ; Color
        mov cx,45       ; Espacio 
        call color                
                   
        ret                    
Pantalla endp                  
                               
        end Inicio             
