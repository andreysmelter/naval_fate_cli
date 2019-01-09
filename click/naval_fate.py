import click


@click.group()
@click.version_option(version='1.0.0', message='%(version)s')
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
