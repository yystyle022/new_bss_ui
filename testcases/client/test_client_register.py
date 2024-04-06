import allure
from page.ClientRegisterPage import *
from page.ClientPage import go_to_home_page_no_login
from page.ClientHomePage import click_register_button

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
