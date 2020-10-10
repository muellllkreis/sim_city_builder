import win32gui
import pyautogui

def get_pixel_color(i_x, i_y):
    i_desktop_window_id = win32gui.GetDesktopWindow()
    i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
    max_x = pyautogui.size()[0]
    max_y = pyautogui.size()[1]
##    colours = []
##    if (i_x == 0 and i_y != 0):
##        colours.append(win32gui.GetPixel(i_desktop_window_dc, i_x+2, i_y+1))
##        colours.append(win32gui.GetPixel(i_desktop_window_dc, i_x+2, i_y-1))
##    elif (i_y == 0 and i_x != 0):
##        colours.append(win32gui.GetPixel(i_desktop_window_dc, i_x-2, i_y+1))
##        colours.append(win32gui.GetPixel(i_desktop_window_dc, i_x+2, i_y+1))
##    elif (i_y == 0 and i_x == 0):
##        colours.append(win32gui.GetPixel(i_desktop_window_dc, i_x+2, i_y+1))
##    elif (i_x == max_x and i_y != 0):
##        colours.append(win32gui.GetPixel(i_desktop_window_dc, i_x-2, i_y-1))
##        colours.append(win32gui.GetPixel(i_desktop_window_dc, i_x-2, i_y+1))
##    elif (i_x == max_x and i_y == 0):
##        colours.append(win32gui.GetPixel(i_desktop_window_dc, i_x-2, i_y-1))
##    elif (i_y == max_y and i_x != 0):
##        colours.append(win32gui.GetPixel(i_desktop_window_dc, i_x-2, i_y-1))
##        colours.append(win32gui.GetPixel(i_desktop_window_dc, i_x+2, i_y-1))
##    elif (i_y == max_y and i_x == 0):
##        colours.append(win32gui.GetPixel(i_desktop_window_dc, i_x+2, i_y-1))
##    elif (i_y == max_y and i_x == max_x):
##        colours.append(win32gui.GetPixel(i_desktop_window_dc, i_x-2, i_y-1))
##    else:
####        colours.append(win32gui.GetPixel(i_desktop_window_dc, i_x-2, i_y+1))
####        colours.append(win32gui.GetPixel(i_desktop_window_dc, i_x+2, i_y+1))
####        colours.append(win32gui.GetPixel(i_desktop_window_dc, i_x-2, i_y-1))
##        colours.append(win32gui.GetPixel(i_desktop_window_dc, i_x+2, i_y-1))
##    i_colour = int(sum(colours)/len(colours))
    i_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
    win32gui.ReleaseDC(i_desktop_window_id,i_desktop_window_dc)
    return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)
