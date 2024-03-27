# -*- coding: utf-8 -*-
import json
import re

import jsonpath
import requests
from common.yaml_util import read_config_file, read_extract_file, write_extract_file


class RequestsUtil:

    session = requests.session()

    def __init__(self, base, base_url):
        self.base_url = read_config_file(base, base_url)
        self.last_headers = {}

    # 分析yaml用例是否符合规范
    def analysis_yaml(self, caseinfo):
        # 1.必须要有四个一级关键字：name, base_url, request, validate
        caseinfo_keys = dict(caseinfo).keys()
        if 'name' in caseinfo_keys and 'base_url' in caseinfo_keys and 'request' in caseinfo_keys and 'validate' in caseinfo_keys:
            # 2.request下必须包含两个二级关键字：method, url
            request_keys = dict(caseinfo['request']).keys()
            if 'method' in request_keys and 'url' in request_keys:
                # 参数（data，jason，params），请求头，文件上传不能约束
                method = caseinfo["request"]["method"]
                del caseinfo["request"]["method"]
                url = caseinfo["request"]["url"]
                del caseinfo["request"]["url"]
                headers = None
                if jsonpath.jsonpath(caseinfo, '$..headers'):
                    headers = caseinfo["request"]["headers"]
                    del caseinfo["request"]["headers"]
                files = None
                if jsonpath.jsonpath(caseinfo, '$..files'):
                    files = caseinfo["request"]["files"]
                    for key,value in dict(files).items():
                        files[key] = open(value, 'rb')
                    del caseinfo["request"]["files"]
                # 将caseinfo["request"]剩下的值当作参数，传给kwargs
                res = self.send_request(method=method, url=url, headers=headers, files=files, **caseinfo["request"])
                return_data = res.json()
                return_text = res.text
                print(return_data)
                # 提取接口关联的变量，支持正则和json提取
                if 'extract' in caseinfo_keys:
                    for key,value in dict(caseinfo['extract']).items():
                        if '.+？' in value or '.*?' in value:
                            re_value = re.search(value, return_text)
                            if re_value:
                                extract_data = {key: re_value.group(1)}
                                write_extract_file(extract_data)
                        else:
                            extract_data = {key: return_data['access_token']}
                            write_extract_file(extract_data)

            else:
                print("request下必须包含两个二级关键字：method, url")
        else:
            print('必须要有四个一级关键字：name, base_url, request, validate')

    # 统一替换方法，替换的值是字符串、字典
    # 不管什么类型统一转成字符串
    def replace_value(self, data):
        if data and isinstance(data, dict):
            str = json.dumps(data)
        else:
            str =data
        # 替换值
        for i in range(str.count("{{")):
            if "{{" in str and "}}" in str:
                start_index = str.index("{{")
                end_index = str.index("}}")
                old_value = str[start_index:end_index + 2]
                new_value = read_extract_file(old_value[2:-2])
                str = str.replace(old_value, new_value)
        # 还原数据类型
        if data and isinstance(data, dict):
            data = json.loads(str)
        else:
            data = str
        return data

    # 统一请求方法
    def send_request(self, method, url, headers=None, **kwargs):
        # 处理请求方法
        self.last_method = str(method).lower()
        # 处理请求路径
        self.base_url = self.base_url + self.replace_value(url)
        # 处理请求头
        if headers and isinstance(headers, dict):
            self.last_headers = self.replace_value(headers)
        # 处理请求数据，可能是params,data,json
        for key, value in kwargs.items():
            if key in ["params", "data", "json"]:
                kwargs[key] = self.replace_value(value)
        # 发送请求
        res = RequestsUtil.session.request(method=self.last_method, url=self.base_url, headers=self.last_headers, **kwargs)
        return res


if __name__ == '__main__':
    url = "/cgi-bin/tags/update?access_token={{access_token}}&aa={{www}}"
    for i in range(url.count("{{")):
        if "{{" in url and "}}" in url:
            start_index = url.index("{{")
            end_index = url.index("}}")
            old_value = url[start_index:end_index+2]
            new_value = read_extract_file(old_value[2:-2])
            url = url.replace(old_value, new_value)
            print(url)

