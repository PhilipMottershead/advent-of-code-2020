def checkPassword(minChars,maxChars,char,password):
    count = 0
    for i in password:
        if i == char:
            count = count +1

    if count >= int(minChar) and count <= int(maxChar):
        return True
    else:
        return False

def checkPasswordPart2(x,y,char,password):
    if (password[int(x)-1] == char) ^ (password[int(y)-1] == char):
        return True
    else:
        return False
      
f = open("day-2/input.txt", "r")
lines = f.read().splitlines()
part1count = 0
part2count = 0

for line in lines: 
    l = line.split(" ")
    minMax = l[0].split("-")
    minChar = minMax[0]
    maxChar = minMax[1]
    char = l[1].strip(":")
    password = l[2]
    if(checkPassword(minChar,maxChar,char,password)):
        part1count = part1count + 1
    if(checkPasswordPart2(minChar,maxChar,char,password)):
        part2count = part2count + 1

print(part1count)
print(part2count)