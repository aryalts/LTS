# -*- coding: utf-8 -*-
import requests
import json
from common.requests_util import RequestsUtil
from common.yaml_util import write_extract_file, read_extract_file, read_testcase_file
import pytest


class TestRequests:
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcases/get_token.yml'))
    def test_get_token(self, caseinfo):
        RequestsUtil('base', 'base_gzh_url').analysis_yaml(caseinfo)

    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcases/upload_file.yml'))
    def test_upload_file(self, caseinfo):
        RequestsUtil('base', 'base_gzh_url').analysis_yaml(caseinfo)

    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcases/select_file.yml'))
    def test_select_file(self, caseinfo):
        RequestsUtil('base', 'base_gzh_url').analysis_yaml(caseinfo)

    # @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcases/edit_file.yml'))
    # def test_edit_file(self, caseinfo):
    #     RequestsUtil('base', 'base_gzh_url').analysis_yaml(caseinfo)


    # def test_get1(self):
    #     url = "/cgi-bin/token"
    #     params = {
    #         "grant_type": "client_credential",
    #         "appid": "wxe5dffc3ccc684c11",
    #         "secret": "fda62efd5315ec2d53bd3b189e6c688f"
    #     }
    #     res = RequestsUtil('base', 'base_gzh_url').send_request("GET", url=url, params=params)
    #     # res = requests.get(url=url, params=params)
    #     return_data = res.json()
        #
        # # 把中间变量写入extract.yml文件
        # extract_data = {"access_token":return_data['access_token']}
        # write_extract_file(extract_data)

    # def test_get2(self):
    #     url = "/cgi-bin/tags/get?access_token"
    #     params = {
    #         "access_token": "{{access_token}}"
    #     }
    #     res = RequestsUtil('base', 'base_gzh_url').send_request(method="GET", url=url, params=params)
    #     return_data = res.json()
    #
    #
    # def test_post(self):
    #     url = "/cgi-bin/tags/update?access_token={{access_token}}"
    #     data = {
    #         "tag": {"id": 21769, "name": "厦门1703575579282"}
    #     }
    #
    #     res = RequestsUtil('base', 'base_gzh_url').send_request(method="post", url=url, json=data)
    #     return_data = res.json()


    # def test_file(self):
    #     url = "/cgi-bin/media/uploadimg?access_token={{access_token}}"
    #     data = {
    #         "media": open(r"F:\file.png", "rb")
    #     }
    #
    #     res = RequestsUtil('base', 'base_gzh_url').send_request("post", url=url, files=data)
    #     # res = requests.post(url=url, files=data)
    #     return_data = res.json()
    #     print(return_data)




