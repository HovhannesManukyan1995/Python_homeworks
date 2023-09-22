import random

def chinga_chuk(a,b):
    print(a)
    print(b)
    cnt1=0
    cnt2=0
    if a==b:
        return cnt1,cnt2
    if a=='R' and b=='P':
        cnt2+=1
    if a=='P' and b=='R':
        cnt1+=1
    if a=='R' and b=='S':
        cnt1+=1
    if a=='S' and b=='R':
        cnt2+=1
    if a=='S' and b=='P':
        cnt1+=1
    if a=='P' and b=='S':
        cnt2+=1
    return cnt1, cnt2

def main():
    player=0
    comp=0
    list1=['R','P','S']
    while True:
        player_inp=input('Enter action:R,P,S: ')
        comp_inp=random.choice(list1)
        ch_ch=chinga_chuk(player_inp,comp_inp)
        player+=ch_ch[0]
        comp+=ch_ch[1]
        print(player,comp)
        if player==3:
            print('Player wins','\n',player,'\n',comp)
            break
        if comp==3:
            print('Computer wins','\n',player,'\n',comp)
            break
    
main()






