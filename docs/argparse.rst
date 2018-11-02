Naval Fate argparse Implementation
==================================

``argparse``:

    * "The argparse module makes it easy to write user-friendly command-line interfaces".
    * Defines what arguments it requires, and argparse will figure out how to parse
      those out of sys.argv. 
    * Automatically generate help message.
    * Automatically generate usage messages.
    * Issue errors when users give the program invalid arguments.


Minimal Example
---------------

* Code:

.. code:: python

    import argparse

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print(args.accumulate(args.integers))


* How it looks like when you run it:

.. code-block:: none

    $ python prog.py 1 2 3 4
    4

    $ python prog.py 1 2 3 4 --sum
    10

* Help message:

.. code-block:: none

    $ python prog.py -h
    usage: prog.py [-h] [--sum] N [N ...]

    Process some integers.

    positional arguments:
     N           an integer for the accumulator

    optional arguments:
     -h, --help  show this help message and exit
     --sum       sum the integers (default: find the max)


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

    import argparse

    from api import ship_new
    from api import ship_move
    from api import ship_shoot
    from api import mine_set
    from api import mine_remove

    # create the top-level parser
    parser = argparse.ArgumentParser(description='Naval Fate')
    subparsers = parser.add_subparsers(dest="subparser_name")

    # create the subparser for the "ship" command
    ship_parser = subparsers.add_parser('ship')
    ship_subparser = ship_parser.add_subparsers(
        dest="subcommand_name")

    # create the subparser for "ship new"
    ship_subparser_new = ship_subparser.add_parser(
        'new', description='Creates a new ship.')
    ship_subparser_new.add_argument(
        'name', nargs='+', help='Name of the ship.')

    # create the subparser for "ship move"
    ship_subparser_move = ship_subparser.add_parser(
        'move', description='Moves ship to the new location X,Y.')
    ship_subparser_move.add_argument(
        'name', type=str, help='Name of the ship.')
    ship_subparser_move.add_argument(
        'x', type=float, help='X coordinate.')
    ship_subparser_move.add_argument(
        'y', type=float, help='Y coordinate.')
    ship_subparser_move.add_argument(
        '--speed', type=float, 
        help='Speed in knots [default: 10].', default=10)

    # create the subparser for "ship shoot"
    ship_subparser_shoot = ship_subparser.add_parser(
        'shoot', description='Makes ship fire to X,Y.')
    ship_subparser_shoot.add_argument(
        'name', type=str, help='Name of the ship.')
    ship_subparser_shoot.add_argument(
        'x', type=float, help='X coordinate.')
    ship_subparser_shoot.add_argument(
        'y', type=float, help='Y coordinate.')

    # create the subparser for the "mine" command
    mine_parser = subparsers.add_parser('mine')
    mine_subparser = mine_parser.add_subparsers(dest="subcommand_name")

    # create the subparser for the "mine set"
    mine_subparser_set = mine_subparser.add_parser('set')
    mine_subparser_set.add_argument(
        'x', type=float, help='X coordinate.')
    mine_subparser_set.add_argument(
        'y', type=float, help='Y coordinate.')

    mine_subparser_set_group = mine_subparser_set.add_mutually_exclusive_group()
    mine_subparser_set_group.add_argument('--moored', action='store_true', default=True, help='Moored (anchored) mine.')
    mine_subparser_set_group.add_argument('--drifting', action='store_true', help='Drifting mine.')

    # create the subparser for the "mine remove"
    mine_subparser_remove = mine_subparser.add_parser('remove')
    mine_subparser_remove.add_argument('x', type=float, help='X coordinate.')
    mine_subparser_remove.add_argument('y', type=float, help='Y coordinate.')


    def cli(cmdargs):
        
        if cmdargs.subparser_name == 'ship' and \ 
           cmdargs.subcommand_name =='new':
            ship_new(names=cmdargs.name)

        elif cmdargs.subparser_name == 'ship' and \
            cmdargs.subcommand_name =='move':
            ship_move(ship=cmdargs.name, 
                      x=cmdargs.x, 
                      y=cmdargs.y, 
                      speed=cmdargs.speed)

        elif cmdargs.subparser_name == 'ship' and \
             cmdargs.subcommand_name =='shoot':
            ship_shoot(ship=cmdargs.name,
                       x=cmdargs.x, 
                       y=cmdargs.y)

        elif cmdargs.subparser_name == 'mine' and \
             cmdargs.subcommand_name =='set':

            if cmdargs.drifting:
                mine_type = 'drifting'
            else:
                mine_type = 'moored'

            mine_set(x=cmdargs.x,
                     y=cmdargs.y,
                     ty=mine_type)

        elif cmdargs.subparser_name == 'mine' and \
             cmdargs.subcommand_name =='remove':
            mine_remove(x=cmdargs.x,
                        y=cmdargs.y)


    if __name__ == '__main__':

        cmdargs = parser.parse_args()
        cli(cmdargs)
