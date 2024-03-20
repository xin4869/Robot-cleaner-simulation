class Direction():
    north = (0, -1)
    south = (0, 1)
    east = (1, 0)
    west = (-1, 0) 

    direction_list = [north, east, south, west]


    def get_next_clockwise(facing):
        return Direction.direction_list[(Direction.direction_list.index(facing) + 1) % 4]
    
    def get_next_counterclockwise(facing):
        return Direction.direction_list[(Direction.direction_list.index(facing) - 1) % 4]
    
    def get_degrees(direction):
        if direction == Direction.north:
            return 0
        elif direction == Direction.east:
            return 90
        elif direction == Direction.south:
            return 180
        elif direction == Direction.west:
            return 270
        else:
            print("Invalid direction!")

    



        
        