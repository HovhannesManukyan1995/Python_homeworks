def smallest_one(a):
    sm=a[0]
    si=0
    for i in range(1,len(a)):
        if a[i]<sm:
            sm=a[i]
            si=i
    return si
def sort_sel(a):
    b=[]
    for i in range(len(a)):
        smol=smallest_one(a)
        b.append(a.pop(smol))
    return b
print(sort_sel([1,8,4,6,3,5]))

