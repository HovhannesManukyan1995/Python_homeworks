def hang_create(a):
    #create hang pikture
    p1='_'*6+'\n'
    p2='|'
    p3=' '
    p4='\n'
    p5='O'
    p6='\ '
    p7='/'
    if a==0:
        pass
    if a==1:
        print(p1+p2+p3*4+p2+p4+(p2+p4)*6+'4 attempts')
    if a==2:
        print(p1+p2+p3*4+p2+p4+p2+p3*4+p5+p4+(p2+p4)*5+'3 attempts')
    if a==3:
        print(p1+p2+p3*4+p2+p4+p2+p3*4+p5+p4+p2+p3*4+p2+p4+(p2+p4)*5+'2 attempts')
    if a==4:
        print(p1+p2+p3*4+p2+p4+p2+p3*4+p5+p4+p2+p3*3+p7+p2+p6+p4+(p2+p4)*4+'1 attempt')
    if a==5:
        print(p1+p2+p3*4+p2+p4+p2+p3*4+p5+p4+p2+p3*3
                +p7+p2+p6+p4+p2+p3*3+p7+p3+p6+p4+(p2+p4)*3+p4+'You Dead')
    

            
def question_spl(a):
    #split question
    ind=a.index('?')
    quest=a[:ind]
    ans=a[ind+1:]
    return quest,ans



def main():
    #Game logik
    cnt=0
    quest=question_spl('what is the capital of Rushia:?moskow')
    print('This is a Hangman Game:You have 5 attempts:Good Luck:')
    print(quest[0])
    ans=quest[1]
    c='-'*len(ans)
    #loop until you win or loose
    while True:
      if c==ans:
        print('you win')
        break
      b=input('enter a letter: ')
      if b.lower() not in ans:
        cnt+=1
      #loop for cheking input
      for j in range(len(ans)):
                if ans[j]==b.lower():
                    c=c[: j]+b.lower()+c[j+1:]
      hang_create(cnt)
      if cnt==5:
          break
      print(c)

if __name__=='__main__':
    main()




