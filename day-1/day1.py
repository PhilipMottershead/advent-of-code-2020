f = open("day-1/input.txt", "r")
lines = f.read().splitlines()
res = [int(i) for i in lines]
res.sort()
print(res)

for num in res:
    for numB in res:
        for numC in res:
            if num + numB + numC == 2020:
                print(num * numB * numC)
                break