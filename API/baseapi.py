import logging
import pymysql
import yaml
import requests
from logger import logger
class BaseApi:
    def request(self,method, url, **kwargs):
        '''
        发起接口请求
        :param method: 请求方法
        :param url: 请求url
        :param kwargs: 其他参数
        :return:
        '''
        conf=self.load_yaml('../config/baseconf.yml')
        logger.info(f'******************接口请求信息********************\n请求方法:{method}\n接口地址:{url}\n入参信息:{kwargs}')
        r=requests.request(method, conf['baseurl']+url, **kwargs)
        logger.info(f'******************接口返回信息********************\n{r.json()}')
        return r
    def mysql_select(self,sql):
        '''
        数据库查询
        :return:
        '''
        conf=self.load_yaml('../config/baseconf.yml')
        testdb = pymysql.connect(host=str(conf['mysql']['host']), port=int(conf['mysql']['port']), user=conf['mysql']['user'], passwd=str(conf['mysql']['password']),
                                 db=conf['mysql']['db'], charset="utf8")
        cursor = testdb.cursor()
        cursor.execute(sql)
        testdb.commit()
        results = cursor.fetchall()
        return results

    def load_yaml(self,path):
        '''
        yaml文件转换json
        :param path:
        :return:
        '''
        with open(path,encoding='utf-8') as f:
            read=f.read()
        return yaml.safe_load(read)
    def step(self):
        pass
