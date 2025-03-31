x = float(input("a value:"))

def cookie(x):
    if x>= 0 and x<=1:
        def error(a,b):
            y = (a**((2*b)+1))/((2*b)+1)
            return y

        n = 0
        while error(x,n) > 0.0001:
            n += 1

        running = 0
        for i in range(n):
            current = (((-1)**1)*(x**((2*i)+1)))/((2*i)+1)
            running =+ current

    else:
        return("Error!")

    print(running,n,error(x,n))

print(cookie(x))

