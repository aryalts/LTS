# -*- coding: utf-8 -*-
import json
import requests
from common.yaml_util import read_config_file, read_extract_file


class RequestsUtil:

    session = requests.session()

    def __init__(self, base, base_url):
        self.base_url = read_config_file(base, base_url)
        self.last_headers = {}

    def analysis_yaml(self, caseinfo):
        # 1.必须要有四个以及关键字：name, base_url, request, validate
        caseinfo_keys = dict(caseinfo).keys()
        if 'name' in caseinfo_keys and 'base_url' in caseinfo_keys and 'request' in caseinfo_keys and validate in caseinfo_keys:
            # request下必须包含method, url
            request_keys = dict(caseinfo['request']).keys()
            if 'method' in request_keys and 'url' in request_keys:
                print(caseinfo)
            else:
                print("request下必须包含method, url")
        else:
            print('必须要有四个以及关键字：name, base_url, request, validate')


    # 替换的值是字符串或字典
    def replace_value(self, data):
        if data and isinstance(data, dict):
            str = json.dumps(data)
        else:
            str =data
        # url = "/cgi-bin/tags/update?access_token={{access_token}}&aa={{www}}"
        for i in range(str.count("{{")):
            if "{{" in str and "}}" in str:
                start_index = str.index("{{")
                end_index = str.index("}}")
                old_value = str[start_index:end_index + 2]
                new_value = read_extract_file(old_value[2:-2])
                str = str.replace(old_value, new_value)
                print(str)
        if data and isinstance(data, dict):
            data = json.loads(str)
        else:
            data = str
        return data

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
            if key in ["params","data","json"]:
                kwargs[key] = self.replace_value(value)

        # 发送请求
        res = RequestsUtil.session.request(method=self.last_method, url=self.base_url, headers=self.last_headers, **kwargs)
        print(res.json())
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

