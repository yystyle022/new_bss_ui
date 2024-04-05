from common.playwrightFunction import *
from common.allure_function import write_log_to_allure_report
from base.ClientCmInstanceListBase import ClientInstanceList
from base.ClientInstanceExpandBase import ClientInstanceExpandBase

sums = random.randint(3, 10)


def expand_server_number(page, instanceId, duration=2, sums=sums):
    '''
    扩容差分账号
    @param page:
    @param instanceId: 实例Id
    @param duration: 扩容时长
    @param sums: 扩容数量
    @return:
    '''

    with allure.step('点击实例的扩容按钮，进入扩容详情页面'):
        page.click(ClientInstanceList().InstanceExpandAccountNumberButtonXpath(instanceId))
        write_log_to_allure_report(page, "点击实例的扩容按钮，进入扩容详情页面")
        sleep(2)

    with allure.step('扩容页面选择购买时长'):
        if duration == 1:
            page.click(ClientInstanceExpandBase().PurchaseDurationIsDayXpath())
            write_log_to_allure_report(page, "选择购买时长为1天，选择成功")
        elif duration == 2:
            page.click(ClientInstanceExpandBase().PurchaseDurationIsMonthXpath())
            write_log_to_allure_report(page, "选择购买时长为1个月，选择成功")
        elif duration == 3:
            page.click(ClientInstanceExpandBase().PurchaseDurationIsYearXpath())
            write_log_to_allure_report(page, "选择购买时长为1年，选择成功")

    with allure.step('填写扩容数量'):
        page.fill(ClientInstanceExpandBase().SumInputXpath(), f'{sums}')
        write_log_to_allure_report(page, f'输入的扩容数量为:{sums}')

    with allure.step('点击提交扩容按钮，进入提交订单页面'):
        page.click(ClientInstanceExpandBase().SubmitExpandButtonXpath())
        write_log_to_allure_report(page, '点击提交扩容按钮，进入提交订单页面')
        sleep(1)


def search_instance(page, instanceId):
    '''
    查询实例，返回实例下正式账号数量
    @param instanceId:
    @return:
    '''
    with allure.step('实例id输入框输入需要扩容的实例Id'):
        page.fill(ClientInstanceList().InstanceIdInputXpath(), instanceId)
        write_log_to_allure_report(page, f'输入实例Id：{instanceId}')

    with allure.step('点击查询按钮进行实例查询'):
        page.click(ClientInstanceList().QueryButtonXpath())
        write_log_to_allure_report(page, "点击查询按钮进行实例查询")
        sleep(1)

    with allure.step('获取扩容前实例下差分账号个数'):
        number = page.query_selector(ClientInstanceList().InstanceFormalAccountNumberSumsXpath(instanceId)).text_content()
        write_log_to_allure_report(page, f"获取扩容前实例下差分账号个数：{number}")

    return number
