import time
import pyautogui
import pygetwindow as gw
import cv2
import collections
import pickle

from threading import Thread

import win32gui
import win32api

import gui.guihelper as gh
import gui.menu as menu
import gui.playview as pv
import gui.stats as stats

import game.terrains as t
import game.tile_params as tp
import game.maputils as mu


import core.bot_brain as bb
import core.camera as cc

import helpers.color_grabber as cg
import helpers.navigator as navi

from PIL import Image
import pytesseract

Box = collections.namedtuple('Box', 'left top width height')
pyautogui.PAUSE = 0.05
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class Bot:
    def pause_game(self):
        pyautogui.hotkey('alt', 'p')

    def build_city(self, window):
        ##make setup
        hill_bar = pyautogui.locateOnScreen('images/hill_bar.png', region=(0,0, window.width, window.height))
        make_btn = pyautogui.locateOnScreen('images/make_button.png', region=(0,0, window.width, window.height), confidence=0.85)
        build_done_btn = pyautogui.locateOnScreen('images/done_button.png', region=(0,0, window.width, window.height), confidence=0.85)

        pyautogui.moveTo(pyautogui.center(hill_bar))#((hill_bar.left + (hill_bar.width/2)+2), (hill_bar.top + hill_bar.height))
        pyautogui.dragTo(pyautogui.center(hill_bar)[0], (hill_bar.top + hill_bar.height) + 2, 1, button='left') 

        pyautogui.moveTo(pyautogui.center(make_btn))
        pyautogui.click()
        time.sleep(2)

        pyautogui.moveTo(pyautogui.center(build_done_btn))
        pyautogui.click()
        time.sleep(1)

        pyautogui.write('Botcitz', interval=0.25)
        build_done_btn2 = pyautogui.locateOnScreen('images/done_button2.png', region=(0,0, window.width, window.height))
        pyautogui.moveTo(pyautogui.center(build_done_btn2))
        pyautogui.doubleClick()
        time.sleep(1)

        cancel_np_btn = pyautogui.locateOnScreen('images/cancel_newspaper.png', region=(0,0, window.width, window.height))
        pyautogui.moveTo(pyautogui.center(cancel_np_btn))
        pyautogui.click()

        self.pause_game()

    def full_build(self):
        time.sleep(0.5)
        self.build_city(self.gui.window)

        #move mouse out of the way for menu to be recognized
        current_position = (self.gui.window.width/2, self.gui.window.height/2)
        pyautogui.moveTo(current_position)
        
        self.gui.menu = self.gui.create_menu(self.gui.window)
        self.gui.click_menu(self.gui.menu.zoom_in, 2)

        scroller_vertical = pyautogui.center(self.gui.scrollbar_v)
        scroller_horizontal = pyautogui.center(self.gui.scrollbar_h)

        print("VERTICAL: ", self.gui.scrollbar_v)
        print("HORIZONTAL: ", self.gui.scrollbar_h)

        #pyautogui.moveTo(scroller_vertical)
        #pyautogui.dragTo(scroller_vertical[0], scroller_vertical[1] - 135, 2, button='left')
        #time.sleep(2)

        for i in range (55):
            self.navigator.move_tile("up")
        
        self.navigator.v_cursor = self.navigator.climb_to_zero(self.gui)
        
    def start_on_edge(self):
        self.gui.menu = self.gui.create_menu(self.gui.window)
        self.navigator.v_cursor = self.navigator.climb_to_zero(self.gui) 

    def gui_init(self):
        self.gui.scrollbar_v = Box(left=555, top=138, width=16, height=288)
        self.gui.scrollbar_h = Box(left=91, top=410, width=464, height=16)

    def save_state(self, worldmap, slices):
        to_store = [worldmap, slices]
        f = open('store_2.mem', 'wb')
        pickle.dump(to_store, f)
        f.close()

    def load_state(self):
        f = open('store.mem', 'rb')
        to_load = pickle.load(f)
        self.navigator.world_map = to_load[0]
        self.navigator.map_slices = to_load[1]
        f.close()

    def make_building_zone(self, tile, size):
        for x in range(size):
            for y in range(size):
                print((self.navigator.world_map[tile.x + x][tile.y + y].terrain[0]))
                # uncomment when map updated
                # (self.navigator.world_map[tile.x + x][tile.y + y].occupied) or
                if((self.navigator.world_map[tile.x + x][tile.y + y].terrain[0] != 'G') and
                   (self.navigator.world_map[tile.x + x][tile.y + y].terrain[0] != 'F')):
                    print("Space is occupied or not ground, can't build")
                    return

        self.navigator.move_to_tile(tile.x, tile.y)
        self.gui.click_menu(self.gui.menu.roads)
        
        for x in range(size):
            for y in range(size):
                if (x == 0) or (x == size-1):
                    self.navigator.move_to_tile(tile.x + x, tile.y + y) 
                    pyautogui.moveTo(self.navigator.v_cursor)
                    self.navigator.world_map[tile.x + x][tile.y + y].occupied = True
                    self.navigator.world_map[tile.x + x][tile.y + y].on_top = "ROAD"
                    #next line should be removed after next mapping
                    self.navigator.world_map[tile.x + x][tile.y + y].terrain = "ROAD"
                    pyautogui.click()
                    time.sleep(0.01)
                    if cg.get_pixel_color(self.navigator.v_cursor[0], self.navigator.v_cursor[1]) != tp.ROAD:
                        pyautogui.click()    
                elif (y == 0) or (y == size-1):
                    self.navigator.move_to_tile(tile.x + x, tile.y + y)
                    pyautogui.moveTo(self.navigator.v_cursor)
                    self.navigator.world_map[tile.x + x][tile.y + y].occupied = True
                    self.navigator.world_map[tile.x + x][tile.y + y].on_top = "ROAD"
                    #next line should be removed after next mapping
                    self.navigator.world_map[tile.x + x][tile.y + y].terrain = "ROAD"
                    pyautogui.click()
                    time.sleep(0.01)
                    if cg.get_pixel_color(self.navigator.v_cursor[0], self.navigator.v_cursor[1]) != tp.ROAD:
                        pyautogui.click()    

    def schedule_action(self, action):
        self.actions.append()

    def __init__(self):
        self.brain = bb.Brain()
        self.gui = gh.GUIHelper()
        self.gui_init()
        self.navigator = navi.Navigator(self.gui)
        self.actions = []

def main():
    bot = Bot()
    #only uncomment one of the two cases below to initiate the bot either
    #from somewhere on the edge of a built map or from the build screen
    #bot.full_build()
    bot.start_on_edge()
    ## load existing world_map into memory
    try:
        bot.load_state()
    except FileNotFoundError:
        bot.navigator.create_and_slice_world_map()
        bot.save_state(bot.navigator.world_map, bot.navigator.map_slices)

## USE TO CALIBRATE WHEN DOING START_ON_EDGE
##    bot.navigator.move_to_tile(0,0)
##    while True:
##        win32gui.SetPixel(bot.navigator.i_desktop_window_dc, bot.navigator.v_cursor[0], bot.navigator.v_cursor[1], win32api.RGB(0,255,0))

    bot.make_building_zone(bot.navigator.world_map[2][2], 6)
    bot.make_building_zone(bot.navigator.world_map[40][50], 6)
    bot.make_building_zone(bot.navigator.world_map[100][100], 10)

    bot.save_state(bot.navigator.world_map, bot.navigator.map_slices)
    
    print(bot.navigator.num_build_zones())
    #bot.gui.build_budget_window()
   
def check_budget():
    while True:
        print(pytesseract.image_to_string(pyautogui.screenshot(region=(stats.time_money.top, stats.time_money.left, stats.time_money.width, stats.time_money.height)), lang='eng'))
        time.sleep(10)

if __name__ == "__main__":
    main()
    budget_monitor = Thread(target = check_budget)
    #budget_monitor.start()
    #budget_monitor.daemon = True


