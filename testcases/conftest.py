# -*- coding=utf-8 -*-
# @Time : 2024/4/12 11:22
# @Author : yangyang
# @File : new_bss_ui/conftest.py
import os
import pytest
from screeninfo import get_monitors
from page.ManagementLoginPage import *
from page.ManagementPage import go_to_login_page
from playwright.sync_api import sync_playwright
from common.read_config import load_config_files


def pytest_generate_tests(metafunc):
    if 'browser' in metafunc.fixturenames:
        browsers = load_config_files('common.yaml')['browser']
        metafunc.parametrize("browser", browsers, indirect=True)


@pytest.fixture(scope="session")
def get_user_id():
    '''
    获取测试的用户名
    @return:
    '''
    return load_config_files('login.yaml')['client']['user_yangyang']['UserId']


@pytest.fixture(scope="session")
def screen_resolution():
    '''
    获取屏幕分辨率
    @return:
    '''
    monitor = get_monitors()[0]
    return (monitor.width, monitor.height)


@pytest.fixture(scope="session")
def get_headless():
    '''
    无头模式
    @return:
    '''
    return load_config_files('common.yaml')['headless']


@pytest.fixture()
def browser(request, screen_resolution, get_headless):
    '''
    浏览器未登录驱动
    @param request:
    @param screen_resolution:
    @param get_headless:
    @return:
    '''
    browser_name = request.param
    width, height = screen_resolution
    with sync_playwright() as p:
        if browser_name == 'firefox':
            browser = p.firefox.launch(headless=get_headless)
        elif browser_name == 'chromium':
            browser = p.chromium.launch(headless=get_headless)
        else:
            channel = "chrome" if browser_name == 'chrome' else "msedge"
            browser = p.chromium.launch(channel=channel, headless=get_headless)
        context = browser.new_context(viewport={'width': width, 'height': height})
        page = context.new_page()
        yield {'page': page, 'name': browser_name}
        context.close()
        browser.close()
        p.stop()


@pytest.fixture()
def browser_login_management(request, screen_resolution, get_headless):
    ss_file = os.path.join(os.path.dirname(__file__), '..', 'management_login_data.json')
    browser_name = request.param
    width, height = screen_resolution
    with sync_playwright() as p:
        if browser_name == 'firefox':
            browser = p.firefox.launch(headless=get_headless)
        elif browser_name == 'chromium':
            browser = p.chromium.launch(headless=get_headless)
        else:
            channel = "chrome" if browser_name == 'chrome' else "msedge"
            browser = p.chromium.launch(channel=channel, headless=get_headless)
        if os.path.isfile(ss_file):
            context = browser.new_context(storage_state=ss_file, viewport={'width': width, 'height': height})
        else:
            context = browser.new_context(viewport={'width': width, 'height': height})
        page = context.new_page()
        go_to_login_page(page)
        input_account_number(page)
        input_password(page)
        click_login_button(page)
        assert_element_exist(page, ManagementLeftNavicationBar().serviceProductManagementXpath())
        yield page
        try:
            context.storage_state(path=ss_file)
        except Exception as e:
            print(e)
        context.close()
        browser.close()
        p.stop()
