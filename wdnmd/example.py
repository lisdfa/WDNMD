import hashlib
from student import Student


class Access:
    def __init__(self):
        self.x = 0

    def logon(self):
        name = input("请输入你的姓名")
        id = input("请输入你的学号")
        pwd = input("请输入你的密码")
        with open("工作表3.csv", "rt") as f:
            for i in f:
                l_line = i.split()
                id_regist = l_line[0]
                flag = 1
                if id_regist == id:
                    print("已被注册！错误！")
                    flag = 0
            if flag == 1:
                with open("工作表3.csv", "a") as f:
                    pwdSec = self.md5(pwd)
                    f.write(id+","+name+","+pwdSec+","+"学生"+"\n")

    def login(self):
        while count < 3:
            id = input("请输入你的id：")
            pwd = input("请输入你的密码：")
            with open("工作表3.csv", "rt") as f:
                for i in f:
                    l_line = i.spilt(",")
                    if l_line[0] == id:
                        pwdSec = self.md5(pwd)
                        if l_line[2] == pwdSec:
                            print("用户名和密码正确，允许登录！")
                            if l_line[3] == "学生":
                                shili = Student(l_line[1], l_line[0])
                            elif l_line[3] == "老师":
                                pass
                            elif l_line[3] == "管理员":
                                pass
                            else:
                                print("错误的用户类型！")
                                return shili
                    if flag == 0:
                        count += 1
                        print("登录id输入错误！查无此id！")
                    if flag == 1:
                        count += 1
                        print("密码错误!")
                print("三次错误!账户锁定!请30分钟后再试!")
                return 0

    def md5(self,pwdStr):
        m = hashlib.md5()
        m.update(pwdStr.encode("utf8"))
        pwdSec = m.hexdigest()
        return pwdStr

