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
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
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

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
     [ 0,-1], # go left
     [ 1, 0], # go down
     [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    
    # Frontier list
    frontier_n_dist = []
    # position
    pos = init
    # dist
    dist = 0
    # Add starting point to frontier list
    frontier_n_dist.append([dist,init[0],init[1]])
    
    while(len(frontier_n_dist)!=0):
        path=[]
        # Optional here: sort according to distance before popping.
        #frontier_n_dist = sorted(frontier_n_dist, key=lambda x:x[0])
        cur_dist, x, y = frontier_n_dist.pop(0)
        if (x==goal[0] and y==goal[1]):
            path = cur_dist
            print(path)
            return path
        else:
            # Add cur to visited list
            visited[x,y]=1
            # Increase distance by 1
            dist = cur_dist + 1
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
    
        print("frontier_n_dist= ", frontier_n_dist)
    
    path = 'fail'
    print(path)
    return path

search(grid, init, goal, cost)

