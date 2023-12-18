from common.report_add_img import add_img_to_report
from web.config.driver_config import getSeleniumDriver
import pytest


driver = None


@pytest.fixture()
def chrome_driver():
    global driver
    driver = getSeleniumDriver()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # 获取钩子方法的调用结果
    out = yield
    # 从钩子方法的调用结果中获取测试报告
    report = out.get_result()
    report.description = str(item.function.__doc__)

    # 共三个阶段，分别为：setup，call，teardown
    if report.when == "call":
        if report.failed:
            add_img_to_report(driver, "失败截图", need_sleep=False)
