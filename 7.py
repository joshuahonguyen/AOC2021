from time import sleep
nums = []
with open("78a.txt", "r") as numbers:
    n = ""
    for number in numbers.read():
        if number == "," or number == "\n":
            nums.append(int(n))
            n = ""
        else:
            n += number
        
    b = []
    with open("78b.txt", "r") as bingos:
        for bingo in bingos:
            for bing in bingo:
                if bing == " " or bing == "\n":
                    try:
                        b.append(int(n))
                    except:
                        pass
                    n = ""
                else:
                    n += bing
    
    bo = []
    i = 0
    i2 = 0
    a, c = [], []
    for bingo in b:
        if i == 5:
            c.append(a)
            a = []
            i = 0
        
        if i2 == 25:
            bo.append(c)
            c = []
            i2 = 0

        a.append(bingo)
        i += 1
        i2 += 1
    c.append(a)
    bo.append(c)

    index = 1
    for num in nums:
        for bogo in range(len(bo)):
            print(bogo)
            for bog in range(5):
                for n in range(5):
                    if bo[bogo][bog][n] == num:
                        bo[bogo][bog][n] = "X"
                print(bo[bogo][bog])
        print(index, num)
        input("")
        index+=1

#88 72