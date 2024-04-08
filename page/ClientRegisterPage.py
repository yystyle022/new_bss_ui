from base.ClientRegisterBase import *
from common.allure_function import write_log_to_allure_report


def assert_into_register_page_success(page):
    '''
    断言是否进入注册页面
    @param page:
    @return:
    '''
    try:
        assert page.wait_for_selector(ClientRegisterBase().UserRegisterNodeXpath(), timeout=5000), '进入注册页面失败'
        write_log_to_allure_report(page, '进入注册页面成功')
    except Exception as error:
        write_log_to_allure_report(page, f'进入注册页面失败：{error}')


def assert_input_phone_number_incorrect(page):
    '''
    断言手输入的手机号错误
    @param page:
    @return:
    '''
    try:
        assert page.wait_for_selector(ClientRegisterBase().PleaseInputRightPhoneNumberWarningXpath(), timeout=5000), '输入手机号错误'
        write_log_to_allure_report(page, '输入手机号正确')
    except Exception as error:
        write_log_to_allure_report(page, f'输入手机号错误：{error}')


def input_phone_number(page, phoneNumber):
    '''
    输入手机号
    @param page:
    @param phoneNumber:
    @return:
    '''
    page.fill(ClientRegisterBase().PhoneNumberInputFrameXpath(), phoneNumber)
    write_log_to_allure_report(page, f'输入的手机号为：{phoneNumber}')


def click_get_verification_code(page):
    '''
    点击获取验证码按钮
    @param page:
    @return:
    '''
    page.click(ClientRegisterBase().GetVerificationCodeButtonXpath())
    write_log_to_allure_report(page, "点击获取验证码按钮")
