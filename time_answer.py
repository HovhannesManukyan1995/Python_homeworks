import random
from inputimeout import inputimeout



countries={
"Japan":"Tokyo",
"Armenia":"Yerevan",
"Spain":"Madrid",
"USA":"Washington",
"Russia":"Moscow",
}
count=0
lis=list(countries.items())
random.shuffle(lis)
dic=dict(lis)
print(dic)
for k,v in dic.items():
    print('what is a capital of:',k)
    try:
        something = inputimeout(prompt='enter answer: ', timeout=10)
        if something==v.lower():
            print('rite')
            count+=1
    except Exception:
         print( 'time is up')
         break
print('you have ',count,'rite answer')
