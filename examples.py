class Figure:

    def Perimetr(self):
        pass

class Square(Figure):

    def __init__(self,a,b):
        super().__init__()
        self.side1 = a
        self.side2 = b

    def Perimetr(self):
        return (self.side1+self.side2)*2
    
class treeugolnik(Figure):
    def __init__(self,a,b,c):
        super().__init__()
        self.side1 = a
        self.side2 = b
        self.side3 = c

    def Perimetr(self):
        return self.side1+self.side2+self.side3
    

f1 = Square(10, 20)
f2 = treeugolnik(3,4,5)


sp = [f1, f2]

for x in sp:
    print(x.Perimetr())

    
