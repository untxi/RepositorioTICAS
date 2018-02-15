; Dibujo de Triangulos                                                     
; --------------------------------------------------------------------------

.model small    ; Define el tama¤o del programa
.stack 100h     ; Pila de la m quina           
                                               
.data           ; Definir las constantes y variables
                                               
        ; Valores de los puntos de la figura   
        X1      dw ?    ; Valor X, punto 1 de la figura
        Y1      dw ?    ; Valor Y, punto 1 de la figura
        X2      dw ?    ; Valor X, punto 2 de la figura
        Y2      dw ?    ; Valor Y, punto 2 de la figura
        X3      dw ?    ; Valor X, punto 3 de la figura
        Y3      dw ?    ; Valor Y, punto 3 de la figura
                                               
        ; Valores auxiliares para decrementar o aumentar los valores
        ; en el dibujo de una l¡nea            
        x       dw ?                            
        y       dw ?                           
                                               
        ; Valores de los puntos que utiliza Dibuja L¡nea
        ; Utilizando el algoritmo de Bresenham 
        DLX1    dw ?    ; x                    
        DLY1    dw ?    ; y                    
        DLX2    dw ?    ; x' = x2-x1           
        DLY2    dw ?    ; y' = y2-y1                     
        e       dw ?    ; e = y'/x' - 0.5      
                                                
        ; Otras variables                       
        Color   db 9     ; Color de los pixeles
        Video   dw 0A000h 
                          
        ; Segmento de Video
        CGD     dw 3CEh ; Direcci¢n del puerto del controlador grafico
        CGBit   db 8    ; Registro del CG (8 es su id)
        CGMode  db 5    ; Registro del CG (5 es su id). Indica los modos
                        ; de lectura y escritura que se usan
                                        
        ;Contadores                     
        Ccoord   dw 1  ; Contador de coordenadas (x,y)
        i        dw 0  ; Contador
                     
        ;Datos para l¡nea decreciente
        DistanciaX      dw 0    ; Distancia entre x1-x2
        DistanciaY      dw 0    ; Distancia entre y1-y2
        Avance          dw 0    ; Factor de avance de Y
        Avanzar         dw 0    ; Acumulador de lo avanzado en Y
        Cantidad        dw 0    ; Lo que avanza en Y en el presente ciclo
                          
        ;Varibles utilizadas en Bresenham
        DeltaX          dw ?
        DeltaY          dw ?
        NumPixels       dw ?
        D               dw ?
        DInc1           dw ?
        DInc2           dw ?
        XInc1           dw ?
        XInc2           dw ?
        YInc1           dw ?
        YInc2           dw ?
                                                              
.code           ; C¢digo del programa                         
                                                              
Inicio:                                                       
        ; @data retorna la direcci¢n del primer elemento en el 
        ; segmento de datos                                   
        MOV AX,@data    ; Inicializaci¢n del segmento de datos
        MOV DS,AX       ; pasa la informaci¢n del registro al segmento 
                        ; de datos                            
                                                              
        ; Modo Gr fico en VGA 640*480                         
        MOV Al,12h                                            
        MOV AH,00h                                            
        INT 10h                                               
                                                              
        MOV AL,0                                              
        MOV AH,06h                                            
        INT 10h                                               
                    
        ; Color del fondo de pantalla                         
        MOV BH,0    
        MOV BL,0                                              
        MOV AH,0Bh                                            
        INT 10h                                               
                                                              
        ; Muestra el puntero del mouse                        
        MOV AX,0001h                                                 
        INT 33h                                                      
                                                                     
Mouse1: ; Obtiene las coordenadas del mouse                   
                                                                     
        MOV BX, BYTE PTR 0        ; Activa bot¢n izquierdo del mouse
        MOV AX,0005h                                                 
        INT 33h      
        JMP Mouse2                                                   
                                                                     
Mouse2: ; Si se di¢ un click con el bot¢n izquierdo llama a CrdX
                                                                
        CMP AX,1        ; Comparaci¢n con 1, Click bot¢n izquierdo(1)
        JE  CrdX        ; Si son iguales(1), se di¢ click, llama a CrdX
        JMP Mouse1      ; Salta a Mouse1                      
                                                                     
CrdX: ; Si la coordenada X es 0, llama a Crdy; sino regresa a Mouse1
                                                              
        CMP CX,0        ; Comparaci¢n con 0
        JE  CrdY        ; Si son iguales(0), CoordX = 0, llama a CrdY
        JNE C           ; Si x no es 0 llama a coordenada.    
        JMP Mouse1      ; Salta a Mouse1                      
                                                              
CrdY: ; Si la coordenada Y es 0, como la coord X tambi‚n era 0, llama 
      ; a terminar                                            
                                                              
        CMP DX,0        ; Comparaci¢n con 0
        JZ  Terminar    ; Si son iguales(0), CoordY = 0, llama Terminar
        JNE C           ; Si y no es cero llama a coordenada  
        JMP Mouse1      ; Salta a Mouse1                      
                                                              
C:      MOV AX,300
        MOV DLX1,AX      
        MOV AX,200       
        MOV DLY1,AX      
        MOV AX,50        
        MOV DLX2,AX      
        MOV AX,70        
        MOV DLY2,AX      
        CALL DibujaLinea 
                         
        MOV AX,50        
        MOV DLX1,AX      
        MOV AX,70        
        MOV DLY1,AX      
        MOV AX,300
        MOV DLX2,AX      
        MOV AX,40
        MOV DLY2,AX      
        CALL DibujaLinea 
                                
        MOV AX,300       
        MOV DLX1,AX      
        MOV AX,40
        MOV DLY1,AX      
        MOV AX,300       
        MOV DLX2,AX      
        MOV AX,200       
        MOV DLY2,AX      
        CALL DibujaLinea 
                
        CALL Coordenada
                         
        JMP Mouse1       
                                 
Terminar: ; Devuelve el control al DOS, termina el programa     
                                 
        MOV AX,4C00h                                          
        INT 21h                                            
                                                              
; Asigna los valores de entrada (clicks) a los puntos
Coordenada PROC NEAR     
                                                                 
Izq:    CMP AX,1         
        JE  Izq          
                         
;        INC Ccoord      ; Aumenta el n£mero de coordenadas (x,y)
        CMP Ccoord,1    ; Primera coordenada, punto 1
        JE  C1                   
        CMP Ccoord,2    ; Segunda coordenada, punto 2
        JE  C2                   
        CMP Ccoord,3    ; Tercera coordenada, punto 3
        JE  C3                   
                                 
                                 
C1:     CALL Click1              
        JMP R                    
                                 
C2:     CALL Click2              
        JMP R                    
                                 
C3:                              
                                 
        CALL Click3              
        JMP R                    
                                 
R:      RET                      
                                 
Coordenada ENDP                                                              
                                 
; Asigna las coordenadas del punto 1
Click1 PROC NEAR 
                                 
        MOV AX,X1
        CMP AX,0 
        JE  Cero1
        JNE Asig1
                 
Cero1:  MOV AX,Y1
        CMP AX,0     
        JE  SiInc1
        JNE Asig1 
                  
SiInc1: INC Ccoord
        JMP Asig1           
                 
Asig1:  INC Ccoord
        MOV X1,CX
        MOV Y1,DX                
        XOR CX,CX       ; Limpiar CX
        XOR DX,DX       ; Limpiar DX       
        RET               
                          
Click1 ENDP               
                                                                 
; Asigna las coordenadas del punto 2 y dibuja la linea entre
; los puntos 1 y 2       
Click2 PROC NEAR 
                          
        MOV AX,X2
        CMP AX,0     
        JE  Cero2
        JNE Asig2
                 
Cero2:  MOV AX,Y2
        CMP AX,0 
        JE  SiInc2
        JNE Asig2
                         
SiInc2: INC Ccoord
        JMP Asig2
                 
Asig2:  MOV X2,CX
        MOV Y2,DX         
                         
        MOV AX,X1       ; X1 --> DLX1
        MOV DLX1,AX                                        
        MOV AX,Y1       ; Y1 --> DLY1                                   
        MOV DLY1,AX                                        
        MOV AX,X2       ; X2 --> DLX2
        MOV DLX2,AX                     
        MOV AX,Y2       ; Y2 --> DLY2
        MOV DLY2,AX                                        
        CALL DibujaLinea    
                         
        XOR CX,CX       ; Limpiar CX
        XOR DX,DX       ; Limpiar DX       
        RET                 
                            
Click2 ENDP              
                                            
; Asigna las coordenadas del punto 3 y dibuja las lineas entre
; los puntos 3,2 y 3,1                                                              
Click3 PROC NEAR         
                            
        MOV AX,X3    
        CMP AX,0     
        JE  Cero3    
        JNE Asig3    
                     
Cero3:  MOV AX,Y3    
        CMP AX,0     
        JE  SiInc3   
        JNE Asig3
                  
SiInc3: INC Ccoord
        JMP Asig3
                 
Asig3:  MOV AX,0         
        MOV Ccoord,AX
        INC COLOR
        MOV X3,CX           
        MOV Y3,DX           
                            
        MOV AX,X3       ; X3 --> DLX1
        MOV DLX1,AX                                        
        MOV AX,Y3       ; Y3 --> DLY1
        MOV DLY1,AX                                        
        MOV AX,X2       ; X2 --> DLX2
        MOV DLX2,AX                     
        MOV AX,Y2       ; Y2 --> DLY2
        MOV DLY2,AX                                        
        CALL DibujaLinea    
                            
        MOV AX,X3       ; X3 --> DLX1
        MOV DLX1,AX                                        
        MOV AX,Y3       ; Y3 --> DLY1
        MOV DLY1,AX                                        
        MOV AX,X1       ; X1 --> DLX2
        MOV DLX2,AX                     
        MOV AX,Y1       ; Y1 --> DLY2
        MOV DLY2,AX  
                                                
        CALL DibujaLinea    
                     
        MOV AX,0
        MOV X1,AX
        MOV Y1,AX
        MOV X2,AX
        MOV Y2,AX
        MOV X3,AX
        MOV Y3,AX
        MOV Ccoord,AX
        
        XOR CX,CX       ; Limpiar CX
        XOR DX,DX       ; Limpiar DX       
        RET               
                         
Click3 ENDP              
                         
; Dibuja una l¡nea entre dos puntos
DibujaLinea PROC NEAR
                     
        ; Ordenar puntos
        MOV AX,DLX1   
        CMP AX,DLX2  
        JG  Ordena
        JNG Ver
                     
Ordena: MOV AX,DLX1      
        MOV BX,DLX2
        MOV DLX1,BX
        MOV DLX2,AX
        MOV AX,DLY1
        MOV BX,DLY2
        MOV DLY1,BX
        MOV DLY2,AX
                   
        ; Es la l¡nea vertical?
Ver:    MOV AX,DLX1 
        CMP AX,DLX2 
        JE  Vertical 
                    
        ; Es la l¡nea horizontal?
Hor:    MOV AX,DLY1   
        CMP AX,DLY2
        JE  Horizontal
                      
        ; Es la l¡nea creciente?  
Cre:    MOV AX,DLY1      
        CMP AX,DLY2
        JG  Creciente
                                  
        ; Es la l¡nea decreciente?
Dcr:    MOV AX,DLY1
        CMP AX,DLY2    
        JL  Decreciente
                               
Vertical:              
        CALL LineaVertical
        RET        
                     
Horizontal:         
        CALL LineaHorizontal
        RET           
                            
Creciente:          
        CALL LineaCreciente
        RET                
                         
Decreciente:                
        CALL LineaDecreciente
        RET                 
                            
DibujaLinea ENDP            
                            
; Dibuja una l¡nea Vertical (s¢lo aumentan los Y)
LineaVertical PROC NEAR
                            
        MOV AX,DLY1  
        CMP AX,DLY2  
        JG  CambY    
        JNG SigaY
                   
CambY:  MOV AX,DLY1
        MOV BX,DLY2
        MOV DLY1,BX
        MOV DLY2,AX
                  
SigaY:  MOV AX,DLX1
        MOV X,AX
        MOV AX,DLY1
        MOV Y,AX
           
CVer:   CALL PIXEL 
        INC Y         
        MOV AX,Y    
        CMP AX,DLY2    
        JG  RVer
        JL  CVer
                            
RVer:   RET         
                                                                
LineaVertical ENDP                              
                                 
; Dibuja una l¡nea Horizontal (s¢lo aumentan los X)
LineaHorizontal PROC NEAR
                       
        MOV AX,DLX1    
        CMP AX,DLX2    
        JG  CambX      
        JNG SigaX      
                       
CambX:  MOV AX,DLX1    
        MOV BX,DLX2    
        MOV DLX1,BX    
        MOV DLX2,AX    
                       
SigaX:  MOV AX,DLX1
        MOV X,AX      
        MOV AX,DLY1   
        MOV Y,AX
          
CHor:   CALL PIXEL 
        INC X         
        MOV AX,X      
        CMP AX,DLX2      
        JG  RHor         
        JL  CHor         
                         
RHor:   RET                 
                                                  
LineaHorizontal ENDP     
                                 
; Dibuja una l¡nea creciente (y1 > y2) && (x1 < x2)
LineaCreciente PROC NEAR
                        
        CALL Bresenham  
        RET             
                              
LineaCreciente ENDP                            
                                               
; Dibuja una l¡nea decreciente (y1 < y2) && (x1 < x2)
LineaDecreciente PROC NEAR
                      
        CALL Bresenham
        RET  
                                                    
LineaDecreciente ENDP  
             
; Aplica el algoritmo de Bresenham
Bresenham PROC NEAR
                                
        ; Inicializando Valores                  
        MOV AX,0          
        MOV i,AX          
                                        
        ; DeltaX = ABS(DLX2-DLX1)
DelX:   MOV AX,DLX2         
        CMP AX,DLX1             
        JG  PositivoX     
        JL  NegativoX     
        JE  CeroX         
                                
PositivoX:           
        MOV AX,DLX2             
        SUB AX,DLX1
        MOV DeltaX,AX
        JMP DelY
                 
NegativoX:                       
        MOV AX,DLX1             
        SUB AX,DLX2                
        MOV DeltaX,AX           
        JMP DelY
                                
CeroX:  MOV AX,0          
        MOV DeltaX,AX     
        JMP DelY            
                                
        ; DeltaY = ABS(DLY2-DLY1)
DelY:   MOV AX,DLY2       
        CMP AX,DLY1       
        JG  PositivoY
        JL  NegativoY
        JE  CeroY         
                                
PositivoY:                
        MOV AX,DLY2       
        SUB AX,DLY1       
        MOV DeltaY,AX     
        JMP Cond1         
                                
NegativoY:                       
        MOV AX,DLY1             
        SUB AX,DLY2                
        MOV DeltaY,AX           
        JMP Cond1         
                                
CeroY:  MOV AX,0          
        MOV DeltaY,AX           
        JMP Cond1         
                          
Cond1:  ; If (DeltaX >= DeltaY)
        MOV AX,DeltaX          
        CMP AX,DeltaY          
        JG  Proc1       ; SI
        JE  Proc1       ; SI
        JL  Proc2       ; NO
                                                
Proc1:  MOV AX,DeltaX           ; NumPixels = DeltaX + 1
        ADD AX,1                                        
        MOV NumPixels,AX                        
        MOV AX,DeltaY           ; D = (2*DeltaY) - DeltaX
        ADD AX,AX
        SUB AX,DeltaX
        MOV D,AX                                
        MOV AX,DeltaY           ; DInc1 = DeltaY shl 1
        SHL AX,1                ; (Corrimiento a la izquierda)
        MOV DInc1,AX        
        MOV AX,DeltaY           ; DInc2 = (DeltaY - DeltaX) shl 1
        SUB AX,DeltaX                           
        SHL AX,1            
        MOV DInc2,AX        
        MOV AX,1                
        MOV XInc1,AX            ; XInc1 = 1                
        MOV XInc2,AX            ; XInc2 = 1                
        MOV YInc2,AX            ; YInc2 = 1
        MOV AX,0 
        MOV YInc1,AX            ; YInc1 = 0
        JMP Cond2           
                                                
Proc2: ; If (DeltaX < DeltaY)                   
        MOV AX,DeltaY           ;NumPixels = DeltaY + 1
        ADD AX,1                                       
        MOV NumPixels,AX    
        MOV AX,DeltaX           ; D = (2*DeltaX) - DeltaY
        ADD AX,AX
        SUB AX,DeltaY       
        MOV D,AX            
        MOV AX,DeltaX           ; DInc1 = DeltaX shl 1
        SHL AX,1                ; (Corrimiento a la izquierda)
        MOV DInc1,AX                       
        MOV AX,DeltaX           ; DInc2 = (DeltaX - DeltaY) shl 1
        SUB AX,DeltaY                      
        SHL AX,1                           
        MOV DInc2,AX                       
        MOV AX,0               
        MOV XInc1,AX            ; XInc1 = 0           
        MOV AX,1                
        MOV XInc2,AX            ; XInc2 = 1           
        MOV YInc1,AX            ; YInc1 = 1
        MOV YInc2,AX            ; YInc2 = 1
        JMP Cond2           
                                           
Cond2: ; If (DLX1 > DLX2)   
        MOV AX,DLX1         
        CMP AX,DLX2         
        JG  Proc3       ; SI
        JNG Cond3       ; NO
                            
Proc3:  MOV AX,XInc1            ; XInc1 = -XInc1
        NEG AX              
        MOV XInc1,AX        
        MOV AX,XInc2            ; XInc2 = -XInc2
        NEG AX              
        MOV XInc2,AX        
        JMP Cond3           
                            
Cond3: ; If (DLY1 > DLY2)   
        MOV AX,DLY1         
        CMP AX,DLY2         
        JG  Proc4       ; SI
        JNG Proc5       ; NO
                            
Proc4:  MOV AX,YInc1            ; YInc1 = -YInc1
        NEG AX                                
        MOV YInc1,AX                          
        MOV AX,YInc2            ; YInc2 = -YInc2
        NEG AX              
        MOV YInc2,AX        
        JMP Proc5           
                            
Proc5:  MOV AX,DLX1             ; X = DLX1
        MOV X,AX            
        MOV AX,DLY1             ; Y = DLY1
        MOV Y,AX            
        JMP For             
                            
For:    INC i
        CALL PIXEL          
        MOV AX,D                ; If (D < 0)
        CMP AX,0            
        JL  Proc6       ; SI
        JNL Proc7       ; NO
                            
Proc6:  MOV AX,D                ; D = D + DInc1
        ADD AX,DInc1        
        MOV D,AX            
        MOV AX,X                ; X = X + XInc1
        ADD AX,XInc1        
        MOV X,AX                           
        MOV AX,Y                ; Y = Y + YInc1
        ADD AX,YInc1        
        MOV Y,AX            
        JMP Salto           
                            
Proc7:  MOV AX,D                ; D = D + DInc2
        ADD AX,DInc2        
        MOV D,AX                               
        MOV AX,X                ; X = X + XInc2
        ADD AX,XInc2        
        MOV X,AX            
        MOV AX,Y                ; Y = Y + YInc2
        ADD AX,YInc2        
        MOV Y,AX            
        JMP Salto           
                            
Salto: ; Verifica el estado del For
        ; i = NumPixels?
        MOV AX,i            
        CMP AX,NumPixels    
        JL  For         ; NO
        JGE Sale        ; SI
                              
Sale:   RET                 
                                            
Bresenham ENDP                             
                                           
; Pinta un pixel en pantalla en una posici¢n x,y especificada
Pixel PROC NEAR
        PUSHF       
          PUSH AX BX CX DX ES
          MOV AX,y 
          MOV DX,80 
          MUL DX        ;Multiplica la fila por los 80 bytes de cada linea
          MOV BX,x
          MOV CL,BL      
          SHR BX,1      ;Divide entre 8 bits para obtener byte espec¡fico
          SHR BX,1      ;Como cada pixel esta representado por un bit debe     
          SHR BX,1      ;obtenerse el bit exacto a modificar
          ADD BX,AX     ;Suma para obtener offset completo de la posici¢n
                        ;donde esta el pixel a modificar
          AND CL,7      ;Limpia 3 ultimos bits, residuo de la div entre 
                        ;8 bits
          XOR CL,7      ;Obtiene el complemento       
          MOV AH,1                             
          SHL AH,CL     ;Mascara de bit exacto a modificar, este es el valor
                        ;para CGBit, cuando se realice out
          MOV DX,CGD    ;Direcci¢n donde esta el registro a modificar
          MOV AL,CGBit  ;ID del registro a modificar
          OUT DX,AX     ;Modificaci¢n del registro
          MOV AH,02h    ;Valor para el registro CGMode 
          MOV AL,CGMode ;ID del registro a modificar
          OUT DX,AX     ;Modificaci¢n del registro y situa el modo de
                        ;escritura 2 y de lectura 0
          MOV AX,Video
          MOV ES,AX     ;Inicializa el es con el segmento de video                             
          MOV AL,ES:[BX] ;carga el registro latch
          MOV AL,Color  ;carga nuevo color de pixel
          MOV ES:[BX],AL ;cambia el color pero lo hace de forma distinta
                        ;el modo de escritura 2 toma el valor mascara del 
                        ;CGBit, para saber cual bit debe modificar, y por
                        ;medio de l¢gica, altera el valor del bit en los 4 
                        ;bitplanes para cargar el nuevo color. No modifica 
                        ;directamente el campo de memoria
          MOV AH,0FFh   ;Restablecimiento de los valores default del modo
          MOV AL,CGBit  ;gr fico
          OUT DX,AX             
          MOV AH,00h            
          MOV AL,CGMode         
          OUT DX,AX             
                                
          POP ES DX CX BX AX    
        POPF                    
        RET                     
                                
Pixel ENDP              ; Fin del procedimiento
           
END Inicio                                                 
