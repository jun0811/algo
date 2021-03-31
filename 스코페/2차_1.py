n = int(input())
full_str = input()
part_str = input()
part_str_lth = len(part_str)
j = 0

fail_func = [0] * part_str_lth
for i in range(1,part_str_lth):
    if part_str[i] == part_str[j]:
        j += 1
        fail_func[i] = j
    else:
        if j!=0:
            j = fail_func[j-1]
            if part_str[i]==part_str[j]:
                j+=1
                fail_func[i] = j
fail_func = [0] + fail_func
p = 0
check = 0
check_arr = []
for f in range(len(full_str)):
    if full_str[f] == part_str[p]:
        p+=1
    else:
        if p!=0:
            p = fail_func[p]
            if full_str[f] == part_str[p]:
                p+=1
        else:
            p = fail_func[p]
    if p == part_str_lth:
