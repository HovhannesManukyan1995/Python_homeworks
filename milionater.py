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
    return int(count)

    
    

def take_file_users(a):
    type(a)==str()
    b=open(a ,'r')
    c=b.readlines()
    a=''
    md={}
    for i in c:
        p,x=i.split()
        md[p]=int(x)
    for i in c:
        a+=i
    print(a)
    b.close()
    return a,md


def select_user(a,md):
    b=input('Enter user name: ')
    if b in md :
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
    d=str(a).split('\n')
    if b!='no' and b not in a:
        f=b+' '+str(coun)
        d.append(f)
    if b=='no':
        print('Guest'+str(coun)+'\n')
        return d
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


def hint50_50(a):
    b=[]
    b.append(a[0])
    a.pop(0)
    random_quest=random.choice(a)
    b.append(random_quest)
    return b
def hint_friend_call(a):
    return a[0]

def hint_hall_help(a):
    b={}
    c=''
    d=100
    f=1
    v=0
    for i in range(len(a)):
       if i <3:
            f=random.randint(0,d)
            v+=f
            b[a[i]]=f
            d=d-f
       else:
            b[a[i]]=100-v 
    for k,v in b.items():
       c+=k+':'+str(v)+'%'+'\n'
    h=c.split('\n')
    h.pop(-1)
    return h


def del_hint(a,b,c):
    for i in a:
        if b==i:
            a.remove(i)
            c=c-1
    return a,c


def input_hints():
    a=input('Enter hint: ')
    return a


def main():
     user=take_file_users('top_players.txt')
     seluser= select_user(user[0],user[1])
     mix=mix_quest(take_questions_file('questions.txt'),5)
     count=0
     count_hints=3
     hints= ['50/50','call to friend','hall help']
     for i in mix:
          cut1=cut_quest(i)
          spl=spl_tupl(cut1)
          print(cut1[0],'\n')
          print('\n'.join(mix_quest(spl,len(spl))),'\n')  
          if count_hints>0 :
              print('You have',count_hints,
                      'hints','\n',(','.join(hints)))      
              inphint=input_hints()
          if inphint =='50/50' and '50/50' in str(hints):
              print('\n'.join(hint50_50(spl)))
          if inphint =='hall help' and 'hall help' in str(hints):
              hallhelp=hint_hall_help(spl)
              print('\n'.join(mix_quest(hallhelp,len(hallhelp))))
          if inphint =='call to friend' and 'call to friend' in str(hints):
              print(''.join(hint_friend_call(spl)))
          delhint=del_hint(hints,inphint,count_hints)
          hints=delhint[0]            
          count_hints=delhint[1]
          inp=input_ans(spl[0])
          count+=inp
     delus=collect_user(user[0],seluser,count)
     sorteus=sorted_users(delus)
     print(sorteus)
     input_in_file(sorteus,'top_players.txt')
main()
