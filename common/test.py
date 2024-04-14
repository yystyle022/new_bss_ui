# -*- coding=utf-8 -*-
# @Time : 2024/4/11 15:49
# @Author : yangyang
# @File : new_bss_ui/test.py
from screeninfo import get_monitors

from common.read_config import load_config_files


def get_headless():
    '''
    获取配置文件中的headless的值
    @return:
    '''
    return load_config_files('common.yaml')['headless']


def screen_resolution():
    monitor = get_monitors()[0]
    return (monitor.width, monitor.height)


def browser_list():
    return load_config_files('common.yaml')['browser']


if __name__ == '__main__':
    print(browser_list())

