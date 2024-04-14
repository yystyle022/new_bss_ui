import yaml
import pytest
from page.ManagementLoginPage import *
from playwright.sync_api import sync_playwright
from base.ClientHomeBase import ClientHomeBase
from base.ClientLoginBase import ClientLoginBase
from page.ManagementPage import go_to_login_page
from common.read_config import load_config_files

save_directory = os.path.join(os.path.dirname(__file__), '..', 'picture')


def get_headless():
    '''
    获取配置文件中的headless的值
    @return:
    '''
    return load_config_files('common.yaml')['headless']


@pytest.fixture()
def chrome_client_login():
    ss_file = 'login_data.json'
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=get_headless(), args=["--start-maximized"])
        if os.path.isfile(ss_file):
            context = browser.new_context(storage_state=ss_file, no_viewport=True)
        else:
            context = browser.new_context(no_viewport=True)
        page = context.new_page()
        page.goto(clientURL)
        sleep(1)
        if page.query_selector(ClientHomeBase().registerButtonXpath()):
            page.click(ClientHomeBase().loginButtonXpath())
            page.fill(ClientLoginBase().loginInputXpath('请输入账号或手机号码'), clientUsername)
            page.fill(ClientLoginBase().loginInputXpath('请输入密码'), clientPassword)
            page.click(ClientLoginBase().submitButtonXpath())
            sleep(2)
            while True:
                frame_xpath = ClientLoginBase().sliderVerificationIframeXpath()
                download_images(page, image_name="slider", frame_xpath=frame_xpath, image_xpath=ClientLoginBase().sliderPicXpath(), save_directory=save_directory)
                download_images(page, image_name="background", frame_xpath=frame_xpath, image_xpath=ClientLoginBase().sliderBackPicXpath(), save_directory=save_directory)
                position = dragbox_location(page)
                x = position['x'] + position['width'] / 2
                y = position['y'] + position['height'] / 2
                distance = get_slide_locus(get_slide_distance() * (280 / 680) + 6)
                page.mouse.move(x, y)
                page.mouse.down()
                for i in distance:
                    x = x + i
                    page.mouse.move(x, y)
                page.mouse.up()
                sleep(2)
                if page.query_selector(ClientHomeBase().consoleXpath()):
                    break
        yield page
        try:
            context.storage_state(path=ss_file)
        except Exception as e:
            print(e)
        context.close()
        browser.close()
        p.stop()


@pytest.fixture()
def chromium_client_login():
    ss_file = 'login_data.json'
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=get_headless(), args=["--start-maximized"])
        if os.path.isfile(ss_file):
            context = browser.new_context(storage_state=ss_file, no_viewport=True)
        else:
            context = browser.new_context(no_viewport=True)
        page = context.new_page()
        page.goto(clientURL)
        sleep(1)
        if page.query_selector(ClientHomeBase().registerButtonXpath()):
            page.click(ClientHomeBase().loginButtonXpath())
            page.fill(ClientLoginBase().loginInputXpath('请输入账号或手机号码'), clientUsername)
            page.fill(ClientLoginBase().loginInputXpath('请输入密码'), clientPassword)
            page.click(ClientLoginBase().submitButtonXpath())
            sleep(1)
            while True:
                frame_xpath = ClientLoginBase().sliderVerificationIframeXpath()
                download_images(page, image_name="slider", frame_xpath=frame_xpath, image_xpath=ClientLoginBase().sliderPicXpath(), save_directory=save_directory)
                download_images(page, image_name="background", frame_xpath=frame_xpath, image_xpath=ClientLoginBase().sliderBackPicXpath(), save_directory=save_directory)
                position = dragbox_location(page)
                x = position['x'] + position['width'] / 2
                y = position['y'] + position['height'] / 2
                distance = get_slide_locus(get_slide_distance() * (280 / 680) + 6)
                page.mouse.move(x, y)
                page.mouse.down()
                for i in distance:
                    x = x + i
                    page.mouse.move(x, y)
                page.mouse.up()
                sleep(2)
                if page.query_selector(ClientHomeBase().consoleXpath()):
                    break
        yield page
        try:
            context.storage_state(path=ss_file)
        except Exception as e:
            print(e)
        context.close()
        browser.close()
        p.stop()


@pytest.fixture()
def edge_client_login():
    ss_file = 'login_data.json'
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=get_headless(), args=["--start-maximized"])
        if os.path.isfile(ss_file):
            context = browser.new_context(storage_state=ss_file, no_viewport=True)
        else:
            context = browser.new_context(no_viewport=True)
        page = context.new_page()
        page.goto(clientURL)
        sleep(1)
        if page.query_selector(ClientHomeBase().registerButtonXpath()):
            page.click(ClientHomeBase().loginButtonXpath())
            page.fill(ClientLoginBase().loginInputXpath('请输入账号或手机号码'), clientUsername)
            page.fill(ClientLoginBase().loginInputXpath('请输入密码'), clientPassword)
            page.click(ClientLoginBase().submitButtonXpath())
            sleep(2)
            while True:
                frame_xpath = ClientLoginBase().sliderVerificationIframeXpath()
                download_images(page, image_name="slider", frame_xpath=frame_xpath, image_xpath=ClientLoginBase().sliderPicXpath(), save_directory=save_directory)
                download_images(page, image_name="background", frame_xpath=frame_xpath, image_xpath=ClientLoginBase().sliderBackPicXpath(), save_directory=save_directory)
                position = dragbox_location(page)
                x = position['x'] + position['width'] / 2
                y = position['y'] + position['height'] / 2
                distance = get_slide_locus(get_slide_distance() * (280 / 680) + 6)
                page.mouse.move(x, y)
                page.mouse.down()
                for i in distance:
                    x = x + i
                    page.mouse.move(x, y)
                page.mouse.up()
                sleep(2)
                if page.query_selector(ClientHomeBase().consoleXpath()):
                    break
        yield page
        try:
            context.storage_state(path=ss_file)
        except Exception as e:
            print(e)
        context.close()
        browser.close()
        p.stop()


@pytest.fixture()
def firefox_client_login():
    ss_file = 'login_data.json'
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True, args=["--start-maximized"])
        if os.path.isfile(ss_file):
            context = browser.new_context(storage_state=ss_file, no_viewport=True)
        else:
            context = browser.new_context(no_viewport=True)
        page = context.new_page()
        page.goto(clientURL)
        sleep(1)
        if page.query_selector(ClientHomeBase().registerButtonXpath()):
            page.click(ClientHomeBase().loginButtonXpath())
            page.fill(ClientLoginBase().loginInputXpath('请输入账号或手机号码'), clientUsername)
            page.fill(ClientLoginBase().loginInputXpath('请输入密码'), clientPassword)
            page.click(ClientLoginBase().submitButtonXpath())
            sleep(1)
            while True:
                frame_xpath = ClientLoginBase().sliderVerificationIframeXpath()
                download_images(page, image_name="slider", frame_xpath=frame_xpath, image_xpath=ClientLoginBase().sliderPicXpath(), save_directory=save_directory)
                download_images(page, image_name="background", frame_xpath=frame_xpath, image_xpath=ClientLoginBase().sliderBackPicXpath(), save_directory=save_directory)
                position = dragbox_location(page)
                x = position['x'] + position['width'] / 2
                y = position['y'] + position['height'] / 2
                distance = get_slide_locus(get_slide_distance() * (280 / 680) + 6)
                page.mouse.move(x, y)
                page.mouse.down()
                for i in distance:
                    x = x + i
                    page.mouse.move(x, y)
                page.mouse.up()
                sleep(2)
                if page.query_selector(ClientHomeBase().consoleXpath()):
                    break
        yield page
        try:
            context.storage_state(path=ss_file)
        except Exception as e:
            print(e)
        context.close()
        browser.close()
        p.stop()


@pytest.fixture()
def chrome_management_login():
    ss_file = 'management_login_data.json'
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=get_headless(), args=["--start-maximized"])
        if os.path.isfile(ss_file):
            context = browser.new_context(storage_state=ss_file, no_viewport=True)
        else:
            context = browser.new_context(no_viewport=True)
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


@pytest.fixture()
def chromium_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=get_headless(), args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        yield page
        context.close()
        browser.close()
        p.stop()


@pytest.fixture()
def chrome_browser():
    with sync_playwright() as p:
        if get_headless() == True:
            browser = p.chromium.launch(channel="chrome", headless=True, args=["--start-maximized"])
            context = browser.new_context(viewport={'width': 1920, 'height': 1080})
        else:
            browser = p.chromium.launch(channel="chrome", headless=False, args=["--start-maximized"])
            context = browser.new_context(no_viewport=True)
        page = context.new_page()
        yield page
        context.close()
        browser.close()
        p.stop()


@pytest.fixture()
def edge_browser():
    with sync_playwright() as p:
        if get_headless() == True:
            browser = p.chromium.launch(channel="msedge", headless=True, args=["--start-maximized"])
            context = browser.new_context(viewport={'width': 1920, 'height': 1080})
        else:
            browser = p.chromium.launch(channel="msedge", headless=False, args=["--start-maximized"])
            context = browser.new_context(no_viewport=True)
        page = context.new_page()
        yield page
        context.close()
        browser.close()
        p.stop()


@pytest.fixture()
def firefox_browser():
    with sync_playwright() as p:
        if get_headless() == True:
            browser = p.firefox.launch(headless=True, args=["--start-maximized"])
            context = browser.new_context(viewport={'width': 1920, 'height': 1080})
        else:
            browser = p.firefox.launch(headless=False, args=["--start-maximized"])
            context = browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = context.new_page()
        yield page
        context.close()
        browser.close()
        p.stop()
