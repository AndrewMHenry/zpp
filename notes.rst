Profiles
========

..
   In order to define addresses for global variables, ``zpp`` must know
   the location of at least one area of RAM.  Since hard-coding this location
   would be inflexible, we have two options:

   - Require (or at least allow) the source file to define this location.

   - Extend ``zpp`` to



We plan to implement *profiles*, which provide platform-specific
information necessary for ``zpp`` to function.  For example, a profile
may specify locations of free RAM areas, which can be used for allocating
global variables.  In order to support the possibility of processing
a single program against multiple profiles, we allow the profile to
be selected on the command line.  Although it is likely that we will
eventually implement each profile in a particular file, we require only
the identifier for the profile as the argument to maintain flexibility.

For example, the following command might process a "Hello World" program
against a profile designed for TI-83 Plus applications: ::

  zpp --profile ti83papp -o hello.asm hello.zpp
