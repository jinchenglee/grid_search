# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
#grid = \
#    [[0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 0, 1, 0],
#     [0, 0, 1, 1, 1, 0],
#     [0, 0, 0, 0, 1, 0]]

import numpy as np

# visited maintains cells that already searched/visited
# 1 - visited, 0 - not visited yet.
visited = np.zeros_like(grid)

# frontier maintains cells that touched but not done yet
# 1 - done search, 0 - not yet.
frontier = np.zeros_like(grid)

# expand tracks the searching order
expand = np.zeros_like(grid)-1

# path records the shortest path
path= [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
     [ 0,-1], # go left
     [ 1, 0], # go down
     [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    
    # Frontier list
    frontier_n_dist = []
    # position
    pos = init
    # dist
    dist = 0
    # Add starting point to frontier list
    frontier_n_dist.append([dist,init[0],init[1]])
    # expand_cnt
    expand_cnt = 0
    
    while(len(frontier_n_dist)!=0):

        # Sort according to distance before popping.
        frontier_n_dist = sorted(frontier_n_dist, key=lambda x:x[0])

        # Pop from position 0 - BFS expects FIFO. 
        cur_dist, x, y = frontier_n_dist.pop(0)

        expand[x][y]=expand_cnt

        if (x==goal[0] and y==goal[1]):
            # Successfully found the path, retrieve it
            while(not (x==0 and y==0) ):
                dist_min = expand[x][y]
                # Search in neighborhood
                for d in delta:
                    new_x = x+d[0]
                    new_y = y+d[1]
                    # Record the min(expand) in neighbor
                    if new_x>=0 and new_y>=0 \
                    and new_x<len(grid) and new_y<len(grid[0])  \
                    and expand[new_x][new_y]<dist_min \
                    and expand[new_x][new_y]!=-1 :
                        new_x < len(grid) 
                        dist_min = expand[new_x][new_y]
                        min_x = new_x
                        min_y = new_y
                        min_d = d 
                # record path
                for i in range(len(delta)):
                    if delta[i] == min_d:
                        chosen_delta_name = delta_name[(i+2)%4]
                        path[x][y] = chosen_delta_name

                x = min_x
                y = min_y
                # Path for starting point
                path[min_x][min_y] = chosen_delta_name

            # patch end points
            path[len(grid)-1][len(grid[0])-1] = '*'

            #print(expand)
            return path
        else:
            # Add cur to visited list
            visited[x,y]=1
            # Increase distance by 1
            dist = cur_dist + cost 
            # Add all neighbors of cur into frontier list
            for d in delta:
                new_x = x+d[0]
                new_y = y+d[1]
                if new_x>=0 and new_y>=0 \
                    and new_x<len(grid) and new_y<len(grid[0])  \
                    and frontier[new_x][new_y]!=1 \
                    and visited[new_x][new_y]!=1  \
                    and grid[new_x][new_y]!=1 :
                    frontier[new_x][new_y]=1
                    frontier_n_dist.append([dist,new_x,new_y])
                    #print("\tAdding ", new_pos, "into frontier.")
        # update expand_cnt
        expand_cnt+=1
    
        print("frontier_n_dist= ", frontier_n_dist)
    
    #print(expand)
    print('failed')
    return path

path = search(grid, init, goal, cost)

for i in range(len(path)):
    print(path[i])
