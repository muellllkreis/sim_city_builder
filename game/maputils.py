class Tile:
    def __init__(self, x, y, screen_x, screen_y, map_slice_id, terrain):
        self.x = x
        self.y = y
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.map_slice = map_slice_id
        ## TODO: metalayers
        # LAYER 1: TERRAIN
        self.terrain = terrain
        self.occupied = False
        self.on_top = None

    def __str__(self):
        return "Tile | Slice: " + str(self.map_slice) + ", x: " + str(self.x) + ", y: " + str(self.y) + ", screen_x: " + str(self.screen_x) + ", screen_y: " + str(self.screen_y)

class MapSlice:
    def __init__(self, identifier, map_slice, up_from_origin, down_from_origin, left_from_origin, right_from_origin):
            self.id = identifier
            self.position = (up_from_origin, down_from_origin, left_from_origin, right_from_origin)
            self.tiles = map_slice

    def __str__(self):
        return "Slice | Id: " + str(self.id) + ", Moves up: " + str(self.position[0]) + ", Moves down: " + str(self.position[1]) + ", Moves left: " + str(self.position[2]) + ", Moves right: " + str(self.position[3])
