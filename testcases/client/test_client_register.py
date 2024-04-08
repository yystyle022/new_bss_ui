import allure
from page.ClientRegisterPage import *
from page.ClientPage import go_to_home_page_no_login
from page.ClientHomePage import click_register_button
from page.ClientPage import go_to_account_register_page
from common.allure_function import write_log_to_allure_report


@allure.feature('首页注册跳转')
@allure.title('点击首页注册按钮，正常跳转至注册页面')
def test_register_button_jump(chrome):
    '''
    测试点击首页注册按钮，成功跳转到注册页面
    @param chrome:
    @return:
    '''
    with allure.step('打开网址进入首页'):
        go_to_home_page_no_login(chrome)

    with allure.step('点击注册按钮'):
        click_register_button(chrome)

    with allure.step('验证是否进入注册页面'):
        assert_into_register_page_success(chrome)


@allure.feature('手机号验证')
@allure.title('输入字母，提示:手机号不正确')
def test_phone_number_input_alphabet(chrome):
    '''
    测试手机号输入字母，提示:手机号不正确
    @param chrome:
    @return:
    '''
    with allure.step('打开网址进入首页'):
        go_to_home_page_no_login(chrome)

    with allure.step('点击注册按钮'):
        click_register_button(chrome)

    with allure.step('验证是否进入注册页面'):
        assert_into_register_page_success(chrome)

    with allure.step('输入字母'):
        input_phone_number(chrome, 'ahagsgtQw')

    with allure.step('点击获取验证码'):
        click_get_verification_code(chrome)

    with allure.step('提示:请输入正确的手机号'):
        assert_input_phone_number_incorrect(chrome)


@allure.feature('手机号验证')
@allure.title('输入10位数字，提示:手机号不正确')
def test_phone_number_input_10_number(chrome):
    '''
    输入10位数字，提示:手机号不正确
    @param chrome:
    @return:
    '''
    with allure.step('打开网址进入首页'):
        go_to_home_page_no_login(chrome)

    with allure.step('点击注册按钮'):
        click_register_button(chrome)

    with allure.step('验证是否进入注册页面'):
        assert_into_register_page_success(chrome)

    with allure.step('输入10位数字'):
        input_phone_number(chrome, '1332541124')

    with allure.step('点击获取验证码'):
        click_get_verification_code(chrome)

    with allure.step('提示:请输入正确的手机号'):
        assert_input_phone_number_incorrect(chrome)


@allure.feature('手机号验证')
@allure.title('输入12位数字，提示:手机号不正确')
def test_phone_number_input_12_number(chrome):
    '''
    输入12位数字，提示:手机号不正确
    @param chrome:
    @return:
    '''
    with allure.step('打开网址进入首页'):
        go_to_home_page_no_login(chrome)

    with allure.step('点击注册按钮'):
        click_register_button(chrome)

    with allure.step('验证是否进入注册页面'):
        assert_into_register_page_success(chrome)

    with allure.step('输入12位数字'):
        input_phone_number(chrome, '133254112436')

    with allure.step('点击获取验证码'):
        click_get_verification_code(chrome)

    with allure.step('提示:请输入正确的手机号'):
        assert_input_phone_number_incorrect(chrome)


@allure.feature('手机号验证')
@allure.title('输入汉字，提示:手机号不正确')
def test_phone_number_input_chinese(chrome):
    '''
    输入汉字，提示:手机号不正确
    @param chrome:
    @return:
    '''
    with allure.step('打开网址进入首页'):
        go_to_home_page_no_login(chrome)

    with allure.step('点击注册按钮'):
        click_register_button(chrome)

    with allure.step('验证是否进入注册页面'):
        assert_into_register_page_success(chrome)

    with allure.step('输入汉字'):
        input_phone_number(chrome, '测试文案汉字')

    with allure.step('点击获取验证码'):
        click_get_verification_code(chrome)

    with allure.step('提示:请输入正确的手机号'):
        assert_input_phone_number_incorrect(chrome)


@allure.feature('手机号验证')
@allure.title('输入为空，提示:手机号不正确')
def test_phone_number_input_none(chrome):
    '''
    输入为空，提示:手机号不正确
    @param chrome:
    @return:
    '''
    with allure.step('打开网址进入首页'):
        go_to_home_page_no_login(chrome)

    with allure.step('点击注册按钮'):
        click_register_button(chrome)

    with allure.step('验证是否进入注册页面'):
        assert_into_register_page_success(chrome)

    with allure.step('点击获取验证码'):
        click_get_verification_code(chrome)

    with allure.step('提示:请输入正确的手机号'):
        assert_input_phone_number_incorrect(chrome)
