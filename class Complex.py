class Complex:
    def __init__(self,real, imagine):
        self.real = real
        self.imagine = imagine
    def add(self, number):
        real = self.real + number.real
        imagine = self.imagine + number.imagine
        result = Complex(real,imagine)
        return result
n1 = Complex(5,6)
n2 = Complex(-4,2)
result = n1.add(n2)
print("real:",result.real,"imagine:",result.imagine)
