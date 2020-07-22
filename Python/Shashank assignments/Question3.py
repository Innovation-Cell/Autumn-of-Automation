#YOu ARE IN THE "COMPLEX WORLD" NOW!!!

class complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        if self.y < 0:
            self.y = self.y * -1
            return print(str(str(self.x) + ' ' + '-' + ' ' + str(self.y) + 'i'))
        else:
            return print(str(str(self.x) + ' ' + '+' + ' ' + str(self.y) + 'i'))

    def add(self, other):
        X = self.x + other.x
        Y = self.y + other.y
        return complex(X,Y)

    def sub(self, other):
        X = self.x - other.x
        Y = self.y - other.y
        return complex(X, Y)

    def multiply(self,other):
        #(a+bi)(c+di) = (ac−bd) + (ad+bc)i
        X = ((self.x * other.x) - (self.y * other.y))
        Y = ((self.x * other.y) + (self.y * other.x))
        return complex(X, Y)

    def mod(self):
        sq = self.x ** 2 + self.y ** 2
        return print(sq ** 0.5)

    def conjugate(self):
        z = complex(self.x, self.y)
        return z.display()

    def inverse(self):
        """The multiplicative inverse of a complex number  z=x+iy  where  x,y  are real is the number  c=a+ib
          such that
          z×c=c×z=1
        """
        sq = self.x ** 2 + self.y ** 2
        a = self.x / (sq)
        b = self.y / (sq)
        c = complex(a, b)
        return c.display()
