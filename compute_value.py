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

grid = [[0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]
width = len(grid[0])
height = len(grid)

#width=3
#height=2

goal = [height-1, width-1]

cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

# Init values array
value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]

# initial W array 
W = [[99 for col in range(width*height)] for row in range(width*height)]
W_new = W.copy()

def init_value(width, height):
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
                

def compute_value():
    W_new = W.copy()
    # Floyd-Warshal algorithm
    for k in range(height*width):
        for i in range(height*width):
            for j in range(height*width):
                detour_W_ij = W[i][k]+W[k][j]
                # Debug
                #if i==0 and j==25:
                #    print("k=", k, ", W[0][25] = ", W[i][j], ", W[0][k]=", W[i][k], ", W[k][j]=", W[k][j])
                if W[i][j]>detour_W_ij:
                    W[i][j] = detour_W_ij

def dist_from_src(src):
    print("Distance from:", src) 
    idx = src[0]*width+src[1]
    for i in range(height):
        print(W_new[idx][i*width], ",", W_new[idx][i*width+1], ",", W_new[idx][i*width+2], ",", W_new[idx][i*width+3], ",", W_new[idx][i*width+4],  ",", W_new[idx][i*width+5])

init_value(width,height)
print("init W:")
for m in range(height*width):
    print(W_new[m])

compute_value()

dist_from_src((0,0))
dist_from_src((2,3))
dist_from_src((4,1))
