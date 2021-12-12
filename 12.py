from time import sleep

fish = []
day = 0
with open("1112.txt", "r") as file:
    for line in file.read():
        if line != ",":
            fish.append(int(line))

new_fish = []
while day != 256:
    #print(day, fish), segment new list
    for f in range(len(fish)):
        if fish[f] == 0:
            fish[f] = 7
            new_fish.append(8)
        fish[f] -= 1
    if len(new_fish) != 0:
        for f in range(len(new_fish)):
            fish.append(new_fish[f])
    print(day, len(fish))
    day += 1
    

print(len(fish))
    
