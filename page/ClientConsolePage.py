from common.playwrightFunction import *
from base.ClientHomeBase import ClientHomeBase
from base.ClientLoginBase import ClientLoginBase
from common.allure_function import write_log_to_allure_report


class ClientConsolePage:

    def expand_server_number(page, instanceId=expandInstanceId, duration=2, sums='1'):
        '''
        扩容差分账号
        @param page:
        @param instanceId: 实例Id
        @param duration: 扩容时长
        @param sums: 扩容数量
        @return:
        '''
        with allure.step('实例id输入框输入需要扩容的实例Id'):
            page.fill("//input[@placeholder='请输入']", instanceId)
            write_log_to_allure(f'输入实例Id:{instanceId}')
            screenshot_to_allure(page, f'输入实例Id:{instanceId}')

        with allure.step('点击查询按钮进行实例查询'):
            page.click("//button[1]")
            write_log_to_allure('点击查询按钮进行查询')
            screenshot_to_allure(page, '点击查询按钮进行查询')
            sleep(2)

        with allure.step('获取扩容前实例下差分账号个数'):
            number = page.query_selector(f"//td[text()='{expandInstanceId}']/following-sibling::td[7]").text_content()
            write_log_to_allure(f'实例下的差分账号数量为：{number}')

        with allure.step('点击实例的扩容按钮，进入扩容详情页面'):
            page.click("//a[text()='扩容']")
            write_log_to_allure('点击实例的扩容按钮，进入扩容详情页面')
            screenshot_to_allure(page, '点击实例的扩容按钮，进入扩容详情页面')
            sleep(2)

        with allure.step('扩容页面选择购买时长'):
            if duration == 1:
                page.click("//span[text()='天']")
                write_log_to_allure('选择购买时长为1天，选择成功')
            elif duration == 2:
                page.click("//span[text()='个月']")
                write_log_to_allure('选择购买时长为1个月，选择成功')
            elif duration == 3:
                page.click("//span[text()='年']")
                write_log_to_allure('选择购买时长为1年，选择成功')
            screenshot_to_allure(page, '购买时长选择成功')

        with allure.step('填写扩容数量'):
            page.fill("//input", sums)
            write_log_to_allure(f'输入的扩容数量为:{sums}')
            screenshot_to_allure(page, f'输入的扩容数量为:{sums}')

        with allure.step('点击提交扩容按钮，进入提交订单页面'):
            page.click("text=提交扩容")
            write_log_to_allure('点击提交扩容按钮，进入提交订单页面')
            screenshot_to_allure(page, '点击提交扩容按钮，进入提交订单页面')
            sleep(2)

        with allure.step('点击提交订单按钮，进入确认支付页面'):
            page.click(ClientLiQingDetailsBase().submitOrderButtonXpath())
            write_log_to_allure('点击提交订单按钮，进入确认支付页面')
            screenshot_to_allure(page, '点击提交订单按钮，进入确认支付页面')
            sleep(1)

        with allure.step('点击确认支付按钮，支付订单成功'):
            page.click('text=确认支付')
            write_log_to_allure('点击确认支付按钮，支付订单成功')
            screenshot_to_allure(page, '点击确认支付按钮，支付订单成功')
            sleep(1)

        with allure.step('判断是否支付成功'):
            assert_element_exist(page, ClientLiQingDetailsBase().paySuccessIdentificationXpath())
            write_log_to_allure('支付成功')
            screenshot_to_allure(page, '判断是否支付成功')

        with allure.step('前往控制台页面'):
            page.click("//button[2]")
            write_log_to_allure('点击返回控制台按钮，进入控制台页面')
            screenshot_to_allure(page, '点击返回控制台按钮，进入控制台页面')
            sleep(2)

        with allure.step('点击控制台页面左侧导航栏服务号管理菜单'):
            page.click("//span[text()='服务号管理']")
            write_log_to_allure('点击控制台页面左侧导航栏服务号管理菜单')
            screenshot_to_allure(page, '点击控制台页面左侧导航栏服务号管理菜单')

        with allure.step('点击控制台页面左侧导航栏服务号管理-厘米级服务'):
            page.click("//span[text()='厘米级服务']")
            write_log_to_allure('点击控制台页面左侧导航栏服务号管理-厘米级服务')
            screenshot_to_allure(page, '点击控制台页面左侧导航栏服务号管理-厘米级服务')

        with allure.step('点击控制台页面左侧导航栏服务号管理-厘米级服务-实例'):
            page.click("//span[text()='实例']")
            write_log_to_allure('点击控制台页面左侧导航栏服务号管理-厘米级服务-实例')
            screenshot_to_allure(page, '点击控制台页面左侧导航栏服务号管理-厘米级服务-实例')

        with allure.step('实例id输入框输入需要扩容的实例Id'):
            page.fill("//input[@placeholder='请输入']", instanceId)
            write_log_to_allure(f'输入实例Id:{instanceId}')
            screenshot_to_allure(page, f'输入实例Id:{instanceId}')
            sleep(2)

        with allure.step('点击查询按钮进行实例查询'):
            page.click("//button[1]")
            sleep(5)
            page.click("//button[1]")
            write_log_to_allure('点击查询按钮进行查询')
            screenshot_to_allure(page, '点击查询按钮进行查询')

        with allure.step('获取扩容前实例下差分账号个数'):
            number1 = page.query_selector(f"//td[text()='{expandInstanceId}']/following-sibling::td[7]").text_content()
            write_log_to_allure(f'实例下的差分账号数量为：{number1}')
            print(f"扩容后的差分账号数量为：{number1}")

        assert int(number1) == int(number) + int(sums)
