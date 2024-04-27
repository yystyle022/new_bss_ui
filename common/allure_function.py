import os
import allure
from datetime import datetime


def write_log_to_allure(text):
    '''
    写入日志到allure测试报告
    @param text:
    @return:
    '''
    allure.attach(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  {text}', name=text, attachment_type=allure.attachment_type.TEXT)


def screenshot_to_allure(page, name):
    '''
    截图放入allure测试报告
    @param page:
    @param path:
    @param name:
    @return:
    '''
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    path = f'../result/{name}.png'
    page.screenshot(timeout=5000, path=path)
    allure.attach.file(path, name=datetime.now().strftime("%Y-%m-%d %H:%M:%S") + name, attachment_type=allure.attachment_type.PNG)


def write_log_to_allure_report(page, text, screenshot=True, log=False):
    try:
        if screenshot:
            screenshot_to_allure(page, text)
        if log:
            write_log_to_allure(text)
    except Exception:
        raise Exception('日志写入异常...')
