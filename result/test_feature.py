import pytest
import allure


@allure.feature("登录模块")
class TestLogin():
    @allure.story("登录成功")
    def test_login_success(self):
        print("这是登录测试用例，登录成功")
        pass

    @allure.story("登录失败")
    def test_login_fail(self):
        print("这是登录测试用例，登录失败")
        pass


@allure.feature("搜索模块")
class TestSearch():
    @allure.story("搜索成功")
    def test_login_success(self):
        print("这是搜索测试用例，登录成功")
        pass

    @allure.story("搜索失败")
    def test_login_fail(self):
        allure.attach
        print("这是搜索测试用例，登录失败")
        pass


if __name__ == '__main__':
    pytest.main
