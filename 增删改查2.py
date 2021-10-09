#-*- coding:utf-8 -*-

#名字列表
names = ["沈政委","杨丽云","周玲"]
#功能提示
print("="*50)
print("名字管理系统")
print("1.添加一个新的名字")
print("2.删除一个人的名字")
print("3.修改一个人的名字")
print("4.查找一个人的名字")
print("5.退出")
print("="*50)

while True:
    #获取用户输入
    num = int(input("请输入需要操作的序号："))

    #更具用户输入执行相应操作

    if num == 1:
        add_name = input("请输入你要添加的名字：")
        append_insert = input("向后追加Y,指定插入N：")
        if append_insert =="Y" or append_insert == "y":
            names.append(add_name)
        elif append_insert == "N" or append_insert =="n":
            insert_num = int(input("请输入指定插入的下标："))
            names.insert(insert_num,add_name)
        else:
            print("恁输入的选项不正确！！")        
        print(names)

    elif num==2:
        print(names)
        choose_one = input("pop-->删除最后一个  remove-->删除名字 del-->按下标删除")
        if choose_one == "pop":
            names.pop()
            print(names)
        elif choose_one == "remove":
            del_name = input("请输入你要删除的名字：")
            names.remove(del_name)
            print(names)
        elif choose_one == "del":
            del_name_num = int(input("请输入你要删除名字对应下标："))
            del names[del_name_num]
            print(names)
        else:
            print("请输入pop remove del...")

    elif num ==3:
        print(names)
        amend_name_num = int(input("请输入你要修改的名字的下标："))
        amend_name = input("请输入你修改后的名字")
        names[amend_name_num] = amend_name
        print(names)
    elif num == 4:
        print(names)
        seek_name = input("请输入你要查找的名字")
        if seek_name in names:
            print("找到了")
    elif num == 5:
        break;      
    else:
        print("您的输入有误！请重新输入！")

