import pytest


class TestOrder:

    def test01(self, login):
        username = login['username']
        print(f'{username},下家具单')

    @pytest.mark.usefixtures('login')   # 无法获取login返回值
    def test02(self):
        print('下灯具单')

    def test0(self):
        print('下卫浴单')