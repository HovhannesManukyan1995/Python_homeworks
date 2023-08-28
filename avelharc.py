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
def cut_quest(a):
    b=''
    c=[]
    for i in a:
         for j in range(len(i)):
               if i[j]=='?':
                   b=i[:j]
                   c.append(i[:j])

    return c



def input_file(a,b):
    with open(a,'a') as f:
        f.write(b)
def harc_tal(a):
    harc1=input('enter question:')
    if harc1 in a:
        print('you have such answer:')
        exit()
    patas=input('enter correct answer:')
    avel=input('enter another 3 questions:')
    harc2=harc1+'?'+':'+patas+','+avel+'\n'
    return harc2
def krkin_harc():
    c=''
    harc=input('do you want to add answer?:yes or no:')
    if harc=='yes':
        list1=take_questions_file('test2.txt')
        cut1=cut_quest(list1)
        c=harc_tal(cut1)
        input_file('test2.txt',c)
        krkin_harc()
    else:    
        exit() 
def main():
    list1=take_questions_file('test2.txt')
    cut1=cut_quest(list1)
    ans=krkin_harc()
main()
