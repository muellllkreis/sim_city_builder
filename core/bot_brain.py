class Map:
    def __init__(self, width, height):  
        self.width = width
        self.height = height
        self.terrain = self.create_array('x', self.width, self.height)
        self.coordinates = self.create_array((0,0), self.width, self.height)

    def create_array(self, char, width, height):
        array = [[None for _ in range(width)] for __ in range(height)]
        for column in range(height):
            for row in range (width):
                array[column][row] = char
        return array

    def print_map(self, coordinates=False):
        for column in range(len(self.terrain)):
            for row in range(len(self.terrain[column])):
                if coordinates:
                    print(self.coordinates[column][row], end=" ")
                else:
                    print(self.terrain[column][row][0], end=" ")
            print()

class Brain:
    def __init__(self):
        self.memory = Map(10, 10)
