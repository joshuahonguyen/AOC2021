def oxy(arr, i):
    z, o = [], []
    if arr == None:
        with open("56.txt", "r") as file:
            for f in file:
                f = f.replace("\n", "")
                if f[i] == "0":
                    z.append(f)
                elif f[i] == "1":
                    o.append(f)
    else:
        for f in arr:
            if f[i] == "0":
                z.append(f)
            elif f[i] == "1":
                o.append(f)
    zero = len(z)
    one = len(o)
    if zero > one:
        keep = z
    if zero <= one:
        keep = o
    return keep

def car(arr, i):
    z, o = [], []
    if arr == None:
        with open("56.txt", "r") as file:
            for f in file:
                f = f.replace("\n", "")
                print(f[i])
                if f[i] == "0":
                    z.append(f)
                elif f[i] == "1":
                    o.append(f)
    else:
        for f in arr:
            if f[i] == "0":
                z.append(f)
            elif f[i] == "1":
                o.append(f)
    zero = len(z)
    one = len(o)
    if zero > one:
        keep = o
    if zero <= one:
        keep = z
    return keep

keep, keep2 = None, None
for i in range(12):
    o = oxy(keep, i)
    keep = o

    c = car(keep2, i)
    keep2 = c

    print(keep2, keep)