# -*- coding=utf-8 -*-
# @Time : 2024/4/11 16:38
# @Author : yangyang
# @File : new_bss_ui/read_config.py
import os
import random

import yaml

environment = 'uat'


def load_config_files(*file_paths):
    """
    加载多个YAML配置文件
    :return: 包含所有配置文件内容的字典
    """
    config_data = {}

    for file_path in file_paths:
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config', f'{file_path}')
        if os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as file:
                # 解析YAML内容并合并到config_data字典中
                config_data.update(yaml.safe_load(file))
        else:
            print(f"配置文件 {config_path} 不存在,请检查后重试！")

    return config_data[environment]


if __name__ == '__main__':
    print(random.choice(load_config_files('serverNumber.yaml')['LiQingExpandInstanceId']))
