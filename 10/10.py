import sys

input = open(sys.argv[1], 'r').read().strip()
grid = [[-1 if n == '.' else int(n) for n in line] for line in input.split('\n')]
width = len(grid)
height = len(grid[0])

trail_heads = []
for i in range(width):
    for j in range(height):
        if grid[i][j] == 0:
            trail_heads.append((i, j))

def search(grid, width, height, i, j):
    if grid[i][j] == 9:
        tops = set()
        tops.add((i, j))
        return tops, 1
    
    tops = set()
    rating = 0
    n = grid[i][j]
    if i > 0 and grid[i-1][j] == n+1:
        new_tops, new_rating = search(grid, width, height, i-1, j)
        tops = tops.union(new_tops) 
        rating += new_rating

    if i < width-1 and grid[i+1][j] == n+1:
        new_tops, new_rating = search(grid, width, height, i+1, j)
        tops = tops.union(new_tops) 
        rating += new_rating

    if j > 0 and grid[i][j-1] == n+1:
        new_tops, new_rating = search(grid, width, height, i, j-1)
        tops = tops.union(new_tops) 
        rating += new_rating

    if j < height-1 and grid[i][j+1] == n+1:
        new_tops, new_rating = search(grid, width, height, i, j+1)
        tops = tops.union(new_tops) 
        rating += new_rating

    return tops, rating

tops = [0]*len(trail_heads)
ratings = [0]*len(trail_heads)
for k in range(len(trail_heads)):
    hi, hj = trail_heads[k]
    t, r = search(grid, width, height, hi, hj)
    tops[k] = len(t)
    ratings[k] = r

score = sum(tops)
print(score)

rating = sum(ratings)
print(rating)

