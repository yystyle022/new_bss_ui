# -*- coding=utf-8 -*-
# @Time : 2024/4/12 11:22
# @Author : yangyang
# @File : new_bss_ui/conftest.py

import pytest
from time import sleep
from screeninfo import get_monitors
from page.ManagementLoginPage import *
from page.ManagementPage import go_to_home_page
from playwright.sync_api import sync_playwright
from base.ClientLoginBase import ClientLoginBase
from page.ClientPage import go_to_home_page_no_login
from common.playwright_function import save_directory
from base.ClientLeftNavigationBar import ClientLeftNavigationBar
from common.read_config import load_config_files, management, client


def pytest_generate_tests(metafunc):
    browsers = load_config_files('common.yaml')['browser']
    if 'browser' in metafunc.fixturenames:
        metafunc.parametrize("browser", browsers, indirect=True)
    elif 'browser_login_management' in metafunc.fixturenames:
        metafunc.parametrize("browser_login_management", browsers, indirect=True)
    elif 'browser_login_client' in metafunc.fixturenames:
        metafunc.parametrize("browser_login_client", browsers, indirect=True)
    else:
        print('fixture获取失败，请检查代码。。。。。。。')
        raise ValueError


@pytest.fixture()
def get_random_number():
    '''
    获取厘清扩容实例
    @return:
    '''
    return random.choice(range(2, 11))


@pytest.fixture(scope="session")
def get_expand_liqing_instanceId():
    '''
    获取厘清扩容实例
    @return:
    '''
    instanceIdList = load_config_files('serverNumber.yaml')['LiQingExpandInstanceId']
    return random.choice(instanceIdList)


@pytest.fixture(scope="session")
def get_expand_fenming_instanceId():
    '''
    获取分明扩容实例
    @return:
    '''
    instanceIdList = load_config_files('serverNumber.yaml')['FenMingExpandInstanceId']
    return random.choice(instanceIdList)


@pytest.fixture(scope="session")
def get_expand_orion_instanceId():
    '''
    获取星璨扩容实例
    @return:
    '''
    instanceIdList = load_config_files('serverNumber.yaml')['OrionExpandInstanceId']
    return random.choice(instanceIdList)


@pytest.fixture(scope="session")
def get_user_id():
    '''
    获取测试的用户名
    @return:
    '''
    return load_config_files('login.yaml')['client'][f'{client}']['UserId']


@pytest.fixture(scope="session")
def get_nrtk_broadcast_url():
    '''
    获取nrtk的播发地址
    @return:
    '''
    return load_config_files('host.yaml')['BroadCastHost']


@pytest.fixture(scope="session")
def get_ppp_rtk_broadcast_url():
    '''
    获取ppp-rtk的播发地址
    @return:
    '''
    return load_config_files('host.yaml')['OrionBroadCastHost']


@pytest.fixture(scope="session")
def get_li_qing_mount_point():
    '''
    获取厘清挂载点
    @return:
    '''
    return random.choice(load_config_files('common.yaml')['LiQingMonutPoint'])


@pytest.fixture(scope="session")
def get_fen_ming_mount_point():
    '''
    获取分明挂载点
    @return:
    '''
    return random.choice(load_config_files('common.yaml')['FenMingMonutPoint'])


@pytest.fixture(scope="session")
def get_orion_mount_point():
    '''
    获取星璨挂载点
    @return:
    '''
    return load_config_files('common.yaml')['OrionMonutPoint']


@pytest.fixture(scope="session")
def get_nrtk_port():
    '''
    获取nrtk端口
    @return:
    '''
    return load_config_files('common.yaml')['NrtkPort']


@pytest.fixture(scope="session")
def get_ppp_rtk_port():
    '''
    获取ppp-rtk端口
    @return:
    '''
    return load_config_files('common.yaml')['PPPRTKPort']


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


@pytest.fixture(scope="session")
def get_client_login_information():
    '''
    获取正确的客户端登录信息
    @return:
    '''
    loginInformation = load_config_files('login.yaml')['client'][f'{client}']
    return loginInformation['username'], loginInformation['password']


@pytest.fixture(scope="session")
def get_client_login_information_password_mistake():
    '''
    获取密码错误的客户端登录信息
    @return:
    '''
    loginInformation = load_config_files('login.yaml')['client'][f'{client}']
    return loginInformation['username'], str(loginInformation['password']) + 'mis'


@pytest.fixture(scope="session")
def get_client_login_information_account_no_exist():
    '''
    获取账号不存在的客户端登录信息
    @return:
    '''
    loginInformation = load_config_files('login.yaml')['client'][f'{client}']
    return str(loginInformation['username']) + 'exs', loginInformation['password']


@pytest.fixture(scope="session")
def get_management_login_information():
    '''
    无头模式
    @return:
    '''
    loginInformation = load_config_files('login.yaml')['management'][f'{management}']
    return loginInformation['username'], loginInformation['password']


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
        context = browser.new_context(viewport={'width': width, 'height': height},
                                      )  # 修改用户代理)
        page = context.new_page()
        yield {'page': page, 'name': browser_name}
        context.close()
        browser.close()
        p.stop()


@pytest.fixture()
def browser_login_management(request, screen_resolution, get_headless, get_management_login_information):
    ss_file = os.path.join(os.path.dirname(__file__), '..', 'cookie', 'management_login_data.json')
    browser_name = request.param
    width, height = screen_resolution
    accountNumber, password = get_management_login_information
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
        go_to_home_page(page)
        if check_element_with_timeout(page, ManagementLoginBase().LoginButtonXpath()):
            input_account_number(page, accountNumber)
            input_password(page, password)
            click_login_button(page)
        yield {'page': page, 'name': browser_name}
        try:
            context.storage_state(path=ss_file)
        except Exception as e:
            assert False, e
        context.close()
        browser.close()
        p.stop()


@pytest.fixture()
def browser_login_client(request, screen_resolution, get_headless, get_client_login_information):
    ss_file = os.path.join(os.path.dirname(__file__), '..', 'cookie', 'client_login_data.json')
    browser_name = request.param
    width, height = screen_resolution
    username, password = get_client_login_information
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
        go_to_home_page_no_login(page)
        if check_element_with_timeout(page, ClientLoginBase().submitButtonXpath()):
            page.fill(ClientLoginBase().loginInputXpath('请输入账号或手机号码'), f'{username}')
            page.fill(ClientLoginBase().loginInputXpath('请输入密码'), f'{password}')
            page.click(ClientLoginBase().submitButtonXpath())
            sleep(1.5)
            while True:
                frame_xpath = ClientLoginBase().sliderVerificationIframeXpath()
                download_images(page, image_name="slider", frame_xpath=frame_xpath, image_xpath=ClientLoginBase().sliderPicXpath(), save_directory=save_directory)
                download_images(page, image_name="background", frame_xpath=frame_xpath, image_xpath=ClientLoginBase().sliderBackPicXpath(), save_directory=save_directory)
                write_log_to_allure_report(page, '下载滑块图片成功')
                position = dragbox_location(page)
                x = position['x'] + position['width'] / 2
                y = position['y'] + position['height'] / 2
                distance = get_slide_locus(get_slide_distance() * (280 / 680) + 6)
                write_log_to_allure_report(page, f'计算滑块的滑动距离成功，滑动距离为：{distance}')
                page.mouse.move(x, y)
                page.mouse.down()
                for i in distance:
                    x = x + i
                    page.mouse.move(x, y)
                page.mouse.up()
                write_log_to_allure_report(page, '滑块滑动完成')
                if check_element_with_timeout(page, ClientLeftNavigationBar().consoleOverviewXpath()):
                    break
                page.wait_for_selector(frame_xpath).content_frame().click(ClientLoginBase().refreshSliderBackPicButtonXpath())
                write_log_to_allure_report(page, '滑动验证失败，再次点击刷新滑块图片')
        yield {'page': page, 'name': browser_name}
        try:
            context.storage_state(path=ss_file)
        except Exception as e:
            assert False, e
        context.close()
        browser.close()
        p.stop()
