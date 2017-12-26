.namespace counter

.variable data 1

.code reset
        ;
        ; Initialize the counter with a value of 0.
        ;
        XOR     A
        LD      (data), A
        RET
.end reset

.code read
        ;
        ; ACC = value of counter.
        ;
        LD      A, (data)
        RET
.end read

.code increment
        ;
        ; Increase the value of the counter by 1.
        ;
        LD      A, (data)
        INC     A
        LD      (data), A
        RET
.end increment

.code decrement
        ;
        ; Decrease the value of the counter by 1.
        ;
        LD      A, (data)
        DEC     A
        LD      (data), A
        RET
.end decrement

.end counter
