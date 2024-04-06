import allure
from common.allure_function import write_log_to_allure_report
from base.ClientProductDetailsBase import ClientProductDetailsBase


def purchase_server_number(page, duration=1, activeMethod=1, bindMethod=1, purchaseQuantity=1):
    '''
    购买账号
    @return:
    '''
    with allure.step('选择购买时长'):
        if duration == 1:
            page.click(ClientProductDetailsBase().purchaseDurationOneDayXpath())
            write_log_to_allure_report(page, "选择购买时长为1天，选择成功")
        elif duration == 2:
            page.click(ClientProductDetailsBase().purchaseDurationOneMonthXpath())
            write_log_to_allure_report(page, "选择购买时长为1个月，选择成功")
        elif duration == 3:
            page.click(ClientProductDetailsBase().purchaseDurationOneYearXpath())
            write_log_to_allure_report(page, "选择购买时长为1年，选择成功")

    with allure.step('选择激活方式'):
        if activeMethod == 1:
            write_log_to_allure_report(page, "选择激活方式为自动激活")
        elif activeMethod == 2:
            page.click(ClientProductDetailsBase().manualActiveMethodXpath())
            write_log_to_allure_report(page, "选择激活方式为手动激活")

    with allure.step('选择绑定方式'):
        if bindMethod == 1:
            write_log_to_allure_report(page, "选择绑定方式为自动绑定")
        elif bindMethod == 2:
            page.click(ClientProductDetailsBase().manualBindMethodXpath())
            write_log_to_allure_report(page, "选择绑定方式为手动绑定")

    with allure.step('填写购买数量'):
        page.fill(ClientProductDetailsBase().purchaseSumXpath(), f'{purchaseQuantity}')
        write_log_to_allure_report(page, f"购买账号的数量为：{purchaseQuantity}")

    with allure.step('点击立即购买按钮'):
        page.click(ClientProductDetailsBase().purchaseButtonXpath())
        write_log_to_allure_report(page, "点击立即购买按钮")
