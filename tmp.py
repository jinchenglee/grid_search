# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

goal = [len(grid)-1, len(grid[0])-1]

cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

#------------------------
# Initial (bi-directional) graph weight construction - array representation
#------------------------
def init_value(width, height, W):
    for m in range(height*width):
        for l in range(height*width):
            W[m][l]=99
            (i1,j1) = (int(m/width),m%width) 
            (i2,j2) = (int(l/width),l%width) 
            if grid[i1][j1]==0 and grid[i2][j2]==0:
                if m==l:
                    W[m][l]=0
                else:
                    if j1==j2 and (i1==i2+1 or i1==i2-1):
                        W[m][l]=cost
                    if i1==i2 and (j1==j2+1 or j1==j2-1):
                        W[m][l]=cost
#------------------------
# Floyd-Warshal algorithm
#------------------------
def compute_value(grid, goal, cost):
    width = len(grid[0])
    height = len(grid)

    # initial W array 
    W = [[99 for col in range(width*height)] for row in range(width*height)]

    init_value(width, height, W)

    W_new = W
    for k in range(height*width):
        for i in range(height*width):
            for j in range(height*width):
                detour_W_ij = W[i][k]+W[k][j]
                # Debug
                #if i==0 and j==25:
                #    print("k=", k, ", W[0][25] = ", W[i][j], ", W[0][k]=", W[i][k], ", W[k][j]=", W[k][j])
                if W[i][j]>detour_W_ij:
                    W[i][j] = detour_W_ij

    idx = goal[0]*width + goal[1]
    tmp= [[99 for col in range(len(grid[0]))] for row in range(len(grid))]
    for i in range(height):
        tmp[i][0] = W_new[idx][i*width]
        tmp[i][1] = W_new[idx][i*width+1]
        tmp[i][2] = W_new[idx][i*width+2]
        tmp[i][3] = W_new[idx][i*width+3]
        tmp[i][4] = W_new[idx][i*width+4]
        tmp[i][5] = W_new[idx][i*width+5]

    return tmp

value = compute_value(grid, goal, cost)

for i in range(len(value)):
    print(value[i])


