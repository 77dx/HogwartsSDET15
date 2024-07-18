"""
@ Title:
@ Author: Cathy
@ Time: 2024/4/16 13:54
"""

# python3.6之前的版本，字典是输出无序的；
# python 3.6之后的版本，字典是输出有序的，按照插入的顺序
# 其中sorted实现的排序是，将key或者value取出来排序，然后按照这个顺序保存
# 进一个新的字典中，就可以实现字典排序了，本质上是根据字典输出有序的特性，将字典的值排序后按照顺序写入新字典的过程。

# 字典实现排序的
d = {"cathy":2,"jane":9,"bob":10,"jack":1,"ennis":35}
print(id(d))

# 按照key值升序排序,返回结果为list，可强制转换为dict
d = dict(sorted(d.items()))
print(d)
print(id(d))


# 按照value值，从大到小排序,返回结果为list，可强制转换为dict
print(sorted(d.items(), key=lambda item:item[1],reverse=True))
