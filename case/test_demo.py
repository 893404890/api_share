import allure
import pytest
from API.login import LoginApi

@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('注册登录模块测试')
class TestDemo(LoginApi):

    @allure.story('登录接口测试')
    @pytest.mark.parametrize(
        'username,pwd,cat,expect', [
            ('admin', 'bonree', 'bonree', '用户名、密码错误或账号冻结'),
            ('admin', 'bonree', 'bonree1', '验证码错误'),
            ('admin', 'bonree', 'bonree1', '失败重跑测试')
        ],
        ids=['用户名、密码错误或账号冻结', '验证码错误', '失败重跑测试']
    )
    def test_demo(self,username,pwd,cat,expect):
        r=self.login(username,pwd,cat)
        assert r.json().get('msg') == expect



