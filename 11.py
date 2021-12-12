fish = []
day = 0
with open("1112.txt", "r") as file:
    for line in file.read():
        if line != ",":
            fish.append(int(line))
            
while day != 80:
    print(day, fish)
    for f in range(len(fish)):
        if fish[f] == 0:
            fish[f] = 7
            fish.append(8)
        fish[f] -= 1
    day += 1

print(len(fish))
    
