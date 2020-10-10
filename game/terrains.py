from enum import Enum

##class Terrain(Enum):
##    GROUND = (142, 117, 56)
##    GROUNDBORDER = (154, 134, 69)
##    GROUNDSLOPEFRONT = (162, 146, 81)
##    GROUNDSLOPESIDE = (113, 81, 32)
##    GROUNDSLOPEANGLE = (134, 105, 48)
##    GROUNDSLOPEFACE = (170, 158, 93)
##    FOREST = (4, 89, 0)
##    FORESTDARK = (4, 138, 0)
##    FORESTLIGHT = (4, 65, 0)
##    WATER = (32, 36, 255)
##    WATERWAVE = (48, 60, 255)
##    SHORE = (0, 0, 113)
##    OFFMAP = (65, 28, 4)
##    GRAVEL = (142, 142, 142)
##    MENU = (186, 186, 186)
##    MENU_ELEMENT = (101, 101, 101)
##    SCROLLBAR_1 = (158, 158, 158)
##    SCROLLBAR_2 = (73, 73, 73)

class Terrain:
    types = {(142, 117, 56): "GROUND",
                (154, 134, 69): "GROUNDBORDER",
                (162, 146, 81): "GROUNDSLOPEFRONT",
                (170, 158, 93): "GROUNDSLOPEFACE",
                (113, 81, 32): "GROUNDSLOPESIDE",
                (134, 105, 48): "GROUNDDARK",
                (93, 56, 16): "GROUNDSLOPEHIDDEN",
                (121, 93, 40): "GROUNDDARK",
                (105, 69, 24): "FORESTTRUNK",
                (125, 20, 4): "FORESTTRUNK",
                (109, 85, 0): "FOREST",
                (4, 113, 0): "FOREST",
                (4, 166, 0): "FOREST",
                (85, 48, 12): "FOREST",
                (101, 4, 0): "FOREST",
                (4, 89, 0): "FOREST",
                (0, 65, 65): "FOREST",
                (4, 138, 0): "FORESTDARK",
                (4, 65, 0): "FORESTLIGHT",
                (32, 36, 255): "WATER",
                (48, 60, 255): "WATERWAVE",
                (0, 0, 113): "SHORE",
                (65, 28, 4): "OFFMAP",
                (142, 142, 142): "ROAD",
                (186, 186, 186): "MENU",
                (101, 101, 101): "MENU_ELEMENT",
                (158, 158, 158): "SCROLLBAR_1",
                (73, 73, 73): "SCROLLBAR_2",
                (153, 153, 153): "MENU",
                (243, 243, 243): "MENU",
                (255, 255, 255): "WHITE",
                (0, 0, 0): "FOREST (OR BLACK)"}
        
    
    
