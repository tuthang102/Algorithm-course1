x = 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184


def karatsuba(x,y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        m = max(len(str(x)), len(str(y)))
        m2 = m // 2
        high1 = x // 10**(m2)
        low1 = x % 10**(m2)
        high2 = y // 10**(m2)
        low2 = y % 10**(m2)

        z0 = karatsuba(low1,low2)
        z1 = karatsuba((low1+high1),(low2+high2))
        z2 = karatsuba(high1,high2)

        return (z2 * 10**(2*m2)) + ((z1 - z2 - z0) * 10**(m2)) + (z0)

        

print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592,
               2718281828459045235360287471352662497757247093699959574966967627) == x)
print(karatsuba(100, 21))

for i in range(6, 0, -1):
    print(i)
