# -*- coding: utf-8 -*-
import random

from common.yaml_util import read_extract_file


class DebugTalk:
    # 获取随机数
    def get_random_number(self,min,max):
        return random.randint(int(min),int(max))

    def get_extract_data(self,node_name):
        return read_extract_file(node_name)
