# 1.0版本
def show_menu():
    print("---------------------------")
    print(" 学生管理系统 ")
    print("---------------------------")
    print(" 1:添加学生信息 ")
    print(" 2:删除学生信息 ")
    print(" 3:修改学生信息 ")
    print(" 4:查询学生信息 ")
    print(" 5:查看所有学生信息 ")
    print(" 6:退出系统 ")
    print("---------------------------")


def show_menu1():
    print("---------------------------")
    print(" 1:修改该学生姓名 ")
    print(" 2:修改该学生年龄 ")
    print(" 3:修改该学生性别 ")
    print(" 4:修改该学生信息 ")
    print(" 5:退出修改 ")
    print("---------------------------")


# 定义学生列表，保存所有的学生信息
stu_list = []


# 添加学生信息
def insert_student():
    # 1.通过input函数获取学生的信息
    print('～～添加学生信息～～')
    name = input('请输入学生名字：')

    # 如果名字存在，不能再添加，判断字典中value是否存在
    for stu in stu_list:
        if stu['name'] == name:
            print('~~学生信息已存在～～')
            return

    age = input('请输入学生年龄：')
    gender = input('请输入学生性别：')

    # 2.将学生信息转换为字典进行保存
    stu_dict = {'name': name, 'age': int(age), 'gender': gender}

    # 3.将该学生字典添加到列表中
    stu_list.append(stu_dict)
    print('～～学生信息添加成功～～')


# 删除学生信息
def remove_student():
    # 1.使用input获取要删除的学生姓名
    print('～～删除学生信息～～')
    name = input('请输入要删除的学生姓名：')

    # 2.判断学生信息是否存在
    for stu in stu_list:
        if stu['name'] == name:
            # 3.学生存在，对学生进行删除
            stu_list.remove(stu)

            print('～～学生信息修改成功～～～～')
            break

    # 4.学生不存在，直接结束
    else:
        print('～～学生信息不存在，无法删除～～')


# 修改学生信息
def modify_student():
    # 1.使用input获取要修改的学生姓名
    print('～～修改学生信息～～')
    name = input('请输入要修改的学生姓名：')

    # 2.判断学生信息是否存在
    for stu in stu_list:
        if stu['name'] == name:
            # 3.学生存在，对学生进行修改
            show_menu1()
            opt1 = input('请输入操作编号：')
            if opt1 == '1':
                # 修改该学生姓名
                stu['name'] = input('请输入修改后学生名字：') # 直接修改
            elif opt1 == '2':
                # 修改该学生年龄
                stu['age'] = int(input('请输入修改后学生年龄：'))
            elif opt1 == '3':
                # 修改该学生性别
                stu['gender'] = input('请输入修改后学生性别：')
            elif opt1 == '4':
                # 修改该学生信息
                stu['name'] = input('请输入修改后学生名字：')
                stu['age'] = int(input('请输入修改后学生年龄：'))
                stu['gender'] = input('请输入修改后学生性别：')
            elif opt1 == '5':
                print('已退出修改操作～～')
                break
            else:
                print('输入有误，请重新输入')

            print('～～学生信息修改成功～～')
            break

    # 4.学生不存在，直接结束
    else:
        print('～～学生信息不存在，无法修改，请重新输入～～')
        modify_student()


# 查询学生信息
def find_student():
    # 1.使用input获取要查找的学生姓名
    print('～～查找学生信息～～')
    name = input('请输入要查找的学生姓名：')

    # 2.判断学生信息是否存在
    for stu in stu_list:
        if stu['name'] == name:
            # 3.学生存在，对学生信息进行显示
            print(f'姓名:{stu["name"]}, 年龄:{stu["age"]}, 性别:{stu["gender"]}')

            print('～～该学生信息查询成功～～～～')
            break

    # 4.学生不存在，直接结束
    else:
        print('～～学生信息不存在，无法查到～～')


# 查看所有学生信息
def show_all_info():
    if len(stu_list) > 0:
        for stu in stu_list:
            # print(stu)
            print(f'姓名:{stu["name"]}, 年龄:{stu["age"]}, 性别:{stu["gender"]}')
    else:
        print('～～没有学生信息～～')


while True:
    show_menu()
    opt = input('请输入操作编号：')
    if opt == '1':
        # print('1.添加学生信息')
        insert_student()
    elif opt == '2':
        # print('2.删除学生信息')
        remove_student()
    elif opt == '3':
        # print('3.修改学生信息')
        modify_student()
    elif opt == '4':
        # print('4.查询学生信息')
        find_student()
    elif opt == '5':
        # print('5.查看所有学生信息')
        show_all_info()
    elif opt == '6':
        print('已退出该系统，欢迎下次使用～～')
        break
    else:
        print('输入有误，请重新输入')
        continue

    print("---------------------------")
    input('～～回车键继续操作～～')


if __name__ == '__main__':
    ()