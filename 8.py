import random

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

    arr = []
    inv_arr = []
    for i in range(len(bo)):
        arr.append([[None,None,None,None,None],[None,None,None,None,None],[None,None,None,None,None],[None,None,None,None,None],[None,None,None,None,None]])
        inv_arr.append([[None,None,None,None,None],[None,None,None,None,None],[None,None,None,None,None],[None,None,None,None,None],[None,None,None,None,None]])

    x_arr = []
    inv_x_arr = []
    for i in range(len(bo)):
        x_arr.append([None,None,None,None,None])
        inv_x_arr.append([None,None,None,None,None])
    ob = []
    for b in bo:
        arr1 = []
        for h in range(5):
            arr2 = []
            for i in range(5):
                arr2.append(b[i][h])
            arr1.append(arr2)
        ob.append(arr1)

    x = []
    for b in bo:
        arr1 = []
        ass1 = 0

        for h in range(5):
            arr1.append(b[ass1][ass1])
            ass1 += 1
        x.append(arr1)

    x2 = []
    for b in bo:
        arr1 = []
        ass1 = 4

        for h in range(5):
            arr1.append(b[ass1][h])
            ass1 -= 1
        x2.append(arr1)
    index = 1
    bingoes = []
    for num in nums:
        for bogo in range(len(bo)):
            for bog in range(0, 5):      
                for n in range(0, 5):
                    if bo[bogo][bog][n] == num:
                        arr[bogo][bog][n] = num
                        for bi2 in arr[bogo]:
                            if None not in bi2:
                                if bogo not in bingoes:
                                    bingoes.append(bogo)
                                break
        for bogo in range(len(ob)):
            for bog in range(0,5):
                for n in range(0,5):
                    if ob[bogo][bog][n] == num:
                        inv_arr[bogo][bog][n] = num
                        for bi in inv_arr[bogo]:
                            if None not in bi:
                                if bogo not in bingoes:
                                    print(index, inv_arr[bogo])
                                    bingoes.append(bogo)
                                break
        for bogo in range(len(x)):
            for bog in range(0,5):
                if x[bogo][bog] == num:
                    x_arr[bogo][bog] = num
                    if None not in x_arr[bogo]:
                        if bogo not in bingoes:
                            bingoes.append(bogo)
                        break
        for bogo in range(len(x2)):
            for bog in range(0,5):
                if x2[bogo][bog] == num:
                    inv_x_arr[bogo][bog] = num
                    if None not in inv_x_arr[bogo]:
                        if bogo not in bingoes:
                            print(index, inv_x_arr[bogo])
                            bingoes.append(bogo)
                        break
        print(num, index, bingoes, len(bingoes))
        if len(bingoes) == 100:
            break
        input("")
        index += 1
