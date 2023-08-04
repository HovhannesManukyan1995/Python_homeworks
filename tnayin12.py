#1
#def plus_num(*args):
#    a=0
#    for i in args:
#        if type(i)==int:
#            a+=i
#        else:
#            continue
#    return a
#print(plus_num(1,4,'sdfs',5,'sdf'))
#2
#def plus_str(*args):
#    a=0
#    for i in args:
#        if type(i)==str:
#            a+=1
#        else:
#            continue
#    return a
#print(plus_str(1,4,'sdfs',5,'sdf'))
#3
#def mijin_tv(*args):
#    a=0
#    b=0
#    for i in args:
#        if type(i)==int:
#            a+=i
#            b+=1
#    return a // b
#print(mijin_tv(2,4,56,234,'dfg'))
#4
#def calculator(a,b):
#        plus=a+b
#        bazm=a*b
#        if a>b:
#            minus=a-b
#            baj=a//b
#        else:
#            minus=b-a
#            baj=b//a
#        return plus,bazm,minus,baj
#print(calculator(6,18))
#5
#def upper_str(a):
#    b=''
#    for i in a:
#        if 122>=ord(i)>97:
#            b+=chr(ord(i)-32)
#        else:
#            b+=i
#    return b
#print(upper_str('sfsfsDDF'))
#
#
#6
#def lower_str(a):
#    b=''
#    for i in a:
#        if 90>=ord(i)>65:
#            b+=chr(ord(i)+32)
#        else:
#            b+=i
#    return b
#print(lower_str('sfsfsDDF'))
#7
#def title_str(str1):
#     a=''
#     for i in range(len(str1)):
#          if i==0 and 122>=ord(str1[i])>=97:
#              a+=chr(ord(str1[i])-32)
#          elif str1[i-1]==' ' and 122>=ord(str1[i])>=97 :
#              a+=chr(ord(str1[i])-32)
#          else:
#              a+=str1[i]
#     return a
#print(title_str('hello good world'))
#8
#def hakarak_str(a):
#    b=''
#    for i in a:
#        b=i+b
#    return b
#print(hakarak_str('hello'))
#9
#def bajnel_str(a,b,c):
#     st=''
#     if len(a)>b:
#         st=a[b:c]
#     else:
#         st=a
#     return st
#print(bajnel_str('hello',1,3))
#10
#def longest_word(a):
#    b=a.split()
#    c=''
#    for i in range(len(b)-1):
#        if len(b[i])>len(b[i+1]):
#            c=b[i]
#    return c
#print(longest_word('hello unbelivable world'))
#11
#def biggest_letter(a):
#    b=0
#    c=''
#    for i in a:
#        if a.count(i)>b:
#            b=a.count(i)
#            c=i
#        else:
#            continue
#    return c
#print(biggest_letter('hello world'))
#12
#def biggest_in_longest(a):
#    b=a.split()
#    c=''
#    for i in range(len(b)-1):
#        if len(b[i])>len(b[i+1]):
#            c=b[i]
#    d=0
#    e=''
#    for i in c:
#        if c.count(i)>d:
#            d=c.count(i)
#            e=i
#    return c,e
#print(biggest_in_longest('hello beatifful world'))
#13
#def strind_st(a,b):
#    if len(a)>=b:
#        return a[b],a[-b]
#print(strind_st('hello',1))
#15
#def polind(a):
#    if a==a[::-1]:
#        return 'yes'
#    else:
#        return 'no'
#print(polind('1992'))
#16
#def polind_near(a):
#    for i in range(a):
#        r=a+i
#        l=a-i
#        b=0
#        if str(r)==str(r)[::-1]:
#            b=r
#            break
#        if str(l)==str(l)[::-1]:
#            b=l
#            break
#    return b
#print(polind_near(520))
#17
#def firstlast_art(a):
#    b=str(a)
#    return int(b[0])*int(b[-1])
#print(firstlast_art(1992))
#18
#def list_str(*args):
#    a=list(args)
#    b=0
#    for i in a:
#        if type(i)==str:
#            b+=1
#    return b
#print( list_str('afafd',4,'sfs',5))
#19
#def maxnum_ls(*args):
#    a=list(args)
#    b=0
#    for i in a:
#        if type(i)==int and i>b:
#            b=i
#    return b
#print(maxnum_ls(1,45,3,'sdf'))
#20
#def zuygerknish(*args):
#    a=list(args)
#    b=[]
#    for i in a:
#        if 100>i>=10 and i%2==0:
#            b.append(i)
#    return b
#print(zuygerknish(1,22,23,45,44))
#21
#def listmijin_tv(*args):
#    ls=list(args)
#    a=0
#    b=0
#    for i in ls:
#        if type(i)==int:
#            a+=i
#            b+=1
#    return a//b
#print(listmijin_tv(23,'32',4,3423,'dsg'))
#22
#def lstoxeri_erkar(*args):
#    a=list(args)
#    b=[]
#    for i in a:
#        if type(i)==str:
#            b.append(len(i))
#    return a,b
#print(lstoxeri_erkar('hello',4,'world'))
#23
#def maxmin_rev(*args):
#    a=list(args)
#    b=[]
#    for i in a:
#        if type(i)==int:
#            b.append(i)
#    b.sort()
#    b.reverse()
#    return b
#print(maxmin_rev(3,5,6,7,2,9,1,'ddbgdx'))
#24
#def sort_ind(*a):
#    ls=list(a)
#    b=[len(i) for i in ls]
#    b.sort()
#    [b.pop(el) for el in range(len(b)-1) if b[el]==b[el+1]]
#    c=[]
#    for i in range(len(b)):
#         for j in a:
#             if len(j)==b[i]:
#                 c.append(j)
#    c.reverse()
#    return c     
#print(sort_ind('asaf','a','sa','sgdtrgd'))
#25
#def cont_dzayn(*args):
#    a=0
#    b=''
#    c=0 
#    for i in args:
#        a=0
#        for j in i:
#            if j in 'aeiou':
#                a+=1
#            if c<a:
#                c=a 
#                b=i        
#    return b,c,a
#print(cont_dzayn('ggdfaaa','faaa','sid','sdfiiii','daia'))
#26
#def count_words(*a):
#    ls=list(a)
#    b=''
#    c=0
#    for i in ls: 
#        if len(i.split())>c:
#            c=len(i.split())
#            b=i
#    return b
#print(count_words('sfsfs sfsf sfgs','sggd dg dg dg','sdg sfg sdg'))
#27
#def biggestnum(*a):
#    b=[a[i] for i in range(len(list(a))) if a[i].isdigit()]
#    b.sort()
#    return b[-1]         
#print(biggestnum('sdf','234','325','343df'))
#28
#def tariq_dict(a):
#    b=[int(i) for i in a.values() if i.isdigit()]
#    b.sort()
#    c={}
#    for k,v in a.items():
#            if v==str(b[-1]):
#                c[k]=v
#    return c
#print(tariq_dict({'k':'2','b':'5','c':'3','d':'34','e':'21'}))
#29
#def tvansh_dict(a):
#    b=[int(i) for i in a.values() if i.isdigit()]
#    b.sort()
#    c={}
#    for i in b:
#        for k,v in a.items():
#            if v==str(i):
#                c[k]=v
#    return c 
#print(tvansh_dict({'k':'2','b':'5','c':'3','d':'4','e':'6'}))
#30
#def str_lendic(a):
#    b=[i for i in a.values() ]
#    lenb=0
#    c=[len(i) for i in b if len(i)>lenb]
#    c.sort()
#    d={}
#    for k,v in a.items():
#        if len(v)==c[-1]:
#           d[k]=v
#    return d
#print(str_lendic({'a':'politex','b':'mango','c':'progress'}))



