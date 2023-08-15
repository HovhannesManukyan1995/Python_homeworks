def take_fail(a):
    with open(a) as f:
        return f.readlines()
def input_option():
    inp=input('Enter what option you want to choose` name,surname,age,proffesion: ')
    return inp

def open_sorted(a,b):
    f=open(a,'w')
    f.write(b)
    f.close()

def split_file(a):
    b=''
    c=[]
    e=[]
    for i in a:
        b+=i
    c=b.split('\n')
    c.pop(-1)
    for i in c:
        e.append(i.split())
    return e
def choose_option(a,c):
    if a=='name':
        return check_name(c)
    elif a=='surname':
        return check_surname(c)
    elif a=='age':
        return check_age(c)
    elif a=='proffesion':
        return check_profesion(c)
    return 'wrong option'


def check_surname(b):
    c=[]
    for i in b:
        for j in range(len(i)):
            if j==0:
                c.append(i[j])
    return c
def check_name(b):
    c=[]
    for i in b:
        for j in range(len(i)):
            if j==1:
                c.append(i[j])
    return c
def check_age(b):
    c=[]
    for i in b:
        for j in range(len(i)):
            if j==2:
                c.append(i[j])
    return c
def check_profesion(b):
    c=[]
    for i in b:
        for j in range(len(i)):
            if j==3:
                c.append(i[j])
    return c
def sorted_list(a,b):
    c=[]
    for i in a:
        for j in b:
            if i in j:
                c.append(j)
    return c
def join_file(a):
    b=''
    for i in a:
        for j in i:
            b+=j
            b+=' '
        b+='\n'
    return b
def main():
    take=take_fail('list_people.txt')
    print(''.join(take))
    split_f=split_file(take)
    input1=input_option()
    choose= choose_option(input1,split_f)
    if choose=='wrong option':
        print('wrong option')
        exit()
    sorted_option=sorted(choose)
    sortl=sorted_list(sorted_option,split_f)
    joinf=join_file(sortl)
    open_sorted('sorted_people.txt',joinf)
    print(joinf)
main()
