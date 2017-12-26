NAME = sumtest

all: $(NAME)-app.8xk

.PHONY: clean
clean:
	rm -f $(NAME)-app.*
	rm -f $(NAME).asm

$(NAME)-app.8xk: $(NAME).asm
	zapp

$(NAME).asm: $(NAME).zpp
	zpp -o $(NAME).asm $(NAME).zpp
