import math
import random

elements = [0,1]

maze = [[1,1,1,1,1,1,1,1,1,1],
        [1,2,2,2,2,2,2,2,2,1],
        [1,2,2,2,2,2,2,2,2,1],
        [1,2,2,2,2,2,2,2,2,1],
        [1,2,2,2,2,2,2,2,2,1],
        [1,2,2,2,2,2,2,2,2,1],
        [1,1,1,1,1,1,1,1,1,1]]


def randomize_maze():

    for i in range(7):
        for j in range(10):
            if maze[i][j] == 2:
                r = random.choice(elements)
                maze[i][j] = r


              
def look(pos):
    x = pos[0]
    y = pos[1]
    possible_moves = []

    if (maze[x][y+1] == '<200c>') or (maze[x][y+1] == '$'):
        possible_moves.append((x,y+1))
    if (maze[x][y-1] == '<200c>') or (maze[x][y-1] == '$'):
        possible_moves.append((x,y-1))
    if (maze[x+1][y] == '<200c>') or (maze[x+1][y] == '$'):
        possible_moves.append((x+1,y))
    if (maze[x-1][y] == '<200c>') or (maze[x-1][y] == '$'):
        possible_moves.append((x-1,y))

    if len(possible_moves) == 0:
        maze[x][y] = '-'
        possible_moves = backtrack(pos)

    return possible_moves
  
 

 def backtrack(pos):
    x = pos[0]
    y = pos[1]

    possible_moves = []

    if maze[x][y+1] == '*':
        possible_moves.append((x,y+1))
    if maze[x][y-1] == '*':
        possible_moves.append((x,y-1))
    if maze[x+1][y] == '*':
        possible_moves.append((x+1,y))
    if maze[x-1][y] == '*':
        possible_moves.append((x-1,y))

    return possible_moves
  
 

def distance(possible_moves):

    move_distances = {}

    for move in possible_moves:
        move_distances.update({math.sqrt(abs(((goal[0] - move[0])**2) + ((goal[1] - move[1]) ** 2))):move})

    return move_distances

  
def move(move_distances):

    distances = list(move_distances.keys())
    min_distance = min(distances)

    return move_distances[min_distance]
  
def print_maze(maze, m, n):

    print()

    for i in range(m):
        for j in range(n):
            print(maze[i][j], end = " ")
        print()

    print()
    
    
def decorate_maze():
  for i in range(7):
    for j in range(10):
      if (maze[i][j] == 1):
        maze[i][j] = '▀'
      elif (maze[i][j] == 0):
        maze[i][j] = '<200c>'
        
  maze[goal[0]][goal[1]] = '$'
              
    


print("Enter co-ordinates of start seperated by a comma: ")
print("x bounds: 1-5, y-bounds: 1-8")
x,y = input().split(',')

x = int(x)
y = int(y)

print()

print("Enter co-ordinates of goal seperated by a comma: ")
print("x bounds: 1-5, y-bounds: 1-8")
a,b = input().split(',')

a = int(a)
b = int(b)

start = (x,y)
goal = (a,b)

decorate_maze()

current_position = start

print(f"Start: {start}\nGoal: {goal}")


while (current_position != goal):
    temp = current_position
    maze[temp[0]][temp[1]] = '*'
    print_maze(maze, 7, 10)
    current_position = move(distance(look(current_position)))
