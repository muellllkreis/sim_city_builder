import time
import pyautogui
import pygetwindow as gw
import cv2

import win32gui
import win32api

import gui.menu
import gui.playview as pv

import game.terrains as t

import core.bot_brain as bb

import helpers.color_grabber as cg

# TILE PARAMS
# tile dimensions are:
# - 17 height (including BOTH borders (i.e. 1px each side))
# - 32 width (including half of side borders (i.e. 1px each side)
BORDERCOLOR = (121, 93, 40)
OFFMAPCOLOR = (65, 28, 4)
WATER = (32, 36, 255)
BLACK = (0, 0, 0)
GROUNDLIGHT = (154, 134, 69)
GROUNDDARK = (142, 117, 56)
TILE_HEIGHT = 17
TILE_WIDTH = 32

# DESKTOP SETTINGS
i_desktop_window_id = win32gui.GetDesktopWindow()
i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
red = win32api.RGB(255, 0, 0)

# WINDOW, MENU AND SCROLLBAR
window = None
mn = None
scrollbar = None
scroll_left = None
scroll_right = None
scroll_up = None
scroll_down = None

# finds suitable starting position
# returns position and bool saying if position contains slopes
def find_starting_point(window, brain, current_position):
    found_starting_point = False
    is_candidate = True
    has_slopes = False
    while not found_starting_point:
        for x in range(brain.memory.height):
            for y in range(brain.memory.width):
                color = cg.get_pixel_color(pyautogui.position()[0], pyautogui.position()[1])
                terrain = t.Terrain.types.get(color, ("Unknown: ", color))
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

def climb_to_zero(window):
    v_cursor = (int(window.width/2), int(window.height/2))
    start_point = v_cursor
    
    (r, g, b) = cg.get_pixel_color(v_cursor[0], v_cursor[1])
    
    while ((r, g, b) == OFFMAPCOLOR):
        win32gui.SetPixel(i_desktop_window_dc, v_cursor[0], v_cursor[1], red)
        v_cursor = (v_cursor[0], v_cursor[1]+1)
        (r, g, b) = cg.get_pixel_color(v_cursor[0], v_cursor[1])

    (rr, gr, br) = cg.get_pixel_color(v_cursor[0]+1, v_cursor[1])
    (rd, gd, bd) = cg.get_pixel_color(v_cursor[0]+1, v_cursor[1]-1)
    while ((rr, gr, br) != OFFMAPCOLOR or (rd, gd, bd) != OFFMAPCOLOR):
        (rr, gr, br) = cg.get_pixel_color(v_cursor[0]+1, v_cursor[1])
        (rd, gd, bd) = cg.get_pixel_color(v_cursor[0]+1, v_cursor[1]-1)
        win32gui.SetPixel(i_desktop_window_dc, v_cursor[0], v_cursor[1], red)
        v_cursor = (v_cursor[0]+2, v_cursor[1]-1)

    v_cursor = (v_cursor[0]-3, v_cursor[1]+1)
    tile_center = (v_cursor[0], v_cursor[1] + round(TILE_HEIGHT/2))

    win32gui.SetPixel(i_desktop_window_dc, tile_center[0], tile_center[1], win32api.RGB(0,255,0))
    win32gui.SetPixel(i_desktop_window_dc, tile_center[0]-TILE_WIDTH, tile_center[1]+TILE_HEIGHT, win32api.RGB(0,255,0))
    win32gui.SetPixel(i_desktop_window_dc, tile_center[0]+TILE_WIDTH, tile_center[1]+TILE_HEIGHT, win32api.RGB(0,255,0))
    win32gui.SetPixel(i_desktop_window_dc, tile_center[0], tile_center[1]+TILE_HEIGHT, win32api.RGB(0,255,0))
    win32gui.SetPixel(i_desktop_window_dc, tile_center[0], tile_center[1]+TILE_HEIGHT*2, win32api.RGB(0,255,0)) 
    win32gui.SetPixel(i_desktop_window_dc, tile_center[0]+round(TILE_WIDTH/2), tile_center[1]+round(TILE_HEIGHT/2), win32api.RGB(0,255,0))
    win32gui.SetPixel(i_desktop_window_dc, tile_center[0]-round(TILE_WIDTH/2), tile_center[1]+round(TILE_HEIGHT/2), win32api.RGB(0,255,0))
    win32gui.SetPixel(i_desktop_window_dc, tile_center[0]+round(TILE_WIDTH/2), tile_center[1]+TILE_HEIGHT + round(TILE_HEIGHT/2), win32api.RGB(0,255,0))
    win32gui.SetPixel(i_desktop_window_dc, tile_center[0]-round(TILE_WIDTH/2), tile_center[1]+TILE_HEIGHT + round(TILE_HEIGHT/2), win32api.RGB(0,255,0))

##def move_tile(position, direction):
##    if direction == "up":
##    
##    elif direction == "down":
##
##    elif direction == "right":
##
##    elif direction == "left":

def move_left(presses = 1):
    for i in range(presses):
        pyautogui.press('left')

def move_right(presses = 1):
    for i in range(presses):
        pyautogui.press('right')

def move_up(presses = 1):
    for i in range(presses):
        pyautogui.press('up')

def move_down(presses = 1):
    for i in range(presses):
        pyautogui.press('down')
        
def apply_on_area(window, brain, position, area_x=10, area_y=100):
    pyautogui.moveTo(position)
    pyautogui.mouseDown()
    for x in range(brain.memory.height):
        for y in range(brain.memory.width):
            brain.memory.terrain[x][y] = "GROUND"
            pyautogui.moveTo(pyautogui.position()[0] + 10, pyautogui.position()[1])
        pyautogui.moveTo(pyautogui.position()[0] - 100, pyautogui.position()[1] + 10)
    pyautogui.mouseUp()

def draw_diagonal(brain, size):
    if(size % 2) is 0:
        size += 1
    init = int((size/2) + 1)
    j = 0
    for i in range(size):
        for k in range(size):
            if i >= init and j+i == size-1:
                pyautogui.moveTo(brain.memory.coordinates[i][init - j])
                pyautogui.moveTo(brain.memory.coordinates[i][init + j])
                j -= 1
            if i < init and i == j:
                pyautogui.moveTo(brain.memory.coordinates[i][init - j])
                pyautogui.moveTo(brain.memory.coordinates[i][init + j])
                if(i == init-1):
                    j -= 1
                else:
                    j += 1

def click_menu(menu_item, clicks=1):
    pyautogui.moveTo(menu_item)
    for i in (range(0, clicks)):
        pyautogui.click()

def hold_and_click_menu(menu_item, selection):
    pyautogui.moveTo(menu_item)
    pyautogui.mouseDown()
    time.sleep(0.7)
    for i in (range(1, selection+1)):
        pyautogui.moveTo(menu_item[0], menu_item[1]+(18*i))
    pyautogui.mouseUp()

def create_menu(window):
    #Find and create menu
    before = time.time()
    pyautogui.screenshot('test_screenshot.png', region=(0,0, window.width, window.height))
    print("Took" , time.time() - before, "to take screenshot")
    before = time.time()
    menu_location = pyautogui.locateOnScreen('images/menu.png', region=(0,0, window.width, window.height), confidence=0.8)
    print("Took" , time.time() - before, "to find menu on screen")
    print("Menu is here: ", menu_location)
    mn = menu.Menu(menu_location.left, menu_location.top)
    return mn

def pause_game():
    pyautogui.hotkey('alt', 'p')

def perform_setup():
    #Set Up Window
    window = gw.getWindowsWithTitle('DOSBox 0.73')[0]
    window.moveTo(0,0)
    window.activate()
    return window

def build_city(window):
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

    pause_game()
    
def main():
    brain = bb.Brain()
    window = perform_setup()
## UNCOMMENT THIS AND REMOVE SCROLLER VERTICAL FOR COMPLETE BUILD
##    time.sleep(0.5)
##    scrollbar = pyautogui.locateOnScreen('images/scrollbar.png', region=(0,0, window.width, window.height), confidence=0.8, grayscale=True)
##    build_city(window)
    mn = create_menu(window)

    #Get to starting position (zoom in, check terrain, build road)
    click_menu(mn.zoom_in, 2)

## UNCOMMENT THIS AND REMOVE SCROLLER VERTICAL FOR COMPLETE BUILD
##    current_position = (window.width/2, window.height/2)
##    pyautogui.moveTo(current_position)
##
##    view_center = pyautogui.center(scrollbar)
##    #scroller_vertical = ((scrollbars.left + scrollbars.width - 10), view_center[1])
##    scroller_vertical = pyautogui.center(scrollbar)
##
##    pyautogui.moveTo(scroller_vertical)
##    pyautogui.dragTo(scroller_vertical[0], scroller_vertical[1] - 135, 2, button='left')
##    time.sleep(2)

    scroller_vertical = (561, 282)
    #SCROLLBARS: Box(left=91, top=138, width=480, height=288)
    print("SCROLLER VERTICAL", scroller_vertical)

    v_cursor = climb_to_zero(window)

    print("HERE")

    #hold_and_click_menu(mn.bulldozer, mn.BD_LEVEL)
    
    #brain.memory.print_map()
    #brain.memory.print_map(True)


if __name__ == "__main__":
    main()




