dict = {"zero":"0","one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7","eight":"8","nine":"9"}
s = "onezerotwothree"
res = ""
tmp = ""

for i in range(len(s)):
    if (s[i].isdigit()):
        res += s[i]
        continue
    tmp += s[i]
    print(tmp)
    try:
        if dict[tmp]:
            res += str(dict[tmp])
            tmp = ""
    except:
        continue
print(res)