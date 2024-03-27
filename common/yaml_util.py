# -*- coding: utf-8 -*-
import os
import yaml


# 获得项目根路径
def get_object_path():
    return os.path.abspath(os.getcwd().split('common')[0])


# 读取config.yml
def read_config_file(one_node, two_node):
    with open(get_object_path()+"/config.yml", encoding="utf-8") as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[one_node][two_node]


# 读取extract.yml
def read_extract_file(node_name):
    with open(get_object_path()+"/extract.yml", encoding="utf-8") as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[node_name]


# 写入extract.yml
def write_extract_file(data):
    with open(get_object_path()+"/extract.yml", encoding="utf-8", mode='a') as f:
        yaml.dump(data, stream=f, allow_unicode=True)


# 清空extract.yml
def clear_extract_file():
    with open(get_object_path()+"/extract.yml", encoding="utf-8", mode='w') as f:
        f.truncate()


# 读取yml测试用例
def read_testcase_file(yaml_path):
    with open(get_object_path()+yaml_path, encoding="utf-8") as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value


if __name__ == '__main__':
    # print(read_config_file('base', 'base_wx_url'))
    yml_path = r'\testcases\lvbu\get_token.yml'
    print(read_testcase_file(yml_path))