# Name: Darshan Sardhara
# Instructor Name: Lauresa
# NSID: WLZ670
# Course Name: CMPT 145
# Student ID: 11355677
# section Number: 01
# Course number: 41442
def SolveMaze(m, s, g):

    row_count = len(m)
    column_count = len(m[0])

    if s == g:
        return True

    if row_count < 0 or row_count >= len(m) or column_count < 0 or column_count >= len(m[0]) or m[row_count][
        column_count] == 1 or m[row_count][column_count] == 'P':
        return False

    m[row_count][column_count] = 'P'

    if SolveMaze(m, (row_count - 1, column_count), g) or \
            SolveMaze(m, (row_count, column_count - 1), g) or \
            SolveMaze(m, (row_count + 1, column_count), g) or \
            SolveMaze(m, (row_count, column_count + 1), g):
        return True

    m[row_count][column_count] = 0
    return False


def read_maze(file):
    maze = []
    with open(file, 'r') as f:
        for line in f:
            row = [int(cell) for cell in line.split()]
            maze.append(row)
    return maze



def display_path(m, s, g):
    path_exists = SolveMaze(m, s, g)
    print(path_exists)
    if path_exists:
        m[g[0]][g[1]] = 'P'
        print("Path from start to goal:")
        for row in m:
            print(" ".join(str(cell) if cell != 'P' else 'p' for cell in row))
    else:
        print("No path found.")


maze = read_maze('Maze1.txt')
start_loc = (0, 3)
goal_loc = (4, 5)

display_path(maze, start_loc, goal_loc)
