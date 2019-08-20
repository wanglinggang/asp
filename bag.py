bag_net = []
for i in range(6):
    bag_net.append([])
    for j in range(31):
        bag_net[i].append(0)

goods_weight = [0, 6, 10, 15, 20, 25]
goods_value = [0, 38, 88, 108, 160, 198]

for i in range(1,6):
    for j in range(1, 31):
        if j - goods_weight[i] < 0:
            bag_net[i][j] = bag_net[i-1][j]
        else:
            if  bag_net[i-1][j] > goods_value[i] + bag_net[i-1][j - goods_weight[i]]:
                bag_net[i][j] = bag_net[i-1][j]
            else:
                bag_net[i][j] =  goods_value[i] + bag_net[i-1][j - goods_weight[i]]
print("推车可装最高价值为：", bag_net[5][30])