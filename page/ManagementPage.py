from time import sleep
from page.CommonPageFunction import assert_element_exist
from base.ManagementLoginBase import ManagementLoginBase
from common.allure_function import write_log_to_allure_report

# Uat
host = "https://bss-backend-uat.sixents.com"

# Prod
# host = "https://bssadmin.sixents.com"


# 登录页面
LoginPageUrl = f"{host}/login"
# 首页
HomePageUrl = f"{host}/home"
# 服务订单页面
ServiceOrderPageUrl = f"{host}/server/order/list"
# 线下订单申请页面
OfflineOrderApplicationPageUrl = f"{host}/server/order-offline/apply-list"
# 线下订单审核页面
OfflineOrderReviewPageUrl = f"{host}/finance/offline-order/audit"
# 服务订单页面
ServerOrderPageUrl = f"{host}/server/order/list"
# 实例列表页面
InstanceListPageUrl = f"{host}/server/example-list"
# 差分账号页面
ServerNumberPageUrl = f"{host}/server/account-list"


def go_to_login_page(page):
    '''
    去登录页
    @param page:
    @return:
    '''
    page.goto(LoginPageUrl)
    write_log_to_allure_report(page, text='去登录页')


def go_to_home_page(page):
    '''
    去首页
    @param page:
    @return:
    '''
    page.goto(HomePageUrl)
    write_log_to_allure_report(page, text='去管理端首页')


def go_to_service_order_page(page):
    '''
    去服务订单页面
    @param page:
    @return:
    '''
    page.goto(ServiceOrderPageUrl)
    write_log_to_allure_report(page, text='去服务订单页面')


def go_to_offline_order_page(page):
    '''
    去线下订单页面
    @param page:
    @return:
    '''
    page.goto(OfflineOrderApplicationPageUrl)
    sleep(1)
    write_log_to_allure_report(page, text='去线下订单页面')


def go_to_order_review_page(page):
    '''
    去订单审核页面
    @param page:
    @return:
    '''
    page.goto(OfflineOrderReviewPageUrl)
    sleep(1)
    write_log_to_allure_report(page, text='去订单审核页面')


def go_to_instance_list_page(page):
    '''
    去实例列表页面
    @param page:
    @return:
    '''
    page.goto(InstanceListPageUrl)
    sleep(1)
    write_log_to_allure_report(page, text='去实例列表页面')


def go_to_server_number_list_page(page):
    '''
    去账号列表页面
    @param page:
    @return:
    '''
    page.goto(ServerNumberPageUrl)
    sleep(1)
    write_log_to_allure_report(page, text='去账号列表页面')


def go_to_server_order_page(page):
    '''
    去服务订单页面
    @param page:
    @return:
    '''
    page.goto(ServerOrderPageUrl)
    sleep(2)
    write_log_to_allure_report(page, text='去服务订单页面')
