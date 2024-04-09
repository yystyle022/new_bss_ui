from time import sleep
from base.ClientHomeBase import ClientHomeBase
from base.ClientConsoleBase import ClientConsoleBase
from base.ClientRegisterBase import ClientRegisterBase
from base.ClientCmInstanceListBase import ClientInstanceList
from common.allure_function import write_log_to_allure_report

# Uat
host = "https://bss-user-uat.sixents.com"

# Prod
# host = "https://www.sixents.com"

# PageUrl
HomePage = f"{host}"
# 控制台概览页面
ConsoleOverviewPageUrl = f"{host}/home/index"
# 厘米级服务概览页面
CmServiceOverviewPageUrl = f"{host}/server/cm/index"
# 厘米级服务实例页面
CmServiceInstancePageUrl = f"{host}/server/cm/example/index"
# 厘米级服务正式账号页面
CmServiceFormalAccountNumberPageUrl = f"{host}/server/cm/officialAccount/index"
# 厘米级服务试用账号页面
CmServiceTryAccountNumberPageUrl = f"{host}/server/cm/trialAccount/index"
# 亚米级服务概览页面
DmServiceOverviewPageUrl = f"{host}/server/dm/index"
# 亚米级服务实例页面
DmServiceInstancePageUrl = f"{host}/server/dm/example/index"
# 亚米级服务正式账号页面
DmServiceFormalAccountNumberPageUrl = f"{host}/server/dm/officialAccount/index"
# 亚米级服务试用账号页面
DmServiceTryAccountNumberPageUrl = f"{host}/server/dm/trialAccount/index"
# 账号注册页面
AccountRegisterPageUrl = f"{host}/user/register"


def go_to_console_overview_page(page):
    '''
    去控制台概览页面
    @param page:
    @return:
    '''
    page.goto(ConsoleOverviewPageUrl)
    try:
        page.wait_for_selector(ClientConsoleBase().ServcieTotalXpath(), timeout=5000)
        write_log_to_allure_report(page, '进入控制台概览页面成功')
    except Exception:
        write_log_to_allure_report(page, f'进入控制台概览页面失败')
        assert False, '进入控制台概览页面失败'


def go_to_cm_service_instance_page(page):
    '''
    去厘米级服务实例页面
    @param page:
    @return:
    '''
    page.goto(CmServiceInstancePageUrl)
    try:
        page.wait_for_selector(ClientInstanceList().CmListTitleXpath(), timeout=5000)
        write_log_to_allure_report(page, '进入厘米级服务实例页面成功')
    except Exception:
        write_log_to_allure_report(page, f'进入厘米级服务实例页面失败')
        assert False, '进入厘米级实例列表失败'


def go_to_dm_service_instance_page(page):
    '''
    去亚米级服务实例页面
    @param page:
    @return:
    '''
    page.goto(DmServiceInstancePageUrl)
    try:
        page.wait_for_selector(ClientInstanceList().DmListTitleXpath(), timeout=5000)
        write_log_to_allure_report(page, '进入亚米级服务实例页面成功')
    except Exception:
        write_log_to_allure_report(page, f'进入亚米级服务实例页面失败')
        assert False, '进入亚米级实例列表失败'


def go_to_home_page_no_login(page):
    '''
    去往首页，未登录
    @param page:
    @return:
    '''
    page.goto(HomePage)
    try:
        page.wait_for_selector(ClientHomeBase().registerButtonXpath(), timeout=5000)
        write_log_to_allure_report(page, '进入首页成功')
    except Exception:
        write_log_to_allure_report(page, f'进入首页失败')
        assert False, '进入首页失败'


def go_to_account_register_page(page):
    '''
    去往账号注册页面
    @param page:
    @return:
    '''
    page.goto(AccountRegisterPageUrl)
    write_log_to_allure_report(page, '去往账号注册页面')
