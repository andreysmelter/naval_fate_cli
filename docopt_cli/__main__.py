import docopt

from . import naval_fate
from . import __version__


def main():
    cmdargs = docopt.docopt(naval_fate.__doc__, version=__version__)
    naval_fate.cli(cmdargs)


if __name__ == '__main__':
    main()
