# -*- coding=utf-8 -*-
# @Time : 2024/4/16 11:23
# @Author : yangyang
# @File : new_bss_ui/CommonPageFunction.py
from common.allure_function import write_log_to_allure_report


def click_operation(page, element, text='点击元素', log=True):
    '''
    点击操作
    @param element:元素
    @param text:点击位置名称
    @return:
    '''
    page.click(element)
    if log:
        write_log_to_allure_report(page, text=text)


def input_operation(page, element, content, text='输入内容', log=True):
    '''
    输入操作
    @param page:
    @param element:
    @param content:
    @return:
    '''
    page.fill(element, f"{content}")
    if log:
        write_log_to_allure_report(page, text=text)


def get_element_content(page, element, text='获取元素文本信息', log=True):
    '''
    获取元素文本内容
    @param page:
    @param element:
    @return:
    '''
    content = page.query_selector(element).text_content()
    if log:
        write_log_to_allure_report(page, text=text)
    return content


def assert_element_exist(page, element, timeout=5000):
    '''
    断言元素存在
    @param page:
    @return:
    '''
    try:
        page.wait_for_selector(element, timeout=timeout)
        write_log_to_allure_report(page, f'元素{element}存在,已找到')
    except Exception:
        write_log_to_allure_report(page, f'元素{element}未找到')
        assert False, f"未找到元素{element}"
