import allure
from time import sleep

from base.ClientHomeBase import ClientHomeBase
from page.ClientPage import go_to_home_page_no_login
from page.CommonPageFunction import *
from common.playwright_function import *
from base.ClientLoginBase import ClientLoginBase
from common.allure_function import write_log_to_allure_report


class ClientLoginPage:
    def client_login(self, page, clientUsername, clientPassword, element):
        '''
        登录官网
        @param page:
        @return:
        '''
        with allure.step('打开官网进入登录页面'):
            # page.goto('https://bss-front-uat.sixents.com/')
            go_to_home_page_no_login(page)

            # click_operation(page, ClientHomeBase().loginButtonXpath())
            # sleep(30)

        with allure.step('输入用户名'):
            input_operation(page, ClientLoginBase().loginInputXpath('请输入账号或手机号码'), clientUsername, text=f'输入用户名:{clientUsername}')

        with allure.step('输入密码'):
            input_operation(page, ClientLoginBase().loginInputXpath('请输入密码'), clientPassword, text=f'输入密码:{clientPassword}')

        with allure.step('点击登录按钮'):
            click_operation(page, ClientLoginBase().submitButtonXpath(), text='点击登录按钮')
            sleep(1)

        with allure.step('滑动滑块，进行登录验证'):
            while True:
                frame_xpath = ClientLoginBase().sliderVerificationIframeXpath()
                download_images(page, image_name="slider", frame_xpath=frame_xpath, image_xpath=ClientLoginBase().sliderPicXpath(), save_directory=save_directory)
                download_images(page, image_name="background", frame_xpath=frame_xpath, image_xpath=ClientLoginBase().sliderBackPicXpath(), save_directory=save_directory)
                write_log_to_allure_report(page, '下载滑块图片成功')
                position = dragbox_location(page)
                x = position['x'] + position['width'] / 2
                y = position['y'] + position['height'] / 2
                distance = get_slide_locus(get_slide_distance() * (280 / 680) + 6)
                write_log_to_allure_report(page, f'计算滑块的滑动距离成功，滑动距离为')
                page.mouse.move(x, y)
                page.mouse.down()
                for i in distance:
                    x = x + i
                    page.mouse.move(x, y)
                page.mouse.up()
                write_log_to_allure_report(page, '滑块滑动完成')
                sleep(1)
                if check_element_with_timeout(page, element, timeout=4):
                    break
                page.wait_for_selector(frame_xpath).content_frame().click(ClientLoginBase().refreshSliderBackPicButtonXpath())
                write_log_to_allure_report(page, '滑动验证失败，再次点击刷新滑块图片')

        with allure.step(f'验证页面元素{element}是否存在'):
            assert_element_exist(page, element)
