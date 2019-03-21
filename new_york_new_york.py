import sys

lines = sys.stdin.readlines()
i=0
N = lines[i]
i += 1
output = []
while(i < len(lines)):
    no_of_b = int(lines[i])
    i += 1
    if (no_of_b == 0):
        break
    arr = []
    sk = {}
    sum_ov = 0
    for j in range(no_of_b):
        (l,r,h) = lines[i].split(' ')
        i += 1
        l,r,h = int(l), int(r), int(h)
        j = l
        #print("I:", l, r, h)
        while (j < r):
            mh, mr = sk.get(j, (0,0))
            if (mh <= h):
                sk[j] = h, r
                sum_ov += 1
            elif (sk[mr-1][0] == mh):
                j = mr
                continue
            elif (mh > h and mr > r):
                break
            j += 1
    output.append(str(sum_ov))
print("\n".join(output))
