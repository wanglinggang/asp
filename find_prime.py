# This program will find the prime number within 10000
print("1000以内的质数是：")
for i in range(2,1000):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i)