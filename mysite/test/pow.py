def myPow(x: float, n: int) -> float:
    print(n)
    if n == 0:
        return 1
    if n > 0:
        if n % 2 == 0:
            return myPow(x, n / 2) * myPow(x, n / 2)
        else:
            return myPow(x, n - 1) * x
    if n < 0:
        return 1 / myPow(x, -n)

if __name__=="__main__":
    # myPow(0.00001, 2147483647)
    print(myPow(2, 10))