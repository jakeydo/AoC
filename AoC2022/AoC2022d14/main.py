from collections import defaultdict

f = open("real.txt")
lines = f.readlines()

grid = defaultdict(lambda: ".")

min_x = 1000
max_x = 0
min_y = 0
max_y = 0

for line in lines:
  pairs = line.strip().split(" -> ")
  #print(pairs)
  xs = []
  ys = []
  for pair in pairs:
    x,y = pair.split(",")
    xs.append(int(x))
    ys.append(int(y))
    min_x = min(min_x,int(x))
    max_x = max(max_x,int(x))
    max_y = max(max_y,int(y))
  for i in range(1,len(xs)):
    x1 = min(xs[i-1],xs[i])
    x2 = max(xs[i-1],xs[i])
    y1 = min(ys[i],ys[i-1])
    y2 = max(ys[i-1],ys[i])
    
    for x in range(x1,x2+1):
      for y in range(y1,y2+1):
        grid[(x,y)] = "#"

#grid[(500,0)] = "+"
max_y += 1
print()
rows=[]
for i in range(max_y+1):
  row = ""
  for j in range(min_x,max_x+1):
    row += grid[(j,i)]
  rows.append(row)

for row in rows:
  print(row)

print("min_x: " + str(min_x))
print("max_x: " + str(max_x))
print("max_y: " + str(max_y))

sand_is_falling = True
sand_escaped = False
current_position = (500,0)

def next_sand_position(grid, current_position):
  x,y = current_position
  if y == max_y:
    return (x,y)
  elif grid[(x,y+1)] == ".":
    return (x,y+1)
  elif grid[(x-1,y+1)] == ".":
    return (x-1,y+1)
  elif grid[(x+1,y+1)] == ".":
    return (x+1,y+1)
  else:
    return (x,y)

while not sand_escaped:
  next_position = next_sand_position(grid,current_position)
  x,y = next_position
  if next_position == (500,0):
    sand_escaped = True
    grid[(500,0)] = "o"
  elif next_position == current_position:
    grid[current_position] = "o"
    current_position = (500,0)
  else:
    current_position = next_position
    min_x = min(x,min_x)
    max_x = max(x,max_x)

print()
rows=[]
for i in range(max_y+1):
  row = ""
  for j in range(min_x,max_x+1):
    row += grid[(j,i)]
  rows.append(row)

for row in rows:
  print(row)

sand_count = 0

for i in range(max_y+1):
  for j in range(min_x,max_x+1):
    if grid[(j,i)] == "o":
      #print((i,j))
      sand_count += 1

print("part 1 answer: " + str(sand_count))