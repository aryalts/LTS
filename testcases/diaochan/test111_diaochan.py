# _*_ coding:utf-8 _*-
import json

import allure
import pytest
import requests
import yaml

age = 1

# 读取yaml文件
def read_yaml(yaml_path):
    with open(yaml_path,mode="r",encoding="utf-8") as f:
        value = yaml.load(f,Loader=yaml.FullLoader)
        return value

@allure.epic("自助分析")
@allure.feature("模型管理")
class Testcase1:
    @allure.story("接口名称1")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("case",read_yaml("./testCases/get_token.yml"))
    @pytest.mark.skipif(age>2,reason='超过2跳过')
    @pytest.mark.smoke
    def test_baili(self,case):
        allure.dynamic.title("接口名称1正常值" + case["name"])
        allure.dynamic.description("接口名称4正常值%s描述" % case["name"])
        allure.attach(body=case["base_url"],name="请求地址:",attachment_type=allure.attachment_type.TEXT)
        allure.attach(body=case["request"]["method"], name="请求方式:", attachment_type=allure.attachment_type.TEXT)
        data = case["request"]["params"]
        allure.attach(body=json.dumps(data), name="请求数据:", attachment_type=allure.attachment_type.TEXT)
        rep =requests.get(url=case["base_url"],params=data)
        allure.attach(body=rep.text, name="响应数据:", attachment_type=allure.attachment_type.TEXT)




    @allure.story("接口名称2")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.productmanage
    def test_lvbu(self,excute_sql):
        allure.dynamic.title("接口名称2正常值"+excute_sql)
        allure.dynamic.description("接口名称2正常值%s描述" % excute_sql)
        for i in range(1,5):
            with allure.step("步骤"+str(i)+""):
                print("1")
        print("吕布:"+excute_sql)
        with open("D:\\1.JPG",mode="rb") as f:
            allure.attach(body=f.read(),name="错误截图",attachment_type=allure.attachment_type.JPG)

    @allure.story("接口名称3")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.run(order=1)
    @pytest.mark.smoke
    def test_diaochan(self):
        allure.dynamic.title("接口名称3正常值")
        allure.dynamic.description("接口名称3正常值描述")
        print("貂蝉")

@allure.epic("自助分析")
@allure.feature("报表管理")
@pytest.mark.parametrize("parm",["东东","喜喜","楠楠"])
class Testcase2:
    @allure.story("接口名称4")
    @allure.severity(allure.severity_level.NORMAL)
    def test_xiujuan(self,parm):
        allure.dynamic.title("接口名称4正常值"+parm)
        allure.dynamic.description("接口名称4正常值%s描述" % parm)
        print("秀娟:"+parm)