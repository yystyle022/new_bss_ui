import allure
from common.playwrightFunction import *
from base.ClientHomeBase import ClientHomeBase
from base.ClientLoginBase import ClientLoginBase
from common.allure_function import write_log_to_allure_report


class ClientLoginPage:
    def client_login_success(self, page):
        '''
        登录官网成功
        @param page:
        @return:
        '''
        with allure.step('打开官网进入首页'):
            page.goto(clientURL)
            write_log_to_allure_report(page, '打开官网成功')

        with allure.step('点击登录按钮'):
            page.click(ClientHomeBase().loginButtonXpath())
            write_log_to_allure_report(page, '点击页面左上角登录按钮，进入登录页面成功')

        with allure.step('输入用户名'):
            page.fill(ClientLoginBase().loginInputXpath('请输入账号或手机号码'), clientUsername)
            write_log_to_allure_report(page, f'输入用户名:{clientUsername}')

        with allure.step('输入密码'):
            page.fill(ClientLoginBase().loginInputXpath('请输入密码'), clientPassword)
            write_log_to_allure_report(page, f'输入密码:{clientPassword}')

        with allure.step('点击登录按钮'):
            page.click(ClientLoginBase().submitButtonXpath())
            write_log_to_allure_report(page, '点击登录按钮')
            sleep(1)

        with allure.step('滑动滑块，进行登录验证'):
            while True:
                frame_xpath = ClientLoginBase().sliderVerificationIframeXpath()
                download_images(page, image_name="slider", frame_xpath=frame_xpath, image_xpath=ClientLoginBase().sliderPicXpath(), save_directory=os.path.join('..', 'picture'))
                download_images(page, image_name="background", frame_xpath=frame_xpath, image_xpath=ClientLoginBase().sliderBackPicXpath(), save_directory=os.path.join('..', 'picture'))
                write_log_to_allure_report(page, '下载滑块图片成功')
                position = dragbox_location(page)
                x = position['x'] + position['width'] / 2
                y = position['y'] + position['height'] / 2
                distance = get_slide_locus(get_slide_distance() * (280 / 680) + 6)
                write_log_to_allure_report(page, f'计算滑块的滑动距离成功，滑动距离为：{distance}')
                page.mouse.move(x, y)
                page.mouse.down()
                for i in distance:
                    x = x + i
                    page.mouse.move(x, y)
                page.mouse.up()
                write_log_to_allure_report(page, '滑块滑动完成')
                sleep(2)
                if page.query_selector(ClientHomeBase().consoleXpath()):
                    break

        with allure.step('验证是否登录成功'):
            page.wait_for_selector(ClientHomeBase().consoleXpath(), timeout=20)
            write_log_to_allure_report(page, '登录成功！！！')

    def client_login_fail(self, page, text, username, password):
        '''
        登录失败，密码错误
        @param page:
        @return:
        '''
        with allure.step('打开官网进入首页'):
            page.goto(clientURL)
            write_log_to_allure_report(page, f'打开官网成功')

        with allure.step('点击登录按钮'):
            page.click(ClientHomeBase().loginButtonXpath())
            write_log_to_allure_report(page, '点击页面左上角登录按钮，进入登录页面成功')

        with allure.step('输入用户名'):
            page.fill(ClientLoginBase().loginInputXpath('请输入账号或手机号码'), username)
            write_log_to_allure_report(page, f'输入用户名:{username}')

        with allure.step('输入密码'):
            page.fill(ClientLoginBase().loginInputXpath('请输入密码'), password)
            write_log_to_allure_report(page, f'输入密码:{password}')

        with allure.step('点击登录按钮'):
            page.click(ClientLoginBase().submitButtonXpath())
            write_log_to_allure_report(page, '点击登录按钮')
            sleep(1)

        with allure.step('获取登录页面滑块验证信息'):
            frame_xpath = ClientLoginBase().sliderVerificationIframeXpath()
            download_images(page, image_name="slider", frame_xpath=frame_xpath, image_xpath=ClientLoginBase().sliderPicXpath(), save_directory=os.path.join('..', 'picture'))
            download_images(page, image_name="background", frame_xpath=frame_xpath, image_xpath=ClientLoginBase().sliderBackPicXpath(), save_directory=os.path.join('..', 'picture'))
            write_log_to_allure_report(page, '下载滑块图片成功')
            position = dragbox_location(page)
            x = position['x'] + position['width'] / 2
            y = position['y'] + position['height'] / 2
            distance = get_slide_locus(get_slide_distance() * (280 / 680) + 6)
            write_log_to_allure_report(page, f'开始计算滑块滑动数据，滑动的距离列表为{distance}')

        with allure.step('滑动滑块验证'):
            page.mouse.move(x, y)
            page.mouse.down()
            for i in distance:
                x = x + i
                page.mouse.move(x, y)
            page.mouse.up()
            write_log_to_allure_report(page, '开始移动滑块进行验证')
            sleep(2)

        with allure.step(f'弹出登陆登录失败弹窗'):
            assert_element_exist(page, ClientLoginBase().loginPasswordMistakeXpath(text))
            write_log_to_allure_report(page, f'弹出登陆登录失败弹窗,弹窗提示{text}')
