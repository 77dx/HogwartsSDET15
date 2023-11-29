import pytest
from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestSelenium:

    def setup(self):
        # 创建浏览器驱动
        self.driver = webdriver.Chrome()
        # 窗口最大化
        self.driver.maximize_window()
        # 进入网站

        # 设置全局的隐士等待
        self.driver.implicitly_wait(5)


    def teardown(self):
        self.driver.quit()

    def a_test_selenium(self):
        # 点击社区
        self.driver.find_element(By.LINK_TEXT, '社区').click()
        # 定义显式等待规则
        def wait(x):
            l = len(self.driver.find_elements(By.XPATH,'//*[@title="Become an Appium Pro"]'))
            return l >=1
        WebDriverWait(self.driver,10).until(wait)
        # 点击第一条帖子
        self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a').click()


    def b_test_date(self):
        self.driver.get('https://www.12306.cn/index/')
        # 修改时间控件的值
        self.driver.execute_script('a=document.getElementById("train_date");a.value="2023-11-05"')
        print(self.driver.execute_script('document.getElementById("train_date").value'))
        sleep(5)

    def c_test_alert(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to.frame('iframeResult')
        # drag = self.driver.find_element(By.ID, '//*[@id="droppable"]')
        # print(drag)
        # drop =w self.driver.find_element(By.ID, '//*[@id="draggable"]')
        # action = ActionChains(self.driver)
        # action.drag_and_drop(drag,drop).perform()
        sleep(3)

    def test_login(self):
        self.driver.get('https://user.wanshifu.com/login')
        # cookie设置还未实现
        cookies = {
            'hotline_id': '16843242028 _0',
            'wsf_user_token':'d34d8510-0f2f-466c-86d8-1f20f038dd87'
        }
        # self.driver.add_cookie({"name":"hotline_id","value":"16843242028 _0"})
        # self.driver.add_cookie({"name": "wsf_user_token", "value": "d34d8510-0f2f-466c-86d8-1f20f038dd87"})
        # print(self.driver.get_cookie('hotline_id'))
        # self.driver.refresh()

        self.driver.find_element(By.XPATH,'//*[@class="login-user"]').send_keys('鱼小七')
        self.driver.find_element(By.XPATH, '//*[@class="login-password"]').send_keys('Cathy8877')
        self.driver.find_element(By.XPATH,'//*[@class="login-button-main login-button-container"]').click()
        sleep(2)

        ele_close_icon =False
        try:
            ele_close_icon = self.driver.find_element(By.XPATH,'//*[@class="close-icon"]')
        except Exception as e:
            print(e)

        if ele_close_icon:
            ele_close_icon.click()

        self.driver.find_element(By.XPATH,'//a[@href="/placeorder"]').click()
        sleep(2)

        # js = "window.scrollTo(0,document.body.scrollHeight)"

        ele = self.driver.find_element(By.XPATH,'//*[@class="prefix-desc required"]')
        self.driver.execute_script("arguments[0].scrollIntoView();",ele)
        sleep(2)

        # self.driver.find_element(By.XPATH,'//input[@id="rc_select_4"]').click()

        sleep(2)

        # self.driver.find_element(By.XPATH, '//input[text()="床类")]').click()
        # self.driver.find_element(By.XPATH,'//span[text()="皮床")]').click()
        # 商品库选择商品
        self.driver.find_element(By.XPATH,'//*[@class="start-add-goods-placeorder"]').click()
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,'.ant-checkbox-input:nth-child(1)').click()
        self.driver.find_element(By.XPATH,'//span[text()="确 定"]').click()
        sleep(2)
        # 上滑页面，准备本地上传图片
        js = "window.scrollBy(0,-500)"
        self.driver.execute_script(js)
        sleep(1)
        self.driver.find_element(By.XPATH,'//div[@class="upload-text"]/input').click()
        sleep(3)


        '''
        # 点击下一页
        self.driver.find_element(By.XPATH,'//*[@class="ant-btn ant-btn-primary"]').click()

        sleep(2)

        # 下单第二页
        self.driver.find_element(By.XPATH,'//*[@name="aiaddress"]').send_keys('万某某，13311111111，广东省深圳市宝安区某某街道某某路')
        self.driver.find_element(By.XPATH,'//*[text()="立即识别"]').click()
        sleep(2)

        self.driver.find_element(By.XPATH,'//*[text()="已到货"]').click()

        sleep(5)
        
        '''



