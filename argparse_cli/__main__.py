from . import naval_fate


def main():
    cmdargs = naval_fate.parser.parse_args()
    naval_fate.cli(cmdargs)


if __name__ == '__main__':
    main()
