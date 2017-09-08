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
        [0, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
#grid = \
#    [[0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 0, 1, 0],
#     [0, 0, 1, 1, 1, 0],
#     [0, 0, 0, 0, 1, 0]]

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
    frontier = []
    frontier_n_dist = []
    # Visited list
    visited = []
    # position
    pos = init
    # dist
    dist = 0
    # Add starting point to frontier list
    frontier.append(init)
    frontier_n_dist.append([dist,init[0],init[1]])
    
    while(len(frontier)!=0):
        path=[]
        cur = frontier.pop(0)
        cur_n_dist = frontier_n_dist.pop(0)
        if (cur==goal):
            path = cur_n_dist
            print(path)
        else:
            # Add cur to visited list
            visited.append(cur)
            # Increase distance by 1
            dist = cur_n_dist[0] + 1
            # Add all neighbors of cur into frontier list
            for d in delta:
                new_pos = [cur[0] + d[0], cur[1]+d[1]]
                if new_pos[0]>=0 and new_pos[1]>=0 \
                    and new_pos[0]<len(grid) and new_pos[1]<len(grid[0])  \
                    and (not (new_pos in frontier)) \
                    and (not (new_pos in visited)) \
                    and grid[new_pos[0]][new_pos[1]]!=1 :
                    frontier.append(new_pos)
                    frontier_n_dist.append([dist,new_pos[0],new_pos[1]])
                    #print("\tAdding ", new_pos, "into frontier.")
    
        #print("Cur = ", cur, "Frontier = ", frontier)
    
    #print("Failed.")
    path = 'fail'
    print path
    return path

search(grid, init, goal, cost)

