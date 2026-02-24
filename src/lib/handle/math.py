import random

#在a~b里面随机选个数
def random_n(a,b):
    r_num = random.random() * (b - a) + a
    return r_num

#在a~b闭区间平均取c个数(包括a和b)，从小到大排列取第num个数
def recursion(a,b,c,num):
    f_num = a + (num - 1) * (b - a) / (c - 1)
    return f_num

#在a~b闭区间平均取c个数(包括a和b)，从大到小排列取第num个数
def recursion_d(a,b,c,num):
    f_num = b - (num - 1) * (b - a) / (c - 1)
    return f_num


