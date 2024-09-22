# coding:utf-8
#迭代公式:e0=1, en=e(n-1)+(n的阶乘分之一)
#当en-e(n-1)的绝对值小于10^(-5)时迭代停止
#阶乘的函数定义
def Update_rule(n):
    s=1#阶乘从1开始相乘
    for i in range(1,n+1):
        s*=i
    return s
#Update_rule函数有正确的逻辑，并且确实返回了一个数值。然后才能在后续的计算中使用该函数的返回值。
ei=1
n=1
while 1/Update_rule(n)>10**(-5):
    ei+=1/Update_rule(n)
    n+=1
print('e的近似值为：{:.6f}'.format(ei))

#字符串格式化限制小数点个数。例：
#number = 3.14159
#print("{:.2f}".format(number))  # 输出: 3.14
