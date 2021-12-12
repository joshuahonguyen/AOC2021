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
        
        if y1 == y2:
            xmin = min(x1, x2)
            xmax = max(x1, x2)
            print(xmin, xmax)
            for x in range(xmin, xmax+1):
                vector[y1][x] += 1
        elif x1 == x2:
            ymin = min(y1, y2)
            ymax = max(y1, y2)
            for y in range(ymin, ymax+1):
                vector[y][x1] += 1
        
not_zero = 0
for v in range(len(vector)):
    for point in range(len(vector[v])):
        if vector[v][point] > 1:
            not_zero += 1
print(not_zero)
            

map = open("map.txt", "w")
for v in range(len(vector)):
    map.write(str(vector[v]))
    map.write("\n")
map.close()


