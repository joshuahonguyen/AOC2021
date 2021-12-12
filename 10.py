vector = []
for i in range(1000):
    v = []
    for j in range(1000):
        v.append(0)
    vector.append(v)

with open("910.txt", "r") as location:
    for loc in location:
        x1, y1 = 0, 0
        x2, y2 = 0, 0

        loc = loc.replace("\n", "")
        nums = loc.split(" -> ")

        x1 = int(nums[0].split(",")[0])
        x2 = int(nums[1].split(",")[0])
        y1 = int(nums[0].split(",")[1])
        y2 = int(nums[1].split(",")[1])
        
        xmin = min(x1, x2)
        xmax = max(x1, x2)
        ymin = min(y1, y2)
        ymax = max(y1, y2)
        
        if y1 == y2 and x1 != x2:
            xmin = min(x1, x2)
            xmax = max(x1, x2)
            for x in range(xmin, xmax+1):
                vector[y1][x] += 1
        elif x1 == x2 and y1 != y2:
            ymin = min(y1, y2)
            ymax = max(y1, y2)
            for y in range(ymin, ymax+1):
                vector[y][x1] += 1
        else:
            dx = 1 if x2 >= x1 else -1
            dy = 1 if y2 >= y1 else -1
            y = y1
            for x in range(x1, x2+dx, dx):
                vector[y][x] += 1
                y += dy

not_zero = 0
for v in range(len(vector)):
    for point in range(len(vector[v])):
        if vector[v][point] >= 2:
            not_zero += 1
        elif vector[v][point] == 0:
            vector[v][point] = "."
print(not_zero)
            

map = open("map.txt", "w")
for v in range(len(vector)):
    map.write(str(vector[v]).replace("'", "").replace(", ", "").replace("[", "").replace("]", ""))
    map.write("\n")
map.close()


