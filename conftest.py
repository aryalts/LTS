# -*- coding: utf-8 -*-
import pytest
from common.yaml_util import clear_extract_file


# 每次执行前清空extract.yml
@pytest.fixture(scope="session", autouse=True)
def clear_extract():
    clear_extract_file()

