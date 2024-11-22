class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def subtract(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def multiply(self, other):
        return ComplexNumber(self.real * other.real - self.imag * other.imag,
                             self.real * other.imag + self.imag * other.real)

    def is_equal(self, other):
        return self.real == other.real and self.imag == other.imag

    def __str__(self):
        return f"{self.real} + {self.imag}i"

# Example usage
c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(1, 4)
print("Addition:", c1.add(c2))
print("Subtraction:", c1.subtract(c2))
print("Multiplication:", c1.multiply(c2))
print("Are equal:", c1.is_equal(c2))
