import pytest
import yaml

from pythoncode.calculator import Calculator


def get_datas():
    with open('../testing/data/calc.yml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    ids_datas = datas['add']['ids']
    # print(add_datas)
    # print(ids_datas)
    return [add_datas, ids_datas]

class TestCalc:
    def setup_class(self):
        self.calc = Calculator()

    @pytest.mark.parametrize('a,b,e',get_datas()[0],ids=get_datas()[1])
    def test_add(self,a:int, b, e):
        result = round(self.calc.add(a,b),1)
        assert result == e

    @pytest.mark.parametrize('a,b,e',[(2,1,1),(-3,2,-5),(3,5,-2),(1,1,0)])
    def test_sub(self,a,b,e):
        assert self.calc.sub(a,b) == e

