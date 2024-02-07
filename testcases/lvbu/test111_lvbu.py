# -*- coding: utf-8 -*-
import allure
import pytest
import requests
import yaml
import json


def read_yaml(yaml_path):
    with open(yaml_path, mode="r", encoding="utf-8") as f:
        value = yaml.load(f, Loader=yaml.FullLoader)
        return value


@allure.epic("项目名称：测试项目")
@allure.feature("模块名称：吕布")
@allure.severity(allure.severity_level.BLOCKER)
class TestApi:
    @allure.story("接口名称：查询接口1")
    @pytest.mark.parametrize("caseinfo", read_yaml("./testcases/lvbu/get_token.yml"))
    def test_lvbu(self, caseinfo):
        print(caseinfo)
        allure.dynamic.title("用例标题：" + caseinfo["name"])
        allure.dynamic.description(caseinfo["description"])
        allure.attach(body=caseinfo["request"]["url"], name="请求地址：", attachment_type=allure.attachment_type.TEXT)
        allure.attach(body=caseinfo["request"]["method"], name="请求方式：", attachment_type=allure.attachment_type.TEXT)
        data = caseinfo["request"]["data"]
        allure.attach(body=json.dumps(data), name="请求数据：", attachment_type=allure.attachment_type.TEXT)
        rep = requests.get(url=caseinfo["request"]["url"], params=data)
        allure.attach(body=rep.text, name="响应数据：", attachment_type=allure.attachment_type.TEXT)
        print("吕布")

    @allure.story("接口名称：查询接口2")
    def test_lvbu1(self):
        allure.dynamic.title("用例标题：正确参数2")
        print("吕布1")


@allure.epic("项目名称：测试项目")
@allure.feature("模块名称：吕布")
@allure.severity(allure.severity_level.BLOCKER)
class TestApi2:
    @allure.story("接口名称：查询接口3")
    @pytest.mark.parametrize("args_name, age", [["张飞", "18"], ["关羽", "17"]])
    def test_lvbu3(self, args_name , age):
        allure.dynamic.title("用例标题：" + args_name + age)
        allure.dynamic.description(args_name + "用例描述")
        print("吕布3")

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("接口名称：查询接口4")
    def test_lvbu4(self, execute_sql):
        allure.dynamic.title("用例标题：" + execute_sql)
        allure.dynamic.description(execute_sql + "用例描述")
        print("吕布4")
