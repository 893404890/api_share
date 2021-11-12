import allure
import requests

from API.baseapi import BaseApi

"""
测试用例功能模块的测试代码
"""
from logger import logger

@allure.feature('增删改查测试用例')
class TestCase(BaseApi):

    def setup_class(self):
        self.url = " http://127.0.0.1:5000/testcase"
    @allure.story('增')
    def test_add(self,getid,getname,geteamil,getinfo):

        data = {
            "id": getid,
            "username":getname,
            "email": geteamil,
            "info": getinfo
        }

        r = requests.post(self.url, json=data)
        logger.info(r.json())

        assert  'success' in r.json()['msg']

    @allure.story('删')
    def test_delete(self):

        param = {"id": 1636598737}
        r = requests.delete(self.url, params=param)
        logger.info(r.json())
        # 第一步，只验证接口能够发送成功
        assert r.status_code == 200

    @allure.story('查')
    def test_select(self):

        # 不输入任何值做筛选，返回完整的列表
        # 如果输入筛选条件，则返回给匹配的数据列表
        r = requests.get(self.url)
        logger.info(r.json())
        # 只验证接口能够发送成功
        assert r.status_code == 200
        param = {"id": 1636598737}
        r1 = requests.get(self.url, params=param)
        logger.info(r1.json())
        assert r1.status_code == 200

    @allure.story('改')
    def test_update(self):

        data = {
            "id": 1636598737,
            "username": "周栒",
            "email": "zhouxun@bonree.com1",
            "info": "湖南"
        }
        r = requests.put(self.url, json=data)
        logger.info(r.json())
        # 第一步，只验证接口能够发送成功
        assert r.status_code == 200
