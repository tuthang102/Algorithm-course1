import math


def karatsuba(n1, n2):
    if (n1 < 10) or (n2 < 10):
        return n1*n2
    else:
        m = max(len(str(n1)), len(str(n2)))
        m2 = int(math.ceil(float(m/2)))
        high1 = int(math.floor(n1/(10**m2)))
        low1 = int(n1 % (10**m2))
        high2 = int(math.floor(n2 / (10 ** m2)))
        low2 = int(n2 % (10 ** m2))
        z0 = karatsuba(low1, low2)
        z1 = karatsuba(low1+high1, low2+high2)
        z2 = karatsuba(high1, high2)
        return (z2*10**(2*m2))+((z1-z2-z0)*10**m2)+z0

### TEST CASE:

print('Test result:', karatsuba(12345679, 63), '---', 'Answer:', 12345679*63)
print('Test result:', karatsuba(3, 21), '---', 'Answer:', 3*21)
print('Test result:', karatsuba(12345679, 9), '---', 'Answer:', 12345679*9)


        
        