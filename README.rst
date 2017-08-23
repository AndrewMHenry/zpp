MOTIVATION
==========

``spasm`` is pretty nice, but it doesn't have built-in support for declaring
global variables.  It's easy enough to get around this with ``#define``
edirectives, but a low recursion limit makes this difficult to do cleanly.
Since there doesn't seem to be a portable alternative to ``spasm`` that has
the features I want, my alternatives are

- Roll my own assembler, or

- Write a preprocessor that provides the desired functionality.

This project is an attempt at the latter.

DESIGN
======

The purpose of this project is convenience.  However, the overriding design
goal for the program is *simplicity*: the program should be small, easy to
write, and easy to understand.

In order to get something working quickly, we begin with producing
``spasm``-compatible assembler source.  However, producing portable assembler
source is a tempting future possibility.

EXAMPLE
=======

The following code snippet illustrates the input source ::

  .namespace counter;

  .variable data 1;

  .routine reset;
          XOR     A
          LD      (data), A
  .end reset;

  .routine increment;
          LD      A, (data)
          INC     A
          LD      (data), A
  .end increment;

  .routine decrement;
          LD      A, (data)
          DEC     A
          LD      (data), A
  .end decrement;

  .end counter;

INTRODUCTION
============

``zpp`` is a Z80 assembly language preprocessor.
