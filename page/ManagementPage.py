from base.ManagementLoginBase import *
from common.allure_function import write_log_to_allure_report

# Uat
host = "https://bss-backend-uat.sixents.com"

# Prod
# host = "https://bssadmin.sixents.com"


# 登录页面Url
LoginPageUrl = f"{host}/login"


def go_to_login_page(page):
    '''
    去登录页
    @param page:
    @return:
    '''
    page.goto(LoginPageUrl)
    try:
        assert page.wait_for_selector(ManagementLoginBase().LoginButtonXpath(), timeout=5000), '进入管理端登录页面失败'
        write_log_to_allure_report(page, '进入管理端登录页面成功')
    except Exception as error:
        write_log_to_allure_report(page, f'进入管理端登录页面失败：{error}')
