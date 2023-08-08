import random

def take_questions_file(a):
    type(a)==str()
    b=open(a,'r')
    c=b.readlines()
    a=''
    for i in c:
        a+=i
    a=a.strip()
    d=a.split('\n')
    b.close()
    return d

def mix_quest(a,b):
     c=random.sample(a,b)
     return c


def cut_quest(a):
        for j in range(len(a)):
               if a[j]=='?':
                   return a[:j], a[j+1:]


def spl_tupl(a):
    for i in range(len(a)):
        if i==1:
            b= a[i].split(',')
            return b


def input_ans(b):
    a=input('enter answer:')
    count=0
    if a==b:
        count+=1
        return 'rite'
    else:
        return 'wrong'


def take_file_users(a):
    type(a)==str()
    b=open(a ,'r')
    c=b.readlines()
    a=''
    for i in c:
        a+=i
    print(a)
    b.close()
    return a


def select_user(a):
    b=input('Enter user name: ')
    if b in a :
        an=input('Do you want to restart results:yes or no:  ')
        if an=='yes':
            print('Welcome',b,'\n')
        if an=='no':
            print('You play as: Guest','\n')
            return  'no'
    else:
        print('Welcome ',b,'\n')
    return b


def collect_user(a,b,coun):
    d=a.split('\n')
    if b!='no' and b not in a:
        f=b+' '+str(coun)
        d.append(f)
    if b=='no':
        e='Guest'+' '+str(coun)
        d.append(e)
    for i in range(len(d)):
        if b in d[i]:
            d.pop(i)
            e=b+' '+str(coun)
            d.append(e)
    return d


def sorted_users(a):
    b=[]
    d=[]
    for i in a:
        for j in i:
            if j.isdigit():
                b.append(j)
    b.sort()
    b.reverse()
    for el in b:
        for k in a:
            if el in k and k not in d:
                d.append(k)            
    return '\n'.join(d)


def input_in_file(a,f):
    type(f)==str()
    b=open(f,'w')
    b.write(a)
    b.close()
    return 'done'




def main():
      
     user=take_file_users('top_players.txt')
     seluser= select_user(user)
     mix=mix_quest(take_questions_file('questions.txt'),10)
     print(mix)
     count=0
     for i in mix:
          cut1=cut_quest(i)
          spl=spl_tupl(cut1)
          print(cut1[0])
          print('\n'.join(mix_quest(spl,len(spl))))
          inp=input_ans(spl[0])
          if inp=='rite':
              count+=1
     delus=collect_user(user,seluser,count)
     sorteus= sorted_users(delus)
     input_in_file(sorteus,'top_players.txt')
     print(sorteus)
main()
