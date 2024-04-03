from common.playwrightFunction import write_log_to_allure, screenshot_to_allure


def write_log_to_allure_report(page, text):
    try:
        screenshot_to_allure(page, text)
    except Exception:
        raise '日志写入异常'
