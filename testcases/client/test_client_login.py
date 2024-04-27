# -*- coding: utf-8 -*-
# @Time : 2023/3/26 21:41
# @Author : yangyang
# @File : 2222/test_client_login.py
from time import sleep
from base.CommonElementBase import CommonElementBase
from page.ClientLoginPage import ClientLoginPage
from page.ManagementLoginPage import *
from base.ClientLoginBase import ClientLoginBase
from page.ClientPage import go_to_home_page_no_login
from common.playwright_function import save_directory
from base.ClientLeftNavigationBar import ClientLeftNavigationBar
from page.CommonPageFunction import input_operation, click_operation, assert_element_exist


# @allure.feature('测试登录官网')
# def test_login_client_success(browser, get_client_login_information):
#     '''
#     登录成功
#     @param browser:
#     @param get_client_login_information:
#     @return:
#     '''
#     browser_name = browser['name']
#     page = browser['page']
#     username, password = get_client_login_information
#     allure.dynamic.title(f'{browser_name}浏览器-登录官网-登录成功')
#
#     with allure.step('测试登录官网-登录成功'):
#         ClientLoginPage().client_login(page, username, password, ClientLeftNavigationBar().consoleOverviewXpath())
#
#
# @allure.feature('测试登录官网')
# def test_login_client_password_mistake(browser, get_client_login_information_password_mistake):
#     '''
#     登录密码错误
#     @param browser:
#     @param get_client_login_information_password_mistake:
#     @return:
#     '''
#     browser_name = browser['name']
#     page = browser['page']
#     username, password = get_client_login_information_password_mistake
#     allure.dynamic.title(f'{browser_name}浏览器-登录官网-密码错误')
#
#     with allure.step('测试登录官网-密码错误'):
#         ClientLoginPage().client_login(page, username, password, ClientLoginBase().loginPageToastXpath('密码错误'))
#
#
# @allure.feature('测试登录官网')
# def test_login_client_username_no_exist(browser, get_client_login_information_account_no_exist):
#     '''
#     登录账号不存在
#     @param browser:
#     @param get_client_login_information_account_no_exist:
#     @return:
#     '''
#     browser_name = browser['name']
#     page = browser['page']
#     username, password = get_client_login_information_account_no_exist
#     allure.dynamic.title(f'{browser_name}浏览器-登录官网-账号不存在')
#
#     with allure.step('测试登录官网-账号不存在'):
#         ClientLoginPage().client_login(page, username, password, ClientLoginBase().loginPageToastXpath('账号不存在'))
#
#
# @allure.feature('测试登录官网')
# def test_login_password_no_input(browser, get_client_login_information_account_no_exist):
#     '''
#     密码为空
#     @param browser:
#     @param get_client_login_information_account_no_exist:
#     @return:
#     '''
#     browser_name = browser['name']
#     page = browser['page']
#     username, password = get_client_login_information_account_no_exist
#     allure.dynamic.title(f'{browser_name}浏览器-登录官网-密码为空提示：账号或密码不能为空')
#
#     with allure.step('打开官网进入登录页面'):
#         go_to_home_page_no_login(page)
#
#     with allure.step('输入用户名'):
#         input_operation(page, ClientLoginBase().loginInputXpath('请输入账号或手机号码'), username, text=f'输入用户名:{username}')
#
#     with allure.step('点击登录按钮'):
#         click_operation(page, ClientLoginBase().submitButtonXpath(), text='点击登录按钮')
#         sleep(1)
#
#     with allure.step('验证提示：账号或密码不能为空'):
#         assert_element_exist(page, element=ClientLoginBase().accountOrPasswordNotBeNoneXpath())
#
#
# @allure.feature('测试登录官网')
# def test_login_account_no_input(browser, get_client_login_information_account_no_exist):
#     '''
#     账号为空
#     @param browser:
#     @param get_client_login_information_account_no_exist:
#     @return:
#     '''
#     browser_name = browser['name']
#     page = browser['page']
#     username, password = get_client_login_information_account_no_exist
#     allure.dynamic.title(f'{browser_name}浏览器-登录官网-账号为空提示：账号或密码不能为空')
#
#     with allure.step('打开官网进入登录页面'):
#         go_to_home_page_no_login(page)
#
#     with allure.step('输入密码'):
#         input_operation(page, ClientLoginBase().loginInputXpath('请输入密码'), password, text=f'输入密码:{password}')
#
#     with allure.step('点击登录按钮'):
#         click_operation(page, ClientLoginBase().submitButtonXpath(), text='点击登录按钮')
#         sleep(1)
#
#     with allure.step('验证提示：账号或密码不能为空'):
#         assert_element_exist(page, element=ClientLoginBase().accountOrPasswordNotBeNoneXpath())
#
#
# @allure.feature('测试登录官网')
# def test_login_account_and_password_no_input(browser):
#     '''
#     账号与密码都为空
#     @param browser:
#     @param get_client_login_information_account_no_exist:
#     @return:
#     '''
#     browser_name = browser['name']
#     page = browser['page']
#     allure.dynamic.title(f'{browser_name}浏览器-登录官网-账号与密码都为空提示：账号或密码不能为空')
#
#     with allure.step('打开官网进入登录页面'):
#         go_to_home_page_no_login(page)
#         sleep(1)
#
#     with allure.step('点击登录按钮'):
#         click_operation(page, ClientLoginBase().submitButtonXpath(), text='点击登录按钮')
#
#     with allure.step('验证提示：账号或密码不能为空'):
#         assert_element_exist(page, element=ClientLoginBase().accountOrPasswordNotBeNoneXpath())
#
#
# @allure.feature('测试登录官网')
# def test_phone_number_login_phone_number_input_mistake(browser):
#     '''
#     手机号登录，手机号输入错误
#     @param browser:
#     @param get_client_login_information_account_no_exist:
#     @return:
#     '''
#     browser_name = browser['name']
#     page = browser['page']
#     allure.dynamic.title(f'{browser_name}浏览器-登录官网-手机号登录-手机号输入错误：请输入正确的手机号')
#
#     with allure.step('打开官网进入登录页面'):
#         go_to_home_page_no_login(page)
#         sleep(1)
#
#     with allure.step('点击手机号登录'):
#         click_operation(page, ClientLoginBase().phoneNumberLoginTabXpath())
#
#     with allure.step('输入错误的手机号'):
#         input_operation(page, ClientLoginBase().loginInputXpath('11位手机号'), '123456789', text=f'输入错误的手机号:123456789')
#
#     with allure.step('点击登录按钮'):
#         click_operation(page, ClientLoginBase().phoneNumberLoginPageSubmitButtonXpath(), text='点击登录按钮')
#
#     with allure.step('验证提示：请输入正确的手机号'):
#         assert_element_exist(page, element=ClientLoginBase().phoneNumberMistakeToastXpath())
#
#
# @allure.feature('测试登录官网')
# def test_phone_number_login_phone_number_no_input(browser):
#     '''
#     手机号登录，不输入手机号
#     @param browser:
#     @param get_client_login_information_account_no_exist:
#     @return:
#     '''
#     browser_name = browser['name']
#     page = browser['page']
#     allure.dynamic.title(f'{browser_name}浏览器-登录官网-手机号登录-不输入手机号：请输入正确的手机号')
#
#     with allure.step('打开官网进入登录页面'):
#         go_to_home_page_no_login(page)
#         sleep(1)
#
#     with allure.step('点击手机号登录'):
#         click_operation(page, ClientLoginBase().phoneNumberLoginTabXpath())
#
#     with allure.step('点击登录按钮'):
#         click_operation(page, ClientLoginBase().phoneNumberLoginPageSubmitButtonXpath(), text='点击登录按钮')
#
#     with allure.step('验证提示：请输入正确的手机号'):
#         assert_element_exist(page, element=ClientLoginBase().phoneNumberMistakeToastXpath())
#
#
# @allure.feature('测试登录官网')
# def test_phone_number_login_no_input_verification_code(browser, get_client_login_information):
#     '''
#     手机号登录：不输入验证码直接登录
#     @param browser:
#     @param get_client_login_information_account_no_exist:
#     @return:
#     '''
#     browser_name = browser['name']
#     page = browser['page']
#     username, password = get_client_login_information
#     allure.dynamic.title(f'{browser_name}浏览器-登录官网-手机号登录-不输入验证码直接登录，提示：请输入验证码')
#
#     with allure.step('打开官网进入登录页面'):
#         go_to_home_page_no_login(page)
#
#     with allure.step('点击手机号登录'):
#         click_operation(page, ClientLoginBase().phoneNumberLoginTabXpath())
#
#     with allure.step('输入正确的手机号'):
#         input_operation(page, ClientLoginBase().loginInputXpath('11位手机号'), username, text=f'输入手机号:{username}')
#
#     with allure.step('点击登录按钮'):
#         click_operation(page, ClientLoginBase().phoneNumberLoginPageSubmitButtonXpath(), text='点击登录按钮')
#
#     with allure.step('验证提示：请输入验证码'):
#         assert_element_exist(page, element=ClientLoginBase().pleaseInputVerificationCodeToastXpath())
#
#
# @allure.feature('测试登录官网')
# def test_phone_number_login_input_mistake_verification_code(browser, get_client_login_information):
#     '''
#     手机号登录：输入错误的验证码
#     @param browser:
#     @param get_client_login_information:
#     @return:
#     '''
#     browser_name = browser['name']
#     page = browser['page']
#     username, password = get_client_login_information
#     allure.dynamic.title(f'{browser_name}浏览器-登录官网-手机号登录-输入错误的验证码，提示：验证码错误')
#
#     with allure.step('打开官网进入登录页面'):
#         go_to_home_page_no_login(page)
#
#     with allure.step('点击手机号登录'):
#         click_operation(page, ClientLoginBase().phoneNumberLoginTabXpath())
#
#     with allure.step('输入正确的手机号'):
#         input_operation(page, ClientLoginBase().loginInputXpath('11位手机号'), username, text=f'输入手机号:{username}')
#
#     with allure.step('点击获取验证码按钮'):
#         click_operation(page, ClientLoginBase().getVerificationCodeButtonXpath(), text='点击获取验证码按钮')
#
#     with allure.step('滑动滑块验证'):
#         while True:
#             frame_xpath = ClientLoginBase().sliderVerificationIframeXpath()
#             download_images(page, image_name="slider", frame_xpath=frame_xpath, image_xpath=ClientLoginBase().sliderPicXpath(), save_directory=save_directory)
#             download_images(page, image_name="background", frame_xpath=frame_xpath, image_xpath=ClientLoginBase().sliderBackPicXpath(), save_directory=save_directory)
#             write_log_to_allure_report(page, '下载滑块图片成功')
#             position = dragbox_location(page)
#             x = position['x'] + position['width'] / 2
#             y = position['y'] + position['height'] / 2
#             distance = get_slide_locus(get_slide_distance() * (280 / 680) + 6)
#             write_log_to_allure_report(page, f'计算滑块的滑动距离成功，滑动距离为：{distance}')
#             page.mouse.move(x, y)
#             page.mouse.down()
#             for i in distance:
#                 x = x + i
#                 page.mouse.move(x, y)
#             page.mouse.up()
#             write_log_to_allure_report(page, '滑块滑动完成')
#             sleep(1)
#             if check_element_with_timeout(page, ClientLoginBase().regetVerificationCodeButtonXpath()):
#                 break
#             page.wait_for_selector(frame_xpath).content_frame().click(ClientLoginBase().refreshSliderBackPicButtonXpath())
#             write_log_to_allure_report(page, '滑动验证失败，再次点击刷新滑块图片')
#
#     with allure.step('输入错误的验证码'):
#         input_operation(page, ClientLoginBase().loginInputXpath('输入验证码'), '999999', text=f'输入错误的验证码:999999')
#
#     with allure.step('点击登录按钮'):
#         click_operation(page, ClientLoginBase().phoneNumberLoginPageSubmitButtonXpath(), text='点击登录按钮')
#
#     with allure.step('验证提示：验证码错误'):
#         assert_element_exist(page, element=ClientLoginBase().vertificationCodeMistakeToastXpath())


@allure.feature('测试登录官网')
def test_phone_number_login_input_expire_verification_code(browser, get_client_login_information):
    '''
    手机号登录，输入过期的验证码，提示：验证码已过期
    @param browser:
    @param get_client_login_information:
    @return:
    '''
    browser_name = browser['name']
    page = browser['page']
    username, password = get_client_login_information
    allure.dynamic.title(f'{browser_name}浏览器-登录官网-手机号登录-输入过期的验证码，提示：验证码已过期')

    with allure.step('打开官网进入登录页面'):
        go_to_home_page_no_login(page)

    with allure.step('点击手机号登录'):
        click_operation(page, ClientLoginBase().phoneNumberLoginTabXpath())

    with allure.step('输入正确的手机号'):
        input_operation(page, ClientLoginBase().loginInputXpath('11位手机号'), username, text=f'输入手机号:{username}')

    with allure.step('输入过期的验证码'):
        input_operation(page, ClientLoginBase().loginInputXpath('输入验证码'), '000000', text=f'输入过期的验证码:000000')

    with allure.step('点击登录按钮'):
        click_operation(page, ClientLoginBase().phoneNumberLoginPageSubmitButtonXpath(), text='点击登录按钮')

    with allure.step('验证提示：验证码已过期'):
        assert_element_exist(page, element=CommonElementBase().SpanElementContainsTextXpath('验证码过期'))
