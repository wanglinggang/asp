#This is the program for repay
m = [100 , 50 , 20 , 10 , 5 , 1]
money = 168
c = [0 , 0 , 0 , 0 , 0 , 0]

c[0] = money//m[0]
money = money - 100*c[0]

c[1] = money//m[1]
money = money - 50*c[1]

c[2] = money//m[2]
money = money - 20*c[2]

c[3] = money//m[3]
money = money - 10*c[3]

c[4] = money//m[4]
money = money -5*c[4]

c[5] = money//m[5]
money = money - 1*c[5]

print("100元有:{0[0]}张，50元有:{0[1]}张，20元有:{0[2]}张，10元有:{0[3]}张，5元有:{0[4]}张，1元有:{0[5]}张".format(c))