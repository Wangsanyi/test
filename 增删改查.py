#-*- coding:utf-8 -*-
#列表xxx
xxx=["李明","张华","姜力"]
print("="*50)
print(xxx)
print("增1")
print("删2")
print("改3")
print("查4")
print("退出5")

print("="*50)
while True:
    num=int(input("请输入序号"))
    #增
    if num == 1:
        xxx_z = input("增加的名字")
        num_z = int(input("后面添加1 插入2"))
        if num_z == 1:
            xxx.append(xxx_z)
        elif num_z == 2:
            num_z_l = int(input("插入的位置"))
            xxx.insert(num_z_l,xxx_z)
        else:
            print("你输入的不正确")
        print(xxx)

    elif num == 2:
        num_s = int(input("删除最后一个1 移除名字2 删除位置3"))
        if num_s == 1:
            xxx.pop()
        elif num_s == 2:
            xxx_s = input("你要删除的名字")
            num.remove(xxx_s)
        elif num_s == 3:
            num_s_s = int(input("删除位置从0开始"))
            del xxx[num_s_s]
        else :
            print("输入不正确")
        print(xxx)

    elif num == 3:
        num_g = int(input("你要修改的位置，从0开始"))
        xxx_g = input("你要改的名字")
        xxx[num_g] = xxx_g
        print(xxx)

    elif num == 4:
        xxx_c = input("你要查的名字")
        if xxx_c in xxx:
            print("找到了")
        else:
            print("输入不正确")
        print[xxx]

    elif num == 5:
        break

    else:
        print("输入不正确")
        print[xxx]



print(xxx)


