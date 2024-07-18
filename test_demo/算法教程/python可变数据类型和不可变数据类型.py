"""
@ Title:
@ Author: Cathy
@ Time: 2024/4/16 15:34
"""
import copy
"""
首先，需要有意识的区分 赋值 和 拷贝。
赋值: 变量 = 变量 和 变量 = 具体的值
变量与变量之间的赋值，都是复制一份指向，指向同一块内存，不新开内存，两个变量操作是同一块内存地址；
变量与数据之间的赋值，都是开辟一片新的内存，被重新赋值了的变量，指向新地址；未被重新赋值的变量，还是指向旧地址。

拷贝：浅拷贝 和 深拷贝
浅拷贝：拷贝列表和字典地址与原地址不一样，但是里面元素的地址都是一样的。
给origin增加/删除元素，copy不会更新，反之，给copy增加/删除元素，origin也不会更新，因为新开了内存，但copy并没有指向；
给origin已有元素重新赋值，copy不会更新，反之亦然；
给origin原地修改可变数据类型，copy会更新，反之亦然，因为两者指向同一片内存，原地修改，内存地址不会变，指向也不会变。

深拷贝：通过递归的方式，重新申请一块内存，创建一个新的变量，与原变量内容一摸一样，其他则毫不相关吧，待验证。。。
"""

# 不可变数据类型，赋值操作，就意味着重新开辟了一块内存地址，新的指向新地址，旧的指向旧地址
def int_():
    a = 5
    print(f"a={a}")
    print(f"a的id是{id(a)}")
    b = a
    print(f"b={b}")
    print(f"b的id是{id(b)}")
    print("***给a重新赋值，a指向新地址，b指向老地址****")
    b = b-1
    print(f"a={a}")
    print(f"a的id是{id(a)}")
    print(f"b={b}")
    print(f"b的id是{id(b)}")

    print("------将数组元素赋值给一个变量，l[3]与x指向一致，为l[3]的地址——-----")
    l = [1, 2, 3, 4]
    x = l[3]
    print(f"l的id={id(l)}")
    print(f"l[3]的id={id(l[3])}")
    print(f"x={x}")
    print(f"x的id={id(x)}")
    print("***lp删除掉l[3]，x还是指向原l[3]的地址，l[3]只是列表没有再引用了，数据还未被回收，所以x还是指向这个地址******")
    l.pop()
    print(f"l的id={id(l)}")
    print(f"x={x}")
    print(f"x的id={id(x)}")


# 可变数据类型，赋值操作，开辟新内存，新的指向新地址，旧的指向旧地址；更新数据，内存不变，指向不变
# 如数组内元素的数据类型为不可变类型，更新元素后，数组内存id不变，元素的id更新，所有的指向都更新为新的id
def list_():
    m = [1,2,5,6,9]
    print(f"m={m}")
    print(f"m的id={id(m)}")
    n = m
    print(f"n={n}")
    print(f"n的id={id(n)}")
    print("*****给m重新赋值say，m指向新地址，n指向老地址*****")
    m = ['s','a','y']
    print(f"m={m}")
    print(f"m的id={id(m)}")
    print(f"n={n}")
    print(f"n的id={id(n)}")

    print("————————————【原地修改lis的值，不进行赋值操作】————————————")
    x = [2,4,5,7,9]
    y = x
    print(id(x[0]))
    print(id(y[0]))
    print(f"x={x}")
    print(f"x的id={id(x)}")
    print(f"y={y}")
    print(f"y的id={id(y)}")
    print("*****更新[0]的值，数组指向都不变，都指向新的【0】的地址****")
    x[0] = 100
    print(id(x[0]))
    print(id(y[0]))
    print(f"x={x}")
    print(f"x的id={id(x)}")
    print(f"y={y}")
    print(f"y的id={id(y)}")
    print("*****给x删除一个元素,x和y都指向原地址，未开辟新地址*****")
    x.pop()
    print(f"x={x}")
    print(f"x的id={id(x)}")
    print(f"y={y}")
    print(f"y的id={id(y)}")

    print("-------更新数组内的可变元素------")
    i = [3,4,[1,2]]
    j = i
    print(id(i[2]))
    print(id(j[2]))
    print(f"i={i}")
    print(f"i的id={id(i)}")
    print(f"j={j}")
    print(f"i的id={id(i)}")
    print("****list[2]增加一个值*****")
    i[2].append(5)
    print(id(i[2]))
    print(id(j[2]))
    print(f"i={i}")
    print(f"i的id={id(i)}")
    print(f"j={j}")
    print(f"i的id={id(i)}")

    print("-------测试一下浅拷贝，列表地址不一样，但是元素地址一样------")
    l1 = [3,6,[7,9,0]]
    l2 = copy.copy(l1)
    print(id(l1[0]))
    print(id(l2[0]))
    print(f"l1={l1}")
    print(f"l1的id={id(l1)}")
    print(f"l2={l2}")
    print(f"l2的id={id(l2)}")
    print("***浅拷贝，更新不可变元素值***")
    l1[0] = 50
    print(id(l1[0]))
    print(id(l2[0]))
    print(f"l1={l1}")
    print(f"l1的id={id(l1)}")
    print(f"l2={l2}")
    print(f"l2的id={id(l2)}")

    print("****另一组数据*****")
    l3 = [[1,2,3],4,5]
    l4 = copy.copy(l3)
    print(id(l3[0]))
    print(id(l4[0]))
    print(f"l3={l3}")
    print(f"l3的id={id(l3)}")
    print(f"l4={l4}")
    print(f"l4的id={id(l4)}")

    print("***原地更新可变元素值***")
    l3[0].pop()
    print(id(l3[0]))
    print(id(l4[0]))
    print(f"l3={l3}")
    print(f"l3的id={id(l3)}")
    print(f"l4={l4}")
    print(f"l4的id={id(l4)}")

def dict_():
    print("********字典赋值，被赋值的变量，字典以及所有的元素地址都是一样的,原字典改了，被赋值的字典都是一起跟着改的****")
    a = {'one': [1,2,3], 'two': 2, 'three': 3}
    b = a
    print(f"a={a}")
    print(f"b={b}")
    print(f"a one 的id={id(a['one'])}")
    print(f"b one 的id={id(b['one'])}")
    print(f"a的id={id(a)}")
    print(f"b的id={id(b)}")
    a['rrr'] = 100
    print(f"***{b}******")

    # 浅拷贝的字典，字典的地址不一样，字典元素的地址浅拷贝与原地址一样
    print("****浅拷贝的字典地址不一样，元素地址一样****")
    c = a.copy()
    d = copy.copy(c)
    print(c == d)   # True
    print(f"a={a}")
    print(f"c={c}")
    print(f"a的id={id(a)}")
    print(f"c的id={id(c)}")
    print(f"a[one]的id={id(a['one'])}")
    print(f"c[one]的id={id(c['one'])}")
    print("浅拷贝，给原字典新增了元素，浅拷贝字典无新元素")
    a['six'] = 6
    print(f"a={a}")
    print(f"c={c}")
    print("浅拷贝，给浅拷贝字典新增了元素，原字典无新元素")
    c['seven'] = 7
    print(f"a={a}")
    print(f"c={c}")
    print("浅拷贝，通过原地修改可变数据类型的原字典某个value，浅拷贝字典也会更新对应value")
    a['one'].append(333)
    print(f"a的id={id(a['one'])}")
    print(f"c的id={id(c['one'])}")
    print(f"a={a}")
    print(f"c={c}")
    print("浅拷贝，通过赋值(会开新内存，指向也跟着变了)修改原字典某个value，浅拷贝字典不会更新对应value")
    a['one'] = [111, 222]
    print(f"a={a}")
    print(f"c={c}")
    print("浅拷贝，更新浅拷贝字典的某个value，原字典对应的value值不会更改")
    c['two'] = 22222
    print(f"a={a}")
    print(f"c={c}")
    print("浅拷贝，清除原字典的所有元素，浅拷贝数据还在,因为内存中的数据没有删除，只是移除了的引用")
    a.clear()
    print(f"a={a}")
    print(f"c={c}")








if __name__ == '__main__':
    # int_()
    # list_()
    dict_()
