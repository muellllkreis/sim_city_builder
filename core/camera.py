import win32gui
import win32api
import collections
import pyautogui

Box = collections.namedtuple('Box', 'left top width height')

class Camera:
    def __init__(self, window_left, window_top, px_width, px_height, up=0, down=0, left=0, right=0):
        self.viewport = Box(window_left, window_top, px_width, px_height)
        self.view_center = pyautogui.center(self.viewport)
        self.up = up
        self.down = down
        self.left = left
        self.right = right
