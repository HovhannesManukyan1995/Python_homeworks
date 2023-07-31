#import random
#quest=['What is  capital of France:?paris,erevan,london,pekin',
#        'What is  capital of USA:?washington,erevan,moskow,paris',
#        'What is first name of Hitler:?adolf,dolf,roberto,poxos',
#        'What is capital of Armenia:?erevan,pekin,paris,tbilisi',
#        'What is capital of Brazil:?barzil,pekin,paris,buenos aires',
#        'What is capital of UK:?london,paris,erevan,tbilisi',
#        'What is capital of Austria:?vienna,erevan,lisbon,roma',
#        'What is capital of Italy:?roma,washington,brazil,lisbon', 
#        'What is capital of UAE:?abu dhabi,washington,erevan,moskow',
#        'What is capital of Rusia:?moskow,berlin,pekin,dzori mayla',
#        'What is capital of Germani:?berlin,moskow,lisbon,erevan',
#        'What is capital of Portugaly:?lisbon,washington,erevan,roma',
#        'What is capital of Argentina:?buenos aires,erevan,karnut,basen',
#        'What is capital of Kamerun:?yaunde,bangi,kumasi,juba',
#        'What is capital of Chad:?njamena,yaunde,bangi,juda']
#def mix_quest(a,b):
#     c=random.sample(a,b)
#     return c
#def cut_quest(a):
#        for j in range(len(a)):
#               if a[j]=='?':
#                   return a[:j], a[j+1:]
#def spl_tupl(a):
#    for i in range(len(a)):
#        if i==1:
#            b= a[i].split(',')
#            return b 
#def inp_ans(b):
#    a=input('enter answer:')
#    count=0
#    if a==b:
#        count+=1
#        return 'rite'
#    else:
#        return 'wrong'
#
#def main():
#     mix=mix_quest(quest,10)
#     count=0
#     for i in mix:
#          cut1=cut_quest(i)
#          spl=spl_tupl(cut1)
#          print(cut1[0])
#          print('\n'.join(mix_quest(spl,len(spl))))
#          inp=inp_ans(spl[0])
#          if inp=='rite':
#              count+=1
#     print(count)
#main()

 
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


#def capitalize_str(str1):
#    a=''
#    if 122>=ord(str1[0])>=97:
#         a+=chr(ord(str1[0])-32)+str1[1:]
#    return a
#print(capitalize_str('hello good world'))


#def count_str(str1,letter):
#     count1=0
#     for i in str1:
#         if i==letter:
#              count1+=1
#     return count1
#print(count_str('hello world','o'))



#def index_str(str1,letter): 
#    index=''
#    for i in range(len(str1)):
#         if str1[i]==letter and len(index)==0:
#              index+=str(i)
#         elif str1[i]==letter and len(index)>0:
#              index+=','+str(i)
#    return index
#print(index_str('sfsgs','s'))

#def swapcase_str(str1):
#     a=''
#     for i in str1:
#         if 122>=ord(i)>=97:
#             i = chr(ord(i)-32)
#             a+=i
#         elif 90>=ord(i)>=65:
#             i = chr(ord(i)+32)
#             a+=i
#         else:
#             a+=i
#     return a
#print(swapcase_str('hello GOOD world'))


#def lower_str(str1):
#      a=''
#      for i in str1: 
#          if 122>=ord(i)>=97:
#              a+=i
#          elif 90>=ord(i)>=65:
#              b=chr(ord(i)+32)
#              a+=b
#      return a
#print(lower_str('Hello World'))

#def endswith_str(str1,letter):
#    if letter==str1[-1]:
#        return True
#    else:
#        return False
#print(endswith_str('hello world','w'))

#def zfill_str(str1,numb):
#    if len(str1)>=int(numb):
#        return str1
#    else:
#        str1=('0'*int(numb))+str1
#        return str1
#print(zfill_str('hello world','25'))


#def isalnum_str(str1):
#    for i in str1:
#        if 122>=ord(i)>=65 :
#            return False
#            break
#    return True
#print(isalnum_str(',;'))











