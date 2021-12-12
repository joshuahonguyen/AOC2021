fuels = []
line_str = ""
maxi = 0

with open("1314.txt", "r") as file:
    for line in file.read():
        if line != ",":
            line_str += line
        else:
            fuels.append(int(line_str))
            if int(line_str) > maxi:
                maxi = int(line_str)
            line_str = ""
    fuels.append(int(line_str))

mimimum = 999999999
for pos in range(1000):
    output = 0
    for fuel in fuels:
        if fuel >= pos:
            for step in range(fuel-pos):
                output += (fuel - pos - step)
        else:
            for step in range(pos-fuel):
                output += (pos - step - fuel)
    if output < mimimum:
        mimimum = output
print(mimimum)