#def list_sort(ml):
#    list1=[]
#    list2=[]
#    cnt=0
#    cnt2=0
#    for i in range(len(ml)-1):
#        if  ml[i]<ml[i+1] and i==len(ml)-2 and cnt>=cnt2:
#            cnt+=1
#            cnt2=cnt
#            list2=[]
#            list1.append(ml[i])
#            list1.append(ml[i+1])
#            list2.extend(list1)
#        if ml[i]<ml[i+1] :
#            cnt+=1
#            list1.append(ml[i])
#        if ml[i]>=ml[i+1] and cnt>=cnt2:
#            cnt2=cnt
#            cnt=0
#            list2=[]
#            list1.append(ml[i])
#            list2.extend(list1)
#            list1=[]
#    return list2,ml
#print(list_sort([1,2,3,2,5,6,7,8,2]))
#print(list_sort([1,2,3,4,2,3,4,5,65,345,346,2343,77757,6546547,75757865,7657653868,4,5,6,7,98,566,3243,32423,34223775]))
















def parChecker(symbolString):
    s = []
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.append(symbol)
        else:
            if len (s)==0:
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and len(s)==0:
        return True
    else:
        return False

print(parChecker('()()'))

