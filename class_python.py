class house:
    def __init__(self,hark=0,lusamut=0,dur=0):
        self.hark=hark
        self.lusamut=lusamut
        self.dur=dur
    def remont(self):
        print('your house has',self.hark,'floors',',',self.lusamut,'windows',
                self.dur,'doors')
h1=house(1,4,2)
h1.remont()

