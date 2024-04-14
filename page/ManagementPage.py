from common.playwrightFunction import assert_element_exist
from base.ManagementLoginBase import ManagementLoginBase

# Uat
host = "https://bss-backend-uat.sixents.com"

# Prod
# host = "https://bssadmin.sixents.com"


# 登录页面
LoginPageUrl = f"{host}/login"
# 服务订单页面
ServiceOrderPageUrl = f"{host}/server/order/list"
# 线下订单申请页面
OfflineOrderApplicationPageUrl = f"{host}/server/order-offline/apply-list"
# 线下订单审核页面
OfflineOrderReview = f"{host}/finance/offline-order/audit"


def go_to_login_page(page):
    '''
    去登录页
    @param page:
    @return:
    '''
    page.goto(LoginPageUrl)
    assert_element_exist(page, ManagementLoginBase().LoginButtonXpath())


def go_to_service_order_page(page):
    '''
    去服务订单页面
    @param page:
    @return:
    '''
    page.goto(ServiceOrderPageUrl)


def go_to_offline_order_page(page):
    '''
    去线下订单页面
    @param page:
    @return:
    '''
    page.goto(OfflineOrderApplicationPageUrl)


def go_to_order_review_page(page):
    '''
    去订单审核页面
    @param page:
    @return:
    '''
    page.goto(OfflineOrderReview)
