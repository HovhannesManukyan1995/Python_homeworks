#import math
#import random
#import time
#
#
#countries={
#"Japan":"Tokyo",
#"Armenia":"Yerevan",
#"Spain":"Madrid",
#"USA":"Washington",
#"Russia":"Moscow",
#}
#lis=list(countries.items())
#random.shuffle(lis)
#scnt=0
#cnt=0
#timelimit=10
#flag=False
#print('Hello. You have 3 chanses to answer wrong and 10 second to think')
#for i in lis:
#    if scnt==3:
#         break
#    start=time.time()
#    print('What is the capital of: ',i[0]) 
#    ans=input('Enter answer: ')
#    end=time.time()
#    diff=math.floor(end-start)
#    print(diff)
#    if diff<=timelimit:
#        break
#        if ans==i[1].lower():
#           print('Correct')
#           cnt+=1
#        else:
#            scnt+=1
#            print('wrong')
#    else:
#         print('BOOM')
#print('You have ',cnt,'correct and',scnt,'incorect answers')        


#dict 19
#d1={'a':100,'b':200,'c':300}
#d2={'a':200,'b':300,'d':200}
#d3={}
#for k,v in d1.items():
#    if k in d2:
#       d3[k]=d2[k]+v
#    else:
#        d3[k]=v
#    for i,j in d2.items():
#        if i not in d3:
#            d3[i]=j
#print(d3)


#dict23
#list_i=[{'item':'item1','am':400},
#        {'item':'item2','am':300},
#        {'item':'item1','am':750}]
#d1={}
#for i in list_i:
#        if i['item'] not in d1:
#            d1[i['item']]=i['am']
#        else:
#            d1[i['item']]+=i['am']
#print(d1)


#dict30
#items={'item1':24,'item2':55,'item3':45,'item4':60,'item5':56}
#lis=[]
#for k,v in items.items():
#    lis.append(v)
#lis.sort()
#del lis[:-3]
#for i in lis:
#    for k,v in items.items():
#        if v==i:
#            print(k,v)
           

#list5
#lis=['asd','word','wow','1991']
#count=0
#for i in lis:
#    if len(i)>2 and i[0]==i[-1]:
#        count+=1
#print(count)

#list6
#lis=[(2,5),(1,2),(2,3),(4,2),(2,1)]
#lis1=[]
#for i in lis:
#    lis1.append(list(i))
#for i in lis1:
#    i.reverse()
#lis2=sorted(lis1)
#lis3=[]
#for i in lis2:
#    i.reverse()
#    lis3.append(tuple(i))
#print(lis3)





