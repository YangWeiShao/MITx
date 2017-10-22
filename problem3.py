s = input()
maxx = 0
index = 0

for i in range(len(s)-1): # iterate over each letter
    count = 0
    for j in range (i, len(s)-1):
        if s[j] <= s[j+1]:
            count += 1
        else:
            break
    if count > maxx:
        index = i
        maxx = count

print(s[index:index+maxx+1])


# pick a letter
# if letter <= right
    # count +1
    # check next letter
# else
    # go to next letter
    # max = count
