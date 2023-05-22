import typing as tp

def getPath(maze:list):
    if (maze is None) or (len(maze)==0):
        return None
    
    path = []

    if (getPathSub(maze, len(maze)-1, len(maze[0])-1, path)):
        return path
    
    return None

def getPathSub(maze:list, row:int, col:int, path:list):
    if (col<0) or (row<0) or (maze[row][col]==False):
        return False
    
    isAtOrigin = (row==0) and (col==0)

    if isAtOrigin or getPathSub(maze, row, col-1, path) or getPathSub(maze, row-1, col, path):
        p = [row, col]
        path.append(p)
        return True
    
    return False

if __name__ == "__main__":
    r:int = 3
    c:int = 5

    r_b, c_b = 1, 3

    maze = [[True]*c for j in range(r)]
    maze[r_b][c_b] = False
    print(maze)

    print(getPath(maze=maze))

