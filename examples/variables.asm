.begin namespace vars

.variable counter 1    ; an ordinary one-byte variable named `counter`

.begin variable table  ; 256-byte table in RAM aligned on a 256-byte boundary
.align 256
.size 256
.end table

.end vars
