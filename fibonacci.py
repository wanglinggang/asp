#This program will count the numbers of rabbit
num_rabbit = [1 ,1 , 1]
month = 12
i = 3
tmp = 0
while i <= 12:
    tmp = num_rabbit[i-1] + num_rabbit[i-2]
    num_rabbit.append(tmp)
    i = i +1
print("The numbers of rabbit is",num_rabbit[12])