.MODEL Small

.STACK 100h

.DATA
  TiraUNO   DB 'Hola Mundo!', 10, 13, 0
  TiraDOS DB 20 DUP ( 0 )

.586
.CODE

Inicio:
  MOV AX, @DATA
  MOV DS, AX

  MOV SI, OFFSET TiraUNO
  MOV DI, OFFSET TiraDOS

  Ciclo:
    MOV AL, [SI]
    CMP AL, 0      
    JE FinCiclo

    CMP AL, 'a'
    JB MoverApuntadores
    CMP AL, 'z'
    JG MoverApuntadores
      ADD AL, 'A' - 'a'
    MoverApuntadores:
    MOV [DI], AL
    INC SI
    INC DI
  JMP Ciclo
  FinCiclo:

  MOV AX, 4C00h
  INT 21h

END Inicio
 