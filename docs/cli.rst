Naval Fate CLI
==============

.. code-block:: none

    Naval Fate.

    Usage:
        naval_fate.py ship new <name>...
        naval_fate.py ship <name> move <x> <y> [--speed=<kn>]
        naval_fate.py ship <name> shoot <x> <y>
        naval_fate.py mine (set|remove) <x> <y> [--moored|--drifting]
        naval_fate.py -h | --help
        naval_fate.py --version

    Options:
        -h --help     Show this screen.
        --version     Show version.
        --speed=<kn>  Speed in knots [default: 10].
        --moored      Moored (anchored) mine.
        --drifting    Drifting mine.

Conventions
-----------

Commands
~~~~~~~~

* Regular words typycally after program (entry point). 
* Example:
    * ``ship``
    * ``mine``
    * ``move``
    * ``set``
    * ``remove``


Arguments
~~~~~~~~~

* Words starting with "<", ending with ">" and/or UPPER-CASE 
  words are interpreted as positional arguments.
* Example:
    * ``<name>``
    * ``<x>``
    * ``<y>``


Options
~~~~~~~

* Words starting with one or two dashes 
  (with exception of "-", "--" by themselves) are 
  interpreted as short (one-letter) or long options, 
  respectively.
* Example:
    * ``--speed=<kn>``
    * ``--moored``
    * ``--drifting``
    * ``--help`` or ``-h``
    * ``--version``

[optional elements]
~~~~~~~~~~~~~~~~~~~

* Elements (options, arguments, commands) enclosed with square 
  brackets "[ ]" are marked to be *optional*.
* Example:
      * ``[--speed=<kn>]``
      * ``[--moored|--drifting]``


(required elements)
~~~~~~~~~~~~~~~~~~~

* All elements are required by default, if not included 
  in brackets "[ ]". However, sometimes it is necessary to 
  mark elements as required explicitly with parens 
  "( )". For example, when you need to group 
  mutually-exclusive elements.
* Example:
    * ``(set|remove)``

mutually-exclusive | elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Mutually-exclusive elements can be separated with a pipe "|".
* Example:
    * ``(set|remove)``

repeated element...
~~~~~~~~~~~~~~~~~~~

* Use ellipsis "..." to specify that the argument 
  (or group of arguments) to the left could be repeated 
  one or more times.
* Example:
    * ``<name>...``
