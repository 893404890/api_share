"""
测试用例相关接口信息
"""

from flask import request
from flask_restful import Resource
from testcase_moudle import TestCase
from server import db
from logger import logger


class TestCaseServer(Resource):

    def get(self):
        '''
        查找
        :return:
        '''
        case_id = request.args.get("id")
        logger.info(f"接收到的参数id <==== {case_id}")
        if case_id:
            case_data = TestCase.query.filter_by(id=case_id).first()
            if case_data:
                # datas = [{"id": case_data.id, "node_id": case_data.node_id, "remark": case_data.remark}]
                datas = [case_data.as_dict()]
            else:
                datas = []
        else:
            case_datas = TestCase.query.all()
            # datas = [{"id": case_data.id, "node_id": case_data.node_id, "remark": case_data.remark} for case_data in
            #          case_datas]
            datas = [case_data.as_dict() for case_data in case_datas]
        logger.info(f"将要返回的内容 ====> {datas}")
        return {"code": 0, "msg": {"data": datas}}

    def post(self):
        '''
        新增
        :return:
        '''
        # 获取调用该接口传入的json数据
        case_data = request.json
        logger.info(f"接收到的参数 <==== {case_data}")
        # 获取调用该接口传入的json数据中的id
        case_id = case_data.get("id")
        # 使用数据体中的id进行查询，查询到了则使用下述的else逻辑
        exist = TestCase.query.filter_by(id=case_id).first()
        logger.info(f"{exist}")
        # 不存在的时候进行数据的新增操作
        if not exist:
            testcase = TestCase(**case_data)
            # 处理不符合字符串的格式的内容 转换成json字符串
            # 如果本身是字符串，会被dumps 转码，如果数据类型
            # 本来就是字符串，即无需使用dumps
            # testcase.node_id = json.dumps(case_data.get("node_id"))
            db.session.add(testcase)
            db.session.commit()
            logger.info(f"将要返回的内容 ====> Case id {case_id} success add")
            return {"code": 0, "msg": f"Case id {case_id} success add"}
        else:
            return {"code": 40001, "msg": f"Case is exist"}

    def put(self):
        '''
        修改
        :return:
        '''
        case_data = request.json
        logger.info(f"接收到的参数 <==== {case_data}")
        # 获取调用该接口传入的json数据中的id
        case_id = case_data.get("id")
        # 使用数据体中的id进行查询，查询到了则使用下述的else逻辑
        exist = TestCase.query.filter_by(id=case_id).first()
        logger.info(f"{exist}")
        if exist:
            # case_data['node_id'] = json.dumps(case_data.get("node_id"))
            TestCase.query.filter_by(id=case_id).update(case_data)
            db.session.commit()
            logger.info(f"将要返回的内容 ====> Case id {case_id} success change to {case_data}")
            return {"code": 0, "msg": f"Case id {case_id} success change to {case_data}"}
        else:
            return {"code": 40002, "msg": f"Case is not exist"}

    def delete(self):
        '''
        删除
        :return:
        '''
        case_id = request.args.get("id")
        logger.info(f"接收到的参数id <==== {case_id}")
        if not case_id:
            return {"code": 40003, "msg": "Delete case_id must not null"}
        exist = TestCase.query.filter_by(id=case_id).first()
        logger.info(f"{exist}")
        if exist:
            TestCase.query.filter_by(id=case_id).delete()
            db.session.commit()
            return {"code": 0, "msg": f"Case id {case_id} success delete"}
        else:
            return {"code": 40002, "msg": f"Case is not exist"}
