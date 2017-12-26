.begin namespace counterlib

; A single-byte global variable holds the value of the counter:
;
.variable counter 1

; Before this library is used, 
;
.begin init
        XOR     A
        LD      (counter), A
.end init

read:
        LD      A, (counter)
        RET

increment:
        LD      A, (counter)
        INC     A
        LD      (counter), A
        RET

.end namespace counterlib
