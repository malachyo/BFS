import random
import pprint

def maze(size, lvl, st):     # define function

  matrix = [[random.randint(0,10) for row in range(size)] for col in range(size)]

  for row in range(len(matrix)):
    for col in range(len(matrix)):
      if matrix[row][col] > lvl:
        matrix[row][col] = "-" #free
      else:
        matrix[row][col] = "|"  # wall
  return matrix




maze = maze(10, 5, [0,0])
pprint.pprint(maze)

# find all edges for node N
def find_edges(matrix, node):
  x,y = node
  edges = []
  length = len(matrix)
  # while a = a:
  for x,y in (x, y+1), (x, y-1), (x+1, y), (x-1,y), (x+1,y-1), (x+1,y+1), (x-1,y-1), (x-1,y+1):
    if 0 <= x < length and 0 <= y < length:
      # check if matrix[x][y] is a free space
      if matrix[x][y] == '-':
        edges.append([x,y])
  return edges




# return open edges for node N

# calling find_edges
print(find_edges(maze, [0,0]))

# row col


def bfs(maze, node):
  queue = [[node]]
  explored = []
  goal = [len(maze)-1, len(maze)-1]
  while queue:
    # FIFO
    path = queue.pop(0)
    node = path[-1]
    # check if we have searched path before
    if node not in explored:
      explored.append(node)
      # layer one connections to node
      edges = find_edges(maze, node)
      for edge in edges:
        new_path = list(path)
        new_path.append(edge)
        queue.append(new_path)
        if edge == goal:
          return new_path
  return ('no path found')
print(bfs(maze, (0,0)))


def dfs(maze, node):
  stack = [[node]]
  explored = []
  goal = [len(maze)-1, len(maze)-1]
  while stack:
    # FIFO
    path = stack.pop()
    node = path[-1]
    # check if we have searched path before
    if node not in explored:
      explored.append(node)
      # layer one connections to node
      edges = find_edges(maze, node)
      for edge in edges:
        new_path = list(path)
        new_path.append(edge)
        stack.append(new_path)
        if edge == goal:
          return new_path
  return ('no path found')
print(dfs(maze, (0,0)))
