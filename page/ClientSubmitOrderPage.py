import allure
from base.ClientSubmitOrderBase import ClientSubmitOrderBase
from base.ClientPayTheOrderBase import ClientPayTheOrderBase
from common.allure_function import write_log_to_allure_report


def click_submit_order_button(page):
    '''
    点击提交订单按钮
    @return:
    '''

    with allure.step('点击提交订单按钮'):
        page.click(ClientSubmitOrderBase().submitOrderButtonXpath())
        write_log_to_allure_report(page, '点击提交订单按钮')

    with allure.step('验证是否进入确认支付页面'):
        try:
            assert page.wait_for_selector(ClientPayTheOrderBase().InOrderPaymentPageXpath(), timeout=5000), '进入订单支付页面失败'
            write_log_to_allure_report(page, '进入订单确认支付页面成功')
        except Exception as error:
            write_log_to_allure_report(page, f'进入订单确认支付页面失败：{error}')
