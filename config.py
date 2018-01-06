import configparser
import os


def get_config(sec_name, key_name):

    '''
    :param sec_name:配置文件类别名称
    :param key_name: 配置文件值名称
    :return:
    '''

    config = configparser.ConfigParser()   # 创建读取配置文件的对象
    path = os.path.split(os.path.realpath(__file__))[0] + '/config.ini'     # 获取当前配置文件的路径

    config.read(path)  # 调用read方法读取配置文件
    if sec_name in config.sections() and key_name in config.options(sec_name):
        return config.get(sec_name, key_name)
    else:
        return None


if __name__ == '__main__':
    pass