import win32gui
import win32api

import pyautogui

import game.tile_params as tp
import game.terrains as t
import game.maputils as mu

import core.camera as cc

import helpers.color_grabber as cg

class Navigator:
    # finds suitable starting position
    # returns position and bool saying if position contains slopes
    def find_starting_point(self, window, brain, current_position):
        found_starting_point = False
        is_candidate = True
        has_slopes = False
        while not found_starting_point:
            for x in range(brain.memory.height):
                for y in range(brain.memory.width):
                    color = cg.get_pixel_color(pyautogui.position()[0], pyautogui.position()[1])
                    terrain = t.Terrain.types.get(color, ("U", color))
                    print(terrain)
                    if(terrain[0] is 'W'):
                        is_candidate = False
                        break
                    if "SLOPE" in terrain:
                        has_slopes = True
                    brain.memory.terrain[x][y] = terrain
                    brain.memory.coordinates[x][y] = (pyautogui.position()[0], pyautogui.position()[1])
                    pyautogui.moveTo(pyautogui.position()[0] + 10, pyautogui.position()[1])
                if(not is_candidate):
                    current_position = (current_position[0] + 100, current_position[1] + 100)
                    pyautogui.moveTo(current_position)
                    pyautogui.click()
                    current_position = (window.width/2, window.height/2)
                    pyautogui.moveTo(current_position)
                    is_candidate = True
                    break
                pyautogui.moveTo(pyautogui.position()[0] - 100, pyautogui.position()[1] + 10)
            if(x is brain.memory.height-1 and y is brain.memory.width-1):
                found_starting_point = True
                return(current_position, has_slopes)
                print("Found starting point!")

    def climb_to_zero(self, gui):
        v_cursor = (int(self.gui.window.width/2)-150, int(self.gui.window.height/2))
        start_point = v_cursor
        
        (r, g, b) = cg.get_pixel_color(v_cursor[0], v_cursor[1])
        
        while ((r, g, b) == tp.OFFMAPCOLOR or (r,g,b) in tp.TREECOLORS):
            if(r,g,b) in tp.TREECOLORS:
                #if we hit a tree, move to the left a bit to make sure we get away
                v_cursor = (v_cursor[0] - 10, v_cursor[1])
                (r, g, b) = cg.get_pixel_color(v_cursor[0], v_cursor[1])
                continue
            win32gui.SetPixel(self.i_desktop_window_dc, v_cursor[0], v_cursor[1], win32api.RGB(0,255,0))
            v_cursor = (v_cursor[0], v_cursor[1]+1)
            (r, g, b) = cg.get_pixel_color(v_cursor[0], v_cursor[1])

        (rr, gr, br) = cg.get_pixel_color(v_cursor[0]+1, v_cursor[1])
        (rd, gd, bd) = cg.get_pixel_color(v_cursor[0]+1, v_cursor[1]-1)
        while ((rr, gr, br) != tp.OFFMAPCOLOR or (rd, gd, bd) != tp.OFFMAPCOLOR):
            (rr, gr, br) = cg.get_pixel_color(v_cursor[0]+1, v_cursor[1])
            (rd, gd, bd) = cg.get_pixel_color(v_cursor[0]+1, v_cursor[1]-1)
            win32gui.SetPixel(self.i_desktop_window_dc, v_cursor[0], v_cursor[1], win32api.RGB(0,255,0))
            v_cursor = (v_cursor[0]+2, v_cursor[1]-1)

        v_cursor = (v_cursor[0]-3, v_cursor[1]+1)
        tile_center = (v_cursor[0], v_cursor[1] + round(tp.TILE_HEIGHT/2))
        return tile_center

    def move_tile(self, direction):
        if direction == "up":
            self.camera.down -= 1
            pyautogui.moveTo(pyautogui.center(self.gui.scroll_up))
            pyautogui.click()
        elif direction == "down":
            self.camera.down += 1
            pyautogui.moveTo(pyautogui.center(self.gui.scroll_down))
            pyautogui.click()
        elif direction == "right":
            self.camera.left -= 1
            pyautogui.moveTo(pyautogui.center(self.gui.scroll_right))
            pyautogui.click()
        elif direction == "left":
            self.camera.left += 1
            pyautogui.moveTo(pyautogui.center(self.gui.scroll_left))
            pyautogui.click()
        elif direction == "up_right":
            self.camera.down -= 1
            self.camera.left -= 1
            self.move_tile("up")
            self.move_tile("right")
        elif direction == "up_left":
            self.camera.down -= 1
            self.camera.left += 1
            self.move_tile("up")
            self.move_tile("left")
        elif direction == "down_right":
            self.camera.down += 1
            self.camera.left -= 1
            self.move_tile("down")
            self.move_tile("right")
        elif direction == "down_left":
            self.camera.down += 1
            self.camera.left += 1
            self.move_tile("down")
            self.move_tile("left")

    def move_to_tile(self, x, y):
        # 1. find tile in world_map and extract slice
        # 2. if tile is on current slice, skip to 5
        # 3. find slice in map_slices and get its position
        # 4. move destination_pos - current_pos for each direction
        # 5. find screen coordinates from map_slice and put v_cursor there
        dest = self.world_map[x][y]
        mslice = self.map_slices[dest.map_slice-1]

        #check if slice is in camera view
        if (self.camera.down != mslice.position[1]) or (self.camera.left != mslice.position[2]):
            vertical_tiles =  self.camera.down - mslice.position[1]
            horizontal_tiles = self.camera.left - mslice.position[2]
            direction_v = "up" if vertical_tiles > 0 else "down"
            direction_h = "right" if horizontal_tiles > 0 else "left"
            
            for y in range(abs(vertical_tiles)):
                self.move_tile(direction_v)
                    
            for x in range(abs(horizontal_tiles)):
                self.move_tile(direction_h)

        self.v_cursor = (dest.screen_x, dest.screen_y)
        

    def is_build_zone(self, x, y):
        steps = 0
        start_x = x
        start_y = y
        while(self.world_map[x][y].terrain[0] is 'R'):
            self.visited[x][y] = 1
            steps += 1
            x+=1
            if(self.visited[x][y] == 1):
                break
        if(steps < 3):
            return 0
        steps = 0
        x -= 1
        while(self.world_map[x][y].terrain[0] is 'R'):
            self.visited[x][y] = 1
            steps += 1
            y +=1
            if(self.visited[x][y] == 1):
                break
        if(steps < 3):
            return 0
        steps = 0
        y -= 1
        while(self.world_map[x][y].terrain[0] is 'R'):
            self.visited[x][y] = 1
            steps += 1
            x-=1
            if(self.visited[x][y] == 1):
                break
        if(steps < 3):
            return 0
        steps = 0
        x += 1
        while(self.world_map[x][y].terrain[0] is 'R'):
            self.visited[x][y] = 1
            steps += 1
            y -=1
            if(self.visited[x][y] == 1):
                break
        if(steps < 3):
            return 0
        if(start_x != x) or (start_y != y):
            return 0
        return 1

    def num_build_zones(self):
        num_rectangles = 0
        self.visited = [[0 for _ in range(len(self.world_map))] for __ in range(len(self.world_map))]

        for r in range(len(self.world_map)):
            for c in range(len(self.world_map)):
                if self.visited[r][c] == 0 and (self.world_map[r][c] == None or self.world_map[r][c].terrain[0] != 'R'):
                    continue
                num_rectangles += self.is_build_zone(r, c)
        return num_rectangles
        
    def create_and_slice_world_map(self):
        #create big map
        map_size = 130
        map_array = [[None for _ in range(map_size)] for __ in range(map_size)]

        map_slices = []

        #mapslice 8x8 array
        #total mapslices = 8x8/128x128 = 256
        #create mapslice relative to camera position and v_cursor
        #v_cursor should always be in top of map_slice
        slice_size = 10
        slice_distance_v = 4
        slice_distance_h = 5

        slice_number = 0
        for mslice_x in range(12):
            moves_up = 0
            moves_down = 0
            moves_right = 0
            moves_left = 0
            for mslice in range(12):
                print("CAMERA: ", self.camera.down, ",", self.camera.left)
                map_slice_array = [[None for _ in range(slice_size)] for __ in range(slice_size)] 
                map_slice = mu.MapSlice(slice_number, map_slice_array, moves_up, self.camera.down, self.camera.left, moves_right)
                slice_number += 1
                it_cursor = self.v_cursor
                outer_cursor = self.v_cursor
                for x in range(slice_size):
                    for y in range(slice_size):
                        coord_x = (mslice_x * slice_size) + x
                        coord_y = (mslice * slice_size) + y
                        screen_x = it_cursor[0]
                        screen_y = it_cursor[1]
                        color = cg.get_pixel_color(it_cursor[0], it_cursor[1])
                        terrain = t.Terrain.types.get(color, ("U", color))
                        tile = mu.Tile(coord_x, coord_y, screen_x, screen_y, slice_number, terrain)
                        map_array[coord_x][coord_y] = tile
                        print(coord_x, coord_y, " equals ", screen_x, screen_y)
                        map_slice.tiles[x][y] = tile
                        it_cursor = (it_cursor[0] - round(tp.TILE_WIDTH/2), round(it_cursor[1] + tp.TILE_HEIGHT/2))
                    outer_cursor = (outer_cursor[0] + round(tp.TILE_WIDTH/2), round(outer_cursor[1] + tp.TILE_HEIGHT/2))
                    it_cursor = outer_cursor
                print("SLICE INFO: ", mslice, "Moves: ", map_slice.position[1], map_slice.position[2])
                map_slices.append(map_slice)
                
                for y in range(slice_distance_v):
                    self.move_tile("down")
                    
                for x in range(slice_distance_h):
                    self.move_tile("left")

                moves_down += slice_distance_v
                moves_left += slice_distance_h
                #self.camera.down = moves_down
                #self.camera.left = moves_left
            for x in range(moves_left):
                self.move_tile("right")
                    
            for y in range(moves_down):
                self.move_tile("up")

            moves_down = 0
            moves_left = 0
            #self.camera.left = 0
            #self.camera.down = 0

            for y in range(slice_distance_v):
                self.move_tile("down")
                
            for x in range(slice_distance_h):
                self.move_tile("right")

        self.world_map = map_array
        self.map_slices = map_slices


    def __init__(self, gui):
        print("Building navigator..")
        self.i_desktop_window_id = win32gui.GetDesktopWindow()
        self.i_desktop_window_dc = win32gui.GetWindowDC(self.i_desktop_window_id)
        self.gui = gui
        self.camera = cc.Camera(self.gui.scrollbar_h.left, self.gui.scrollbar_v.top + tp.SCROLLBUTTON_SIZE, self.gui.scrollbar_h.width, self.gui.scrollbar_v.height - (tp.SCROLLBUTTON_SIZE*2))
        self.v_cursor = None
        self.world_map = None
        self.map_slices = None
        self.visited = [[0 for _ in range(130)] for __ in range(130)]
        print("Done")

