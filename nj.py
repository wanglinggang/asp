#This program is for n! count
def  nj(n):
    if n == 1:
        return 1
    else:
        ans = n * nj(n-1)
        return  ans
print("100! is",nj(20))
