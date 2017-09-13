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

# Init values array
value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]

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
                
#--------------
# Debug print
#--------------
def dist_from_src(src, W, width, height):
    print("Distance from:", src) 
    idx = src[0]*width+src[1]
    for i in range(height):
        print(W[idx][i*width], ",", W[idx][i*width+1], ",", W[idx][i*width+2], ",", W[idx][i*width+3], ",", W[idx][i*width+4],  ",", W[idx][i*width+5])

#------------------------
# Floyd-Warshal algorithm
#------------------------
def compute_value(grid, goal, cost):
    width = len(grid[0])
    height = len(grid)

    # initial W array 
    W = [[99 for col in range(width*height)] for row in range(width*height)]

    init_value(width, height, W)
    print("init W:")
    for m in range(height*width):
        print(W[m])

    W_new = W.copy()
    for k in range(height*width):
        for i in range(height*width):
            for j in range(height*width):
                detour_W_ij = W[i][k]+W[k][j]
                # Debug
                #if i==0 and j==25:
                #    print("k=", k, ", W[0][25] = ", W[i][j], ", W[0][k]=", W[i][k], ", W[k][j]=", W[k][j])
                if W[i][j]>detour_W_ij:
                    W[i][j] = detour_W_ij

    # Debug print
    dist_from_src((0,0), W, width, height)
    dist_from_src((2,3), W, width, height)
    dist_from_src((4,1), W, width, height)

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

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right
delta_name = ['^', '<', 'v', '>']
#-------------------
# Draw the policy along path
#-------------------
def draw_path(value, goal):
    policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    width = len(value[0])
    height = len(value)

    for i in range(height):
        for j in range(width):
            # Reset min_xx
            min_neighbor_value = 99
            min_direction = 5 
            # Browsing neighbors
            for direction in delta:
                x = i+direction[0]
                y = j+direction[1]
                # if (x,y) within borders
                if x>-1 and x<height and y>-1 and y<width:
                    if value[x][y]<min_neighbor_value:
                        #print("i,j,x,y=", i, j, x, y, "value[x][y] = ", value[x][y])
                        min_neighbor_value = value[x][y]
                        for p in range(len(delta)):
                            if direction==delta[p]:
                                min_direction = p
            # Goal
            if i==goal[0] and j==goal[1]:
                policy[goal[0]][goal[1]] = '*'
            # Post processing
            elif min_direction==5:
                print("Error!!! Invalid default min_direction 5.")
            elif value[i][j]!=99:
                policy[i][j] = delta_name[min_direction]
                #print("policy[",i,"][",j,"]=",policy[i][j])

    return policy

value = compute_value(grid, goal, cost)

print("Distance value to goal at:", goal)
for i in range(len(value)):
    print(value[i])

policy = draw_path(value, goal)
print("Policy map to goal at:", goal)
for i in range(len(policy)):
    print(policy[i])


