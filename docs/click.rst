Naval Fate click Implementation
===============================

``click``:

    * “Command Line Interface Creation Kit”.
    * "Creating beautiful command line interfaces in a composable 
      way with as little code as necessary".
    * Support arbitrary nesting of commands.
    * Automatic help message generation.
    * Support for lazy loading of subcommands at runtime.
    * It’s highly configurable but comes with sensible defaults out of the box.


Minimal Example
---------------

* Code:

.. code:: python

    # hello.py

    import click

    @click.command()
    @click.option('--count', default=1, help='Number of greetings.')
    @click.option('--name', prompt='Your name', help='The person to greet.')
    def hello(count, name):
        """Simple program that greets NAME for a total of COUNT times."""
        for x in range(count):
            click.echo('Hello %s!' % name)

    if __name__ == '__main__':
        hello()

* How it looks like when you run it:

.. code-block:: none

    $ python hello.py --count=3
    Your name: John
    Hello John!
    Hello John!
    Hello John!

* Help message:

.. code-block:: none

    $ python hello.py --help
    Usage: hello.py [OPTIONS]

      Simple program that greets NAME for a total of COUNT times.

    Options:
      --count INTEGER  Number of greetings.
      --name TEXT      The person to greet.
      --help           Show this message and exit.



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

* ``naval_fate.py`` module:

.. code:: python

    # naval_fate.py

    import click


    @click.group()
    @click.version_option()
    def cli():
        """Naval Fate."""


    @cli.group()
    def ship():
        """Manages ships."""


    @ship.command('new')
    @click.argument('name', nargs=-1)
    def ship_new(name):
        """Creates a new ship."""
        for n in name:
            click.echo('Created ship {}'.format(n))


    @ship.command('move')
    @click.argument('ship')
    @click.argument('x', type=float)
    @click.argument('y', type=float)
    @click.option('--speed', metavar='KN', default=10,
                  help='Speed in knots.')
    def ship_move(ship, x, y, speed):
        """Moves SHIP to the new location X,Y."""
        click.echo('Moving ship {} to [{},{}] with speed {}'.format(ship, x, y, speed))


    @ship.command('shoot')
    @click.argument('ship')
    @click.argument('x', type=float)
    @click.argument('y', type=float)
    def ship_shoot(ship, x, y):
        """Makes SHIP fire to X,Y."""
        click.echo('Ship {} fires to [{},{}]'.format(ship, x, y))


    @cli.group('mine')
    def mine():
        """Manages mines."""


    @mine.command('set')
    @click.argument('x', type=float)
    @click.argument('y', type=float)
    @click.option('ty', '--moored', flag_value='moored',
                  default=True,
                  help='Moored (anchored) mine. Default.')
    @click.option('ty', '--drifting', flag_value='drifting',
                  help='Drifting mine.')
    def mine_set(x, y, ty):
        """Sets a mine at a specific coordinate."""
        click.echo('Set {} mine at [{},{}]'.format(ty, x, y))


    @mine.command('remove')
    @click.argument('x', type=float)
    @click.argument('y', type=float)
    def mine_remove(x, y):
        """Removes a mine at a specific coordinate."""
        click.echo('Removed mine at [{},{}]'.format(x, y))


    if __name__ == '__main__':
        cli()
