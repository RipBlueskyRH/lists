def matching (words):
    c=0
    list1=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            c=c+1
            list1.append(word)
    print(list1)
    return c
count=matching(["hello", "lvl", "brb", "121"])
print(count)