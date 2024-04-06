import allure
from base.ClientRegisterBase import *
from common.allure_function import write_log_to_allure_report


def assert_into_register_page_success(page):
    '''断言是否进入注册页面'''
    try:
        assert page.wait_for_selector(ClientRegisterBase().UserRegisterNode(), timeout=5000), '进入亚米级实例列表失败'
        write_log_to_allure_report(page, '进入注册页面成功')
    except Exception as error:
        write_log_to_allure_report(page, f'进入注册页面失败：{error}')
