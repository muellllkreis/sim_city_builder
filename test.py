import pickle
import game.terrains as t
import game.tile_params as tp
import game.maputils as mu

f = open('store_2.mem', 'rb')
to_load = pickle.load(f)

map_array = to_load[0]
map_slices = to_load[1]

for y in range(120):
    for x in range(120):
        if map_array[x][y] is None:
            print('N', end=" ")
        elif hasattr(map_array[x][y], 'on_top'):
            print('█', end="")
        else:
            if map_array[x][y].terrain[0] is 'W':
                print('░', end="")
            elif map_array[x][y].terrain[0] is 'G':
                print('▓', end="")    
            else:
                print('▒', end="")
    print()
