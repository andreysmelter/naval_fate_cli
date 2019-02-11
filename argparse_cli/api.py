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


def mine_remove(x, y, ty):
    """Removes a mine at a specific coordinate."""
    print('Removed {} mine at [{},{}]'.format(ty, x, y))
