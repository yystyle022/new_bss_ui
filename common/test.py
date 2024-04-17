# -*- coding=utf-8 -*-
# @Time : 2024/4/11 15:49
# @Author : yangyang
# @File : new_bss_ui/test.py
from screeninfo import get_monitors
import sys
import os

from testcases.conftest import save_directory
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


def get_client_yangyang_login_information():
    '''
    无头模式
    @return:
    '''
    loginInformation = load_config_files('login.yaml')['management']['user_sixents']
    return loginInformation['username'], loginInformation['password']


if __name__ == '__main__':
    print(save_directory)
