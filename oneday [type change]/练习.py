# usage: 练习
# date: 2019/11/18
# filepath: cloud1908/01.oneday/练习.py

# 思考题:
#  有这样一个阶梯;
#  每走2层最后剩下一层;每走3层剩下2层;每走4层剩下3层;
#  每走5层最后剩下4层;每走6层剩下5层;每次走7层恰好走完;
#  请问阶梯最短有多少层?

# 练习题:
# 1. 写一个程序判断用户输入的是不是数字, 如果是那么是否是奇数?
# 2. 写一个程序来计算用户输入数字的立方
# 3. 写一个程序来计算人民币转化为欧元
# 4. 根据输入的成绩进行打分, 学习成绩>=90分的同学用A表示;60-89分之间的用B表示;60分以下的用C表示;
# 5. 写一个程序判断用户输入的内容是否为空, 若为空则直接提示用户重新输入, 若不为空则打印用户输入

# 1.
n = input("please input: ")
if n.isdigit():
    n = int(n)
    if n % 2 == 1:
        print(n,"is a number"+""+"是奇数")
    else:
        print(n,"不是奇数")
else:
    print(n,"not a number")
# in 判断在不在里面

# 2.
s = input("please input: ")
if s.isdigit():
    s = int(s)
    print(s ** 3)
else:
    print(s,"not a number")

# 3.
rmb = input("Please enter the amount of RMB to be converted: ")
if not rmb.isalpha():                # 判断一个字符串是否全部由字母组成！！！
    new_rmb = float(rmb)
    Euro = new_rmb * 0.1289
    print(Euro)
else:
    print("输入错误！！！")

# 4.
c = input("Please enter your score: ")
c = int(c)
if c >= 90:
    print("A")
else:
    if 89 >= c >= 60:
        print("B")
    else:
        if 59 >= c >= 0:
            print("C")
        else:
            print("Please enter the correct score: ")

# 5.
while True:
    r = input("please input: ")
    if not bool(r):
        pass
    else:
        print(r)
        break

# 思考题：
h = 0
while True:
    if h % 2 == 1 and h % 3 == 2 and h % 4 == 3 and h % 5 == 4 and h % 6 == 5 and h % 7 == 0:
        print(h)
        break
    else:
        h += 7