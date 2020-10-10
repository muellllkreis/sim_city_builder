    while True:
        win32gui.SetPixel(i_desktop_window_dc, v_cursor[0], v_cursor[1], win32api.RGB(255, 91, 239))


    if not is_left:
        print("NOT LEFT THIS CAN ACTUALLY HAPPEN") 

    #9. center view on tile_center
    pyautogui.moveTo(v_cursor)
    pyautogui.click()
    pyautogui.moveTo(v_cursor[0]+200,v_cursor[1]+200)
    time.sleep(0.05)

    #10. we move up until our tile center has these neighboring pixels:
    #            GROUNDDARK     GROUNDLIGHT
    #GROUNDLIGHT GROUNDLIGHT    tile_center     GROUNDLIGHT
    #                           GROUNDDARK
    #like this we make sure, that we have the correct camera position
    #NOTE: we need to have TWO light tiles on the left otherwise it is not
    #a unique position
    print("Checking camera position...")
    (up_r, up_g, up_b) = cg.get_pixel_color(v_cursor[0], v_cursor[1]-1)
    (down_r, down_g, down_b) = cg.get_pixel_color(v_cursor[0], v_cursor[1]+1)
    (left_r, left_g, left_b) = cg.get_pixel_color(v_cursor[0]-1, v_cursor[1])
    (left_r_1, left_g_1, left_b_1) = cg.get_pixel_color(v_cursor[0]-2, v_cursor[1])
    (left_r_2, left_g_2, left_b_2) = cg.get_pixel_color(v_cursor[0]-1, v_cursor[1]-1)
    (right_r, right_g, right_b) = cg.get_pixel_color(v_cursor[0]+1, v_cursor[1])
    while not (((up_r, up_g, up_b) == GROUNDLIGHT) and
              ((down_r, down_g, down_b) == GROUNDDARK) and
              ((left_r, left_g, left_b) == GROUNDLIGHT) and
              ((left_r_1, left_g_1, left_b_1) == GROUNDLIGHT) and
              ((left_r_2, left_g_2, left_b_2) == GROUNDDARK) and
              ((right_r, right_g, right_b) == GROUNDLIGHT)):
        (up_r, up_g, up_b) = cg.get_pixel_color(v_cursor[0], v_cursor[1]-1)
        (down_r, down_g, down_b) = cg.get_pixel_color(v_cursor[0], v_cursor[1]+1)
        (left_r, left_g, left_b) = cg.get_pixel_color(v_cursor[0]-1, v_cursor[1])
        (left_r_1, left_g_1, left_b_1) = cg.get_pixel_color(v_cursor[0]-2, v_cursor[1])
        (left_r_2, left_g_2, left_b_2) = cg.get_pixel_color(v_cursor[0]-1, v_cursor[1]-1)
        (right_r, right_g, right_b) = cg.get_pixel_color(v_cursor[0]+1, v_cursor[1])
        print(((up_r, up_g, up_b) == GROUNDLIGHT), (up_r, up_g, up_b))
        print(((down_r, down_g, down_b) == GROUNDDARK), (down_r, down_g, down_b))
        print(((left_r, left_g, left_b) == GROUNDLIGHT), (left_r, left_g, left_b))
        print(((left_r_1, left_g_1, left_b_1) == GROUNDLIGHT), (left_r_1, left_g_1, left_b_1))
        print(((left_r_2, left_g_2, left_b_2) == GROUNDDARK), (left_r_2, left_g_2, left_b_2))
        print(((right_r, right_g, right_b) == GROUNDLIGHT), (right_r, right_g, right_b))
        print()
        move_up(1)

    print(((up_r, up_g, up_b) == GROUNDLIGHT), (up_r, up_g, up_b))
    print(((down_r, down_g, down_b) == GROUNDDARK), (down_r, down_g, down_b))
    print(((left_r, left_g, left_b) == GROUNDLIGHT), (left_r, left_g, left_b))
    print(((left_r_1, left_g_1, left_b_1) == GROUNDLIGHT), (left_r_1, left_g_1, left_b_1))
    print(((left_r_2, left_g_2, left_b_2) == GROUNDDARK), (left_r_2, left_g_2, left_b_2))
    print(((right_r, right_g, right_b) == GROUNDLIGHT), (right_r, right_g, right_b))
    print()
    
    #9. center view on tile_center
    pyautogui.moveTo(v_cursor)
    pyautogui.click()

    while True:
        win32gui.SetPixel(i_desktop_window_dc, v_cursor[0], v_cursor[1], win32api.RGB(255,255,0))
        win32gui.SetPixel(i_desktop_window_dc, v_cursor[0]+TILE_WIDTH, v_cursor[1], win32api.RGB(0,255,0))
        win32gui.SetPixel(i_desktop_window_dc, v_cursor[0], v_cursor[1]+TILE_HEIGHT-1, win32api.RGB(0,255,0))
        win32gui.SetPixel(i_desktop_window_dc, v_cursor[0], v_cursor[1]+((TILE_HEIGHT-1)*2), win32api.RGB(0,0,255))
        win32gui.SetPixel(i_desktop_window_dc, v_cursor[0]+round(TILE_WIDTH/2), v_cursor[1]+round(TILE_HEIGHT/2), win32api.RGB(0,255,0))
        win32gui.SetPixel(i_desktop_window_dc, v_cursor[0]-round(TILE_WIDTH/2), v_cursor[1]+round(TILE_HEIGHT/2), win32api.RGB(0,255,0))

def find_top_tile(window, v_cursor):
    (r, g, b) = cg.get_pixel_color(v_cursor[0], v_cursor[1])
    while ((r, g, b) != OFFMAPCOLOR):
        v_cursor = (v_cursor[0], v_cursor[1] - TILE_HEIGHT)
        (r, g, b) = cg.get_pixel_color(v_cursor[0], v_cursor[1])
        win32gui.SetPixel(i_desktop_window_dc, v_cursor[0], v_cursor[1], win32api.RGB(255,255,0))

    while True:
        win32gui.SetPixel(i_desktop_window_dc, v_cursor[0], v_cursor[1], win32api.RGB(255,255,0))
##        win32gui.SetPixel(i_desktop_window_dc, v_cursor[0], v_cursor[1] + TILE_HEIGHT, win32api.RGB(0,255,0))
##        win32gui.SetPixel(i_desktop_window_dc, v_cursor[0], v_cursor[1] + TILE_HEIGHT, win32api.RGB(0,255,0))
##        win32gui.SetPixel(i_desktop_window_dc, v_cursor[0], v_cursor[1] + TILE_HEIGHT, win32api.RGB(0,255,0))
##        win32gui.SetPixel(i_desktop_window_dc, v_cursor[0], v_cursor[1] + TILE_HEIGHT, win32api.RGB(0,255,0))
        win32gui.SetPixel(i_desktop_window_dc, tile_center[0]+TILE_WIDTH, tile_center[1], win32api.RGB(0,255,0))
        win32gui.SetPixel(i_desktop_window_dc, tile_center[0], tile_center[1]+TILE_HEIGHT, win32api.RGB(0,255,0))
        win32gui.SetPixel(i_desktop_window_dc, tile_center[0]+round(TILE_WIDTH/2), tile_center[1]+round(TILE_HEIGHT/2), win32api.RGB(0,255,0))
        win32gui.SetPixel(i_desktop_window_dc, tile_center[0]-round(TILE_WIDTH/2), tile_center[1]+round(TILE_HEIGHT/2), win32api.RGB(0,255,0))

def find_tile_center(window):
    # test for tile detection

    #1. move (virtual) cursor to center of window
    v_cursor = fall_to_ground_border(window, (int(window.width/2), int(window.height/2)))

    #   initalize is_left, is_top (see #5, #6)
    #   also decrement v_cursor[1] because it is now 1 too far
    is_top = False

    #win32gui.SetPixel(i_desktop_window_dc, v_cursor[0], v_cursor[1], win32api.RGB(255,255,255))

    while not is_top:
        (r, g, b) = cg.get_pixel_color(v_cursor[0], v_cursor[1])
        if (((r, g, b) == OFFMAPCOLOR) or ((r, g, b) == WATER)):
            v_cursor = fall_to_ground_border(window, v_cursor)
        
        is_left = True
        #4. found borderpixel candidate, 
        borderpx = v_cursor

        #5. check left and right pixel and decide if it is left or right border elem
        check_px = (v_cursor[0]+1, v_cursor[1])
        (r, g, b) = cg.get_pixel_color(check_px[0], check_px[1])
        if (r, g, b) != BORDERCOLOR:
            is_left = False

        #6. now we have to figure out if we are looking at the top two pixels or
        #   just somewhere at the border. check right and left diagonal pixels if
        #   they also have the border color. the top and bottom ones are the only
        #   border pixels with these neighbors
        if is_left:
            rightpx = (v_cursor[0]+1, v_cursor[1])
            chkpx_br = (rightpx[0]+1, v_cursor[1]+1)
            chkpx_bl = (v_cursor[0]-1, v_cursor[1]+1)
            (rbr, gbr, bbr) = cg.get_pixel_color(chkpx_br[0], chkpx_br[1])
            (rbl, gbl, bbl) = cg.get_pixel_color(chkpx_bl[0], chkpx_bl[1])
            win32gui.SetPixel(i_desktop_window_dc, chkpx_br[0], chkpx_br[1], win32api.RGB(0,0,255))
            win32gui.SetPixel(i_desktop_window_dc, chkpx_bl[0], chkpx_bl[1], win32api.RGB(0,0,255))
            is_top = True if (((rbr, gbr, bbr) == BORDERCOLOR) and ((rbl, gbl, bbl) == BORDERCOLOR)) else False
        else:
            leftpx = (v_cursor[0]-1, v_cursor[1])
            chkpx_bl = (leftpx[0]-1, leftpx[1]+1)
            chkpx_br = (v_cursor[0]+1, v_cursor[1]+1)
            (rbr, gbr, bbr) = cg.get_pixel_color(chkpx_br[0], chkpx_br[1])
            (rbl, gbl, bbl) = cg.get_pixel_color(chkpx_bl[0], chkpx_bl[1])
            win32gui.SetPixel(i_desktop_window_dc, chkpx_br[0], chkpx_br[1], win32api.RGB(0,0,255))
            win32gui.SetPixel(i_desktop_window_dc, chkpx_bl[0], chkpx_bl[1], win32api.RGB(0,0,255))
            is_top = True if (((rbr, gbr, bbr) == BORDERCOLOR) and ((rbl, gbl, bbl) == BORDERCOLOR)) else False

        #7. if_top is true, we are good. if not, we are in trouble
        #   we go top right until we find the top two pixels
        if is_top:
            break

        if not is_left:
            v_cursor = (v_cursor[0]+1, v_cursor[1]-1)
        else:
            v_cursor = (v_cursor[0]+2, v_cursor[1]-1)
  
        #win32gui.SetPixel(i_desktop_window_dc, v_cursor[0], v_cursor[1], win32api.RGB(255,255,0))


    #8. get to the center pixel(s) - there are two center pixels horizontally
    tile_center = (v_cursor[0], v_cursor[1] - round(TILE_HEIGHT/2))
    v_cursor = tile_center

    while True:
        win32gui.SetPixel(i_desktop_window_dc, v_cursor[0], v_cursor[1], win32api.RGB(255,255,0))

    # check backup.py for removed code

    return tile_center

def fall_to_ground_border(window, v_cursor):
    no_ground_down = False
    no_ground_right = False
    count = 0
    start_point = v_cursor
    #2. get color under virtual cursor
    (r, g, b) = cg.get_pixel_color(v_cursor[0], v_cursor[1])
    #3. move it down until it has found the color of a tile border rgb(121, 93, 40)
    while (((r, g, b) != BORDERCOLOR) and (not no_ground_down)):
        win32gui.SetPixel(i_desktop_window_dc, v_cursor[0], v_cursor[1], red)
        v_cursor = (v_cursor[0], v_cursor[1]+1)
        (r, g, b) = cg.get_pixel_color(v_cursor[0], v_cursor[1])
        if ((r, g, b) == BLACK):
            (r1, g1, b1) = cg.get_pixel_color(v_cursor[0]+1, v_cursor[1])
            (r2, g2, b2) = cg.get_pixel_color(v_cursor[0]-1, v_cursor[1])
            no_ground_down = True
            v_cursor = start_point
            count += 1

    while (((r, g, b) != BORDERCOLOR) and no_ground_down and (not no_ground_right)):
        if(count >= 3):
            count = 0
            move_left(10)
            v_cursor = start_point
            no_ground_right = False
            no_ground_down = False
        win32gui.SetPixel(i_desktop_window_dc, v_cursor[0], v_cursor[1], red)
        v_cursor = (v_cursor[0]+1, v_cursor[1])
        (r, g, b) = cg.get_pixel_color(v_cursor[0], v_cursor[1])
        if ((r, g, b) == BLACK):
            (r1, g1, b1) = cg.get_pixel_color(v_cursor[0], v_cursor[1]+1)
            (r2, g2, b2) = cg.get_pixel_color(v_cursor[0], v_cursor[1]-1)
            no_ground_right = True
            v_cursor = start_point
            count += 1

    while (((r, g, b) != BORDERCOLOR) and no_ground_right):
        win32gui.SetPixel(i_desktop_window_dc, v_cursor[0], v_cursor[1], red)
        v_cursor = (v_cursor[0]-1, v_cursor[1])
        (r, g, b) = cg.get_pixel_color(v_cursor[0], v_cursor[1])
        if ((r, g, b) == BLACK):
            (r1, g1, b1) = cg.get_pixel_color(v_cursor[0], v_cursor[1]+1)
            (r2, g2, b2) = cg.get_pixel_color(v_cursor[0], v_cursor[1]-1)
            move_left(10)
            v_cursor = start_point
            no_ground_right = False
            no_ground_down = False

    return v_cursor


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
