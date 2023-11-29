from functools import reduce

import yaml
from setuptools.dist import sequence


def get_datas():
    with open('../testing/data/calc.yml') as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    ids_datas = datas['add']['ids']
    return [add_datas, ids_datas]


class Demo:

    def get_datas(self):
        with open('../testing/data/calc.yml') as f:
            datas = yaml.safe_load(f)
        add_datas = datas['add']['datas']
        ids_datas = datas['add']['ids']
        return [add_datas, ids_datas]

    def display_data(self):
        print('2222')
        print(self.get_datas())




# def bar(func):
#     func()
# bar(foo)


# print(reduce((lambda x, y: x * y), [1]))

class A:

    a = 10

    def bar(self):
        b = 20
        print(self.a)

    def foo(self):
        print(self.a + 10)


A().foo()




