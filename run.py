# _*_ coding:utf-8 _*-
import os
import time

import pytest

if __name__ == '__main__':
    pytest.main()
    time.sleep(5)
    os.system("allure generate reports/temps -o reports/allures --clean")
