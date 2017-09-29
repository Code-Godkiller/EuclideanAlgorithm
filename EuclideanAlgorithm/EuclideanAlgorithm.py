#欧几里得辗转相除法

def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x % y)


print(gcd(1000,24))