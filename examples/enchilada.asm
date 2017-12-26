.require platform ti83p-app
.require library terminal

.string greeting "HELLO WORLD!"

.begin main
        CALL    terminal.clear
        CALL    terminal.home
        LD      HL, greeting
        CALL    terminal.print
        CALL    terminal.wait
.end main
