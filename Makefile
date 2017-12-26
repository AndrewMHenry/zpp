.PHONY: clean test

clean:
	find -name '*~' -delete
	find -name 'actual.asm' -delete
	find -name 'actual.hex' -delete
	find -name 'expected.hex' -delete

test:
	python3 -m unittest discover
