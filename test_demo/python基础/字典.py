"""
@ Title:
@ Author: Cathy
@ Time: 2024/4/20 14:57
"""
# 创建字典的方式真是多种多样
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a == b == c == d == e)  # True

# 返回list，所有的key值
print(list(a))
# 返回键值对的个数
print(len(a))
# 根据键取值，键不存在会抛异常
print(a['one'])
# 根据键取值，键不存在，返回None,不抛异常
print(a.get("one3"))
# 设置元素
a['four'] = 4
print(a)
# 删除元素
del a['one']
print(a)
# 判断键是否在字典中，在返回True，不在返回False
print('four' in a)   # not in
# 清空字典,删除a对这块内存的引用，实际数据还存在在内存
a.clear()
print(a)
# 浅拷贝
bb = b.copy()
print(bb)
# 把列表的值当key写入字典，value都为None
list = [33,44,55]
dict_list = {}
print(dict_list.fromkeys(list))
# 返回key和value，以元组形式
print([i for i in b.items()])
# b.keys(),将key值以列表方式返回
print([i for i in b.keys()])
# pop(key),字典删除元素，key值不存在会抛异常, 返回被删除的value
res = b.pop('one')
print(res)
# popitem() 删除最后插入的元素，后进先出原则LIFO, 返回key和value
b["five"] = 5
b["four"] = 4
res = b.popitem()
print(res)
print(b)
# reversed(d)，逆转字典
bbb = {3:1, 44:2, 66:4, 11:3}
print([i for i in reversed(bbb)])
print([i for i in reversed(bbb.keys())])
print([i for i in reversed(bbb.values())])
# 待确认原理...
print(bbb.values() == bbb.values())



