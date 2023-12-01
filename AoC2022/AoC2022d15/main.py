f = open("real.txt")
max_search = 4000000
#check_line = 2000000
#check_line = 10
lines = f.readlines()

sensors = []
beacons = []
for line in lines:
  line = line.strip()
  front, back = line.split(":")
  x_part,y_part = front.split(", ")
  sensor_x = int(x_part.split("=")[-1])
  sensor_y = int(y_part.split("=")[-1])
  x_part,y_part = back.split(", ")
  beacon_x = int(x_part.split("=")[-1])
  beacon_y = int(y_part.split("=")[-1])
  sensors.append((sensor_x,sensor_y))
  beacons.append((beacon_x,beacon_y))

def distance_between(p1,p2):
  x_max = max(p1[0],p2[0])
  x_min = min(p1[0],p2[0])
  y_max = max(p1[1],p2[1])
  y_min = min(p1[1],p2[1])
  x_dist = x_max - x_min
  y_dist = y_max - y_min
  return x_dist + y_dist

def all_points_within_distance(p1,distance):
  points = set()
  for i in range(p1[0]-(distance+1),p1[0]+(distance+1)):
    for j in range(p1[1]-(distance+1),p1[1]+(distance+1)):
      new_point = (i,j)
      if distance_between(p1,new_point) <= distance:
        points.add(new_point)
  return points
      
def impossible_points_along_y(y, sensors, beacons):
  impossible_points = set()
  for i in range(len(sensors)):
    beacon_distance = distance_between(sensors[i],beacons[i])
    for point in all_points_within_distance(sensors[i],beacon_distance):
      if point[1] == y:
        impossible_points.add(point)
  for beacon in beacons:
    if beacon in impossible_points:
      impossible_points.remove(beacon)
  return impossible_points

def is_point_visible(p1,sensors):
  for i in range(len(sensors)):
    sensor_distance = distance_between(sensors[i],beacons[i])
    point_distance = distance_between(p1,sensors[i])
    if point_distance <= sensor_distance:
      return True
  return False

def minimum_visible_x(sensors,beacons):
  min_x = sensors[0][0]
  for i in range(len(sensors)):
    sensor = sensors[i]
    beacon = beacons[i]
    min_vis_x = sensor[0] - distance_between(sensor,beacon)
    min_x = min(min_x,min_vis_x)
  return min_x

def maximum_visible_x(sensors,beacons):
  max_x = sensors[0][0]
  for i in range(len(sensors)):
    sensor = sensors[i]
    beacon = beacons[i]
    max_vis_x = sensor[0] + distance_between(sensor,beacon)
    max_x = max(max_x,max_vis_x)
  return max_x

def potentially_visible_xs(sensors):
  xs = set()
  for i in range(len(sensors)):
    sensor = sensors[i]
    beacon = beacons[i]
    beacon_distance = distance_between(sensor,beacon)
    min_x = sensor[0] - beacon_distance
    max_x = sensor[0] + beacon_distance
    for x in range(min_x,max_x+1):
      xs.add(x)
  return xs

def perimeter(sensor,beacon):
  distance = distance_between(sensor,beacon)
  sx,sy = sensor
  points = set()
  for x in range(distance+1):
    p1 = (sx+x,sy+distance-x)
    p2 = (sx+x,sy-distance+x)
    p3 = (sx-x, sy+distance-x)
    p4 = (sx-x, sy-distance+x)
    points.add(p1)
    points.add(p2)
    points.add(p3)
    points.add(p4)
  return points

def edge_points_at_y(i,sensors,beacons,y):
  sensor = sensors[i]
  sx,sy = sensor
  beacon = beacons[i]
  radius = distance_between(sensor,beacon)
  points = set()
  if y < sy-radius or y > sy+radius:
    return None
  else:
    delta_y = sy-y
    delta_x = radius-abs(delta_y)
    p1 = (sx+delta_x,y)
    p2 = (sx-delta_x,y)
    points.add(p1)
    points.add(p2)
    return points
  
def is_detectable_by_sensor_at_y(point,sensor_index,sensors,beacons,y):
  edge_points = edge_points_at_y(sensor_index,sensors,beacons,y)
  if edge_points:
    point_list = list(edge_points)
    p1 = point_list[0]
    p1x = p1[0]
    if(len(point_list)>1):
      p2 = point_list[1]
      p2x = p2[0]
    else:
      p2x = p1x
    minx = min(p1x,p2x)
    maxx = max(p1x,p2x)
    pointx = point[0]
    return minx <= pointx <= maxx
  return False

def next_x_outside_sensor_at_y(sensor_index,sensors,beacons,y):
  edge_points = edge_points_at_y(sensor_index,sensors,beacons,y)
  point_list = list(edge_points)
  p1 = point_list[0]
  p1x = p1[0]
  if(len(point_list)>1):
    p2 = point_list[1]
    p2x = p2[0]
  else:
    p2x = p1x
  maxx = max(p1x,p2x)
  return maxx+1
  
    
#impossible_points = impossible_points_along_y(check_line,sensors,beacons)
#impossible_count = len(impossible_points)

min_x = minimum_visible_x(sensors,beacons)
max_x = maximum_visible_x(sensors,beacons)

print(min_x)
print(max_x)

impossible_count = 0
"""
for x in range(min_x,max_x+1):
  if x%10000 == 0:
    print(x)
  point = (x,check_line)
  if is_point_visible(point,sensors):
    impossible_count += 1
    if point in beacons:
      impossible_count -= 1
"""

"""
check_xs = potentially_visible_xs(sensors)
print(len(check_xs))
for x in check_xs:
  point = (x,check_line)
  if is_point_visible(point,sensors):
    impossible_count += 1
    if point in beacons:
      impossible_count -= 1
"""

#(len(perimeter(sensors[0],beacons[0])))

#print(sorted(perimeter(sensors[5],beacons[5])))

other_perimeter = set()
"""
for i in range(30):
  points = edge_points_at_y(5,sensors,beacons,i)
  print(points)
"""

#print(next_x_outside_sensor_at_y(5,sensors,beacons,20))

magic_point = None

for y in range(max_search+1):
  x = 0
  while x < max_search+2:
    point = (x,y)
    detectable = False
    for i in range(len(sensors)):
      if is_detectable_by_sensor_at_y(point,i,sensors,beacons,y):
        x = next_x_outside_sensor_at_y(i,sensors,beacons,y)
        detectable = True
        break
      else:
        x += 1
    if not detectable:
      magic_point = point
      print("couldn't detect" + str(point))

px,py = magic_point
magic_number = 4000000*px + py

print("part 2 answer: " + str(magic_number))

print("part 1 answer: " + str(impossible_count))
