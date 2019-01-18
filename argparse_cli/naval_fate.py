import argparse

from .api import ship_new
from .api import ship_move
from .api import ship_shoot
from .api import mine_set
from .api import mine_remove
from . import __version__

# create the top-level parser
parser = argparse.ArgumentParser(description='Naval Fate')
parser.add_argument('--version', action='version', version=__version__)
subparsers = parser.add_subparsers(dest='subparser_name')

# create the subparser for the "ship" command
ship_parser = subparsers.add_parser('ship')
ship_subparser = ship_parser.add_subparsers(dest='subcommand_name')

# create the subparser for "ship new"
ship_subparser_new = ship_subparser.add_parser('new', description='Creates a new ship.')
ship_subparser_new.add_argument('name', nargs='+', help='Name of the ship.')

# create the subparser for "ship move"
ship_subparser_move = ship_subparser.add_parser('move', description='Moves ship to the new location X,Y.')
ship_subparser_move.add_argument('name', type=str, help='Name of the ship.')
ship_subparser_move.add_argument('x', type=float, help='X coordinate.')
ship_subparser_move.add_argument('y', type=float, help='Y coordinate.')
ship_subparser_move.add_argument('--speed', type=float, help='Speed in knots [default: 10].', default=10)

# create the subparser for "ship shoot"
ship_subparser_shoot = ship_subparser.add_parser('shoot', description='Makes ship fire to X,Y.')
ship_subparser_shoot.add_argument('name', type=str, help='Name of the ship.')
ship_subparser_shoot.add_argument('x', type=float, help='X coordinate.')
ship_subparser_shoot.add_argument('y', type=float, help='Y coordinate.')

# create the subparser for the "mine" command
mine_parser = subparsers.add_parser('mine')
mine_subparser = mine_parser.add_subparsers(dest='subcommand_name')

# create the subparser for the "mine set"
mine_subparser_set = mine_subparser.add_parser('set')
mine_subparser_set.add_argument('x', type=float, help='X coordinate.')
mine_subparser_set.add_argument('y', type=float, help='Y coordinate.')

mine_subparser_set_group = mine_subparser_set.add_mutually_exclusive_group()
mine_subparser_set_group.add_argument('--moored', action='store_true', default=True, help='Moored (anchored) mine.')
mine_subparser_set_group.add_argument('--drifting', action='store_true', help='Drifting mine.')

# create the subparser for the "mine remove"
mine_subparser_remove = mine_subparser.add_parser('remove')
mine_subparser_remove.add_argument('x', type=float, help='X coordinate.')
mine_subparser_remove.add_argument('y', type=float, help='Y coordinate.')


def cli(cmdargs):
    
    if cmdargs.subparser_name == 'ship' and cmdargs.subcommand_name =='new':
        ship_new(names=cmdargs.name)

    elif cmdargs.subparser_name == 'ship' and cmdargs.subcommand_name =='move':
        ship_move(ship=cmdargs.name, 
                  x=cmdargs.x, 
                  y=cmdargs.y, 
                  speed=cmdargs.speed)

    elif cmdargs.subparser_name == 'ship' and cmdargs.subcommand_name =='shoot':
        ship_shoot(ship=cmdargs.name,
                   x=cmdargs.x, 
                   y=cmdargs.y)

    elif cmdargs.subparser_name == 'mine' and cmdargs.subcommand_name =='set':

        if cmdargs.drifting:
            mine_type = 'drifting'
        else:
            mine_type = 'moored'

        mine_set(x=cmdargs.x,
                 y=cmdargs.y,
                 ty=mine_type)

    elif cmdargs.subparser_name == 'mine' and cmdargs.subcommand_name =='remove':
        mine_remove(x=cmdargs.x,
                    y=cmdargs.y)


if __name__ == '__main__':

    cmdargs = parser.parse_args()
    cli(cmdargs)