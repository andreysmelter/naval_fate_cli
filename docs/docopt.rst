Naval Fate docopt Implementation
================================

``docopt``:

    * Define the interface for your command-line app.
    * Automatically generate a parser for it.

Minimal Example
---------------

* Code:

.. code:: python

    """
    Usage:
        my_program.py tcp <host> <port> [--timeout=<seconds>]
        my_program.py serial <port> [--baud=9600] [--timeout=<seconds>]
        my_program.py (-h | --help | --version)
    """
    from docopt import docopt

    if __name__ == '__main__':

        print(docopt(__doc__, version='1.0.0'))


* How it looks like when you run it:

.. code-block:: none

    $ python my_program.py tcp 127.0.0.1 443

    {
        "--baud": None,
        "--help": False,
        "--timeout": None,
        "--version": False, 
        "-h": False, 
        "<host>": "127.0.0.1", 
        "<port>": "443", 
        "serial": False, 
        "tcp": True
    }


* Help message:

.. code-block:: none

    $ python my_program.py --help
    Usage:
        my_program.py tcp <host> <port> [--timeout=<seconds>]
        my_program.py serial <port> [--baud=9600] [--timeout=<seconds>]
        my_program.py (-h | --help | --version)


Naval Fate Example
------------------

* Reference CLI:

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


* ``api.py`` module:

.. code:: python

    def ship_new(names):
        """Creates a new ship."""
        for name in names:
            print('Created ship {}'.format(name))


    def ship_move(ship, x, y, speed):
        """Moves SHIP to the new location X,Y."""
        print('Moving ship {} to [{},{}] with speed {} KN'.format(ship, x, y, speed))


    def ship_shoot(ship, x, y):
        """Makes SHIP fire to X,Y."""
        print('Ship {} fires to [{},{}]'.format(ship, x, y))


    def mine_set(x, y, ty):
        """Sets a mine at a specific coordinate."""
        print('Set {} mine at [{},{}]'.format(ty, x, y))


    def mine_remove(x, y):
        """Removes a mine at a specific coordinate."""
        print('Removed mine at [{},{}]'.format(x, y))


* ``naval_fate.py`` module:

.. code:: python

    """
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
    """

    import docopt

    from api import ship_new
    from api import ship_move
    from api import ship_shoot
    from api import mine_set
    from api import mine_remove


    def cli(cmdargs):
        
        if cmdargs['ship'] and cmdargs['new']:
            ship_new(names=cmdargs['<name>'])

        elif cmdargs['ship'] and cmdargs['move']:
            ship_move(ship=cmdargs['<name>'][0], 
                      x=cmdargs['<x>'], 
                      y=cmdargs['<y>'], 
                      speed=cmdargs['--speed'])

        elif cmdargs['ship'] and cmdargs['shoot']:
            ship_shoot(ship=cmdargs['<name>'][0],
                       x=cmdargs['<x>'], 
                       y=cmdargs['<y>'])

        elif cmdargs['mine'] and cmdargs['set']:
            if cmdargs['--moored']:
                mine_type = 'moored'
            else:
                mine_type = 'drifting'

            mine_set(x=cmdargs['<x>'],
                     y=cmdargs['<y>'],
                     ty=mine_type)

        elif cmdargs['mine'] and cmdargs['remove']:
            mine_remove(x=cmdargs['<x>'],
                        y=cmdargs['<y>'])


    if __name__ == '__main__':

        cmdargs = docopt.docopt(__doc__, version='1.0.0')
        cli(cmdargs)