class Map:  
    def __init__(self, width, height):  
        self.width = width
        self.height = height
        self.array = self.create_array('x', self.width, self.height)

    def create_array(self, char, width, height):
        array = [[None for _ in range(width)] for __ in range(height)]
        for column in range(height):
            for row in range (width):
                array[column][row] = char
        return array

    def print_map(self):
        for column in range(len(self.array)):
            for row in range(len(self.array[column])):
                print(self.array[column][row], end=" ")
            print()

    def diagonals(self, size):
        diagonals = set()
        if(size % 2) is 0:
            size += 1
            print("Adjusted size to ", size)
        if(size >= self.width) or (size >= self.height):
            print("Invalid Dimensions")
            return
        init = int((size/2) + 1)
        j = 0
        for i in range(size):
            for k in range(size):
                if i >= init and j+i == size-1:
                    self.array[i][init - j] = 'D'
                    self.array[i][init + j] = 'D'
                    diagonals.add((i,init - j))
                    diagonals.add((i,init + j))
                    j -= 1
                if i < init and i == j:
                    self.array[i][init - j] = 'D'
                    self.array[i][init + j] = 'D'
                    diagonals.add((i,init - j))
                    diagonals.add((i,init + j))
                    if(i == init-1):
                        j -= 1
                    else:
                        j += 1
        return list(diagonals)

    def split_diagonals(self, diagonals):
        # get start and end points of diagonals
        start_point = diagonals[0]
        end_point = diagonals[-1]
        diagonals.remove(start_point)
        #axis points have half the x value of end point
        axis_points = list(filter(lambda el: (el[0]*2 == end_point[0]), diagonals))
        #get connections
        #first: left path (deprecated: start to axis)
        previous = start_point
        diags = [[start_point],[start_point]]
        step = 1
        for x in range(2):
            for i in range(len(diagonals)):
                if((diagonals[i][0] == step) and (abs(previous[1]-diagonals[i][1]) == 1)):
                   diags[x].append(diagonals[i])
                   previous = diagonals[i]
                   step += 1
            # remove already existing diagonal path from original list
            diagonals = [el for el in diagonals if el not in diags[x]]
            diagonals.append(end_point)
            step = 1
            previous = start_point
        # now we have the left and the right path in one ordered list each
        # these need to be split by the size but the axis has to be in both
        # size of a path == difference between start and axis column + 1
        path_length = abs(start_point[0] - axis_points[0][0]) + 1
        split_diags = [[],[],[],[]]
        # do this 4 times because we know we have exactly 4 paths
        split_diags[0] = diags[0][:path_length]
        split_diags[1] = diags[0][path_length-1:]
        split_diags[2] = diags[1][:path_length]
        split_diags[3] = diags[1][path_length-1:]
        print(split_diags)
                    
gen_map = Map(25, 30)
diagonals = gen_map.diagonals(7)
diagonals.sort()
gen_map.print_map()

print('\n', diagonals)
gen_map.split_diagonals(diagonals)


##print("I:", i, "J:", j, "SIZE-J:", size-j, "I+J:", i+j,
##      "I-J:", i-j, "INIT-J:", init-j, "J-INIT:", j-init,
##      (i >= init and j == size+1)or(i < init and i == j))
