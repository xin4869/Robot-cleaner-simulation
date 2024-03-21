class Robot():
    def __init__(self, name):
        self.set_name(name)
        self.world = None
        self.location = None
        self.facing = None
        self.brain = None
        self.destroyed is False
        
    def set_name(self, name):
        if not name:
            self.name = "Incognito"
        else:
            self.name = name

    def get_name(self):
        return self.name
    
    def get_world(self):
        return self.world

    def set_world(self, world, location, facing):
        target_square = world.get_square(location)
        if target_square.is_empty and self.world is None:
            self.world = world
            self.location = location
            self.facing = facing
            return True
        else:
            return False
