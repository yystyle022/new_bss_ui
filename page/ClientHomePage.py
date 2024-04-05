import allure
from base.ClientHomeBase import ClientHomeBase
from common.allure_function import write_log_to_allure_report


def click_home_page_console_button(page):
    '''
    点击首页控制台按钮
    @return:
    '''
    with allure.step('点击首页右上角控制台按钮，进入控制台页面'):
        page.click(ClientHomeBase().consoleXpath())
        write_log_to_allure_report(page, '点击首页右上角控制台按钮，进入控制台页面')


def click_purchase_button(page, product=1):
    '''
    首页点击立即购买按钮
    @param page:
    @return:
    '''
    if product == 1:
        page.click(ClientHomeBase().liqingHomePageTitleXpath())
        page.click(ClientHomeBase().liqingHomePagePurchaseButtonXpath())
        write_log_to_allure_report(page, '购买的账号为厘清')
    elif product == 2:
        page.click(ClientHomeBase().fenmingHomePageTitleXpath())
        page.click(ClientHomeBase().fenmingHomePagePurchaseButtonXpath())
        write_log_to_allure_report(page, '购买的账号为分明')
