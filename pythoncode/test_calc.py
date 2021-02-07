import pytest
from pythoncode.calculator import Calculator
import yaml


def get_datas():
    with open("./data.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        add_datas = datas["datas"]
        add_ids = datas["myids"]
        return [add_datas, add_ids]


class TestCalc():
    def setup_class(self):
        self.calc = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,expect",
                             get_datas()[0],
                             ids=get_datas()[1])
    def test_add(self, a, b, expect, myfixture):
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (1, 1, 0), (-3, -2, -1), (1000, 2000, -1000)],
                             ids=["int", "minus", "bigint"])
    def test_sub(self, a, b, expect):
        assert expect == self.calc.sub(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (1, 1, 1), (-3, -2, 6), (1000, 2, 2000)],
                             ids=["int", "minus", "bigint"])
    def test_mul(self, a, b, expect):
        assert expect == self.calc.mul(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (1, 1, 1), (-6, -3, 2), (1000, 500, 2)],
                             ids=["int", "minus", "bigint"])
    def test_div(self, a, b, expect, myfixture):
        # self.calc = Calculator()
        assert expect == self.calc.div(a, b)
