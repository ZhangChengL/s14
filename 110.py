#使用while循环实现输出2 - 3 + 4 - 5 + 6 ... + 100 的和
# i=0
# c=2
# while c<101:
#     if c % 2 == 0:
#         i += c
#     else:
#         i =i - c
#     c=c+1
# print(i)
#
# tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])

# map以及lambda表达式的应用：
#         a. 利用 map、自定义函数 将所有是奇数的元素加100 l1 = [11, 22, 33, 44, 55]
#         b. 利用 map、lambda表达式 将所有是偶数的元素加100 l1 = [11, 22, 33, 44, 55]

# l = [11, 22, 33, 44, 55]
# a = []
# for i in l:
#     if i % 2 != 0:
#         i=i+100
#         a.append(i)
#     else:
#         a.append(i)
# print(a)

#写代码实现 9*9 乘法表
aa=[]
for i in range(1,10):
    for f in range(1,10):
        if i >= f:
            x = i * f
            cc=(f,'*',i,'=',x)
            aa.append(cc)
    print(aa)
    aa=[]