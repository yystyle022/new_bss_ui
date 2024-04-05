import allure
from base.ClientPaySuccessBase import ClientPaySuccessBase
from base.ClientPayTheOrderBase import ClientPayTheOrderBase
from common.allure_function import write_log_to_allure_report


def click_pay_order_button(page):
    '''
    点击支付订单按钮
    @param page:
    @return:
    '''
    with allure.step('点击确认支付按钮'):
        page.click(ClientPayTheOrderBase().ConfirmPaymentButtonXpath())
        write_log_to_allure_report(page, '点击确认支付按钮')

    with allure.step('验证是否支付成功'):
        try:
            assert page.wait_for_selector(ClientPaySuccessBase().paySuccessIdentificationXpath(), timeout=5000), '订单支付失败'
            write_log_to_allure_report(page, '订单支付成功')
        except Exception as error:
            write_log_to_allure_report(page, f'订单支付失败:{error}')
