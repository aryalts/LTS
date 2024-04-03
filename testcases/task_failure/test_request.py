# -*- coding: utf-8 -*-
import requests
import json

from common.parameters_util import read_csv_file
from common.requests_util import RequestsUtil
from common.yaml_util import write_extract_file, read_extract_file, read_testcase_file
import pytest


class TestRequests:

    # @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcases/task_failure/batchUpdateRuleConfigStatus.yml'))
    # def test_select_file(self, caseinfo):
    #     RequestsUtil('base', 'base_jk_url').analysis_yaml(caseinfo)

    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcases/task_failure/getEventlogs.yml'))
    def test_select_file(self, caseinfo):
        RequestsUtil('base', 'base_jk_url').analysis_yaml(caseinfo)

    # @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcases/task_failure/getEventDetailLogs.yml'))
    # def test_select_file(self, caseinfo):
    #     RequestsUtil('base', 'base_jk_url').analysis_yaml(caseinfo)

    # @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcases/get_token.yml'))
    # def test_get_token(self, caseinfo)
    #     RequestsUtil('base', 'base_gzh_url').analysis_yaml(caseinfo)

    # @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcases/upload_file.yml'))
    # def test_upload_file(self, caseinfo):
    #     RequestsUtil('base', 'base_gzh_url').analysis_yaml(caseinfo)
    # @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcases/edit_file.yml'))
    # def test_edit_file(self, caseinfo):
    #     RequestsUtil('base', 'base_gzh_url').analysis_yaml(caseinfo)

    # access_tokens = ""
    # def test_get1(self):
    #     url = "https://api.weixin.qq.com/cgi-bin/token"
    #     params = {
    #         "grant_type": "client_credential",
    #         "appid": "wxc0eb54861a3bc22d",
    #         "secret": "7356c7ddc104fcdceec95f21ed267148"
    #     }
    #     # res = RequestsUtil('base', 'base_gzh_url').send_request("GET", url=url, params=params)
    #     res = requests.get(url=url, params=params)
    #     return_data = res.json()
    #     TestRequests.access_tokens = return_data['access_token']
    #     print(return_data)
    #
    #
    #     # 把中间变量写入extract.yml文件
    #     # extract_data = {"access_token":res['access_token']}
    #     # write_extract_file(extract_data)
    #
    # def test_get2(self):
    #     url = "https://api.weixin.qq.com/cgi-bin/tags/get?access_token"
    #     params = {
    #         "access_token":TestRequests.access_tokens
    #     }
    #     # res = RequestsUtil('base', 'base_gzh_url').send_request(method="GET", url=url, params=params)
    #     res = requests.get(url=url, params=params)
    #     return_data = res.json()
    #     print(return_data)

    #
    # def test_post(self):
    #     url = "/cgi-bin/tags/update?access_token={{access_token}}"
    #     data = {
    #         "tag": {"id": 21769, "name": "厦门1703575579282"}
    #     }
    #
    #     res = RequestsUtil('base', 'base_gzh_url').send_request(method="post", url=url, json=data)
    #     return_data = res.json()

    # def test_analysis(self):
    #     url = "/api/model/home/tree"
    #     data = {
    #         "tag": {"id": 21769, "name": "厦门1703575579282"}
    #     }
    #
    #     res = RequestsUtil('base', 'base_php_url').send_request(method="get", url=url, json=data)
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




