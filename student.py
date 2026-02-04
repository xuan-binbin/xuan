def info_print():
    print("=" * 30)
    print("          学员管理系统 v1.0")
    print("1.添加学员")
    print("2.删除学员")
    print("3.修改学员")
    print("4.显示所有学员")
    print("5.退出系统")
    print("=" * 30)
info = []



def add_info():
    new_id = input("请输入学号：")
    new_name = input("请输入姓名：")
    new_phone = input("请输入手机号：")

    for i in info:
        if i["id"] == new_id:
            print("学号已存在")
            return
    student = {}
    student = {"id": new_id, "name": new_name, "phone": new_phone}
    info.append(student)
    print('新增成功')


def del_info():
    del_id = input("请输入学号：")
    del_name = input("请输入姓名：")
    del_phone = input("请输入手机号：")
    for i in info:
        if i["id"] == del_id:
            info.remove(i)
            print("删除成功")
            return
    print("没有此用户")

def modify_info():
    modify_id = input("请输入学号：")
    modify_name = input("请输入姓名：")
    modify_phone = input("请输入手机号：")
    for i in info:
        if i["id"] == modify_id:
            #这是删除再修改
            # info.remove(i)
            # student = {}
            # student = {"id": modify_id, "name": modify_name, "phone": modify_phone}
            # info.append(student)
            i["name"] = modify_name
            i["phone"] = modify_phone
            print("修改成功")
            return
    print("没有此用户")

def all_info():
    if len(info) == 0:
        print("没有用户")
        return
    print("学号\t姓名\t手机号")
    for i in info:
        print(i["id"],i["name"],i["phone"],sep="\t")

while True:
    info_print()
    user_choice = input("请输入你的选择(1-5)：")
    if user_choice == "1":
        print("添加")
        add_info()
    elif user_choice == "2":
        print("删除")
        del_info()
    elif user_choice == "3":
        print("修改")
        modify_info()
    elif user_choice == "4":
        print("显示所有")
        all_info()
    elif user_choice == "5":
        user_input = input("是否退出 y/n:\n")
        if user_input == "y":
            print("退出")
            break
        elif user_input == "n":
            continue
        else:
            print("输入错误,请重新输入y或n：")
    else:
        print("输入错误,请重新输入1-5：")