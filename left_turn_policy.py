# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.

ego_dir = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
ego_dir_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[0, 0],
        [0, 0]]

init = [1, 2, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [0, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

width = len(grid[0])
height = len(grid)
act_dim = len(action)
ego_dir_dim = len(ego_dir)

# Dictionary 
#   dist[src_x,src_y,src_ego_face_dir, dst_x,dst_y, dst_ego_face_dir] = [action, distance2destination]
#   (the "action" is a bit confusing. It is only meaningful to direct neighbours.)
dist = {}

# Build the init dictionary based on graph structure
def init(height, width, ego_dir):

    # Source position, ego_dir
    for src_i in range(height):
        for src_j in range(width):

            # Destination position
            for dst_i in range(height):
                for dst_j in range(width):

                    if grid[src_i][src_j]==0 and grid[dst_i][dst_j]==0: 
                        hit = False

                        for idx,val in enumerate(ego_dir): # Direct neighbors
                            if (src_i+val[0],src_j+val[1])==(dst_i,dst_j):
                                hit = True
                                if idx==0: # UP
                                    dist[src_i,src_j, 'up'   , dst_i,dst_j, 'up'] = ['#', 1]
                                    dist[src_i,src_j, 'left' , dst_i,dst_j, 'up'] = ['R', 2]
                                    dist[src_i,src_j, 'down' , dst_i,dst_j, 'up'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'right', dst_i,dst_j, 'up'] = ['L', 20]

                                    dist[src_i,src_j, 'up'   , dst_i,dst_j, 'left'] = ['L', 20]
                                    dist[src_i,src_j, 'left' , dst_i,dst_j, 'left'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'down' , dst_i,dst_j, 'left'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'right', dst_i,dst_j, 'left'] = ['NULL', 'INF']

                                    dist[src_i,src_j, 'up'   , dst_i,dst_j, 'down'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'left' , dst_i,dst_j, 'down'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'down' , dst_i,dst_j, 'down'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'right', dst_i,dst_j, 'down'] = ['NULL', 'INF']

                                    dist[src_i,src_j, 'up'   , dst_i,dst_j, 'right'] = ['R', 2]
                                    dist[src_i,src_j, 'left' , dst_i,dst_j, 'right'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'down' , dst_i,dst_j, 'right'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'right', dst_i,dst_j, 'right'] = ['NULL', 'INF']
                                elif idx==1: # LEFT
                                    dist[src_i,src_j, 'up'   , dst_i,dst_j, 'left'] = ['L', 20]
                                    dist[src_i,src_j, 'left' , dst_i,dst_j, 'left'] = ['#', 1]
                                    dist[src_i,src_j, 'down' , dst_i,dst_j, 'left'] = ['R', 2]
                                    dist[src_i,src_j, 'right', dst_i,dst_j, 'left'] = ['NULL', 'INF']

                                    dist[src_i,src_j, 'up'   , dst_i,dst_j, 'up'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'left' , dst_i,dst_j, 'up'] = ['R', 2]
                                    dist[src_i,src_j, 'down' , dst_i,dst_j, 'up'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'right', dst_i,dst_j, 'up'] = ['NULL', 'INF']

                                    dist[src_i,src_j, 'up'   , dst_i,dst_j, 'down'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'left' , dst_i,dst_j, 'down'] = ['L', 20]
                                    dist[src_i,src_j, 'down' , dst_i,dst_j, 'down'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'right', dst_i,dst_j, 'down'] = ['NULL', 'INF']

                                    dist[src_i,src_j, 'up'   , dst_i,dst_j, 'right'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'left' , dst_i,dst_j, 'right'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'down' , dst_i,dst_j, 'right'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'right', dst_i,dst_j, 'right'] = ['NULL', 'INF']
                                elif idx==2: # DOWN 
                                    dist[src_i,src_j, 'up'   , dst_i,dst_j, 'down'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'left' , dst_i,dst_j, 'down'] = ['L', 20]
                                    dist[src_i,src_j, 'down' , dst_i,dst_j, 'down'] = ['#', 1]
                                    dist[src_i,src_j, 'right', dst_i,dst_j, 'down'] = ['R', 2]

                                    dist[src_i,src_j, 'up'   , dst_i,dst_j, 'up'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'left' , dst_i,dst_j, 'up'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'down' , dst_i,dst_j, 'up'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'right', dst_i,dst_j, 'up'] = ['NULL', 'INF']

                                    dist[src_i,src_j, 'up'   , dst_i,dst_j, 'left'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'left' , dst_i,dst_j, 'left'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'down' , dst_i,dst_j, 'left'] = ['R', 2]
                                    dist[src_i,src_j, 'right', dst_i,dst_j, 'left'] = ['NULL', 'INF']

                                    dist[src_i,src_j, 'up'   , dst_i,dst_j, 'right'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'left' , dst_i,dst_j, 'right'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'down' , dst_i,dst_j, 'right'] = ['L', 20]
                                    dist[src_i,src_j, 'right', dst_i,dst_j, 'right'] = ['NULL', 'INF']
                                elif idx==3: # RIGHT
                                    dist[src_i,src_j, 'up'   , dst_i,dst_j, 'right'] = ['R', 2]
                                    dist[src_i,src_j, 'left' , dst_i,dst_j, 'right'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'down' , dst_i,dst_j, 'right'] = ['L', 20]
                                    dist[src_i,src_j, 'right', dst_i,dst_j, 'right'] = ['#', 1]

                                    dist[src_i,src_j, 'up'   , dst_i,dst_j, 'up'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'left' , dst_i,dst_j, 'up'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'down' , dst_i,dst_j, 'up'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'right', dst_i,dst_j, 'up'] = ['L', 20]

                                    dist[src_i,src_j, 'up'   , dst_i,dst_j, 'left'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'left' , dst_i,dst_j, 'left'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'down' , dst_i,dst_j, 'left'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'right', dst_i,dst_j, 'left'] = ['NULL', 'INF']

                                    dist[src_i,src_j, 'up'   , dst_i,dst_j, 'down'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'left' , dst_i,dst_j, 'down'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'down' , dst_i,dst_j, 'down'] = ['NULL', 'INF']
                                    dist[src_i,src_j, 'right', dst_i,dst_j, 'down'] = ['R', 2]

                        if (src_i,src_j)==(dst_i,dst_j): # Self to self
                            dist[src_i,src_j, 'up'   , dst_i,dst_j, 'up'] = ['NULL', 0]
                            dist[src_i,src_j, 'left' , dst_i,dst_j, 'up'] = ['NULL', 'INF']
                            dist[src_i,src_j, 'down' , dst_i,dst_j, 'up'] = ['NULL', 'INF']
                            dist[src_i,src_j, 'right', dst_i,dst_j, 'up'] = ['NULL', 'INF']

                            dist[src_i,src_j, 'up'   , dst_i,dst_j, 'left'] = ['NULL', 'INF']
                            dist[src_i,src_j, 'left' , dst_i,dst_j, 'left'] = ['NULL', 0]
                            dist[src_i,src_j, 'down' , dst_i,dst_j, 'left'] = ['NULL', 'INF']
                            dist[src_i,src_j, 'right', dst_i,dst_j, 'left'] = ['NULL', 'INF']

                            dist[src_i,src_j, 'up'   , dst_i,dst_j, 'down'] = ['NULL', 'INF']
                            dist[src_i,src_j, 'left' , dst_i,dst_j, 'down'] = ['NULL', 'INF']
                            dist[src_i,src_j, 'down' , dst_i,dst_j, 'down'] = ['NULL', 0]
                            dist[src_i,src_j, 'right', dst_i,dst_j, 'down'] = ['NULL', 'INF']

                            dist[src_i,src_j, 'up'   , dst_i,dst_j, 'right'] = ['NULL', 'INF']
                            dist[src_i,src_j, 'left' , dst_i,dst_j, 'right'] = ['NULL', 'INF']
                            dist[src_i,src_j, 'down' , dst_i,dst_j, 'right'] = ['NULL', 'INF']
                            dist[src_i,src_j, 'right', dst_i,dst_j, 'right'] = ['NULL', 0]

                        elif hit==False: #Not immediate neighbors
                            for src_dir in ego_dir_name:
                                for dst_dir in ego_dir_name:
                                    dist[src_i,src_j,src_dir, dst_i,dst_j,dst_dir ]   = ['NULL', 'INF']

                    else: # Unaccessible cell
                        for src_dir in ego_dir_name:
                            for dst_dir in ego_dir_name:
                                dist[src_i,src_j,src_dir, dst_i,dst_j,dst_dir ]   = ['UNAV', 'INF']

#------------------------
# Floyd-Warshal algorithm
#------------------------
def FW(goal):
    dim = width*height

    dist_new = dist.copy()

    # Intermediate point
    for k in range(dim):
        for ego_dir_k in ego_dir_name: 

            # source
            for i in range(dim):
                for ego_dir_i in ego_dir_name: 
    
                    # destination
                    for j in range(dim):
                        for ego_dir_j in ego_dir_name: 
                            print("k=",int(k/width),k%width,ego_dir_k,"i=",int(i/width),i%width,ego_dir_i,"j=",int(j/width),j%width,ego_dir_j)
                            dist_ij = dist[int(i/width),i%width,ego_dir_i,int(j/width),j%width,ego_dir_j]
                            print("\tdist_ij=",dist_ij)
                            dist_ik = dist[int(i/width),i%width,ego_dir_i,int(k/width),k%width,ego_dir_k]
                            print("\tdist_ik=",dist_ik)
                            #if dist_ik[0]!='NULL' and dist_ik[0]!='UNAV':
                            if dist_ik[0]!='UNAV':
                                dist_kj = dist[int(k/width),k%width,ego_dir_k,int(j/width),j%width,ego_dir_j]
                                print("\tdist_kj=",dist_kj)
                                if dist_ik[1]!='INF' and dist_kj[1]!='INF':
                                    detour_ikj = dist_ik[1]+dist_kj[1]
                                    if dist_ij[1]=='INF' or dist_ij[1]>detour_ikj:
                                        print("\tUpdating ","i=",int(i/width),i%width,"j=",int(j/width),j%width,"ego_dir=",ego_dir_i, "dist_ij=",detour_ikj)
                                        dist[int(i/width),i%width,ego_dir_i,int(j/width),j%width,ego_dir_j][1] = detour_ikj

#    # Debug print
#    dist_from_src((0,0), W, width, height)
#    dist_from_src((2,3), W, width, height)
#    dist_from_src((4,1), W, width, height)

    tmp= [[[' ' for col in range(len(grid[0]))] for row in range(len(grid))] for ego_dir_i in range(ego_dir_dim)]
    for i in range(height):
        for j in range(width):
            for e in range(ego_dir_dim):
                dst_dist_min = dist[i,j,ego_dir_name[e],goal[0],goal[1],'up'][1]
                for dst_e in range(ego_dir_dim):
                    tmp_dist = dist[i,j,ego_dir_name[e],goal[0],goal[1],ego_dir_name[dst_e]][1] 
                    if dst_dist_min=='INF':
                        dst_idst_min = tmp_dist
                    elif tmp_dist!='INF':
                        if tmp_dist < dst_dist_min:
                            dst_idst_min = tmp_dist
                tmp[e][i][j] = dst_dist_min

    return tmp

def optimum_policy2D(grid,init,goal,cost):
    pass
    return policy2D
    
init(height,width,ego_dir)

print("init graph build done:")
# Source position, ego_dir
for src_i in range(height):
    for src_j in range(width):
        for ego_dir_i in ego_dir_name:

            # Destination position
            for dst_i in range(height):
                for dst_j in range(width):
                    for ego_dir_j in ego_dir_name:

                        print(src_i,src_j,ego_dir_i,dst_i,dst_j,ego_dir_j,"\t:",dist[src_i,src_j,ego_dir_i,dst_i,dst_j,ego_dir_j])

tmp=FW(goal)
for e in range(ego_dir_dim):
    print(e,":")
    for i in range(height):
        for j in range(width):
            print(i,j,"\t:", tmp[e][i][j])

print("Updated graph build done:")
# Source position, ego_dir
for src_i in range(height):
    for src_j in range(width):
        for ego_dir_i in ego_dir_name:

            # Destination position
            for dst_i in range(height):
                for dst_j in range(width):
                    for ego_dir_j in ego_dir_name:

                        print(src_i,src_j,ego_dir_i,dst_i,dst_j,ego_dir_j,"\t:",dist[src_i,src_j,ego_dir_i,dst_i,dst_j,ego_dir_j])



## #------------------------
## # Initial (bi-directional) graph weight construction - array representation
## #------------------------
## def init_value(width, height, W):
##     for m in range(height*width):
##         for l in range(height*width):
##             W[m][l]=99
##             (i1,j1) = (int(m/width),m%width) 
##             (i2,j2) = (int(l/width),l%width) 
##             if grid[i1][j1]==0 and grid[i2][j2]==0:
##                 if m==l:
##                     W[m][l]=0
##                 else:
##                     if j1==j2 and (i1==i2+1 or i1==i2-1):
##                         W[m][l]=cost
##                     if i1==i2 and (j1==j2+1 or j1==j2-1):
##                         W[m][l]=cost
##                 
## #--------------
## # Debug print
## #--------------
## def dist_from_src(src, W, width, height):
##     print("Distance from:", src) 
##     idx = src[0]*width+src[1]
##     for i in range(height):
##         print(W[idx][i*width], ",", W[idx][i*width+1], ",", W[idx][i*width+2], ",", W[idx][i*width+3], ",", W[idx][i*width+4],  ",", W[idx][i*width+5])
## 



