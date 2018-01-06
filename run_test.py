import os
import time
import unittest
import config
from package import HTMLTestRunner


def suit():
    '''

    获取TestCase组成TestSuite返回。
    :return: TestSuite

    '''

    loader = unittest.TestLoader()
    case_path = config.get_config("directory", "case_path")     # 从配置文件获取TestCase存放的目录
    suite1 = loader.discover(case_path, pattern="*test.py")
    return suite1


if __name__ == "__main__":

    time = time.strftime("%Y-%m-%d-%H-%M-%S")     # 获取当前时间格式并格式化
    path = config.get_config('directory', 'report')  # 从配置文件获取存放report的目录

    # 定义报告文件路径和名字，路径为项目下的report目录，名字是report+当前时间拼接而成，格式定以为（.html）
    report_path = path + "report_" + time + ".html"
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass

    with open(report_path, "wb") as report:

        # 定义测试报告
        runner = HTMLTestRunner.HTMLTestRunner(stream=report,
                                               title="海边管理后台自动化测试报告",
                                               description="用例执行情况")

        # 运行测试用例
        runner.run(suit())