with open("56.txt", "r") as file:
    i = 0
    zero = [0] * 12
    one = [0] * 12
    for binary in file.readlines():
        i = 0
        for bit in binary:
            if bit == "0":
                zero[i] = zero[i] + 1
            elif bit == "1":
                one[i] = one[i] + 1
            i = i + 1
    
    i = 0
    byte = []
    byte2 = []
    while i < 12:
        if zero[i] > one[i]:
            byte.append(0)
            byte2.append(1)
        else:
            byte.append(1)
            byte2.append(0)
        i = i + 1 
    b1 = int(''.join(str(bit) for bit in byte), 2)
    b2 = int(''.join(str(bit) for bit in byte2), 2)
    print(b1*b2)
    

        