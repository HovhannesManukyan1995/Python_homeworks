class Human: 
    def __init__(self, name, surn, age):
        self.name = name
        self.surname = surn
        self.age = age
    def __repr__(self):
        return  self.name +',' + self.surname + ', ' + str(self.age) 
 
 
human = [
      Human('John', 'Pitt', 28),
      Human('Sam', 'Banks', 20),
      Human('Joe', 'Fernandes', 25),
      Human('Karo','Galayan',32),
      Human('Maro','Lalayan',22),
      Human('Varo','Kalayan',42),
      Human('Taro','Nalayan',52),
      Human('Garo','Dalayan',62),
      Human('Daro','Talayan',12),
      Human('Saro','Ralayan',2),
      Human('Baro','Yalayan',33),
      Human('Maro','Dalayan',34),
      Human('Laro','Kalayan',35),
      Human('Paro','Malayan',36)
   ]
 
human.sort(key=lambda x: x.age)
 
print(human)
