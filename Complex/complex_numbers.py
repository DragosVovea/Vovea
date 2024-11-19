
class Complex:
    """
    Creates a complex number
    """
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __str__(self):
        return f"{self.a} + {self.b}i"

    def add(self,c2):
        """
        Makes the sum of complex numbers
        :param c1: complex nr 1
        :param c2: complex nr 2
        :return: return c1+c2
        """
        c=Complex(self.a+c2.a,self.b+c2.b)
        return c

    def __add__(self, other):
        return Complex(self.a+other.a,self.b+other.b)

    def __eq__(self, other):
        if self.a==other.a and self.b==other.b:
            return 'Equal'
        return 'Non Equal'