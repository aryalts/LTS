# -*- coding: utf-8 -*-
import csv

from common.yaml_util import get_object_path


# 读取csv文件
def read_csv_file(csv_path):
    csv_data_list = []
    with open(get_object_path()+csv_path, encoding="utf-8") as f:
        csv_data = csv.reader(f)
        for row in csv_data:
            csv_data_list.append(row)
    return csv_data_list


if __name__ == '__main__':
    read_csv_file('/data/get_token.csv')