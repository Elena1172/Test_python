def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
print (gcd(17,51))
def gcd1(a,b):
    return a if b == 0 else gcd1(b,a%b)
print (gcd(51,5))
print (gcd1(5,51))