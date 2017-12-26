#define firstValue      3
#define secondValue     4
#define thirdValue      5
#define expectedSum     firstValue + secondValue + thirdValue

main:
        PUSH    BC                      ;
        PUSH    DE                      ;
        PUSH    HL                      ;
        LD      HL, firstValue          ; load values into registers
        LD      DE, secondValue         ;
        LD      BC, thirdValue          ;
        LD      (first), HL             ; load registers into variables
        LD      (second), DE            ;
        LD      (third), BC             ;
        LD      HL, (first)             ; load variables into registers
        LD      DE, (second)            ;
        LD      BC, (third)             ;
        ADD     HL, DE                  ; compute sum
        ADD     HL, BC                  ;
        POP     HL                      ;
        POP     DE                      ;
        POP     BC                      ;
        RET                             ;

; VARIABLES

#define first 8478h
#define second 847Ah
#define third 847Ch

sumtest_string:
        .db "Hello!", 0
