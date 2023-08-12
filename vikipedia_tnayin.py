import os.path
def get_content(a):
    with open(a) as file1:
        return file1.read()

def file_existance(a,b):
    check_f=os.path.isfile(a)
    if check_f:
        return True
    else:
        return False
def count_symbols(a):
    c=a.strip()
    list1=list(c)
    c=''
    md={}
    for i in list1:
        if i not in md:
            md[i]=list1.count(i)
    for i,j in md.items():
        c+=i+':'+str(j)+','
    return c
def longest_word(a):
    b=a.strip()
    c=b.split()
    d=''
    count=0
    for i in c:
        if len(i)>count:
            count=len(i)
            d=i
    str1='Longest word is: '+d
    return str1
def sentence_count(a):
    b=a.strip()
    c=b.split('.')
    d='There is a: '+str(len(c))+' :sentences'
    return d
def reversed_words(a):
    b=''
    for i in a[::1]:
        b=i+b
    c=b.split()
    c.reverse()
    return ' '.join(c)
def write_info_file(a,b):
    file1=open(a,'w')
    file1.write(str(b))
#   file1.write(str(count_symbols(b)))
 #   file1.write('\n')
 #   file1.write(str(longest_word(b)))
 #   file1.write('\n')
 #   file1.write(str(sentence_count(b)))
 #   file1.write('\n')
 #   file1.write(str(reversed_words(b)))
    file1.close()
    return 'Done'
def main():
    data1=get_content('data.txt')    
    exixt=file_existance('./data.txt',data1)
    allin=[]
    if exixt==True:
        count_s=count_symbols(data1)
        allin.append(count_s)
        longest_w=longest_word(data1)
        allin.append(longest_w)
        sent_c=sentence_count(data1)
        allin.append(sent_c)
        revers_w=reversed_words(data1)
        allin.append(revers_w)
    joinall='\n'.join(allin)
    print(joinall)
    write_info_file('./return.txt',joinall)
main()



