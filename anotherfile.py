import os

def go_to_file(a):
    os.chdir(a)        
    f=os.listdir()
    return f
def open_file(a,b):
    f=open(a,'w')
    c=f.write(b)
    f.close()
    return c
def file_wach(a):
    e=''
    for i in range(len(a)):
        b=open(a[i],'r')
        c=b.read()
        b.close
        c=c[:-1]
        e+=a[i]+'->'+c+'\n'
        print(a[i]+'->'+c)
    return e
def main():
    filename='exersize'
    file1=go_to_file(filename)
    watc=file_wach(file1)
    os.chdir('..')
    open_file('result.txt',watc)
main()    
         
         
         
         
