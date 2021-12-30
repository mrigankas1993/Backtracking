#back tracking solution to detect if path exist between two points in a 2D matrix
matrix = [[1,1,1,1],
          [1,0,1,1],
          [0,0,1,0],
          [1,1,0,1]]
solution = [[] for j in range(4)]
def isvalid(x,y , N, matrix): # x, y are the abscissa and ordinate of the current position
    if x < 0 or y > N - 1 or x > N - 1 or y < 0:
        return False
    if matrix[x][y] == 1:
        return True
    if matrix[x][y] == 0:
        return False
def path_exist(target, matrix , x, y, visited):
    d = x, y
    if d in dicty:
        return
    dicty.append(d)
    if d == target:
        return True
    if isvalid(x , y, len(matrix), matrix) == False:
        return
    if path_exist(target, matrix, x, y + 1,dicty) == True:
        return True
    if path_exist(target, matrix, x + 1, y,dicty) == True:
        return True
    if path_exist(target, matrix, x - 1, y, dicty) == True:
        return True
    if path_exist(target, matrix, x, y - 1, dicty) == True:
        return True
    return False
dicty = []
print(path_exist((3,3), matrix , 0, 0, dicty)) # here we choose the current position x, y as (0,0) coordinate.
    
    
    
    




