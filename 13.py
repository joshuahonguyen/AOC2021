fuel = []
line_str = ""
maxi = 0

with open("1314.txt", "r") as file:
    for line in file.read():
        if line != ",":
            line_str += line
        else:
            fuel.append(int(line_str))
            if int(line_str) > maxi:
                maxi = int(line_str)
            line_str = ""
    fuel.append(int(line_str))

minimum = 9999999
for i in range(1000):
    outcome = 0
    for f in fuel:
        if f >= i:
            outcome += f - i
        else:
            outcome += i - f
    if outcome < minimum:
        minimum = outcome
print(minimum)