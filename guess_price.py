real_Price = 460
your_Prince = 0
count = 0
while your_Prince != real_Price:
    count = count +1
    your_Prince = int(input("请输入1000以内的整数作为你猜想的价格："))
    if your_Prince > real_Price:
        print("你输入的价格高了。")
    elif your_Prince < real_Price:
        print("你输入的价格低了。")
    else:
        print("恭喜你猜对了。你共用{}次".format(count))
        break