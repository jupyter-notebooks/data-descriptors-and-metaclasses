# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

class Square(object):
    def __init__(self, side):
        self.side = side
    def aget(self):
        return self.side * self.side
    def aset(self, value):
        print("Can't change the area.")
    def adel(self):
        print("Can't delete the area.")
    area = property(aget, aset, adel, doc="Area of the square")

# <codecell>

s = Square(5)

# <codecell>

s.area

# <codecell>

s.area = 36

# <codecell>

del s.area

# <codecell>

class Square(object):
    def __init__(self, side):
        self.side = side
    
    @property
    def area(self):
        '''Calculate the area of the square when the
        attribute is accessed.'''
        return self.side * self.side
    
    @area.setter
    def area(self, value):
        '''Don't allow setting.'''
        print "Can't set the area."
        
    @area.deleter
    def area(self):
        '''Don't allow deleting.'''
        print "Can't delete the area."

if __name__ == "__main__":
    s = Square(5)
    print('Square: %s' % s)
    print('Area: %s' % s.area)
    s.area = 36
    del s.area

# <codecell>


