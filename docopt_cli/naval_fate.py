"""
Naval Fate.

Usage:
  naval_fate.py ship new <name>...
  naval_fate.py ship move <name> <x> <y> [--speed=<kn>]
  naval_fate.py ship shoot <name> <x> <y>
  naval_fate.py mine (set|remove) <x> <y> [--moored|--drifting]
  naval_fate.py -h | --help
  naval_fate.py --version

Options:
  -h, --help    Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.
"""

from .api import ship_new
from .api import ship_move
from .api import ship_shoot
from .api import mine_set
from .api import mine_remove


def cli(cmdargs):
    
    if cmdargs['ship'] and cmdargs['new']:
        ship_new(names=cmdargs['<name>'])

    elif cmdargs['ship'] and cmdargs['move']:
        ship_move(ship=cmdargs['<name>'][0], 
                  x=float(cmdargs['<x>']),
                  y=float(cmdargs['<y>']),
                  speed=float(cmdargs['--speed']))

    elif cmdargs['ship'] and cmdargs['shoot']:
        ship_shoot(ship=cmdargs['<name>'][0],
                   x=float(cmdargs['<x>']),
                   y=float(cmdargs['<y>']))

    elif cmdargs['mine'] and cmdargs['set']:
        if cmdargs['--moored']:
            mine_type = 'moored'
        else:
            mine_type = 'drifting'

        mine_set(x=float(cmdargs['<x>']),
                 y=float(cmdargs['<y>']),
                 ty=mine_type)

    elif cmdargs['mine'] and cmdargs['remove']:
        mine_remove(x=cmdargs['<x>'],
                    y=cmdargs['<y>'])
