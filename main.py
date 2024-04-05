from coordinates import Coordinates
from direction import Direction

def main():
    current = Coordinates(0, 0)
    new = current.get_target_coordinates(Direction.east, 2)
    print(new)

    

main()