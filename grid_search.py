# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
# 
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left, 
# up, and down motions. Note that the 'v' should be 
# lowercase. '*' should mark the goal cell.
#
# This implements the A* algorithm.
#
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
heuristic = [[9, 8, 7, 6, 5, 4],
        [8, 7, 6, 5, 4, 3],
        [7, 6, 5, 4, 3, 2],
        [6, 5, 4, 3, 2, 1],
        [5, 4, 3, 2, 1, 0]]
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

# path_fwd to record in searching phase
# path records the shortest path when retrieving
path= [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
path_fwd= [[[0,0]  for row in range(len(grid[0]))] for col in range(len(grid))]

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
    frontier_n_dist.append([dist+heuristic[init[0]][init[1]], dist,init[0],init[1]])
    # expand_cnt
    expand_cnt = 0
    # path_fwd
    
    while(len(frontier_n_dist)!=0):

        # Sort according to distance before popping.
        frontier_n_dist = sorted(frontier_n_dist, key=lambda x:x[0])

        # Pop from position 0 - BFS expects FIFO. 
        _, cur_dist, x, y = frontier_n_dist.pop(0)

        expand[x][y]=expand_cnt

        if (x==goal[0] and y==goal[1]):
            # Successfully found the path, retrieve it
            while(not (x==0 and y==0) ):
                #print('cur x,y=', x, y)
                action_d = path_fwd[x][y]
                # We are going in reverse order, reverse the action too
                real_action_d = delta[(delta.index(action_d)+2)%4]
                x = x+real_action_d[0]
                y = y+real_action_d[1]
                # Assign the action
                path[x][y] = delta_name[delta.index(action_d)]

            # patch start/end points
            path[len(grid)-1][len(grid[0])-1] = '*'

            print(expand)
            #print(path_fwd)
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
                    frontier_n_dist.append([dist+heuristic[new_x][new_y],dist,new_x,new_y])
                    #print("\tAdding ", new_pos, "into frontier.")
                    path_fwd[new_x][new_y]=d
        # update expand_cnt
        expand_cnt+=1
    
        print("frontier_n_dist= ", frontier_n_dist)
    
    print(expand)
    print('failed')
    return path

path = search(grid, init, goal, cost)

for i in range(len(path)):
    print(path[i])
