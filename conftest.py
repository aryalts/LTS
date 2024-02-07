# -*- coding: utf-8 -*-
import pytest


# def read_yaml():
#     return ['李白', '杜甫', '王维']
#
#
# @pytest.fixture(scope="function",  params=read_yaml())
# def execute_sql(request):
#     print("函数级别的装饰器开始执行")
#     yield request.param
#     print("函数级别的装饰器运行结束")
from common.yaml_util import clear_extract_file


@pytest.fixture(scope="session", autouse=True)
def clear_extract():
    clear_extract_file()

